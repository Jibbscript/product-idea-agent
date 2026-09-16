<!-- Parent: ../AGENTS.md -->
<!-- Generated: 2026-09-15 | Updated: 2026-09-15 -->

# risk-assessment

## Purpose
Pipeline step 9. Reads every prior artifact, identifies risks by category (technical, market, competitive, regulatory, execution, financial), scores each as severity 1–5 × likelihood 1–5, proposes mitigations, and lists must-be-true assumptions, constraints, and dependencies. Writes `risks.md`.

## Key Files

| File | Description |
|------|-------------|
| `SKILL.md` | 255 lines. Review prior artifacts → identify by category → score → mitigate → must-be-true assumptions. Tools: `Read Write WebSearch` |
| `references/risk_categories.md` | Deep dive per category with prompting questions, common failure modes, and mitigation patterns |

## Inputs / Outputs
- **Reads**: all prior artifacts; especially `mvp_spec.md` (technical), `gtm_plan.md` (channel), `competitors.csv` (competitive)
- **Writes**: `risks.md` per `contracts/risks.md`
- **Downstream**: `scorecard-generator` (`execution_difficulty` dimension), `validation-report`

## For AI Agents

### Working In This Directory
- Score = Severity × Likelihood; anything ≥ 15 goes into the Critical Risks section. That threshold appears in the contract and the fixture rubric; do not change it in one place only.
- Edge cases handled: too many risks (top 10–15, group the rest as monitored), risks look manageable (document why, still add contingencies), existential risk (flag prominently, may recommend pivot), regulatory uncertainty (high risk, recommend legal review).
- Must-be-true assumptions should trace back to Key Assumptions in `idea_brief.md` and Open Questions in `mvp_spec.md`.

### Testing Requirements
- Compare against `eval/fixtures/t1-energy-audit/expected_outputs/risks.md`. Confirm the fixture rubric's `key_risks` (sensor accuracy, DIY adoption) are present for t1.

### Common Patterns
- Risk matrix rows are one line each; mitigation column is an action, not a hope.
- Categories use the exact names from `references/risk_categories.md` so the scorecard can count per category.

## Dependencies

### Internal
- `contracts/risks.md` and every upstream contract

### External
- Claude Code `WebSearch` (regulatory and technical fact-checks)

<!-- MANUAL: Any manually added notes below this line are preserved on regeneration -->
