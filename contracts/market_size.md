# Artifact Contract: market_size.md

## Purpose
Documents TAM/SAM/SOM market sizing with methodology and growth projections.

## Producer
- `market-sizing` skill

## Consumers
- `gtm-channels`
- `scorecard-generator`
- `validation-report`

## Schema

```markdown
# Market Size Analysis

## Executive Summary
[1-2 sentence summary of market opportunity]

## TAM (Total Addressable Market)
- **Size**: $[X]B
- **Methodology**: [Top-down from industry reports / Bottom-up calculation]
- **Source**: [citation with URL]
- **Growth Rate**: [X]% CAGR

## SAM (Serviceable Addressable Market)
- **Size**: $[X]M
- **Constraints Applied**: [geographic, segment, technology constraints]
- **Calculation**: [methodology explanation]

## SOM (Serviceable Obtainable Market)
- **Year 1 Target**: $[X]M
- **Assumptions**: [market share %, conversion rates, pricing]
- **Rationale**: [justification for obtainable estimate]

## Market Dynamics
- **Drivers**: [factors accelerating market growth]
- **Constraints**: [factors limiting market growth]
- **Trends**: [relevant macro and micro trends]

## Confidence Assessment
[High/Medium/Low] - [reasoning for confidence level]

## Sources
- [Source 1 with URL and date]
- [Source 2 with URL and date]
```

## Field Definitions

| Field | Required | Description |
|-------|----------|-------------|
| Executive Summary | Yes | 1-2 sentences |
| TAM Size | Yes | Dollar amount with unit (B/M/K) |
| TAM Methodology | Yes | Top-down or Bottom-up |
| TAM Source | Yes | Citation with URL |
| TAM Growth Rate | Yes | CAGR percentage |
| SAM Size | Yes | Dollar amount, smaller than TAM |
| SAM Constraints | Yes | List of constraints applied |
| SOM Year 1 Target | Yes | Dollar amount, smaller than SAM |
| SOM Assumptions | Yes | Market share and other assumptions |
| Market Dynamics | Yes | At least 1 driver, constraint, and trend |
| Confidence Assessment | Yes | High/Medium/Low with reasoning |
| Sources | Yes | At least 2 citations |

## Sizing Methodology Guidelines

### Top-Down Approach
Start with industry reports and narrow down:
1. Total industry market size (from Statista, IBISWorld, etc.)
2. Apply geographic constraints (% in target regions)
3. Apply segment constraints (% matching ICP)
4. Apply technology constraints (% addressable by solution)

### Bottom-Up Approach
Build from unit economics:
1. Number of potential customers (from census, industry data)
2. Percentage that match ICP criteria
3. Expected average revenue per customer
4. Realistic capture rate
