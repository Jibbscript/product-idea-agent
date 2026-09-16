<!-- Parent: ../AGENTS.md -->
<!-- Generated: 2026-09-15 | Updated: 2026-09-15 -->

# solution-wedge

## Purpose
Pipeline step 7. Maps user jobs (functional, emotional, social) from the brief and ICP, force-ranks features into P0 / P1 / P2, chooses a technical approach, and states the differentiation wedge against the gaps found in `competitors.csv`. Writes `mvp_spec.md`.

## Key Files

| File | Description |
|------|-------------|
| `SKILL.md` | 213 lines. Map user jobs → minimum feature set → technical approach → differentiation → timeline. Tools: `Read Write WebSearch` |
| `references/mvp_principles.md` | MVP philosophy, scoping frameworks, wedge strategies, and anti-patterns (feature creep, platform sprawl) |

## Inputs / Outputs
- **Reads**: `idea_brief.md`, `competitors.csv` (weaknesses column → gaps), `icp.yaml` (prioritization)
- **Writes**: `mvp_spec.md` per `contracts/mvp_spec.md`
- **Downstream**: `gtm-channels` (positioning), `risk-assessment` (technical risks), `validation-report`

## For AI Agents

### Working In This Directory
- P0 features each cite the user job they address; the contract format is `[Feature]: [Description] - [User Job Addressed]`.
- Edge cases handled: too many must-haves (ask "would users pay with only this subset?"), no differentiator (segment specialization or execution wedge, possibly rethink), technical uncertainty (flag as risk, prototype first), platform uncertainty (one platform first).
- Has `WebSearch` but no `WebFetch`; it researches technology options, not competitors.

### Testing Requirements
- Compare against `eval/fixtures/t1-energy-audit/expected_outputs/mvp_spec.md`. Check the Open Questions section is non-empty; `risk-assessment` reads it.

### Common Patterns
- Differentiation is stated relative to named competitors from the CSV, not in the abstract.
- Timeline and Success Criteria sections give `gtm-channels` its 90-day frame.

## Dependencies

### Internal
- `contracts/mvp_spec.md`, `contracts/competitors.csv`, `contracts/icp.yaml`

### External
- Claude Code `WebSearch`

<!-- MANUAL: Any manually added notes below this line are preserved on regeneration -->
