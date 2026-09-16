<!-- Parent: ../AGENTS.md -->
<!-- Generated: 2026-09-15 | Updated: 2026-09-15 -->

# contracts

## Purpose
One file per pipeline artifact, defining its schema and naming the skill that produces it and the skills that consume it. These are the interface between skills: a producer must emit exactly this shape, and a consumer may rely on it. The file format matches the artifact format (markdown template, YAML with comments, JSON Schema, or a commented CSV header).

## Key Files

| File | Format | Producer | Consumers |
|------|--------|----------|-----------|
| `idea_brief.md` | Markdown template | `idea-brief-creator` | `demand-signals`, `problem-segment`, `competitive-landscape`, all downstream |
| `signals.md` | Markdown template | `demand-signals` | `market-sizing`, `scorecard-generator`, `validation-report` |
| `icp.yaml` | YAML skeleton | `problem-segment` | `market-sizing`, `pricing-wtp`, `solution-wedge`, `gtm-channels` |
| `competitors.csv` | Commented CSV header + column table | `competitive-landscape` | `pricing-wtp`, `solution-wedge`, `market-sizing`, `scorecard-generator` |
| `market_size.md` | Markdown template | `market-sizing` | `gtm-channels`, `scorecard-generator`, `validation-report` |
| `pricing.yaml` | YAML skeleton | `pricing-wtp` | `scorecard-generator`, `validation-report` |
| `mvp_spec.md` | Markdown template | `solution-wedge` | `gtm-channels`, `risk-assessment`, `validation-report` |
| `gtm_plan.md` | Markdown template | `gtm-channels` | `risk-assessment`, `scorecard-generator`, `validation-report` |
| `risks.md` | Markdown template | `risk-assessment` | `scorecard-generator`, `validation-report` |
| `scorecard.json` | JSON Schema draft-07 with embedded `template` | `scorecard-generator` | `validation-report`, `idea-validation-orchestrator` |

There is no contract file for `validation_report.md`; its template lives in `skills/validation-report/references/report_template.md`.

## Scorecard Dimensions
`scorecard.json` fixes seven weighted dimensions (weights sum to 1.0): `problem_severity` 0.20, `demand_signals` 0.15, `market_size` 0.15, `execution_difficulty` 0.15, `gtm_viability` 0.15, `competitive_intensity` 0.10, `timing` 0.10. Two are inverted (lower is better): `competitive_intensity` and `execution_difficulty`. Composite is a weighted average out of 100; verdict is `GO`, `PIVOT`, or `NO-GO`.

## For AI Agents

### Working In This Directory
- A contract change is never local. Update the producer skill's Output Format, every consumer's Inputs Required, `eval/fixtures/t1-energy-audit/expected_outputs/<artifact>`, and the blueprint's section 7 if you want the design doc to stay honest.
- Keep enum values in sync with the skills that emit them: `competitors.csv` `category` (direct / indirect / alternative), `pricing_model` (subscription / onetime / freemium / usage / free), `market_position` (leader / challenger / niche / emerging).
- CSV rows use semicolons inside a cell for lists (`key_features`, `strengths`, `weaknesses`) so commas stay as delimiters.
- `scorecard.json` is the only machine-validated artifact (the eval runner parses it as JSON and checks key overlap). Keep it valid JSON Schema.

### Testing Requirements
- `python -c "import json; json.load(open('contracts/scorecard.json'))"` after editing the JSON contract.
- `python -c "import yaml; yaml.safe_load(open('contracts/icp.yaml'))"` (and `pricing.yaml`) to confirm the YAML skeletons still parse despite placeholder brackets.

### Common Patterns
- Placeholders are written `[description]`. Skills replace every one; an unresolved bracket in an emitted artifact is a bug.
- Markdown contracts open with Purpose / Producer / Consumers, then a fenced `Schema` block, then field notes.
- Every artifact ends with a Sources or confidence section; consumers read confidence to propagate uncertainty downstream.

## Dependencies

### Internal
- Consumed by every skill under `skills/`
- Mirrored by `eval/fixtures/t1-energy-audit/expected_outputs/`

### External
- JSON Schema draft-07 (for `scorecard.json`)

<!-- MANUAL: Any manually added notes below this line are preserved on regeneration -->
