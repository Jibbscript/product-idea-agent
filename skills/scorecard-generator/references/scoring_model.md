# Scoring Model Deep Dive

Detailed methodology for opportunity scoring.

## Dimension Weights Rationale

| Dimension | Weight | Rationale |
|-----------|--------|-----------|
| Problem Severity | 20% | Foundational - no problem = no business |
| Demand Signals | 15% | Validates problem exists at scale |
| Competitive Intensity | 10% | Context matters more than absolute level |
| Market Size | 15% | Defines ceiling of opportunity |
| Execution Difficulty | 15% | Determines likelihood of success |
| GTM Viability | 15% | Path to customers is essential |
| Timing | 10% | Can accelerate or slow everything |

## Dimension Scoring Details

### Problem Severity (20%)

**What we're measuring**: How painful is this problem for the target customer?

| Score | Label | Indicators |
|-------|-------|------------|
| 10 | Extreme | Spending $10K+/year on solutions; mentioned in every interview |
| 9 | Critical | Active budget; dedicated resources to solve |
| 8 | Significant | Strong complaints; trying multiple solutions |
| 7 | Important | Regular frustration; would reallocate budget |
| 6 | Notable | Mentioned unprompted; seeking solutions |
| 5 | Moderate | Acknowledges problem when asked |
| 4 | Minor | Slight inconvenience; low priority |
| 3 | Minimal | Rarely thinks about it |
| 2 | Negligible | Has workaround that's "fine" |
| 1 | Non-issue | Not actually a problem |

**Evidence sources**: ICP problem_severity score, customer quotes, willingness to pay

### Demand Signals (15%)

**What we're measuring**: Is there validated demand at scale?

| Score | Label | Indicators |
|-------|-------|------------|
| 10 | Explosive | >100K monthly searches, 50%+ YoY growth |
| 9 | Very Strong | 50-100K searches, active large communities |
| 8 | Strong | 20-50K searches, engaged communities |
| 7 | Good | 10-20K searches, regular discussions |
| 6 | Moderate | 5-10K searches, niche communities |
| 5 | Present | 2-5K searches, some community activity |
| 4 | Limited | 1-2K searches, sparse discussions |
| 3 | Weak | <1K searches, rare mentions |
| 2 | Minimal | Almost no search volume or discussions |
| 1 | None | No measurable demand indicators |

**Evidence sources**: signals.md signal score, search volumes, community sizes

### Competitive Intensity (10%) - LOWER IS BETTER

**What we're measuring**: How crowded is the market?

| Score | Label | Indicators |
|-------|-------|------------|
| 1-2 | Blue Ocean | 0-2 direct competitors, greenfield market |
| 3-4 | Light | 3-5 competitors, clear differentiation paths |
| 5-6 | Moderate | 5-10 competitors, some gaps remain |
| 7-8 | Heavy | 10-20 competitors, crowded but fragmented |
| 9-10 | Red Ocean | 20+ competitors or 1-2 dominant players |

**Evidence sources**: competitors.csv count, average threat level

**Scoring note**: Invert for composite calculation (1 becomes 10)

### Market Size (15%)

**What we're measuring**: How big is the opportunity?

| Score | TAM | SAM | Growth |
|-------|-----|-----|--------|
| 10 | >$50B | >$5B | >30% CAGR |
| 9 | $20-50B | $2-5B | 20-30% |
| 8 | $10-20B | $1-2B | 15-20% |
| 7 | $5-10B | $500M-1B | 10-15% |
| 6 | $1-5B | $100-500M | 5-10% |
| 5 | $500M-1B | $50-100M | 5-10% |
| 4 | $100-500M | $10-50M | <5% |
| 3 | $50-100M | $5-10M | Flat |
| 2 | $10-50M | $1-5M | Declining |
| 1 | <$10M | <$1M | Declining |

**Evidence sources**: market_size.md TAM, SAM, CAGR

### Execution Difficulty (15%) - LOWER IS BETTER

**What we're measuring**: How hard is this to build and operate?

| Score | Label | Indicators |
|-------|-------|------------|
| 1-2 | Simple | Proven tech, one developer, weeks to MVP |
| 3-4 | Standard | Known patterns, small team, months to MVP |
| 5-6 | Moderate | Some novel components, cross-functional team |
| 7-8 | Complex | Specialized skills, significant R&D |
| 9-10 | Extreme | Frontier tech, research-grade problems |

**Evidence sources**: mvp_spec.md complexity, risks.md technical risks

**Scoring note**: Invert for composite calculation (1 becomes 10)

### GTM Viability (15%)

**What we're measuring**: Can we reach and acquire customers efficiently?

| Score | Label | Indicators |
|-------|-------|------------|
| 10 | Excellent | Clear channels, <$50 CAC, viral potential |
| 9 | Very Good | Multiple channels, <$100 CAC, referral potential |
| 8 | Good | 2-3 viable channels, $100-200 CAC |
| 7 | Solid | Known channels, $200-500 CAC |
| 6 | Adequate | 1-2 channels, $500-1K CAC |
| 5 | Challenging | Limited channels, $1-2K CAC |
| 4 | Difficult | Few channels, >$2K CAC |
| 3 | Hard | Unclear channels, very high CAC |
| 2 | Very Hard | No obvious channels |
| 1 | No Path | Can't identify how to reach customers |

**Evidence sources**: gtm_plan.md channels, pricing.yaml unit economics

### Timing (10%)

**What we're measuring**: Is now the right time?

| Score | Label | Indicators |
|-------|-------|------------|
| 10 | Perfect | Enabling tech just arrived, regulatory tailwind, competitor misstep |
| 9 | Excellent | Strong trend acceleration, market awakening |
| 8 | Great | Favorable trends, early-mover advantage |
| 7 | Good | Supportive trends, reasonable timing |
| 6 | Neutral | No major tailwinds or headwinds |
| 5 | Mixed | Some positive, some negative factors |
| 4 | Challenging | Headwinds present, timing uncertain |
| 3 | Difficult | Market not ready, may need to wait |
| 2 | Poor | Significant barriers, bad timing |
| 1 | Wrong | Too early or too late |

**Evidence sources**: signals.md trends, market_size.md dynamics, context

## Composite Score Calculation

### Formula

```python
# Invert dimensions where lower is better
comp_inv = 11 - competitive_intensity
exec_inv = 11 - execution_difficulty

# Apply weights
weighted_sum = (
    problem_severity * 0.20 +
    demand_signals * 0.15 +
    comp_inv * 0.10 +
    market_size * 0.15 +
    exec_inv * 0.15 +
    gtm_viability * 0.15 +
    timing * 0.10
)

# Convert to 0-100 scale
composite_score = weighted_sum * 10
```

### Example Calculation

| Dimension | Raw Score | Weight | Contribution |
|-----------|-----------|--------|--------------|
| Problem Severity | 8 | 0.20 | 1.6 |
| Demand Signals | 7 | 0.15 | 1.05 |
| Competitive (inv) | 11-6=5 | 0.10 | 0.5 |
| Market Size | 7 | 0.15 | 1.05 |
| Execution (inv) | 11-4=7 | 0.15 | 1.05 |
| GTM Viability | 7 | 0.15 | 1.05 |
| Timing | 8 | 0.10 | 0.8 |
| **Total** | | | **7.1** |

**Composite Score**: 71/100

## Verdict Thresholds

### GO (Proceed with confidence)
- Composite score ≥ 65
- No dimension below 4
- No critical risks without mitigation

### PIVOT (Opportunity with gaps)
- Composite score 50-64
- OR 1-2 dimensions below 4
- OR unmitigated high risks

### NO-GO (Insufficient opportunity)
- Composite score < 50
- OR 3+ dimensions below 4
- OR unaddressable critical risks

## Confidence Adjustment

Adjust composite score based on data quality:

| Data Quality | Adjustment |
|--------------|------------|
| High (all artifacts complete, recent data) | +0 |
| Medium (most artifacts, some assumptions) | -5 |
| Low (gaps in research, old data) | -10 |

## Comparison Framework

For comparing multiple ideas:

| Criteria | Weight | Idea A | Idea B | Idea C |
|----------|--------|--------|--------|--------|
| Composite Score | 60% | 72 | 65 | 58 |
| Founder Fit | 20% | 8/10 | 9/10 | 6/10 |
| Resource Fit | 20% | 7/10 | 6/10 | 8/10 |
| **Weighted Total** | | **73.6** | **68.4** | **59.2** |
