# Usage Guide

This guide covers how to use the Product Idea Agent skill pack for product validation.

## Quick Start

### Full Validation Workflow

The easiest way to run a complete validation:

```
> Help me validate my startup idea: An AI-powered app that helps
> homeowners identify energy leaks using their phone's thermal camera.
```

Claude will automatically:
1. Recognize this as a product validation task
2. Use the `idea-validation-orchestrator` skill
3. Guide you through all 11 validation steps
4. Generate a comprehensive validation report

### Single Skill Usage

Use individual skills for specific tasks:

```
> Use the demand-signals skill to research interest in home energy auditing
```

```
> Run competitive analysis on the SOC 2 compliance automation space
```

```
> Help me size the market for vintage synthesizer collectors
```

## The 11-Step Workflow

### Step 1: Idea Brief (idea-brief-creator)

**Input**: Raw idea description
**Output**: `idea_brief.md`

```
> I have an idea for a subscription box service that delivers curated
> houseplants with AI-powered care recommendations. Help me structure this.
```

### Step 2: Demand Signals (demand-signals)

**Input**: `idea_brief.md` or idea description
**Output**: `signals.md`

```
> Research demand signals for my plant subscription idea
```

Searches for:
- Google Trends data
- Reddit discussions
- Community engagement
- Search volumes

### Step 3: ICP Definition (problem-segment)

**Input**: `idea_brief.md`
**Output**: `icp.yaml`

```
> Define the ideal customer profile for my product
```

Produces:
- Demographics/firmographics
- Psychographics (goals, frustrations)
- Behavioral patterns
- Problem severity score

### Step 4: Competitive Landscape (competitive-landscape)

**Input**: `idea_brief.md`
**Output**: `competitors.csv`

```
> Map the competitive landscape for compliance automation
```

Identifies:
- Direct competitors
- Indirect alternatives
- Strengths and weaknesses
- Threat levels

### Step 5: Market Sizing (market-sizing)

**Input**: `idea_brief.md`, `icp.yaml`
**Output**: `market_size.md`

```
> Estimate the market size for my idea
```

Calculates:
- TAM (Total Addressable Market)
- SAM (Serviceable Addressable Market)
- SOM (Serviceable Obtainable Market)
- Growth rates

### Step 6: Pricing Research (pricing-wtp)

**Input**: `competitors.csv`, `icp.yaml`
**Output**: `pricing.yaml`

```
> Research pricing for my product category
```

Analyzes:
- Competitor pricing benchmarks
- Willingness-to-pay evidence
- Value ladder design
- Unit economics

### Step 7: MVP Definition (solution-wedge)

**Input**: `idea_brief.md`, `competitors.csv`, `icp.yaml`
**Output**: `mvp_spec.md`

```
> Help me define the MVP scope
```

Defines:
- Must-have features (P0)
- Should-have features (P1)
- Technical approach
- Differentiation strategy

### Step 8: GTM Planning (gtm-channels)

**Input**: `icp.yaml`, `market_size.md`
**Output**: `gtm_plan.md`

```
> Plan the go-to-market strategy
```

Identifies:
- Acquisition channels
- CAC estimates
- Launch strategy
- Growth loops

### Step 9: Risk Assessment (risk-assessment)

**Input**: All prior artifacts
**Output**: `risks.md`

```
> What are the risks for this idea?
```

Documents:
- Technical risks
- Market risks
- Execution risks
- Mitigations

### Step 10: Scorecard (scorecard-generator)

**Input**: All prior artifacts
**Output**: `scorecard.json`

```
> Generate the validation scorecard
```

Scores:
- 7 validation dimensions
- Composite score (0-100)
- GO/PIVOT/NO-GO recommendation

### Step 11: Validation Report (validation-report)

**Input**: All artifacts, `scorecard.json`
**Output**: `validation_report.md`

```
> Compile the full validation report
```

Produces:
- Executive summary
- Section narratives
- Key findings
- Next steps

## Workflow Patterns

### Full End-to-End Validation

Best for new ideas needing comprehensive analysis:

```
> Run a complete product validation on my idea: [description]
```

Time: 2-3 hours with active participation

### Quick Feasibility Check

For rapid initial assessment:

```
> Do a quick feasibility check on [idea]. Focus on demand signals
> and competitive landscape.
```

Runs steps 1-4 only. Time: 30-45 minutes.

### Targeted Deep Dive

When you need specific analysis:

```
> I need a detailed competitive analysis of the data observability market
```

Runs single skill with extra depth.

### Pivot Assessment

When re-evaluating after initial findings:

```
> Based on the competitive intensity, help me explore adjacent
> segments that might be less crowded
```

## Working with Artifacts

### Artifact Locations

All artifacts are saved in your current directory:

```
./
├── idea_brief.md
├── signals.md
├── icp.yaml
├── competitors.csv
├── market_size.md
├── pricing.yaml
├── mvp_spec.md
├── gtm_plan.md
├── risks.md
├── scorecard.json
└── validation_report.md
```

### Referencing Prior Work

Skills automatically read existing artifacts:

```
> I already have an idea brief. Continue with demand signals.
```

### Updating Artifacts

To refine previous output:

```
> The ICP needs to focus more on enterprise customers. Update it.
```

## Understanding the Scorecard

### Dimension Scores (1-10)

| Dimension | What It Measures | Higher = Better |
|-----------|------------------|-----------------|
| Problem Severity | How painful is the problem? | Yes |
| Demand Signals | Is there validated demand? | Yes |
| Competitive Intensity | How crowded is the market? | **No** (lower = better) |
| Market Size | How big is the opportunity? | Yes |
| Execution Difficulty | How hard to build? | **No** (lower = better) |
| GTM Viability | Can you reach customers? | Yes |
| Timing | Is now the right time? | Yes |

### Composite Score

- **75-100**: Strong opportunity
- **65-74**: Good opportunity with some risks
- **50-64**: Moderate opportunity, pivot may be needed
- **Below 50**: Significant challenges

### Recommendations

- **GO**: Proceed with development
- **PIVOT**: Address weak areas before proceeding
- **NO-GO**: Consider different ideas

## Tips for Best Results

### Provide Context

More detail leads to better analysis:

```
> My idea is an AI app for energy audits. Target: US homeowners with
> homes built before 2000. Monetization: freemium with $30/year premium
> and contractor referral fees.
```

### Share Existing Research

If you have data, share it:

```
> I've already interviewed 10 potential customers. Key findings:
> - 80% frustrated with high energy bills
> - 60% have tried DIY solutions
> - Average WTP is $25-40/year
```

### Iterate on Findings

Use insights to refine:

```
> The competitive analysis shows the market is crowded. Can you
> suggest niches that are underserved?
```

### Ask Clarifying Questions

Get deeper when needed:

```
> Why did you score execution difficulty as 6? What would make it easier?
```

## Common Questions

### How long does full validation take?

2-3 hours with active participation. Can be faster for simpler ideas.

### Can I pause and resume?

Yes. Artifacts are saved, and you can resume:

```
> Continue the validation from risk assessment
```

### How accurate is the data?

The skills use web search for current data. Accuracy depends on available sources. Always verify critical claims.

### Can I validate multiple ideas?

Yes. Run validation in separate directories to keep artifacts organized.

### What if I disagree with the recommendation?

The scorecard is a framework, not a verdict. Use it as input to your own judgment.
