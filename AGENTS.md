<!-- Generated: 2026-09-15 | Updated: 2026-09-15 -->

# product-idea-agent

## Purpose
A Claude Code skill pack that runs end-to-end product idea validation. Twelve composable skills (under `skills/`) turn a raw startup concept into a chain of 11 artifacts ending in a GO / PIVOT / NO-GO scorecard and validation report. Artifact shapes are fixed by contracts in `contracts/`; `eval/` holds fixtures and runners for measuring skill-pack output against a no-skills baseline. There is no application code: the product is the markdown skills plus their schemas.

## Key Files

| File | Description |
|------|-------------|
| `README.md` | Skill catalog, artifact flow diagram, install and usage summary |
| `product-idea-agent-skill-pack-implementation-blueprint.md` | Design doc the pack was built from: IdeaBrowser reverse-engineering, per-skill specs, contract schemas, security checklist, eval plan, roadmap |
| `.env.example` | Optional API keys (Google Custom Search, Reddit). Pack works without any; skills fall back to Claude Code WebSearch/WebFetch |
| `LICENSE` | Apache-2.0 |
| `.claude/settings.local.json` | Local Claude Code overrides (currently a `graphify` skill override) |
| `.serena/` | Serena LSP tooling config and cache. Not part of the pack |

## Subdirectories

| Directory | Purpose |
|-----------|---------|
| `skills/` | The 12 skills, one directory each with `SKILL.md` + `references/` (see `skills/AGENTS.md`) |
| `contracts/` | Schema/template per artifact; defines producer and consumer skills (see `contracts/AGENTS.md`) |
| `eval/` | Test fixtures, rubrics, expected outputs, and prompt-generating runners (see `eval/AGENTS.md`) |
| `docs/` | Installation, usage, contributing, and security guides (see `docs/AGENTS.md`) |

## Artifact Pipeline

Skills run in this order in the orchestrator; each emits one artifact into the user's project directory:

| Step | Skill | Artifact | Contract |
|------|-------|----------|----------|
| 1 | `idea-brief-creator` | `idea_brief.md` | `contracts/idea_brief.md` |
| 2 | `demand-signals` | `signals.md` | `contracts/signals.md` |
| 3 | `problem-segment` | `icp.yaml` | `contracts/icp.yaml` |
| 4 | `competitive-landscape` | `competitors.csv` | `contracts/competitors.csv` |
| 5 | `market-sizing` | `market_size.md` | `contracts/market_size.md` |
| 6 | `pricing-wtp` | `pricing.yaml` | `contracts/pricing.yaml` |
| 7 | `solution-wedge` | `mvp_spec.md` | `contracts/mvp_spec.md` |
| 8 | `gtm-channels` | `gtm_plan.md` | `contracts/gtm_plan.md` |
| 9 | `risk-assessment` | `risks.md` | `contracts/risks.md` |
| 10 | `scorecard-generator` | `scorecard.json` | `contracts/scorecard.json` |
| 11 | `validation-report` | `validation_report.md` | (template in `skills/validation-report/references/report_template.md`) |
| — | `idea-validation-orchestrator` | all of the above | — |

## For AI Agents

### Working In This Directory
- Changing an artifact's shape is a three-place edit: the `contracts/` file, the producing skill's Output Format section, and every consuming skill's Inputs Required section. The contract file lists the consumers.
- Skill names must equal their directory name (kebab-case). The `pack: product-idea-agent` metadata field ties skills together.
- Keep every `SKILL.md` under 500 lines. Move detail into `references/`.
- Skills are installed by copying `skills/*` to `~/.claude/skills/`. Nothing in this repo is imported at runtime by anything else, so there is no build.
- Files named `.DS_Store` are macOS noise, not project files. There is no `.gitignore` yet.

### Testing Requirements
- No automated test suite. Validation is manual: run a fixture prompt through Claude Code with the skills installed, save artifacts to `eval/results/<run>/generated/`, then score with `python eval/runners/run_skillpack.py --score --dir <run>`.
- `eval/runners/` needs Python 3 and `pyyaml` (only when a fixture has a `rubric.yaml`, which all five do).
- After editing a skill, run at least fixture `t1-energy-audit` (the only one with a full set of expected outputs) and confirm the artifact still matches its contract.

### Common Patterns
- Every `SKILL.md` follows the same section order: frontmatter, Quick Start, Inputs Required, Step-by-Step Workflow, Workflow Checklist, Output Format, Edge Cases, References. See `docs/CONTRIBUTING.md` for the template.
- Frontmatter `allowed-tools` is space-delimited and restricts what the skill may call. Research skills get `WebSearch WebFetch`; synthesis skills (`scorecard-generator`, `validation-report`) get only `Read Write`.
- Skills cite sources with URLs and mark confidence (High / Medium / Low). Missing data is reported as such rather than invented.
- Reference files are loaded on demand via `{baseDir}`-relative links at the end of each `SKILL.md`.

## Dependencies

### Internal
- `skills/*` ↔ `contracts/*` (artifact schemas)
- `eval/runners/*` → `eval/fixtures/*` (reads `input.md`, `rubric.yaml`, `expected_outputs/`)

### External
- Claude Code with WebSearch / WebFetch for research skills
- Python 3 + `pyyaml` for the eval runners
- agentskills.io skill format (frontmatter fields `name`, `description`, `license`, `metadata`, `allowed-tools`)

<!-- MANUAL: Any manually added notes below this line are preserved on regeneration -->
