<!-- Parent: ../AGENTS.md -->
<!-- Generated: 2026-09-15 | Updated: 2026-09-15 -->

# problem-segment

## Purpose
Pipeline step 3. Lists 3–5 candidate customer segments, researches each, scores problem severity and ability to pay, and picks a primary segment. Writes `icp.yaml` with demographics, firmographics (B2B only), psychographics, and behaviors.

## Key Files

| File | Description |
|------|-------------|
| `SKILL.md` | 185 lines. Identify segments → research characteristics → assess severity → prioritize → write ICP. Tools: `Read Write WebSearch WebFetch` |
| `references/icp_framework.md` | The ICP canvas: segment definition, jobs, pains, gains, buying process, and severity scoring guidance |

## Inputs / Outputs
- **Reads**: `idea_brief.md`; `signals.md` optional but improves segment evidence
- **Writes**: `icp.yaml` per `contracts/icp.yaml`
- **Downstream**: `market-sizing` (SAM depends on it), `pricing-wtp`, `solution-wedge`, `gtm-channels`

## For AI Agents

### Working In This Directory
- `icp.yaml` is YAML consumed by four skills. Field names in `contracts/icp.yaml` are the interface; do not rename keys without updating consumers.
- `firmographics` block is omitted for B2C, so consumers must treat it as optional.
- Edge cases handled: multiple valid segments (pick highest severity × ability to pay, list others as secondary), B2B vs B2C unclear (follow who pays), no segment data (analogous markets, low confidence), international (per-region ICPs).

### Testing Requirements
- Output must parse: `python -c "import yaml; yaml.safe_load(open('icp.yaml'))"`.
- Compare against `eval/fixtures/t1-energy-audit/expected_outputs/icp.yaml`.

### Common Patterns
- Severity is justified with evidence from `signals.md` quotes where available.
- Secondary segments are recorded so `gtm-channels` can plan expansion.

## Dependencies

### Internal
- `contracts/icp.yaml`, `contracts/idea_brief.md`, `contracts/signals.md`

### External
- Claude Code `WebSearch` / `WebFetch`

<!-- MANUAL: Any manually added notes below this line are preserved on regeneration -->
