# Product Idea Agent Skill Pack

A Claude Code plugin that replicates end-to-end product idea validation. Transform raw startup concepts into actionable validation reports with demand signals, market sizing, competitive analysis, and go-to-market strategies.

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

The pack is a Claude Code plugin served from this repository's marketplace. In a Claude Code session:

```text
/plugin marketplace add Jibbscript/product-idea-agent
/plugin install product-idea-agent@jibbscript
```

Update with `claude plugin update product-idea-agent@jibbscript`, remove with `claude plugin uninstall product-idea-agent@jibbscript`. If you installed an earlier version by copying `skills/*` into `~/.claude/skills/`, remove those copies first; the [Installation Guide](docs/INSTALLATION.md) shows how, along with team-wide enablement and `--plugin-dir` for local development.

### Usage

Start a full validation by passing your idea to the orchestrator:

```text
/product-idea-agent:idea-validation-orchestrator An AI-powered app that finds home energy leaks with a phone's thermal camera
```

Describing the idea in plain language works too; the orchestrator triggers on requests like:

```text
Help me validate my startup idea for an AI-powered home energy audit app
```

Run or redo a single step by its namespaced command:

```text
/product-idea-agent:competitive-landscape
```

Every artifact is written to the current project directory, and an interrupted validation resumes from the artifacts already there.

## Skill Catalog

| Skill (`product-idea-agent:`) | Purpose | Output Artifact |
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

Three layers check the plugin:

```bash
# Structure: manifests, marketplace and skill frontmatter (free, every PR)
claude plugin validate . --strict
claude plugin validate .claude-plugin/plugin.json --strict

# Prompt surface: fitness benchmark and its integrity tests (free, every PR)
python3 eval/fable_prompt_bench.py
python3 -m unittest eval/test_fable_prompt_bench.py

# Behavior: plugin eval suite against a no-plugin baseline (paid, on demand)
claude plugin eval . --tag offline --scaffold --allow-tools Write WebSearch WebFetch
```

The eval cases live in `eval/cases/` (tags `smoke`, `offline`, `research`, `full`); see [eval/AGENTS.md](eval/AGENTS.md) for which flags each tag needs.

## License

Apache-2.0 - See [LICENSE](LICENSE) for details.

## Acknowledgments

Each skill uses the [agentskills.io](https://agentskills.io) `SKILL.md` format. The pack is distributed and supported as a Claude Code plugin, which is what lets every skill resolve its artifact contract.
