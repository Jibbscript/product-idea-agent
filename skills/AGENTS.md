<!-- Parent: ../AGENTS.md -->
<!-- Generated: 2026-09-15 | Updated: 2026-09-15 -->

# skills

## Purpose
The deliverable of this repo: 12 Claude Code skills, one directory each. Every directory holds a `SKILL.md` (the instructions Claude loads on trigger) and a `references/` folder with deeper domain material loaded on demand. Copying these directories to `~/.claude/skills/` installs them.

## Key Files
None at this level. `.DS_Store` is macOS noise.

## Subdirectories

| Directory | Step | Reads | Writes | allowed-tools |
|-----------|------|-------|--------|---------------|
| `idea-brief-creator/` | 1 | raw idea text | `idea_brief.md` | Read Write Edit |
| `demand-signals/` | 2 | `idea_brief.md` | `signals.md` | Read Write WebSearch WebFetch Grep |
| `problem-segment/` | 3 | `idea_brief.md`, `signals.md` (opt) | `icp.yaml` | Read Write WebSearch WebFetch |
| `competitive-landscape/` | 4 | `idea_brief.md` | `competitors.csv` | Read Write WebSearch WebFetch Grep |
| `market-sizing/` | 5 | `idea_brief.md`, `icp.yaml`, `competitors.csv` (opt) | `market_size.md` | Read Write WebSearch WebFetch |
| `pricing-wtp/` | 6 | `idea_brief.md`, `competitors.csv`, `icp.yaml` | `pricing.yaml` | Read Write WebSearch WebFetch |
| `solution-wedge/` | 7 | `idea_brief.md`, `competitors.csv`, `icp.yaml` | `mvp_spec.md` | Read Write WebSearch |
| `gtm-channels/` | 8 | `idea_brief.md`, `icp.yaml`, `market_size.md`, `mvp_spec.md` | `gtm_plan.md` | Read Write WebSearch WebFetch |
| `risk-assessment/` | 9 | all prior, esp. `mvp_spec.md`, `gtm_plan.md`, `competitors.csv` | `risks.md` | Read Write WebSearch |
| `scorecard-generator/` | 10 | all nine prior artifacts | `scorecard.json` | Read Write |
| `validation-report/` | 11 | all prior + `scorecard.json` | `validation_report.md` | Read Write |
| `idea-validation-orchestrator/` | — | user's idea | drives steps 1–11 | Read Write WebSearch WebFetch Grep Edit |

Each has its own `AGENTS.md`.

## For AI Agents

### Working In This Directory
- Directory name, frontmatter `name`, and the skill's self-references must all match. Renaming a skill means updating the orchestrator's step list, `README.md`, `docs/USAGE.md`, and any contract that names it as producer or consumer.
- Adding a skill: copy the section structure from `docs/CONTRIBUTING.md`, add a contract under `contracts/` if it emits a new artifact, and wire it into `idea-validation-orchestrator/SKILL.md`.
- `SKILL.md` hard limit is 500 lines. Current files run 120–313 lines. Push detail down into `references/`.
- The `description` field is what triggers the skill. It must state both what the skill does and when to use it, in third person.
- Do not add `scripts/` or `assets/` dirs unless a skill actually needs deterministic code; none do today.

### Testing Requirements
- Trigger the skill in Claude Code with a fixture from `eval/fixtures/*/input.md` and diff the emitted artifact against the matching `contracts/` schema.
- Check the `allowed-tools` line still covers every tool the coverage and How to Work sections rely on.

### Common Patterns
- Section order in every `SKILL.md`: Outcome → Inputs Required → Who reads <artifact> → What <artifact> Must Cover → How to Work → Constraints → What a strong <artifact> looks like → Output Format → Working <domain> → Edge Cases → References. `idea-validation-orchestrator` documents the pipeline instead and keeps its own section order.
- Edge Cases always covers missing data, conflicting data, and the "too much / too little" case for that skill's domain.
- Outputs carry a confidence level and cite sources by URL. Research skills flag anything unverifiable as low confidence rather than dropping it. The sourced / estimated / unverified marking introduced in each skill's Working section is the same discipline applied per figure rather than per artifact.
- Scores in artifacts use fixed scales: 1–10 for signal and dimension scores, 1–5 × 1–5 for risk severity × likelihood.

## Dependencies

### Internal
- `contracts/` for every artifact's schema
- `eval/fixtures/` for realistic inputs

### External
- Claude Code tool names in `allowed-tools`: `Read`, `Write`, `Edit`, `Grep`, `WebSearch`, `WebFetch`

<!-- MANUAL: Any manually added notes below this line are preserved on regeneration -->
