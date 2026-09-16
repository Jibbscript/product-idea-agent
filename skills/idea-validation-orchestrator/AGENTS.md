<!-- Parent: ../AGENTS.md -->
<!-- Generated: 2026-09-15 | Updated: 2026-09-15 -->

# idea-validation-orchestrator

## Purpose
Entry point for a full validation. Runs the 11 skills in order, grouped into five phases (Discovery, Customer & Market, Strategy, Assessment, Synthesis), reports progress from which artifacts already exist on disk, and supports resuming from any step or running a single step. It owns no artifact of its own; it sequences the others and writes everything into the current project directory.

## Key Files

| File | Description |
|------|-------------|
| `SKILL.md` | 201 lines. Step list, progress-and-resumption phase table, full / partial / single-step invocation modes, artifact locations, time estimates (2–3 h total). Tools: `Read Write WebSearch WebFetch Grep Edit` (union of all skills) |
| `references/workflow_guide.md` | Per-phase guidance: what to check before moving on, how artifacts feed forward, common pitfalls, and the named workflows (new idea, pivot assessment, investment readiness, quick feasibility, competitive deep dive) |

## Step Order

| Phase | Steps | Skills |
|-------|-------|--------|
| 1 Discovery | 1–2 | `idea-brief-creator`, `demand-signals` |
| 2 Customer & Market | 3–5 | `problem-segment`, `competitive-landscape`, `market-sizing` |
| 3 Strategy | 6–8 | `pricing-wtp`, `solution-wedge`, `gtm-channels` |
| 4 Assessment | 9–10 | `risk-assessment`, `scorecard-generator` |
| 5 Synthesis | 11 | `validation-report` |

## For AI Agents

### Working In This Directory
- This file is the source of truth for step numbering. `README.md`, `docs/USAGE.md`, `eval/runners/run_skillpack.py` (`SKILLPACK_PROMPT`), and `references/workflow_guide.md` all repeat the list; update them together.
- Adding or reordering a skill: edit the ASCII pipeline diagram, the Progress and Resumption phase table, the Validation Timeline table, and the Artifact Locations tree, all in `SKILL.md`.
- Artifacts are written flat into `./` of the user's project. There is no artifacts subdirectory; do not introduce one without updating every skill's Inputs section.
- The eval skill-pack prompt invokes this skill by name, so renaming it breaks `run_skillpack.py`.

### Testing Requirements
- Run `eval/fixtures/t1-energy-audit/input.md` end to end and confirm all 11 files listed under Artifact Locations exist and the scorecard verdict is GO within 70–85.

### Common Patterns
- Resume phrasing users are told to use: "Continue validation from step X". Keep that string; `docs/USAGE.md` documents it.
- Each step gate is "artifact exists and conforms to its contract" before the next skill starts.

## Dependencies

### Internal
- All eleven sibling skills; `contracts/` for the per-step gate

### External
- Claude Code tools listed in `allowed-tools`

<!-- MANUAL: Any manually added notes below this line are preserved on regeneration -->
