<!-- Parent: ../AGENTS.md -->
<!-- Generated: 2026-09-15 | Updated: 2026-09-15 -->

# eval

## Purpose
Evaluation for the plugin, in three layers. `fable_prompt_bench.py` lints the prompt surface (free, every PR) and `test_fable_prompt_bench.py` tests its integrity checks. `cases/` is the `claude plugin eval` suite that measures behavior against a no-plugin baseline (paid, on demand). `runners/` are the older prompt generators and placeholder scorer, kept until the `full` case reproduces the t1 A/B findings. Five fixture ideas span the expected verdict range (GO through PIVOT).

## Key Files
None at this level. `.DS_Store` is macOS noise.

## Subdirectories

| Directory | Purpose |
|-----------|---------|
| `cases/` | `claude plugin eval` suite, declared by `experimental.evals` in `.claude-plugin/plugin.json`. Results land in `cases/results/` (gitignored) |
| `fixtures/` | Five test ideas, each with `input.md`, `rubric.yaml`, and `expected_outputs/` (see `fixtures/AGENTS.md`) |
| `runners/` | `run_baseline.py` (no skills) and `run_skillpack.py` (with skills, plus `--score`) (see `runners/AGENTS.md`) |
| `results/` | Output directory for runs. Contains only `.gitkeep`; runs are written here as `<mode>_<fixture>_<timestamp>/` |

## Plugin Eval Suite (`cases/`)

Every case is one `case.yaml` (schema 1.1) under `cases/<tag>/<name>/`, pairing a result grader with a process grader. Seeded cases have a `seed.sh` that copies files from `fixtures/t1-energy-audit/`, which stays the single source; the scaffold runs as `bash <case>/seed.sh` in the empty run workspace.

| Tag | Cases | What it checks | Run with |
|-----|-------|----------------|----------|
| `smoke` | 12, one per skill | A request that doesn't name the skill fires `product-idea-agent:<skill>` (`tool_used: Skill`) | `claude plugin eval . --tag smoke --ablation none` |
| `offline` | scorecard-generator, validation-report | Artifact exists and has its contract's keys; zero WebSearch/WebFetch calls although both are granted, which tests `disallowed-tools`; report verdict and composite match the seeded scorecard (regex on its Recommendation or Verdict and Composite lines) | `claude plugin eval . --tag offline --scaffold --allow-tools Write WebSearch WebFetch` |
| `research` | discovery, customer-market, strategy, risk | Each phase, seeded with the fixture's earlier artifacts, writes contract-shaped artifacts and searched the web; one run per arm, each under the 3,600 s cap | `claude plugin eval . --tag research --scaffold --allow-tools Write Edit WebSearch WebFetch` |
| `full` | t1-energy-audit | All eleven artifacts end to end against the no-plugin baseline; reported, not a gate | same flags as `research` |

For stable, comparable numbers pin models: `--model claude-fable-5-1` (or `claude-opus-5-5`) `--judge-model claude-haiku-4-5-20251001`, and bound spend with `--max-cost-usd`. `.github/workflows/plugin-eval.yml` runs any tag this way on manual dispatch. The default `--threshold` is 1.0. Regexes run over the produced file (`target: { source: file, path: ... }`) and check structure only; keep `llm` graders to short verdicts.

## Evaluation Loop (runners, pre-plugin)

1. `python eval/runners/run_skillpack.py --fixture t1-energy-audit` writes `results/skillpack_t1-energy-audit_<ts>/skillpack_prompt.md`, copies `expected/`, and writes `evaluation_info.json`.
2. Paste the prompt into a Claude Code session with the plugin loaded (`claude --plugin-dir .` or the installed plugin); save the 11 artifacts to that run's `generated/` directory.
3. `python eval/runners/run_skillpack.py --score --dir results/skillpack_t1-energy-audit_<ts>` writes `scores.json`.
4. Repeat with `run_baseline.py` for the no-skills comparison. The baseline runner has no scorer; its "next steps" message references a `score_results.py` that does not exist. Use the skillpack scorer on its directory instead (it only needs `evaluation_info.json` and `expected/`).

## For AI Agents

### Working In This Directory
- Only `t1-energy-audit` has a full set of 11 expected outputs. Fixtures t2–t5 ship only `scorecard.json`, so scoring them reports one artifact.
- The scorer is a placeholder: per-artifact metrics are length ratio and word Jaccard, and rubric dimension scores are all set to the artifact completion rate. Rubric `criteria` are loaded but not evaluated. Do not treat `composite_score` as a quality measure yet.
- The two runners duplicate `load_fixture` and `list_fixtures`. If you change fixture layout, change both.
- Never commit run output under `results/` or `cases/results/`.
- Changing a contract's required sections means updating the matching regexes in `cases/*/*/case.yaml`; changing `fixtures/t1-energy-audit/expected_outputs/` changes what the seeded cases start from (the `offline/validation-report` verdict regex names the seeded scorecard's GO / 71).

### Testing Requirements
- `python3 -m unittest eval/test_fable_prompt_bench.py` passes, and `python3 eval/fable_prompt_bench.py` prints no `!!` lines.
- `python eval/runners/run_skillpack.py --list` should print all five fixture ids.
- Requires Python 3.9+ (uses `list[str]` annotations) and `pyyaml`.

### Common Patterns
- Fixture ids are `t<N>-<slug>`; a directory counts as a fixture only if it contains `input.md`.
- Rubrics use five weighted dimensions: correctness 0.25, usefulness 0.25, citation_quality 0.20, reproducibility 0.15, time_to_answer 0.15, each with 1–5 point criteria totaling 100.

## Dependencies

### Internal
- `../skills/` (`SKILLS_DIR` in `run_skillpack.py` locates the plugin root for its printed next steps)
- `../.claude-plugin/plugin.json` (the benchmark reads the plugin name; `experimental.evals` points at `cases/`)
- `../contracts/` (expected outputs must match)

### External
- Python 3.9+, `pyyaml`

<!-- MANUAL: Any manually added notes below this line are preserved on regeneration -->
