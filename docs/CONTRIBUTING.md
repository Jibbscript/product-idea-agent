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

## Quick Start

3-5 lines showing basic usage.

## Inputs Required

- What artifacts or information needed
- Optional inputs

## Step-by-Step Workflow

### Step 1: Name
What to do.

### Step 2: Name
What to do.

...

## Workflow Checklist

```
Progress:
- [ ] Step 1
- [ ] Step 2
- [ ] Output created
```

## Output Format

What the skill produces and where.

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
- Use imperative mood: "Search for..." not "You should search..."
- Include concrete examples
- Document edge cases

#### Tools
- Only request tools actually needed
- Common tools: Read, Write, WebSearch, WebFetch, Grep

#### References
- Use for content >100 lines
- Keep reference files under 200 lines each
- Use relative paths with `{baseDir}`

### Artifact Contracts

If your skill produces a new artifact type:

1. Create a contract in `contracts/`
2. Document the schema clearly
3. Include validation rules
4. Provide example output

### Testing Your Skill

1. Create a test fixture in `eval/fixtures/`
2. Include input.md, expected outputs, rubric.yaml
3. Run the skill against your fixture
4. Verify output matches expected format

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

- [ ] Skill follows template structure
- [ ] SKILL.md is under 500 lines
- [ ] Description includes capabilities AND triggers
- [ ] All tools in allowed-tools are actually used
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
4. Changelog updated automatically

## Community

### Getting Help

- Check existing issues first
- Ask in discussions for questions
- Use issues for bugs/features

### Code of Conduct

Be respectful and constructive. We're all here to build useful tools.

## License

By contributing, you agree that your contributions will be licensed under the Apache-2.0 license.
