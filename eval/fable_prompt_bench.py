#!/usr/bin/env python3
"""Fable 5.1 prompt-fitness benchmark for the product-idea-agent skill pack.

Scores the pack's prompt surface against Anthropic's published prompt-audit
patterns for current Claude models (pressure language, dated scaffolds,
step choreography, fossils) and the Fable 5.1 re-baselining guidance
(context and reasons, outcome-first communication, grounded claims,
delegation, boundaries, judgment). Deterministic, stdlib only, sub-second.

Usage:  python3 eval/fable_prompt_bench.py [-v]
Last stdout line is JSON: {"primary": <0-100>, "sub_scores": {...}}

Surfaces:
  skills/*/SKILL.md            full five-dimension score (80% of primary)
  skills/*/references/*.md     cruft only (10%)
  eval/runners/*_PROMPT        cruft only (10%)

ponytail: static heuristics with an integrity floor; add an LLM-judge
sub-score if the loop starts gaming the regexes instead of rewriting.
"""
from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
RUNNERS = ROOT / "eval" / "runners"

ARTIFACT = {
    "idea-brief-creator": "idea_brief.md",
    "demand-signals": "signals.md",
    "problem-segment": "icp.yaml",
    "competitive-landscape": "competitors.csv",
    "market-sizing": "market_size.md",
    "pricing-wtp": "pricing.yaml",
    "solution-wedge": "mvp_spec.md",
    "gtm-channels": "gtm_plan.md",
    "risk-assessment": "risks.md",
    "scorecard-generator": "scorecard.json",
    "validation-report": "validation_report.md",
    "idea-validation-orchestrator": "validation_report.md",
}
NO_CONTRACT = {"idea-validation-orchestrator", "validation-report"}

WEIGHTS = {"cruft": 0.30, "de_prescription": 0.25, "context_richness": 0.20,
           "fable_utilization": 0.20, "trigger_quality": 0.05}

I = re.IGNORECASE
# --- Group 1a/1b/1c/1d/1e signals from shared/prompt-audit.md -------------
CAPS = re.compile(r"\b(MUST|NEVER|ALWAYS|CRITICAL|IMPORTANT|DO NOT|DON'T)\b")
BANG = re.compile(r"!!")
HEDGE = re.compile(r"\b(try to|if possible|ideally|where possible|when possible)\b", I)
PRESSURE = re.compile(r"\b(be thorough|do not be lazy|don'?t be lazy|do not stop early|be very careful)\b", I)
SCAFFOLD = re.compile(
    r"think step by step|take a deep breath|<scratchpad>|<thinking>|output only (valid )?json"
    r"|\bat most \d+ (words|sentences|bullets|lines)\b|\bunder \d+ words\b"
    r"|\bevery \d+ (tool calls|messages|steps)\b|\bin \d+ words or (less|fewer)\b", I)
FOSSIL = re.compile(
    r"\bno longer\b|\bnow (works|supports|uses)\b|\bused to\b|\bclaude[- ]?(2|3|instant)\b"
    r"|\b(opus|sonnet|haiku)[- ]?4(\.\d)?\b|\bgpt-?[345]\b|\bdon'?t narrate\b"
    r"|\bhold (all )?(findings|results)\b|\bno interim\b|\bnever use (bullets|headers|bold)\b", I)
GRADER = re.compile(r"\b(you will be (graded|scored)|hidden tests?)\b", I)
TIC = re.compile(r"\b(Remember,|Again,|As (stated|mentioned) (above|earlier))")
PROHIBIT = re.compile(r"^\s*[-*]\s*\**(Do not|Don't|Never|Avoid)\b", I)
IDENTITY = re.compile(r"^You are (a|an) (helpful|expert|world-class)", I | re.M)

STEP_HEAD = re.compile(r"^#{2,5}\s*(Step|Phase|Stage)\s*\d+", I | re.M)
NUMBERED = re.compile(r"^\s*\d+[.)]\s+")
CHECKBOX = re.compile(r"^\s*-\s*\[ \]", re.M)
IMPERATIVE = re.compile(
    r"^(create|write|identify|ask|gather|list|document|calculate|extract|define|generate|include"
    r"|add|use|copy|structure|suggest|describe|capture|craft|search|note|flag|check|review|compile"
    r"|determine|rate|score|apply|estimate|find|map|assess|run|read|output|produce|record|select"
    r"|choose|consider|ensure|make|provide|tell|specify|state|compare|organize|summarize|validate"
    r"|research|analyze|evaluate|collect|set|start|follow|track|save|prioritize|highlight)\b", I)
REASON = re.compile(
    r"\b(because|so that|since|which means|this matters|otherwise|the reason|the point is"
    r"|so the|what makes|that is why|without (it|this))\b", I)
AUDIENCE = re.compile(
    r"\b(founders?|investors?|stakeholders?|readers?|audience|decision[- ]makers?"
    r"|a (strong|good|great|useful|weak) (brief|report|analysis|artifact|scorecard|plan|spec|assessment|landscape|profile|estimate|section)"
    r"|what good looks like|quality bar|reads like|the best (briefs|reports|analyses|plans)"
    r"|a reader (should|can|will))\b", I)

FABLE_MARKERS = {
    "outcome_first": r"\b(lead with|first sentence|tl;?dr|outcome first|the headline|open with (the|what))\b",
    "grounded_claims": r"\b(unverified|could(n'?t| not) verify|point to (the )?evidence|traceable to"
                       r"|mark(ed)? (it |them )?as (an? )?(estimate|assumption|inference)|evidence for every|say so)\b",
    "delegation": r"\b(sub-?agents?|delegate|in parallel|concurrently|fan out|spawn)\b",
    "boundaries": r"\b(stop there|report and stop|the deliverable is|without asking|only ask (the user )?when|ask (the user )?only)\b",
    "downstream_intent": r"\b(downstream|consumed by|feeds (into|the)|the next (skill|step) (reads|needs|uses)|who reads this|is read by)\b",
    "judgment_invited": r"\b(your judgment|use judgment|judgment call|non-?obvious|counter-?intuitive|contrarian|steelman|surprising|second-order|what would change (your|the) (mind|verdict)|the interesting (question|finding))\b",
    "depth_calibration": r"\b(how deep|go deeper|depth of research|scale (the|your) (effort|research|search)|proportion(al|ate) to|diminishing returns|enough evidence)\b",
    "self_check": r"\b(before (you )?(finish|finalize|write it up|hand off)|re-?read|sanity[- ]check|check (it|the (artifact|output|draft)) against|fresh eyes|verify (the|your) (artifact|output|draft|numbers))\b",
}
FABLE_RE = {k: re.compile(v, I) for k, v in FABLE_MARKERS.items()}
TRIGGER = re.compile(r"\b(use (this )?(skill )?when|use (it|this) (for|to)|trigger|invoke when|applies when)\b", I)

FENCE = re.compile(r"^```", re.M)


def clamp(x: float, lo: float = 0.0, hi: float = 100.0) -> float:
    return max(lo, min(hi, x))


def split_frontmatter(text: str) -> tuple[dict, str]:
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return {}, text
    fm: dict = {}
    for line in m.group(1).splitlines():
        kv = re.match(r"^\s*([\w-]+):\s*(.*)$", line)
        if kv:
            fm[kv.group(1)] = kv.group(2).strip()
    return fm, text[m.end():]


def strip_code(body: str) -> tuple[str, list[str]]:
    """Return (prose without fenced blocks, list of fenced block contents)."""
    parts, blocks, out, in_code = body.split("\n"), [], [], False
    buf: list[str] = []
    for line in parts:
        if line.startswith("```"):
            if in_code:
                blocks.append("\n".join(buf)); buf = []
            in_code = not in_code
            continue
        (buf if in_code else out).append(line)
    return "\n".join(out), blocks


def sentences(prose: str) -> list[str]:
    lines = [l for l in prose.split("\n") if l.strip() and not l.lstrip().startswith("#") and not l.lstrip().startswith("|")]
    out: list[str] = []
    for l in lines:
        l = re.sub(r"^\s*([-*]|\d+[.)])\s+", "", l)
        l = re.sub(r"\*\*|__|`", "", l).strip()
        l = re.sub(r"^(Step|Phase)\s*\d+\s*[:.-]\s*", "", l, flags=I)
        out.extend(s.strip() for s in re.split(r"(?<=[.!?])\s+", l) if len(s.strip()) > 2)
    return out


# --- dimension scorers -----------------------------------------------------
def cruft_score(body: str, detail: dict) -> float:
    pen = 0
    pen += 4 * len(CAPS.findall(body)); detail["caps"] = len(CAPS.findall(body))
    pen += 3 * len(BANG.findall(body))
    pen += 2 * len(HEDGE.findall(body)); detail["hedges"] = len(HEDGE.findall(body))
    pen += 4 * len(PRESSURE.findall(body))
    pen += 8 * len(SCAFFOLD.findall(body)); detail["scaffolds"] = len(SCAFFOLD.findall(body))
    pen += 5 * len(FOSSIL.findall(body)); detail["fossils"] = len(FOSSIL.findall(body))
    pen += 5 * len(GRADER.findall(body))
    pen += 2 * len(TIC.findall(body))
    pen += 3 * len(IDENTITY.findall(body))
    run, runs = 0, 0
    for line in body.split("\n"):
        if PROHIBIT.match(line):
            run += 1
            if run == 3:
                runs += 1
        else:
            run = 0
    pen += 6 * runs; detail["prohibition_runs"] = runs
    return clamp(100 - pen)


def de_prescription_score(prose: str, blocks: list[str], detail: dict) -> float:
    choreo = len(STEP_HEAD.findall(prose))
    run = 0
    for line in prose.split("\n"):
        if NUMBERED.match(line):
            run += 1
            if run == 5:
                choreo += 1
        else:
            run = 0
    detail["choreography_blocks"] = choreo
    s_c = clamp(100 - 10 * max(0, choreo - 2))
    sents = sentences(prose)
    imp = sum(1 for s in sents if IMPERATIVE.match(s))
    d = imp / len(sents) if sents else 0
    detail["imperative_density"] = round(d, 2)
    s_d = clamp((0.55 - d) / 0.35 * 100)
    checklists = sum(1 for b in blocks if len(CHECKBOX.findall(b)) >= 4)
    detail["checklists"] = checklists
    return clamp(0.5 * s_c + 0.5 * s_d - 15 * min(checklists, 2))


def context_score(prose: str, detail: dict) -> float:
    sents = sentences(prose)
    r = len(REASON.findall(prose)) / max(len(sents), 1)
    detail["reason_ratio"] = round(r, 2)
    s_r = clamp(r / 0.10 * 100)
    lines = [l for l in prose.split("\n") if l.strip() and not l.lstrip().startswith(("#", "|"))]
    bullets = sum(1 for l in lines if re.match(r"^\s*([-*]|\d+[.)])\s", l))
    p = 1 - bullets / len(lines) if lines else 0
    detail["prose_ratio"] = round(p, 2)
    s_p = clamp((p - 0.25) / 0.40 * 100)
    aud = len({m.group(0).lower() for m in AUDIENCE.finditer(prose)})
    detail["audience_markers"] = aud
    s_a = min(aud, 4) / 4 * 100
    return 0.4 * s_r + 0.3 * s_p + 0.3 * s_a


def fable_score(body: str, detail: dict) -> float:
    hits = [k for k, rx in FABLE_RE.items() if rx.search(body)]
    detail["fable_markers"] = hits
    return len(hits) / len(FABLE_RE) * 100


def trigger_score(desc: str, detail: dict) -> float:
    s = 0
    s += 25 if 120 <= len(desc) <= 1024 else 0
    s += 25 if not re.match(r"^(I|You|We)\b", desc) else 0
    s += 25 if TRIGGER.search(desc) else 0
    s += 25 if desc.count(",") <= 8 else 0
    detail["desc_len"] = len(desc)
    return s


def integrity(name: str, fm: dict, text: str, body: str, skill_dir: Path) -> list[str]:
    fails = []
    if fm.get("name") != name:
        fails.append("frontmatter name != dir")
    if not fm.get("description"):
        fails.append("no description")
    if fm.get("pack") != "product-idea-agent":
        fails.append("metadata.pack missing")
    tools = fm.get("allowed-tools", "")
    if "Read" not in tools or "Write" not in tools:
        fails.append("allowed-tools lacks Read/Write")
    n = text.count("\n") + 1
    if not 40 <= n <= 500:
        fails.append(f"line count {n} outside 40-500")
    if len(re.findall(r"\w+", body)) < 250:
        fails.append("body under 250 words")
    if ARTIFACT[name] not in body:
        fails.append(f"does not name artifact {ARTIFACT[name]}")
    if name not in NO_CONTRACT and "contracts/" not in body:
        fails.append("no contracts/ reference")
    for link in re.findall(r"\]\((references/[^)]+)\)", body):
        if not (skill_dir / link).exists():
            fails.append(f"broken link {link}")
    if name == "idea-validation-orchestrator":
        missing = [s for s in ARTIFACT if s != name and s not in body]
        if missing:
            fails.append(f"orchestrator omits {missing}")
    return fails


def norm_sentences(prose: str) -> set[str]:
    return {re.sub(r"[^a-z0-9 ]", "", s.lower()).strip() for s in sentences(prose) if len(s.split()) >= 8}


def score_skill(skill_dir: Path) -> dict:
    name = skill_dir.name
    text = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
    fm, body = split_frontmatter(text)
    prose, blocks = strip_code(body)
    detail: dict = {}
    fails = integrity(name, fm, text, body, skill_dir)
    dims = {
        "cruft": cruft_score(body, detail),
        "de_prescription": de_prescription_score(prose, blocks, detail),
        "context_richness": context_score(prose, detail),
        "fable_utilization": fable_score(body, detail),
        "trigger_quality": trigger_score(fm.get("description", ""), detail),
    }
    total = 0.0 if fails else sum(dims[k] * w for k, w in WEIGHTS.items())
    return {"name": name, "score": round(total, 2), "dims": {k: round(v, 1) for k, v in dims.items()},
            "integrity_failures": fails, "detail": detail, "sentences": norm_sentences(prose)}


def runner_prompts() -> dict[str, str]:
    out = {}
    for py in sorted(RUNNERS.glob("run_*.py")):
        for m in re.finditer(r'(\w+_PROMPT)\s*=\s*"""(.*?)"""', py.read_text(encoding="utf-8"), re.S):
            out[f"{py.name}:{m.group(1)}"] = m.group(2)
    return out


def main() -> int:
    verbose = "-v" in sys.argv
    skills = [score_skill(d) for d in sorted(SKILLS.iterdir()) if (d / "SKILL.md").exists()]
    if len(skills) != len(ARTIFACT):
        print(f"ERROR: expected {len(ARTIFACT)} skills, found {len(skills)}", file=sys.stderr)
        return 1

    # cross-skill boilerplate: identical long sentences in >=3 SKILL.md files
    counts = Counter(s for sk in skills for s in sk["sentences"])
    dups = sorted(s for s, c in counts.items() if c >= 3)
    dup_pen = min(30, 3 * len(dups))

    refs = {}
    for md in sorted(SKILLS.glob("*/references/*.md")):
        refs[str(md.relative_to(ROOT))] = cruft_score(md.read_text(encoding="utf-8"), {})
    runners = {k: cruft_score(v, {}) for k, v in runner_prompts().items()}

    skill_mean = sum(s["score"] for s in skills) / len(skills)
    fable_mean = clamp(sum(s["dims"]["fable_utilization"] for s in skills) / len(skills) - dup_pen)
    # apply the boilerplate penalty through the fable dimension's weight
    skill_mean -= dup_pen * WEIGHTS["fable_utilization"]
    ref_mean = sum(refs.values()) / len(refs) if refs else 100
    run_mean = sum(runners.values()) / len(runners) if runners else 100
    primary = round(0.80 * skill_mean + 0.10 * ref_mean + 0.10 * run_mean, 2)

    print(f"{'skill':32} {'score':>6}  cruft depres ctx  fable trig")
    for s in skills:
        d = s["dims"]
        flag = "  !! " + "; ".join(s["integrity_failures"]) if s["integrity_failures"] else ""
        print(f"{s['name']:32} {s['score']:6.1f}  {d['cruft']:5.0f} {d['de_prescription']:6.0f} {d['context_richness']:4.0f} {d['fable_utilization']:5.0f} {d['trigger_quality']:4.0f}{flag}")
        if verbose:
            print("    ", json.dumps(s["detail"]))
    print(f"{'references (cruft mean)':32} {ref_mean:6.1f}   low: " + ", ".join(f"{k.split('/')[-1]}={v:.0f}" for k, v in sorted(refs.items(), key=lambda kv: kv[1])[:3]))
    print(f"{'runner prompts (cruft mean)':32} {run_mean:6.1f}   " + ", ".join(f"{k}={v:.0f}" for k, v in runners.items()))
    print(f"{'cross-skill boilerplate':32} {len(dups):6d}   sentences repeated in >=3 skills (-{dup_pen})")
    if verbose and dups:
        for s in dups:
            print("     dup:", s[:100])

    sub = {f"skill:{s['name']}": s["score"] for s in skills}
    for k in WEIGHTS:
        sub[k] = round(sum(s["dims"][k] for s in skills) / len(skills), 2)
    sub["fable_utilization"] = round(fable_mean, 2)
    sub["references_cruft"] = round(ref_mean, 2)
    sub["runner_cruft"] = round(run_mean, 2)
    sub["boilerplate_dups"] = len(dups)
    print(json.dumps({"primary": primary, "sub_scores": sub}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
