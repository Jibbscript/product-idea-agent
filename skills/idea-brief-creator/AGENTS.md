<!-- Parent: ../AGENTS.md -->
<!-- Generated: 2026-09-15 | Updated: 2026-09-15 -->

# idea-brief-creator

## Purpose
Pipeline step 1. Turns a raw idea (chat text, notes) into a structured `idea_brief.md` with one-line pitch, problem statement, target customer, solution hypothesis, key assumptions, and success metrics. Every other skill reads this artifact, so it is the root of the dependency graph. The only skill that asks the user clarifying questions by design.

## Key Files

| File | Description |
|------|-------------|
| `SKILL.md` | 134 lines. Extract concept → craft pitch → fill sections → mark unknowns → write brief. Tools: `Read Write Edit` (no web access) |
| `references/brief_template.md` | The `idea_brief.md` template with per-field guidance; mirrors `contracts/idea_brief.md` |
| `references/examples.md` | Worked briefs (B2C mobile app, B2B SaaS, etc.), the first being the t1 energy-audit fixture idea |

## Inputs / Outputs
- **Reads**: user's idea description; optional market hints or prior research
- **Writes**: `idea_brief.md` per `contracts/idea_brief.md`
- **Downstream**: `demand-signals`, `problem-segment`, `competitive-landscape`, then everything else

## For AI Agents

### Working In This Directory
- This skill has no `WebSearch`. Do not add research steps here; that is `demand-signals`' job.
- Edge cases the workflow already handles: vague input (draft with explicit unknowns), multiple ideas (split into separate briefs), solution-first framing (redirect to problem), existing product (frame as feature or pivot).
- Changing the brief's sections means updating `contracts/idea_brief.md`, `references/brief_template.md`, `references/examples.md`, and the Inputs sections of the three direct consumers.

### Testing Requirements
- Feed `eval/fixtures/t1-energy-audit/input.md` and compare to `eval/fixtures/t1-energy-audit/expected_outputs/idea_brief.md`.

### Common Patterns
- Unknowns are left as bracketed placeholders with a note, not guessed.
- Assumptions are written as testable statements so `risk-assessment` can turn them into must-be-true items.

## Dependencies

### Internal
- `contracts/idea_brief.md`

### External
- None

<!-- MANUAL: Any manually added notes below this line are preserved on regeneration -->
