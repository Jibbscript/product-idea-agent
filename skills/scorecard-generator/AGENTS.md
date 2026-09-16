<!-- Parent: ../AGENTS.md -->
<!-- Generated: 2026-09-15 | Updated: 2026-09-15 -->

# scorecard-generator

## Purpose
Pipeline step 10. Pure synthesis, no web access. Pulls evidence from the nine prior artifacts, scores seven dimensions 1–10, computes a weighted composite out of 100, estimates revenue potential, and issues a GO / PIVOT / NO-GO verdict with next steps. Writes `scorecard.json`.

## Key Files

| File | Description |
|------|-------------|
| `SKILL.md` | 246 lines. Gather evidence → score each dimension → composite → revenue potential → recommendation. Tools: `Read Write` |
| `references/scoring_model.md` | Weight rationale per dimension, scoring anchors (what a 3 vs 7 vs 9 looks like), verdict thresholds, revenue indicator bands |

## Inputs / Outputs
- **Reads**: `idea_brief.md`, `signals.md`, `icp.yaml`, `competitors.csv`, `market_size.md`, `pricing.yaml`, `mvp_spec.md`, `gtm_plan.md`, `risks.md`
- **Writes**: `scorecard.json` per `contracts/scorecard.json`
- **Downstream**: `validation-report` (required input), `idea-validation-orchestrator`

## Dimensions and Weights

| Dimension | Weight | Source artifact | Note |
|-----------|--------|-----------------|------|
| `problem_severity` | 0.20 | `icp.yaml`, `signals.md` | |
| `demand_signals` | 0.15 | `signals.md` | |
| `market_size` | 0.15 | `market_size.md` | |
| `execution_difficulty` | 0.15 | `mvp_spec.md`, `risks.md` | inverted: lower = easier |
| `gtm_viability` | 0.15 | `gtm_plan.md`, `pricing.yaml` | |
| `competitive_intensity` | 0.10 | `competitors.csv` | inverted: lower = less competition |
| `timing` | 0.10 | `signals.md`, `risks.md` | |

## For AI Agents

### Working In This Directory
- This is the only artifact the eval scorer machine-checks (JSON parse + top-level key overlap). Output must be strict JSON, no comments, keys as in the contract `template`.
- Weights must sum to 1.0. Changing a weight means editing `contracts/scorecard.json`, `SKILL.md`, `references/scoring_model.md`, and every fixture's `expected_outputs/scorecard.json` (all five fixtures have one).
- Inverted dimensions: the composite formula must account for them, or a highly competitive market would score well. Check `scoring_model.md` before touching the calculation.
- Edge cases handled: missing artifacts (score on available evidence, lower confidence), conflicting evidence (conservative score, note it), borderline (err low), all high scores (sanity-check for bias).

### Testing Requirements
- `python -c "import json; d=json.load(open('scorecard.json')); assert abs(sum(v['weight'] for v in d['scores'].values())-1)<1e-6"`.
- For each fixture, the composite must fall inside `rubric.yaml` → `expectations.composite_score_range` and the verdict must match `expectations.recommendation`.

### Common Patterns
- Every dimension carries an `evidence` string naming the artifact and figure it came from.
- `revenue_potential.indicator` uses `$` to `$$$$` bands defined in `scoring_model.md`.

## Dependencies

### Internal
- `contracts/scorecard.json` and all nine upstream contracts
- `eval/fixtures/*/rubric.yaml` (expected ranges)

### External
- None (no web tools)

<!-- MANUAL: Any manually added notes below this line are preserved on regeneration -->
