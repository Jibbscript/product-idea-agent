<!-- Parent: ../AGENTS.md -->
<!-- Generated: 2026-09-15 | Updated: 2026-09-15 -->

# competitive-landscape

## Purpose
Pipeline step 4. Finds direct competitors, indirect alternatives, and status-quo substitutes; captures pricing, positioning, features, strengths, weaknesses, and a 1–10 threat level per competitor; identifies gaps. Writes `competitors.csv`.

## Key Files

| File | Description |
|------|-------------|
| `SKILL.md` | 169 lines. Direct competitors → indirect alternatives → positioning and pricing → feature gaps → CSV. Tools: `Read Write WebSearch WebFetch Grep` |
| `references/analysis_framework.md` | Competitor categories, positioning map, feature-coverage matrix, threat scoring, and gap-identification method |

## Inputs / Outputs
- **Reads**: `idea_brief.md`; target segment context (from `icp.yaml` if present)
- **Writes**: `competitors.csv` per `contracts/competitors.csv` (13 columns, header required)
- **Downstream**: `pricing-wtp` (benchmarks), `solution-wedge` (gaps), `market-sizing` (sanity check), `scorecard-generator` (`competitive_intensity` dimension)

## For AI Agents

### Working In This Directory
- CSV enum columns must use the exact values in the contract: `category` direct / indirect / alternative; `pricing_model` subscription / onetime / freemium / usage / free; `market_position` leader / challenger / niche / emerging.
- List cells (`key_features`, `strengths`, `weaknesses`) use `;` separators. Quote any cell containing a comma.
- Edge cases handled: zero direct competitors (red flag, dig for alternatives), too many (top 5–7 by threat), sparse info (LinkedIn, press, case studies, note limits), fast-moving market (date the research).
- Search heuristics live under `### Direct Competitors` in `SKILL.md`: Product Hunt, G2, Capterra, "[X] alternatives" queries.

### Testing Requirements
- Output must parse with `python -c "import csv; list(csv.DictReader(open('competitors.csv')))"` and have the 13 contract columns.
- Compare against `eval/fixtures/t1-energy-audit/expected_outputs/competitors.csv`.

### Common Patterns
- The status quo (manual process, spreadsheets, hiring a consultant) is listed as an `alternative` row; it is often the real competitor.
- Threat level combines market position, feature overlap, and funding.

## Dependencies

### Internal
- `contracts/competitors.csv`, `contracts/idea_brief.md`

### External
- Claude Code `WebSearch` / `WebFetch`

<!-- MANUAL: Any manually added notes below this line are preserved on regeneration -->
