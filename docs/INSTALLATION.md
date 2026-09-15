# Installation Guide

This guide covers installing the Product Idea Agent skill pack for use with Claude Code.

## Prerequisites

- Claude Code CLI installed ([installation guide](https://claude.ai/docs/claude-code))
- Claude Code account with API access
- macOS, Linux, or Windows (WSL)

## Quick Install

Copy all skills to your Claude Code skills directory:

```bash
# Clone or download this repository
git clone https://github.com/your-org/product-idea-agent.git
cd product-idea-agent

# Copy all skills to Claude Code
cp -r skills/* ~/.claude/skills/
```

## Selective Install

Install only the skills you need:

```bash
# Core skills for basic validation
cp -r skills/idea-brief-creator ~/.claude/skills/
cp -r skills/demand-signals ~/.claude/skills/
cp -r skills/scorecard-generator ~/.claude/skills/

# Add more as needed
cp -r skills/competitive-landscape ~/.claude/skills/
cp -r skills/market-sizing ~/.claude/skills/
```

## Project-Local Installation

For project-specific use, install to your project's `.claude` directory:

```bash
# From your project root
mkdir -p .claude/skills
cp -r /path/to/product-idea-agent/skills/* .claude/skills/
```

Project-local skills take precedence over global skills.

## Verify Installation

Check that skills are loaded:

```bash
# Start Claude Code
claude

# Ask Claude to list available skills
> What product validation skills do you have?
```

Claude should recognize skills like `idea-brief-creator`, `demand-signals`, etc.

## Skill Dependencies

The skills have dependencies on each other based on artifact flow:

```
idea-brief-creator (required first)
    │
    ├── demand-signals
    ├── problem-segment
    └── competitive-landscape
            │
            ├── market-sizing
            ├── pricing-wtp
            └── solution-wedge
                    │
                    └── gtm-channels
                            │
                            ├── risk-assessment
                            └── scorecard-generator
                                    │
                                    └── validation-report

idea-validation-orchestrator (runs all)
```

For full validation, install all 12 skills. For partial workflows, ensure upstream dependencies are installed.

## Required Tools

The skills use these Claude Code tools (included by default):

| Tool | Required By | Purpose |
|------|-------------|---------|
| Read | All skills | Read existing artifacts |
| Write | All skills | Create new artifacts |
| WebSearch | Research skills | Find market data |
| WebFetch | Research skills | Fetch web pages |
| Grep | Some skills | Search within files |
| Edit | Orchestrator | Modify artifacts |

These tools are pre-approved in each skill's `allowed-tools` field.

## Updating Skills

To update to a newer version:

```bash
# Pull latest changes
cd product-idea-agent
git pull

# Re-copy skills (overwrites existing)
cp -r skills/* ~/.claude/skills/
```

## Uninstalling

Remove all Product Idea Agent skills:

```bash
# Remove all skills from this pack
cd ~/.claude/skills
rm -rf idea-brief-creator demand-signals problem-segment \
       competitive-landscape market-sizing pricing-wtp \
       solution-wedge gtm-channels risk-assessment \
       scorecard-generator validation-report \
       idea-validation-orchestrator
```

## Troubleshooting

### Skills Not Recognized

1. Check skill directory exists: `ls ~/.claude/skills/`
2. Verify SKILL.md is present in each skill folder
3. Restart Claude Code session

### Permission Errors

```bash
# Ensure correct permissions
chmod -R 755 ~/.claude/skills/
```

### Tool Access Denied

If a skill can't use required tools:
1. Check your Claude Code permissions settings
2. Some tools may require explicit approval for network access

### Conflicts with Other Skills

If skill names conflict with other installed skills:
1. Rename the conflicting skill's directory
2. Or use project-local installation to isolate

## Environment Variables

Optional environment variables for enhanced functionality:

```bash
# Copy the example file
cp .env.example ~/.claude/.env

# Edit with your values (optional)
```

See `.env.example` for available variables.

## Next Steps

- Read the [Usage Guide](USAGE.md) for workflow instructions
- Try the [Quick Start](../README.md#quick-start) example
- Run the evaluation suite to test your installation
