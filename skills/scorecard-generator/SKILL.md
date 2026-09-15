---
name: scorecard-generator
description: Calculates validation scores across multiple dimensions to produce an opportunity scorecard. Use when summarizing validation findings into actionable metrics, making go/no-go decisions, or comparing ideas.
license: Apache-2.0
metadata:
  author: product-idea-agent
  pack: product-idea-agent
allowed-tools: Read Write
---

# Scorecard Generator

Calculates multi-dimensional validation scores and generates opportunity scorecards.

## Quick Start

Given all prior artifacts, generate a scorecard:
1. Extract evidence from each artifact
2. Score each dimension (1-10)
3. Calculate composite score
4. Determine revenue potential
5. Generate recommendation
6. Output `scorecard.json`

## Inputs Required

- All prior artifacts:
  - `idea_brief.md`
  - `signals.md`
  - `icp.yaml`
  - `competitors.csv`
  - `market_size.md`
  - `pricing.yaml`
  - `mvp_spec.md`
  - `gtm_plan.md`
  - `risks.md`

## Step-by-Step Workflow

### Step 1: Gather Evidence

Review each artifact and extract relevant metrics:

| Artifact | Key Metrics to Extract |
|----------|------------------------|
| signals.md | Signal strength score, search volumes |
| icp.yaml | Problem severity score |
| competitors.csv | Number of competitors, threat levels |
| market_size.md | TAM, SAM, CAGR |
| pricing.yaml | Unit economics, LTV:CAC |
| mvp_spec.md | Technical complexity |
| gtm_plan.md | Channel viability |
| risks.md | Critical risk count |

### Step 2: Score Each Dimension

Rate each dimension 1-10 based on evidence:

#### Problem Severity (Weight: 20%)
From `icp.yaml` problem_severity score:
- 9-10: Hair-on-fire problem, active spending to solve
- 7-8: Significant pain, some existing solutions
- 5-6: Moderate frustration, workarounds exist
- 3-4: Minor inconvenience
- 1-2: Nice-to-have, not a real problem

#### Demand Signals (Weight: 15%)
From `signals.md` signal score:
- 9-10: High search volume, active communities, strong growth
- 7-8: Good signals, engaged communities
- 5-6: Moderate interest, niche communities
- 3-4: Limited signals, small audiences
- 1-2: No measurable demand

#### Competitive Intensity (Weight: 10%)
From `competitors.csv`:
- 1-2: Blue ocean, no direct competitors (good)
- 3-4: Few competitors, clear differentiation possible
- 5-6: Moderate competition, gaps exist
- 7-8: Crowded market, hard to differentiate
- 9-10: Red ocean, dominated by incumbents (bad)

**Note**: For this dimension, LOWER is BETTER.

#### Market Size (Weight: 15%)
From `market_size.md`:
- 9-10: TAM > $10B, SAM > $1B
- 7-8: TAM $1-10B, SAM $100M-1B
- 5-6: TAM $100M-1B, SAM $10-100M
- 3-4: TAM $10-100M, niche market
- 1-2: TAM < $10M, very small market

#### Execution Difficulty (Weight: 15%)
From `mvp_spec.md` and `risks.md`:
- 1-2: Simple app, proven tech, solo buildable (good)
- 3-4: Standard complexity, small team needed
- 5-6: Moderate complexity, some novel components
- 7-8: Complex system, specialized skills required
- 9-10: Frontier technology, major R&D required (bad)

**Note**: For this dimension, LOWER is BETTER.

#### GTM Viability (Weight: 15%)
From `gtm_plan.md` and `pricing.yaml`:
- 9-10: Clear channels, low CAC, viral potential
- 7-8: Good channels available, reasonable CAC
- 5-6: Some channels, moderate CAC
- 3-4: Limited channels, high CAC
- 1-2: No clear path to customers

#### Timing (Weight: 10%)
From `signals.md`, `market_size.md`, and context:
- 9-10: Perfect timing - enabling tech just matured
- 7-8: Good timing - market ready, trends supportive
- 5-6: Neutral - no major headwinds or tailwinds
- 3-4: Challenging - market not ready or shifting away
- 1-2: Bad timing - too early or too late

### Step 3: Calculate Composite Score

Apply weights and calculate:

```
Composite = (
  Problem Severity × 0.20 +
  Demand Signals × 0.15 +
  (11 - Competitive Intensity) × 0.10 +  # Invert
  Market Size × 0.15 +
  (11 - Execution Difficulty) × 0.15 +   # Invert
  GTM Viability × 0.15 +
  Timing × 0.10
) × 10
```

Result is 0-100.

### Step 4: Determine Revenue Potential

Based on market size and unit economics:
- `$$$` ($10M+ ARR potential): Large SAM, strong economics
- `$$` ($1M-$10M ARR potential): Medium SAM, viable economics
- `$` ($100K-$1M ARR potential): Small SAM or challenging economics

### Step 5: Generate Recommendation

Based on composite score and risk profile:

**GO** (Score ≥ 65 AND no dimension below 4):
- Proceed with development
- Strong overall opportunity
- Manageable risks

**PIVOT** (Score 50-64 OR 1-2 dimensions below 4):
- Opportunity exists but needs adjustment
- Address weak areas before proceeding
- Consider narrowing scope or segment

**NO-GO** (Score < 50 OR 3+ dimensions below 4):
- Insufficient opportunity
- Critical gaps in multiple areas
- Recommend exploring different ideas

### Step 6: Define Next Steps

Based on recommendation, suggest 2-3 immediate actions:
- For GO: Focus on execution priorities
- For PIVOT: Address specific weaknesses
- For NO-GO: Alternative directions to explore

### Step 7: Generate Artifact

Create `scorecard.json` following the contract format.

## Workflow Checklist

```
Scorecard Generation Progress:
- [ ] All artifacts gathered and reviewed
- [ ] Evidence extracted for each dimension
- [ ] Problem severity scored with evidence
- [ ] Demand signals scored with evidence
- [ ] Competitive intensity scored with evidence
- [ ] Market size scored with evidence
- [ ] Execution difficulty scored with evidence
- [ ] GTM viability scored with evidence
- [ ] Timing scored with evidence
- [ ] Composite score calculated
- [ ] Revenue potential determined
- [ ] Recommendation generated
- [ ] Next steps defined
- [ ] scorecard.json created
```

## Output Format

Create `scorecard.json` following the artifact contract in `contracts/scorecard.json`.

Required fields:
- version, idea_name, evaluated_date
- All 7 dimension scores with evidence
- composite_score and calculation_method
- revenue_potential with indicator and range
- recommendation with verdict, rationale, and next_steps

## Scoring Calibration

### Cross-Check Scores

Ensure consistency:
- High problem severity should correlate with strong demand signals
- High competitive intensity may indicate validated market
- Large market should align with multiple viable channels

### Adjust for Context

Consider:
- B2B vs B2C dynamics
- Industry-specific norms
- Founder/team advantages
- Timing of research (market may have changed)

## Edge Cases

**Missing artifacts:**
- Score based on available evidence
- Note lower confidence for affected dimensions
- Recommend gathering missing data

**Conflicting evidence:**
- Document the conflict
- Use more conservative score
- Note in evidence field

**Borderline scores:**
- Err toward lower score unless strong evidence
- Document reasoning
- Flag for validation

**All high scores:**
- Sanity check assumptions
- May indicate bias or insufficient research
- Validate with external perspective

## References

- [scoring_model.md](references/scoring_model.md): Detailed scoring methodology
