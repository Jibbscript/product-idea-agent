<!-- Parent: ../AGENTS.md -->
<!-- Generated: 2026-09-15 | Updated: 2026-09-15 -->

# docs

## Purpose
Human-facing guides for installing, using, extending, and securing the skill pack. `README.md` at the repo root links here.

## Key Files

| File | Description |
|------|-------------|
| `INSTALLATION.md` | Removing old copy-installs, marketplace add / install / update / uninstall, team enablement via `.claude/settings.json`, `--plugin-dir`, troubleshooting |
| `USAGE.md` | Namespaced commands (`/product-idea-agent:<skill>`), the orchestrator taking the idea as an argument, single-step runs, resuming; prompt examples per skill |
| `CONTRIBUTING.md` | Plugin layout, the canonical `SKILL.md` section template, `allowed-tools` vs `disallowed-tools`, the `${CLAUDE_PLUGIN_ROOT}/contracts/` reference form, pre-PR checklist, releasing |
| `SECURITY.md` | Risk categories (credential exposure, prompt injection from fetched web content, data handling), tool-field semantics, and mitigations |

## For AI Agents

### Working In This Directory
- `CONTRIBUTING.md` holds the authoritative `SKILL.md` template. Keep it in sync with what the 12 skills actually look like; if you change section order in the skills, change it here.
- `USAGE.md` restates each skill's trigger phrases and outputs. Renaming a skill or artifact means editing it.
- These are plain markdown, no build step, no link checker.

### Testing Requirements
- None automated. Verify referenced paths (`skills/<name>`, `eval/runners/run_skillpack.py`) still exist after structural changes.

### Common Patterns
- Prompts users would type are shown in blockquotes or fenced blocks prefixed with `>`.
- Skill names are always backticked kebab-case matching the directory under `skills/`; commands a user types carry the `product-idea-agent:` namespace.
- Never document copy-installing `skills/*`; the plugin is the only supported install.

## Dependencies

### Internal
- Describes `../skills/`, `../eval/`, `../contracts/`

### External
- None

<!-- MANUAL: Any manually added notes below this line are preserved on regeneration -->
