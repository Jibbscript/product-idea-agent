# Product Idea Agent Skill Pack

A modular skill pack for Claude Code that replicates end-to-end product idea validation. Transform raw startup concepts into actionable validation reports with demand signals, market sizing, competitive analysis, and go-to-market strategies.

## Overview

This skill pack provides **12 composable skills** that guide you through a comprehensive product validation workflow:

1. **Idea Brief Creation** - Structure raw concepts into validated hypotheses
2. **Demand Signal Research** - Discover search trends and community interest
3. **Problem-Segment Analysis** - Define ICP and validate problem severity
4. **Competitive Landscape Mapping** - Identify competitors and market gaps
5. **Market Sizing** - Estimate TAM/SAM/SOM with growth projections
6. **Pricing & WTP Research** - Analyze pricing models and willingness-to-pay
7. **Solution Wedge Definition** - Scope MVP and differentiation strategy
8. **GTM Channel Planning** - Identify acquisition channels and growth loops
9. **Risk Assessment** - Evaluate technical, market, and execution risks
10. **Scorecard Generation** - Calculate multi-dimensional opportunity scores
11. **Validation Report** - Compile comprehensive validation deliverable
12. **Orchestrator** - Run the complete validation workflow end-to-end

## Quick Start

### Installation

Copy the skills you need to your Claude Code skills directory:

```bash
# Copy all skills
cp -r skills/* ~/.claude/skills/

# Or copy individual skills
cp -r skills/idea-brief-creator ~/.claude/skills/
```

### Usage

Once installed, skills activate automatically based on your prompts:

```
"Help me validate my startup idea for an AI-powered home energy audit app"
```

Or invoke specific skills:

```
"Use the demand-signals skill to research interest in home energy auditing"
```

For complete validation, use the orchestrator:

```
"Run a full product validation on my idea using the idea-validation-orchestrator"
```

## Skill Catalog

| Skill | Purpose | Output Artifact |
|-------|---------|-----------------|
| `idea-brief-creator` | Structure raw idea into hypothesis | `idea_brief.md` |
| `demand-signals` | Research search trends & community signals | `signals.md` |
| `problem-segment` | Define ICP & validate problem severity | `icp.yaml` |
| `competitive-landscape` | Map competitors & identify gaps | `competitors.csv` |
| `market-sizing` | Estimate TAM/SAM/SOM | `market_size.md` |
| `pricing-wtp` | Research pricing & willingness-to-pay | `pricing.yaml` |
| `solution-wedge` | Define MVP scope & differentiation | `mvp_spec.md` |
| `gtm-channels` | Plan acquisition channels | `gtm_plan.md` |
| `risk-assessment` | Identify risks & dependencies | `risks.md` |
| `scorecard-generator` | Calculate opportunity scores | `scorecard.json` |
| `validation-report` | Generate final report | `validation_report.md` |
| `idea-validation-orchestrator` | Run complete workflow | All artifacts |

## Artifact Flow

```
idea_brief.md
    │
    ├──► signals.md ──► market_size.md ──► gtm_plan.md
    │
    ├──► icp.yaml ──► mvp_spec.md ──────────┘
    │
    └──► competitors.csv ──► pricing.yaml
                                   │
                                   ▼
              gtm_plan.md ──► risks.md ──► scorecard.json ──► validation_report.md
```

## Documentation

- [Installation Guide](docs/INSTALLATION.md) - Detailed setup instructions
- [Usage Guide](docs/USAGE.md) - How to use each skill
- [Contributing](docs/CONTRIBUTING.md) - How to contribute new skills
- [Security](docs/SECURITY.md) - Security best practices

## Evaluation

The `eval/` directory contains test fixtures for validating skill quality:

```bash
# Run evaluation suite
python eval/runners/run_skillpack.py
```

## License

Apache-2.0 - See [LICENSE](LICENSE) for details.

## Acknowledgments

This skill pack architecture follows the [agentskills.io](https://agentskills.io) open standard for maximum portability across Claude Code, Claude.ai, and compatible systems.
