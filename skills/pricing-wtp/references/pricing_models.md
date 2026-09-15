# Pricing Models Deep Dive

Detailed analysis of pricing models, strategies, and psychology.

## Pricing Model Comparison

### Subscription Pricing

**How it works**: Recurring payments (monthly/annual) for ongoing access.

**When to use**:
- Continuous value delivery
- Regular product updates
- High retention potential
- Predictable cost structure

**Variations**:
- Per-seat: $X per user per month
- Tiered: Different feature sets at different prices
- Flat-rate: One price for unlimited usage
- Per-unit: Price per resource (storage, projects, etc.)

**Example structure**:
```
Starter: $29/month (3 users, 10 projects)
Pro: $79/month (10 users, unlimited projects)
Business: $199/month (25 users, all features)
Enterprise: Custom (unlimited, SLA, support)
```

**Benchmarks by segment**:
| Segment | Typical Monthly | Typical Annual Discount |
|---------|-----------------|-------------------------|
| Consumer | $5-15 | 15-20% |
| SMB | $20-100 | 15-20% |
| Mid-Market | $100-500 | 10-15% |
| Enterprise | $1,000+ | 5-10% |

### Usage-Based Pricing

**How it works**: Pay for what you use (API calls, transactions, etc.).

**When to use**:
- Variable usage patterns
- Clear usage metric tied to value
- Customers want cost control
- High volume potential

**Variations**:
- Per-unit: $0.01 per API call
- Tiered usage: First 1K free, then $X per 1K
- Credits: Pre-purchase credits, use as needed

**Example structure**:
```
Free: 1,000 API calls/month
Pay-as-you-go: $0.001 per call after free tier
Volume: Discounts at 100K, 1M, 10M call thresholds
Enterprise: Custom pricing, committed volume
```

### Freemium

**How it works**: Free tier with paid upgrades for more features/usage.

**When to use**:
- Low marginal cost to serve free users
- Strong conversion funnel
- Network effects benefit from scale
- Category needs education

**Key metrics**:
- Free to paid conversion: 2-5% is typical
- Time to convert: Track cohort conversion curves
- Free user LTV: Consider referral/network value

**Feature gating strategies**:
```
Free: Core features, limited usage, watermarks
Paid: Remove limits, add features, remove branding
```

### One-Time Purchase

**How it works**: Single payment for permanent access.

**When to use**:
- Discrete value delivery
- Low ongoing costs
- Customer expects ownership
- Impulse purchase potential

**Variations**:
- Perpetual license: Pay once, own forever
- Credits/consumables: One-time purchase, consumed over time
- Lifetime deal: One-time for ongoing access (risky!)

## Pricing Psychology

### Anchoring

Present a high-priced option first to make others seem reasonable.

```
Enterprise: $999/month ← Anchor
Pro: $199/month ← Seems reasonable
Starter: $49/month ← Great deal
```

### Decoy Effect

Add an option that makes another look better.

```
Basic: $20/month (5 users)
Pro: $50/month (10 users) ← Decoy
Business: $75/month (25 users) ← Clearly better than Pro
```

### Charm Pricing

$99 feels significantly less than $100.

Use for:
- Consumer products
- Lower-priced tiers
- Psychological barriers ($100, $1000)

Avoid for:
- Enterprise pricing (looks cheap)
- Premium positioning

### Value Framing

Frame price in terms of value, not cost.

❌ "$99/month"
✅ "Less than $4/day"
✅ "Saves 10 hours/week = $500 in time"

## Unit Economics Benchmarks

### SaaS Benchmarks

| Metric | Healthy Target | Warning Sign |
|--------|----------------|--------------|
| LTV:CAC | 3:1 or higher | Below 2:1 |
| CAC Payback | 12 months or less | Over 18 months |
| Gross Margin | 70-80% | Below 60% |
| Net Revenue Retention | 100%+ | Below 90% |
| Logo Churn | <5% annually | >10% annually |

### CAC Benchmarks by Channel

| Channel | Typical CAC Range | Notes |
|---------|-------------------|-------|
| Organic/SEO | $50-200 | Slow but efficient |
| Content Marketing | $100-300 | Requires investment |
| Paid Search | $200-500 | Competitive categories higher |
| Paid Social | $150-400 | Depends on targeting |
| Outbound Sales | $500-2,000 | High touch, high value |
| Enterprise Sales | $5,000-50,000 | Long cycle, high ACV |

### LTV Calculation

```
LTV = ARPU × Gross Margin × Average Lifetime

Example:
ARPU = $100/month
Gross Margin = 80%
Average Lifetime = 24 months (based on 4% monthly churn)

LTV = $100 × 0.80 × 24 = $1,920
```

## Price Testing Approaches

### Van Westendorp Price Sensitivity

Survey questions:
1. At what price is this too expensive?
2. At what price is this expensive but acceptable?
3. At what price is this a bargain?
4. At what price is this too cheap (quality concern)?

Plot responses to find optimal price range.

### A/B Testing Considerations

- Test significant price differences (not $99 vs $97)
- Consider customer segment differences
- Account for conversion AND lifetime value
- Be careful of customer perception if discovered

### Competitive Price Position

| Position | Relative Price | When to Use |
|----------|----------------|-------------|
| Premium | 20-50% above | Superior product, strong brand |
| Parity | ±10% of average | Matching competition |
| Value | 20-30% below | Cost leadership, new entrant |
| Disruptor | 50%+ below | Category disruption |

## Common Pricing Mistakes

### Mistake 1: Pricing Too Low
- Undervalues the product
- Attracts wrong customers
- Hard to raise later
- Unsustainable economics

### Mistake 2: Too Many Tiers
- Confuses buyers
- Complicates messaging
- Operational overhead
- Stick to 3-4 tiers maximum

### Mistake 3: Feature-Based Only
- Ignores usage patterns
- May not align with value
- Consider hybrid approaches

### Mistake 4: Ignoring Segments
- Different customers have different WTP
- Consider segment-specific pricing
- Use packaging to separate

### Mistake 5: Set and Forget
- Markets change
- Costs change
- Value perception changes
- Review pricing annually
