<!-- Parent: ../AGENTS.md -->
<!-- Generated: 2026-09-15 | Updated: 2026-09-15 -->

# market-sizing

## Purpose
Pipeline step 5. Defines market boundaries, researches TAM from industry reports, narrows to SAM using the ICP, and estimates a realistic SOM with growth projections and a confidence assessment. Writes `market_size.md`.

## Key Files

| File | Description |
|------|-------------|
| `SKILL.md` | 207 lines. Define boundaries → TAM → SAM → SOM → dynamics and confidence. Tools: `Read Write WebSearch WebFetch` |
| `references/sizing_methods.md` | Top-down, bottom-up, and value-theory methods with worked examples and when to use each |

## Inputs / Outputs
- **Reads**: `idea_brief.md`, `icp.yaml` (required for SAM), `competitors.csv` (optional cross-check), `signals.md`
- **Writes**: `market_size.md` per `contracts/market_size.md`
- **Downstream**: `gtm-channels` (scale planning), `scorecard-generator` (`market_size` dimension), `validation-report`

## For AI Agents

### Working In This Directory
- Every TAM/SAM/SOM figure needs a methodology label (top-down or bottom-up) and a cited source URL; `rubric.yaml` scores "market size plausibility" and "source recency" (within 2 years).
- Edge cases handled: no market reports (bottom-up, adjacent markets, low confidence), market in flux (ranges), conflicting sources (report both, use conservative), very small market (report honestly).
- Step 1 insists on a specific boundary statement ("B2B SaaS compliance automation for US fintech startups"). Keep that example; it anchors the fixture t2.

### Testing Requirements
- Compare against `eval/fixtures/t1-energy-audit/expected_outputs/market_size.md`. Confirm SAM ≤ TAM and SOM ≤ SAM.

### Common Patterns
- Figures are given as ranges with a point estimate when sources disagree.
- Confidence Assessment section explains which figure is weakest and why.

## Dependencies

### Internal
- `contracts/market_size.md`, `contracts/icp.yaml`, `contracts/competitors.csv`

### External
- Claude Code `WebSearch` / `WebFetch`

<!-- MANUAL: Any manually added notes below this line are preserved on regeneration -->
