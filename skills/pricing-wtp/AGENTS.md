<!-- Parent: ../AGENTS.md -->
<!-- Generated: 2026-09-15 | Updated: 2026-09-15 -->

# pricing-wtp

## Purpose
Pipeline step 6. Benchmarks competitor pricing from `competitors.csv`, researches adjacent-market pricing, estimates willingness-to-pay for the ICP, and designs a value ladder (free → starter → pro → enterprise) with unit economics. Writes `pricing.yaml`.

## Key Files

| File | Description |
|------|-------------|
| `SKILL.md` | 205 lines. Competitor pricing → adjacent markets → WTP estimate → value ladder → unit economics. Tools: `Read Write WebSearch WebFetch` |
| `references/pricing_models.md` | Subscription, usage, freemium, one-time, and hybrid models; anchoring and tiering psychology; when each fits |

## Inputs / Outputs
- **Reads**: `idea_brief.md`, `competitors.csv` (price_low / price_high / pricing_model columns), `icp.yaml` (buyer context)
- **Writes**: `pricing.yaml` per `contracts/pricing.yaml`
- **Downstream**: `scorecard-generator`, `validation-report`

## For AI Agents

### Working In This Directory
- `competitor_benchmarks` entries in the output should match rows in `competitors.csv` by name.
- Edge cases handled: no visible pricing (archive.org, reviews, press; estimate by category), highly variable (report range, consider usage-based), enterprise-only (ACV benchmarks), price-sensitive (alternative monetization).
- Value ladder tiers and their `purpose` field (acquisition / conversion / expansion) are fixed by the contract.

### Testing Requirements
- Output must parse: `python -c "import yaml; yaml.safe_load(open('pricing.yaml'))"`.
- Compare against `eval/fixtures/t1-energy-audit/expected_outputs/pricing.yaml`.

### Common Patterns
- WTP is expressed as a range with a confidence level and the evidence behind it (competitor anchors, survey data, forum comments).
- Unit economics section states assumed CAC and gross margin so `gtm-channels` and `scorecard-generator` can reuse them.

## Dependencies

### Internal
- `contracts/pricing.yaml`, `contracts/competitors.csv`, `contracts/icp.yaml`

### External
- Claude Code `WebSearch` / `WebFetch`

<!-- MANUAL: Any manually added notes below this line are preserved on regeneration -->
