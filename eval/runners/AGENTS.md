<!-- Parent: ../AGENTS.md -->
<!-- Generated: 2026-09-15 | Updated: 2026-09-15 -->

# runners

## Purpose
Two CLI scripts that turn a fixture into a prompt and, for the skill-pack mode, score saved artifacts. Neither calls an LLM; they prepare inputs and grade outputs around a manual Claude Code run.

## Key Files

| File | Description |
|------|-------------|
| `run_baseline.py` | Builds a no-skills prompt (`BASELINE_PROMPT`) that asks for all 11 deliverables directly. Flags: `--fixture`, `--all`, `--list`, `--output`. Writes `baseline_prompt.md` + `evaluation_info.json` into `results/baseline_<id>_<ts>/` |
| `run_skillpack.py` | Builds a prompt (`SKILLPACK_PROMPT`) that invokes `idea-validation-orchestrator`. Same flags plus `--score --dir <run>`. Also copies `expected/` into the run dir and, on `--score`, compares `generated/` to `expected/` and writes `scores.json` |

## Scoring (in `run_skillpack.py`)
- `score_artifact()`: length ratio, word-set Jaccard, and for `.json` files a parse check plus top-level key overlap.
- `score_results()`: per-rubric-dimension score is currently `artifacts_generated / expected × 100` for every dimension. Composite is the weight-normalised sum. Criteria in the rubric are not evaluated.

## For AI Agents

### Working In This Directory
- Both scripts hard-code `EVAL_DIR = Path(__file__).parent.parent`, so run them from anywhere; paths resolve relative to `eval/`.
- `load_fixture` and `list_fixtures` are copy-pasted between the two files. Change both or extract a shared module.
- `run_baseline.py` prints a follow-up pointing at `score_results.py`, which does not exist. The skillpack scorer works on a baseline run directory since it only needs `evaluation_info.json` and `expected/`; but the baseline runner does not copy `expected/`, so you must add that step or copy it by hand first.
- Prompt templates use `str.format`, so any literal `{` in an `input.md` would break formatting. Fixtures avoid braces.
- `SKILLS_DIR` is defined but unused.

### Testing Requirements
- `python eval/runners/run_skillpack.py --list` and `python eval/runners/run_baseline.py --list` both print five fixtures.
- After changing scoring, run `--score` against a directory with a hand-made `generated/scorecard.json` and confirm `scores.json` has `valid_json: true`.

### Common Patterns
- Run directories are `<mode>_<fixture>_<YYYYMMDD_HHMMSS>` under `eval/results/`.
- `evaluation_info.json` carries `mode`, `fixture_id`, `expected_outputs` list, and the rubric; the scorer reads only this file plus the two subdirectories.

## Dependencies

### Internal
- `../fixtures/` (inputs), `../results/` (outputs)

### External
- Python 3.9+ standard library; `pyyaml` (imported lazily inside `load_fixture`)

<!-- MANUAL: Any manually added notes below this line are preserved on regeneration -->
