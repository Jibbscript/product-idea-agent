---
name: pricing-wtp
description: Researches pricing models and estimates willingness-to-pay for the target market. Use when determining how to price a product, researching what customers will pay, or designing a value ladder.
license: Apache-2.0
metadata:
  author: product-idea-agent
  pack: product-idea-agent
allowed-tools: Read Write WebSearch WebFetch
---

# Pricing & Willingness-to-Pay Research

Researches pricing models, competitor benchmarks, and customer willingness-to-pay.

## Quick Start

Given prior artifacts, research pricing:
1. Analyze competitor pricing models
2. Research pricing in adjacent markets
3. Estimate willingness-to-pay
4. Design value ladder
5. Output `pricing.yaml`

## Inputs Required

- `idea_brief.md` (from idea-brief-creator)
- `competitors.csv` (from competitive-landscape) - for pricing benchmarks
- `icp.yaml` (from problem-segment) - for buyer context

## Step-by-Step Workflow

### Step 1: Analyze Competitor Pricing

From `competitors.csv`, extract:
- Pricing models (subscription, usage, onetime)
- Price ranges (low to high tiers)
- Free tier availability
- Enterprise/custom pricing

Search for additional details:
- "[competitor] pricing page"
- "[competitor] plans comparison"
- "[competitor] pricing reddit" (for real costs)

### Step 2: Research Adjacent Markets

Look at pricing in related categories:
- Similar solutions for different segments
- Different solutions for same problem
- Complementary products

### Step 3: Estimate Value Delivered

Calculate ROI for the customer:
- What's the current cost of the problem?
- What value does your solution deliver?
- What's the expected ROI multiple?

**Pricing Rule of Thumb**: Price at 10-20% of value delivered

### Step 4: Research Willingness-to-Pay

Find evidence of what customers will pay:
- Competitor customer reviews mentioning price
- Reddit/forum discussions about pricing
- Survey data on software spending
- Industry benchmarks for category

### Step 5: Design Value Ladder

Create pricing tiers:
1. **Free/Lead Magnet**: Acquisition driver
2. **Starter**: Entry-level conversion
3. **Pro/Growth**: Core revenue tier
4. **Enterprise**: High-value accounts

For each tier, define:
- Features included/excluded
- Usage limits
- Price point
- Billing cycle

### Step 6: Model Unit Economics

Calculate:
- **ARPC**: Average Revenue Per Customer (monthly)
- **Estimated CAC**: Cost to acquire a customer
- **LTV:CAC Ratio**: Should be 3:1 or higher
- **Payback Period**: Months to recover CAC

### Step 7: Generate Artifact

Create `pricing.yaml` following the contract format.

## Workflow Checklist

```
Pricing Research Progress:
- [ ] Competitor pricing analyzed
- [ ] Adjacent market pricing researched
- [ ] Value delivered estimated
- [ ] WTP evidence gathered
- [ ] Value ladder designed
- [ ] Unit economics modeled
- [ ] pricing.yaml created
```

## Output Format

Create `pricing.yaml` following the artifact contract in `contracts/pricing.yaml`.

Required sections:
- Competitor benchmarks (at least 2)
- Value ladder (at least 2 tiers)
- Unit economics (ARPC, CAC, LTV:CAC, payback)
- WTP evidence (at least 2 sources)
- Recommendation with rationale

## Research Query Templates

### Competitor Pricing
- "[competitor] pricing"
- "[competitor] plans"
- "[competitor] cost"
- "[competitor] pricing page"
- "[competitor] how much site:reddit.com"

### Industry Benchmarks
- "[category] software pricing benchmark"
- "[category] average deal size"
- "SaaS pricing best practices [category]"

### Willingness to Pay
- "would pay for [solution] site:reddit.com"
- "[solution] worth the price"
- "[alternative] too expensive"
- "[category] budget survey"

### Value-Based Pricing
- "[problem] cost to business"
- "[problem] ROI"
- "[solution] saves time money"

## Pricing Model Options

| Model | Best For | Pros | Cons |
|-------|----------|------|------|
| Subscription | SaaS, recurring value | Predictable, compounding | Churn risk |
| Usage-Based | Variable usage patterns | Fair, scales with value | Unpredictable revenue |
| One-Time | Discrete purchases | Simple, immediate revenue | No recurring |
| Freemium | Network effects, virality | Acquisition, scale | Conversion challenge |
| Hybrid | Complex value delivery | Flexible | Confusing |

## Value Ladder Framework

### Tier 1: Free/Lead Magnet
- **Purpose**: Acquire users, demonstrate value
- **Features**: Core functionality, limited usage
- **Price**: $0
- **Conversion goal**: 5-10% to paid

### Tier 2: Starter
- **Purpose**: Convert free users, validate WTP
- **Features**: Full core features, moderate limits
- **Price**: $X/month (low barrier)
- **Typical range**: $9-49/month

### Tier 3: Pro/Growth
- **Purpose**: Core revenue, primary offering
- **Features**: All features, higher limits
- **Price**: $X/month (value sweet spot)
- **Typical range**: $49-199/month

### Tier 4: Enterprise
- **Purpose**: High-value accounts, strategic
- **Features**: Unlimited, customization, support
- **Price**: Custom (annual contract)
- **Typical range**: $10K-100K+/year

## Edge Cases

**No competitor pricing visible:**
- Check archive.org for historical pricing
- Look for customer reviews mentioning price
- Search for pricing disclosure in press releases
- Note as unknown with estimate based on category

**Highly variable pricing:**
- Report the range
- Note key factors that influence price
- Consider usage-based model

**Enterprise-only market:**
- Focus on value-based pricing
- Research typical contract sizes
- Consider ACV (Annual Contract Value) benchmarks

**Price-sensitive market:**
- Note the constraint
- Consider lower price points
- Explore alternative monetization (ads, data, etc.)

## References

- [pricing_models.md](references/pricing_models.md): Detailed pricing model analysis
