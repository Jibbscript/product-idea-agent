# Contributing Guide

Thank you for your interest in contributing to the Product Idea Agent skill pack!

## How to Contribute

### Reporting Issues

Found a bug or have a suggestion? Open an issue with:

1. **Description**: What happened or what you'd like to see
2. **Steps to reproduce**: If it's a bug
3. **Expected behavior**: What should happen
4. **Environment**: Claude Code version, OS, etc.

### Proposing New Skills

Before building a new skill:

1. Open an issue describing the skill
2. Explain what problem it solves
3. Show how it fits in the artifact flow
4. Wait for feedback before implementing

### Submitting Changes

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/my-skill`
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## Skill Development Guide

### Plugin Layout

The repository root is both the plugin root and the marketplace root:

```
.claude-plugin/
├── plugin.json        # name, version (the single source of truth), experimental.evals
└── marketplace.json   # marketplace "jibbscript", one entry with source "./" and no version
skills/<skill>/        # auto-discovered, one directory per skill
contracts/             # artifact schemas, shipped inside the plugin
eval/cases/            # claude plugin eval suite
```

### Skill Structure

Each skill must have:

```
skill-name/
├── SKILL.md           # Required: Instructions (<500 lines)
└── references/        # Optional: Supporting docs
    └── framework.md   # Domain knowledge
```

### SKILL.md Template

```yaml
---
name: skill-name
description: Does X by Y. Use when Z.
license: Apache-2.0
metadata:
  author: your-name
  pack: product-idea-agent
allowed-tools: Read Write WebSearch WebFetch
---

# Skill Title

Brief description.

## Outcome

What the artifact is and what a finished one looks like.

## Inputs Required

- What artifacts or information needed
- Optional inputs

## Who reads <artifact>

Which downstream skills open this file, what each decides with it, and what vagueness here costs them.

## What <artifact> Must Cover

### <Domain Area>
What this part of the artifact contains and how to judge it.

### <Domain Area>
What this part of the artifact contains and how to judge it.

...

## How to Work

Which parts depend on which, what is independent, and what counts as enough.

## Constraints

The requirements the finished artifact must satisfy.

## What a strong <artifact> looks like

The quality bar in this skill's own terms: what a strong artifact does that a weak one does not.

## Output Format

Create `<artifact>` following the artifact contract in `${CLAUDE_PLUGIN_ROOT}/contracts/<artifact>`.

## Working <the skill's own domain noun>

A short prose passage, renamed per skill, covering when to fan independent research out to parallel sub-agents, how each figure is marked sourced, estimated or unverified, how deep the research goes before it stops paying, what the deliverable is and what it is not, which downstream skill reads this artifact, where the model's own judgment is wanted, what the summary leads with, and the check to run before handing off.

## Edge Cases

- **Missing data**: How to handle
- **Conflicts**: Resolution strategy

## References

- [file.md](references/file.md): Description
```

The Working passage is written in each skill's own vocabulary (its artifact, columns, scales and consumers); copying it between skills is the anti-pattern it exists to avoid.

### Skill Guidelines

#### Naming
- Lowercase with hyphens: `my-skill-name`
- Max 64 characters
- Descriptive and specific

#### Description
- Include both capabilities AND trigger conditions
- Use third person: "Analyzes..." not "I analyze..."
- Keep under 1024 characters

#### Instructions
- Keep SKILL.md under 500 lines
- Behavioral sections (Outcome, Who reads <artifact>, How to Work, Constraints, What a strong <artifact> looks like) state the outcome and its constraints in prose, with the reason beside each requirement
- Reference data (scoring scales, field lists, query templates, tables) stays structured as lists and tables
- Include concrete examples
- Document edge cases

#### Tools
The two tool fields do different things, and new skills need both understood:

- `allowed-tools` **pre-approves** the listed tools for the turn that invokes the skill, so they run without a permission prompt. It does not restrict anything: every other tool stays callable under the user's permission settings. List only what the skill uses. Research skills pre-approve `WebSearch WebFetch` so an unattended validation doesn't stall on prompts.
- `disallowed-tools` **removes** the listed tools while the skill is active. `scorecard-generator` and `validation-report` set `disallowed-tools: WebSearch WebFetch`, which is what makes "synthesis reads only the artifacts" an enforced rule. A new skill that must not reach the web does the same.

Both accept a space- or comma-separated string or a YAML list; this pack uses space-separated strings. The benchmark requires `Read` and `Write` in `allowed-tools`, since every skill reads its inputs and writes its artifact.

#### Contracts and references
- Reference an artifact contract only as `${CLAUDE_PLUGIN_ROOT}/contracts/<artifact>`. Claude Code substitutes the plugin's install path when a plugin skill loads; a bare `contracts/...` path resolves against the founder's project directory, where no contracts exist. The benchmark fails on any other form and on a contract file that doesn't exist.
- Link skill-local references relatively, `[file.md](references/file.md)`; they resolve against the skill's own directory.
- Artifacts are written to the current project directory, never under `${CLAUDE_PLUGIN_ROOT}`, which is replaced on every plugin update.

#### References
- Use for content >100 lines
- Keep reference files under 200 lines each

### Artifact Contracts

If your skill produces a new artifact type:

1. Create a contract in `contracts/`
2. Document the schema clearly
3. Include validation rules
4. Provide example output
5. Reference it from the producing skill as `${CLAUDE_PLUGIN_ROOT}/contracts/<artifact>`

### Testing Your Skill

Load your working copy as a session-only plugin, with no install or publish step:

```bash
claude --plugin-dir .
```

Run `/reload-plugins` after each edit. Then:

1. Create a test fixture in `eval/fixtures/` with `input.md`, expected outputs and `rubric.yaml`
2. Add a routing case under `eval/cases/smoke/<skill>/` and, for a new artifact, a structural regex to the case that produces it
3. Run the relevant eval tag (see the checklist below)

## Code Style

### Markdown
- Use ATX-style headers (`#` not underlines)
- One sentence per line for easier diffs
- Use fenced code blocks with language hints

### YAML
- 2-space indentation
- Quote strings with special characters
- Use comments for non-obvious fields

### JSON
- 2-space indentation
- Always include schema version
- Use camelCase for keys

### Python (eval runners)
- Follow PEP 8
- Type hints for function signatures
- Docstrings for public functions

## Pull Request Process

### Before Submitting

Run the checks CI runs, plus the eval tag your change touches:

```bash
claude plugin validate . --strict
claude plugin validate .claude-plugin/plugin.json --strict
python3 -m unittest eval/test_fable_prompt_bench.py
python3 eval/fable_prompt_bench.py
```

The benchmark's primary score must stay within 1.0 of the base branch, with no `!!` integrity lines. For behavior, run the tag that covers your change, for example routing after a description edit:

```bash
claude plugin eval . --tag smoke --ablation none --runs 1
```

Research and synthesis tags need `--scaffold --allow-tools Write Edit WebSearch WebFetch`; see `eval/AGENTS.md`. Evals are paid model calls, so they are not a PR gate.

- [ ] `claude plugin validate` passes with `--strict` on both targets
- [ ] Benchmark within tolerance, integrity tests pass
- [ ] Relevant eval tag run and its result noted in the PR
- [ ] `version` in `.claude-plugin/plugin.json` bumped for any change to skills, contracts or manifests (semver; the marketplace entry carries no version)
- [ ] Skill follows template structure
- [ ] SKILL.md is under 500 lines
- [ ] Description includes capabilities AND triggers
- [ ] All tools in allowed-tools are actually used, and tools the skill must never call are in disallowed-tools
- [ ] Contracts referenced as `${CLAUDE_PLUGIN_ROOT}/contracts/<artifact>`
- [ ] No hardcoded model versions or dates
- [ ] Reference files are focused and concise
- [ ] Test fixture created for new skills
- [ ] README updated if needed

### PR Description

Include:
- What the skill does
- Why it's valuable
- How it fits in the workflow
- Any breaking changes

### Review Process

1. Maintainer reviews within 1 week
2. Address feedback
3. Squash commits before merge

### Releasing

A release is a merged version bump. Tag it so a validation run can be matched to the plugin version that produced it:

```bash
claude plugin tag --push
```

This creates `product-idea-agent--v<version>`, after checking that `plugin.json` and the marketplace entry agree. Users receive the release through `claude plugin update` or `/plugin`.

## Community

### Getting Help

- Check existing issues first
- Ask in discussions for questions
- Use issues for bugs/features

### Code of Conduct

Be respectful and constructive. We're all here to build useful tools.

## License

By contributing, you agree that your contributions will be licensed under the Apache-2.0 license.
