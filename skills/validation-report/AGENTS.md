<!-- Parent: ../AGENTS.md -->
<!-- Generated: 2026-09-15 | Updated: 2026-09-15 -->

# validation-report

## Purpose
Pipeline step 11 and the final deliverable. Pure synthesis, no web access. Reads all ten prior artifacts plus `scorecard.json` and writes a stakeholder-ready `validation_report.md`: executive summary, one section per validation area, key data tables, recommendation, and next steps.

## Key Files

| File | Description |
|------|-------------|
| `SKILL.md` | 318 lines, the longest skill. Review artifacts → executive summary → section narratives → data and visuals → recommendations. Tools: `Read Write` |
| `references/report_template.md` | 408-line full report template, section by section. This is the de facto contract for `validation_report.md`; there is no file for it under `contracts/` |

## Inputs / Outputs
- **Reads**: all prior artifacts; `scorecard.json` is required
- **Writes**: `validation_report.md`
- **Downstream**: none; consumed by the user

## For AI Agents

### Working In This Directory
- The report restates, it does not re-research. If a finding is missing, the report says so and points at the artifact that should contain it.
- Edge cases handled: incomplete artifacts (note gaps, lower confidence), conflicting findings (acknowledge, explain, recommend resolution), borderline verdict (be explicit it is a close call, name deciding factors).
- Verdict and composite in the report must match `scorecard.json` exactly; the report never re-scores.
- Keep `SKILL.md` under 500 lines; it has the least headroom of the twelve. Push new section guidance into `report_template.md`.

### Testing Requirements
- Compare against `eval/fixtures/t1-energy-audit/expected_outputs/validation_report.md`. Confirm every section in `report_template.md` is present and the sources list is deduplicated across artifacts.

### Common Patterns
- Executive summary leads with verdict, composite score, and the three strongest signals and risks.
- Tables are copied from artifacts (TAM/SAM/SOM, competitor summary, risk matrix top rows, scorecard dimensions) rather than paraphrased.

## Dependencies

### Internal
- Every file under `contracts/`, especially `contracts/scorecard.json`

### External
- None (no web tools)

<!-- MANUAL: Any manually added notes below this line are preserved on regeneration -->
