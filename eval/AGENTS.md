<!-- Parent: ../AGENTS.md -->
<!-- Generated: 2026-09-15 | Updated: 2026-09-15 -->

# eval

## Purpose
Evaluation harness for measuring whether the skill pack beats a plain prompt. Five fixture ideas span the expected verdict range (GO through PIVOT). Runners generate the prompt for a fixture in either mode, and a scorer compares saved artifacts against expected outputs. LLM execution is not automated: you run the generated prompt in Claude Code yourself, save the artifacts, then score.

## Key Files
None at this level. `.DS_Store` is macOS noise.

## Subdirectories

| Directory | Purpose |
|-----------|---------|
| `fixtures/` | Five test ideas, each with `input.md`, `rubric.yaml`, and `expected_outputs/` (see `fixtures/AGENTS.md`) |
| `runners/` | `run_baseline.py` (no skills) and `run_skillpack.py` (with skills, plus `--score`) (see `runners/AGENTS.md`) |
| `results/` | Output directory for runs. Contains only `.gitkeep`; runs are written here as `<mode>_<fixture>_<timestamp>/` |

## Evaluation Loop

1. `python eval/runners/run_skillpack.py --fixture t1-energy-audit` writes `results/skillpack_t1-energy-audit_<ts>/skillpack_prompt.md`, copies `expected/`, and writes `evaluation_info.json`.
2. Paste the prompt into Claude Code with `skills/*` installed; save the 11 artifacts to that run's `generated/` directory.
3. `python eval/runners/run_skillpack.py --score --dir results/skillpack_t1-energy-audit_<ts>` writes `scores.json`.
4. Repeat with `run_baseline.py` for the no-skills comparison. The baseline runner has no scorer; its "next steps" message references a `score_results.py` that does not exist. Use the skillpack scorer on its directory instead (it only needs `evaluation_info.json` and `expected/`).

## For AI Agents

### Working In This Directory
- Only `t1-energy-audit` has a full set of 11 expected outputs. Fixtures t2–t5 ship only `scorecard.json`, so scoring them reports one artifact.
- The scorer is a placeholder: per-artifact metrics are length ratio and word Jaccard, and rubric dimension scores are all set to the artifact completion rate. Rubric `criteria` are loaded but not evaluated. Do not treat `composite_score` as a quality measure yet.
- The two runners duplicate `load_fixture` and `list_fixtures`. If you change fixture layout, change both.
- Never commit run output under `results/`.

### Testing Requirements
- `python eval/runners/run_skillpack.py --list` should print all five fixture ids.
- Requires Python 3.9+ (uses `list[str]` annotations) and `pyyaml`.

### Common Patterns
- Fixture ids are `t<N>-<slug>`; a directory counts as a fixture only if it contains `input.md`.
- Rubrics use five weighted dimensions: correctness 0.25, usefulness 0.25, citation_quality 0.20, reproducibility 0.15, time_to_answer 0.15, each with 1–5 point criteria totaling 100.

## Dependencies

### Internal
- `../skills/` (referenced by `SKILLS_DIR` in `run_skillpack.py`, currently unused)
- `../contracts/` (expected outputs must match)

### External
- Python 3.9+, `pyyaml`

<!-- MANUAL: Any manually added notes below this line are preserved on regeneration -->
