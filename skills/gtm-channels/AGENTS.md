<!-- Parent: ../AGENTS.md -->
<!-- Generated: 2026-09-15 | Updated: 2026-09-15 -->

# gtm-channels

## Purpose
Pipeline step 8. Maps where the ICP discovers, consumes, engages, and buys; picks acquisition channels with CAC estimates and priority; designs growth loops, partnerships, a launch strategy, and 90-day milestones. Writes `gtm_plan.md`.

## Key Files

| File | Description |
|------|-------------|
| `SKILL.md` | 243 lines. Map customer presence → viable channels → CAC per channel → growth loops → launch plan. Tools: `Read Write WebSearch WebFetch` |
| `references/channel_playbooks.md` | Per-channel playbooks (content/SEO, paid social, community, partnerships, direct sales, product-led, marketplaces) with typical CAC ranges and fit criteria |

## Inputs / Outputs
- **Reads**: `idea_brief.md`, `icp.yaml` (where customers are), `market_size.md` (scale), `mvp_spec.md` (positioning), `pricing.yaml` (CAC ceiling)
- **Writes**: `gtm_plan.md` per `contracts/gtm_plan.md`
- **Downstream**: `risk-assessment` (GTM risks), `scorecard-generator` (`gtm_viability` dimension), `validation-report`

## For AI Agents

### Working In This Directory
- Primary channel table columns are fixed: Channel, CAC Est., Volume (high/med/low), Priority.
- Defaults encoded in Edge Cases: B2B with no standout channel → content + community; B2C → paid social; enterprise → direct sales with content for demand gen; limited budget → organic, referrals, design partners.
- CAC estimates should be consistent with WTP and gross margin in `pricing.yaml`; the scorecard cross-checks them.

### Testing Requirements
- Compare against `eval/fixtures/t1-energy-audit/expected_outputs/gtm_plan.md`. Confirm at least one growth loop and the 90-day milestone list are present.

### Common Patterns
- Channels are ranked, not listed; priority 1–3 with a rationale each.
- Growth loops are described as input → action → output → reinvestment so risk-assessment can spot the weak link.

## Dependencies

### Internal
- `contracts/gtm_plan.md`, `contracts/icp.yaml`, `contracts/market_size.md`, `contracts/mvp_spec.md`

### External
- Claude Code `WebSearch` / `WebFetch`

<!-- MANUAL: Any manually added notes below this line are preserved on regeneration -->
