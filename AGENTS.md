<!-- Generated: 2026-09-15 | Updated: 2026-09-15 -->

# product-idea-agent

## Purpose
A Claude Code plugin (`product-idea-agent`) that runs end-to-end product idea validation. Twelve composable skills (under `skills/`) turn a raw startup concept into a chain of 11 artifacts ending in a GO / PIVOT / NO-GO scorecard and validation report. Artifact shapes are fixed by contracts in `contracts/`; `eval/` holds fixtures, the prompt-fitness benchmark, the `claude plugin eval` suite and the older prompt runners. There is no application code: the product is the markdown skills plus their schemas. The repository root is both the plugin root and a single-plugin marketplace (`jibbscript`); users install `product-idea-agent@jibbscript`.

## Key Files

| File | Description |
|------|-------------|
| `README.md` | Skill catalog, artifact flow diagram, install and usage summary |
| `product-idea-agent-skill-pack-implementation-blueprint.md` | Design doc the pack was built from: IdeaBrowser reverse-engineering, per-skill specs, contract schemas, security checklist, eval plan, roadmap |
| `.claude-plugin/plugin.json` | Plugin manifest: name (must equal every skill's `metadata.pack`), `version` (the only version authority), `experimental.evals: eval/cases` |
| `.claude-plugin/marketplace.json` | Marketplace `jibbscript` with one entry, `source: "./"`, and no version or component fields |
| `LICENSE` | Apache-2.0 |
| `.claude/settings.local.json` | Local Claude Code overrides (currently a `graphify` skill override) |
| `.serena/` | Serena LSP tooling config and cache. Not part of the pack |

## Subdirectories

| Directory | Purpose |
|-----------|---------|
| `skills/` | The 12 skills, one directory each with `SKILL.md` + `references/` (see `skills/AGENTS.md`) |
| `contracts/` | Schema/template per artifact; defines producer and consumer skills (see `contracts/AGENTS.md`) |
| `eval/` | Fixtures, the prompt-fitness benchmark and its tests, the plugin eval suite (`eval/cases/`), and prompt-generating runners (see `eval/AGENTS.md`) |
| `docs/` | Installation, usage, contributing, and security guides (see `docs/AGENTS.md`) |

## Artifact Pipeline

Skills run in this order in the orchestrator; each emits one artifact into the user's project directory:

| Step | Skill | Artifact | Contract |
|------|-------|----------|----------|
| 1 | `idea-brief-creator` | `idea_brief.md` | `contracts/idea_brief.md` |
| 2 | `demand-signals` | `signals.md` | `contracts/signals.md` |
| 3 | `problem-segment` | `icp.yaml` | `contracts/icp.yaml` |
| 4 | `competitive-landscape` | `competitors.csv` | `contracts/competitors.csv` |
| 5 | `market-sizing` | `market_size.md` | `contracts/market_size.md` |
| 6 | `pricing-wtp` | `pricing.yaml` | `contracts/pricing.yaml` |
| 7 | `solution-wedge` | `mvp_spec.md` | `contracts/mvp_spec.md` |
| 8 | `gtm-channels` | `gtm_plan.md` | `contracts/gtm_plan.md` |
| 9 | `risk-assessment` | `risks.md` | `contracts/risks.md` |
| 10 | `scorecard-generator` | `scorecard.json` | `contracts/scorecard.json` |
| 11 | `validation-report` | `validation_report.md` | (template in `skills/validation-report/references/report_template.md`) |
| — | `idea-validation-orchestrator` | all of the above | — |

## For AI Agents

### Working In This Directory
- Changing an artifact's shape is a three-place edit: the `contracts/` file, the producing skill's Output Format section, and every consuming skill's Inputs Required section. The contract file lists the consumers.
- Skill names must equal their directory name (kebab-case). The `pack: product-idea-agent` metadata field ties skills together.
- Keep every `SKILL.md` under 500 lines. Move detail into `references/`.
- The pack installs only as a plugin. Copying `skills/*` into a skills directory is unsupported, because `${CLAUDE_PLUGIN_ROOT}` is substituted only in plugin skills; do not reintroduce copy-install instructions. Local testing uses `claude --plugin-dir .`. There is no build.
- Skills reference contracts only as `${CLAUDE_PLUGIN_ROOT}/contracts/<artifact>`, and write artifacts to the user's current project directory, never under the plugin root (it is replaced on update).
- Bump `version` in `.claude-plugin/plugin.json` for any change to skills, contracts or manifests; never add a version to the marketplace entry.
- Files named `.DS_Store` are macOS noise, not project files.

### Testing Requirements
- Free, every PR (CI): `claude plugin validate . --strict` and `claude plugin validate .claude-plugin/plugin.json --strict` (the first reads only the manifests, the second also the skills' frontmatter); `python3 -m unittest eval/test_fable_prompt_bench.py`; `python3 eval/fable_prompt_bench.py` (no `!!` lines, primary within 1.0 of the base branch).
- Paid, on demand: `claude plugin eval .` with a tag from `eval/cases/` (`smoke`, `offline`, `research`, `full`); flags per tag are in `eval/AGENTS.md`. After editing a skill, run at least its `smoke` case and the `offline` or `research` case that covers its artifact.
- `eval/runners/` needs Python 3 and `pyyaml` (only when a fixture has a `rubric.yaml`, which all five do).

### Common Patterns
- Every `SKILL.md` follows the same section order: frontmatter, Outcome, Inputs Required, Who reads <artifact>, What <artifact> Must Cover, How to Work, Constraints, What a strong <artifact> looks like, Output Format, Working <domain>, Edge Cases, References. See `docs/CONTRIBUTING.md` for the template. `idea-validation-orchestrator` is the exception: it documents a pipeline rather than producing a research artifact, so it runs Quick Start, Complete Workflow, Who reads the eleven artifacts, Progress and Resumption, How to Use This Skill, Working the Pipeline, What a strong validation run looks like, and its own reference sections.
- Each `SKILL.md` carries a `Working <domain>` passage giving the Fable-era working guidance for that skill: parallel sub-agent research, sourced/estimated/unverified marking, research depth, deliverable boundaries, the downstream artifact consumer, invited judgment, an outcome-first summary and a pre-handoff check, phrased in that skill's own terms rather than shared across files.
- Frontmatter `allowed-tools` is space-delimited and **pre-approves** tools for the invoking turn; it restricts nothing. `disallowed-tools` is what removes tools. Research skills pre-approve `WebSearch WebFetch`; the synthesis skills (`scorecard-generator`, `validation-report`) pre-approve `Read Write` and set `disallowed-tools: WebSearch WebFetch`.
- Skills cite sources with URLs and mark confidence (High / Medium / Low). Missing data is reported as such rather than invented.
- Reference files are loaded on demand via `references/`-relative links at the end of each `SKILL.md`; they resolve against the skill's own directory.
- The orchestrator names each step by its plugin identity (`product-idea-agent:<skill>`) so another plugin's same-named skill is never picked.

## Dependencies

### Internal
- `skills/*` ↔ `contracts/*` (artifact schemas)
- `eval/runners/*` → `eval/fixtures/*` (reads `input.md`, `rubric.yaml`, `expected_outputs/`)
- `eval/cases/*/*/seed.sh` → `eval/fixtures/t1-energy-audit/` (seeds eval workspaces)
- `eval/fable_prompt_bench.py` → `.claude-plugin/plugin.json` (pack name) and `contracts/` (referenced files must exist)

### External
- Claude Code with plugin support (CI pins v2.1.284) and WebSearch / WebFetch for research skills
- Python 3 + `pyyaml` for the eval runners
- agentskills.io skill format (frontmatter fields `name`, `description`, `license`, `metadata`, `allowed-tools`) plus the Claude Code fields `disallowed-tools` and `argument-hint`

<!-- MANUAL: Any manually added notes below this line are preserved on regeneration -->
