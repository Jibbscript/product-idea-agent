---
name: market-sizing
description: Estimates total addressable market (TAM), serviceable addressable market (SAM), and serviceable obtainable market (SOM) with growth projections. Use when quantifying the market opportunity, sizing an investment, or validating market potential.
license: Apache-2.0
metadata:
  author: product-idea-agent
  pack: product-idea-agent
allowed-tools: Read Write WebSearch WebFetch
---

# Market Sizing Analysis

Estimates TAM/SAM/SOM market sizes with methodology and growth projections.

## Quick Start

Given prior artifacts, size the market:
1. Define market boundaries
2. Research TAM from industry sources
3. Calculate SAM based on ICP constraints
4. Estimate realistic SOM
5. Output `market_size.md`

## Inputs Required

- `idea_brief.md` (from idea-brief-creator)
- `icp.yaml` (from problem-segment) - critical for SAM calculation
- `competitors.csv` (optional, helps validate estimates)

## Step-by-Step Workflow

### Step 1: Define Market Boundaries

Clarify what market you're sizing:
- What problem category?
- What customer segment?
- What geographic scope?
- What time horizon?

Be specific: "B2B SaaS compliance automation for US fintech startups" not just "compliance software"

### Step 2: Research TAM (Total Addressable Market)

TAM = Total market if you captured 100% of the opportunity

**Top-Down Approach:**
1. Search for industry reports: "[industry] market size"
2. Find credible sources (Statista, IBISWorld, Gartner, etc.)
3. Note the methodology and date
4. Extract market size and CAGR

**Bottom-Up Approach:**
1. Estimate number of potential customers
2. Multiply by average revenue per customer
3. Cross-reference with top-down sources

### Step 3: Calculate SAM (Serviceable Addressable Market)

SAM = Portion of TAM you can actually serve

Apply constraints from your ICP:
- Geographic constraints (% in target regions)
- Segment constraints (% matching ICP)
- Technology constraints (% addressable by your approach)
- Price point constraints (% who can afford you)

**Formula:**
SAM = TAM × Geographic % × Segment % × Technology % × Price %

### Step 4: Estimate SOM (Serviceable Obtainable Market)

SOM = Realistic market capture in target timeframe

Consider:
- Competitive intensity (more competitors = lower SOM)
- Go-to-market capability
- Brand awareness trajectory
- Sales cycle length

**Typical SOM ranges:**
- Year 1: 0.1% - 1% of SAM for startups
- Year 3: 1% - 5% of SAM with traction
- Year 5: 5% - 15% of SAM as established player

### Step 5: Project Growth Rates

For each level (TAM, SAM, SOM):
- Document CAGR from sources
- Note drivers of growth
- Flag any constraints or headwinds

### Step 6: Assess Confidence

Rate confidence based on:
- **High**: Multiple credible sources, recent data, validated assumptions
- **Medium**: 2-3 sources, some assumptions, reasonable methodology
- **Low**: Limited sources, old data, significant assumptions

### Step 7: Generate Artifact

Create `market_size.md` following the contract format.

## Workflow Checklist

```
Market Sizing Progress:
- [ ] Market boundaries defined
- [ ] TAM researched from industry sources
- [ ] SAM calculated with ICP constraints
- [ ] SOM estimated with realistic assumptions
- [ ] Growth rates documented (CAGR)
- [ ] Confidence level assessed
- [ ] Sources documented
- [ ] market_size.md created
```

## Output Format

Create `market_size.md` following the artifact contract in `contracts/market_size.md`.

Required sections:
- Executive summary
- TAM with methodology and source
- SAM with constraints applied
- SOM with assumptions
- Market dynamics (drivers, constraints, trends)
- Confidence assessment
- Sources (minimum 2 citations)

## Research Query Templates

### Finding TAM Data
- "[industry] market size 2024"
- "[industry] market report"
- "[industry] TAM analysis"
- "site:statista.com [industry]"
- "[industry] market forecast CAGR"

### Finding Segment Data
- "[segment] number of companies"
- "[segment] industry statistics"
- "how many [customer type] in [region]"

### Validating Estimates
- "[competitor] revenue"
- "[competitor] customers"
- "[industry] average deal size"

## Sizing Methods

### Top-Down Method
Start with total market, narrow down:

```
Industry Market Size: $50B (from report)
    × Geographic constraint (US only): 40% → $20B
    × Segment constraint (SMB only): 30% → $6B
    × Technology constraint (cloud-native): 50% → $3B
= SAM: $3B
```

### Bottom-Up Method
Start with unit economics, scale up:

```
Number of target companies: 100,000
    × Addressable by solution: 50% → 50,000
    × Would consider buying: 20% → 10,000
    × Average deal size: $10,000/year
= SAM: $100M
```

### Triangulation
Use both methods and reconcile:
- If they're close (within 2x), take the average
- If they differ significantly, investigate why
- Note the range and confidence

## Edge Cases

**No market reports exist:**
- Use bottom-up calculation
- Reference adjacent markets
- Note lower confidence
- Recommend primary research

**Market in flux:**
- Note rapid change
- Provide range estimates
- Track leading indicators
- Update frequently

**Conflicting sources:**
- Report both figures
- Favor more recent/credible sources
- Note the discrepancy
- Use conservative estimate

**Very small market:**
- This is a valid finding
- Consider if market is growing
- Note if product could expand TAM
- Be realistic about opportunity

## References

- [sizing_methods.md](references/sizing_methods.md): Detailed sizing methodologies and examples
