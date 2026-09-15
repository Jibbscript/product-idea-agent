# Market Sizing Methods

Detailed methodologies for market sizing with examples.

## Method 1: Top-Down Analysis

Start with industry-level data and narrow down.

### Process
1. Find total industry market size from reports
2. Apply segmentation filters
3. Arrive at addressable portion

### Example: Compliance SaaS for Fintechs

```
Step 1: Total GRC (Governance, Risk, Compliance) Software Market
Source: Gartner 2024
TAM = $45B globally

Step 2: Apply Geographic Filter
US market = 35% of global
$45B × 0.35 = $15.75B

Step 3: Apply Industry Filter
Fintech vertical = 8% of GRC spend
$15.75B × 0.08 = $1.26B

Step 4: Apply Size Filter
Startups (seed to Series C) = 15% of fintech spend
$1.26B × 0.15 = $189M

Step 5: Apply Solution Filter
Automated compliance (vs consulting/manual) = 40%
$189M × 0.40 = $75.6M

SAM = $75.6M
```

### Pros and Cons
✅ Uses credible external data
✅ Easily explainable methodology
✅ Good for large, well-researched markets
❌ Requires finding relevant reports
❌ Segmentation percentages are often estimated
❌ May miss emerging segments

## Method 2: Bottom-Up Analysis

Build from unit economics and customer counts.

### Process
1. Count potential customers
2. Estimate conversion funnel
3. Apply pricing assumptions
4. Calculate total market

### Example: Home Energy Audit App

```
Step 1: Count Potential Customers
US homeowners = 85 million households
Homes built before 2000 = 60% → 51 million
With smartphones capable of thermal = 30% → 15.3 million

Step 2: Apply Willingness Filters
Concerned about energy costs = 40% → 6.1 million
Willing to use app = 25% → 1.5 million

Step 3: Apply Pricing
Annual subscription price = $30/year
Additional services revenue = $20/year
Total ARPU = $50/year

Step 4: Calculate SAM
1.5 million × $50 = $75 million

SAM = $75M
```

### Pros and Cons
✅ Grounded in specific assumptions
✅ Works for new/niche markets
✅ Easy to sensitivity test
❌ Assumptions may be wrong
❌ Can miss market dynamics
❌ Labor-intensive to research

## Method 3: Value-Based Sizing

Size by value delivered rather than spend.

### Process
1. Identify the problem cost
2. Estimate value of solution
3. Calculate willingness to pay as % of value
4. Apply to customer base

### Example: DevOps Monitoring Tool

```
Step 1: Problem Cost
Average downtime cost: $5,000/hour
Average incidents/year: 50
Average resolution time: 4 hours
Total cost: $5,000 × 50 × 4 = $1M/year

Step 2: Solution Value
Time saved per incident: 2 hours
Incidents prevented: 20/year
Value delivered: ($5,000 × 20 × 4) + ($5,000 × 50 × 2) = $900K

Step 3: Willingness to Pay
Typical WTP: 10-20% of value delivered
$900K × 15% = $135K/year per customer

Step 4: Apply to Market
Target companies: 50,000 (mid-market tech)
Addressable: 20% → 10,000
SAM: 10,000 × $135K = $1.35B

SAM = $1.35B
```

### Pros and Cons
✅ Connects to real customer value
✅ Supports pricing strategy
✅ Good for B2B
❌ Requires ROI assumptions
❌ Value varies by customer
❌ Harder for B2C

## Method 4: Competitive Proxy

Use competitor data to estimate market size.

### Process
1. Research competitor revenues
2. Estimate market share
3. Calculate implied market size

### Example: Using Competitor Data

```
Step 1: Gather Competitor Data
Competitor A (leader): $200M ARR, est. 35% market share
Competitor B: $80M ARR, est. 15% market share
Competitor C: $50M ARR, est. 10% market share

Step 2: Calculate Implied Market
From Competitor A: $200M / 0.35 = $571M
From Competitor B: $80M / 0.15 = $533M
From Competitor C: $50M / 0.10 = $500M

Step 3: Triangulate
Average: ($571M + $533M + $500M) / 3 = $535M
Conservative estimate (highest share %): $500M

SAM = $500-535M
```

### Pros and Cons
✅ Based on actual market activity
✅ Good reality check
✅ Simple methodology
❌ Competitor data often private
❌ Market share estimates are guesses
❌ Misses future growth

## Triangulation Framework

Use multiple methods and reconcile:

| Method | Estimate | Confidence | Weight |
|--------|----------|------------|--------|
| Top-Down | $100M | Medium | 30% |
| Bottom-Up | $75M | High | 40% |
| Competitive Proxy | $90M | Medium | 30% |
| **Weighted Average** | **$86M** | | |

## Sensitivity Analysis

Test key assumptions:

| Scenario | Key Change | SAM Impact |
|----------|------------|------------|
| Base Case | - | $86M |
| Optimistic | +20% addressable | $103M |
| Pessimistic | -20% addressable | $69M |
| Price Up | +$10 ARPU | $92M |
| Price Down | -$10 ARPU | $80M |

## Common Mistakes

### Mistake 1: TAM as Your Market
❌ "The CRM market is $50B, so our opportunity is $50B"
✅ Apply realistic constraints to reach SAM

### Mistake 2: Ignoring Competition
❌ "We can get 50% of the market in year 1"
✅ New entrants typically capture <1% initially

### Mistake 3: Outdated Sources
❌ Using 2019 report for 2024 analysis
✅ Adjust for growth or find recent data

### Mistake 4: Double Counting
❌ Including same customers in multiple segments
✅ Use mutually exclusive segments

### Mistake 5: Aspirational Sizing
❌ "If we expand to 10 products, TAM is..."
✅ Size for current offering, note expansion potential separately
