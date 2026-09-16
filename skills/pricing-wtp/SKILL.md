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

## Outcome

A finished `pricing.yaml` recommends a pricing model and value ladder for this product, backed by what competitors charge, what adjacent markets charge, what the product is worth to the customer, and what customers have said they will pay, and ends in unit economics (ARPC, CAC, LTV:CAC, payback).

## Inputs Required

- `idea_brief.md` (from idea-brief-creator)
- `competitors.csv` (from competitive-landscape) - for pricing benchmarks
- `icp.yaml` (from problem-segment) - for buyer context

## Who reads pricing.yaml

scorecard-generator pulls the LTV:CAC ratio and the unit economics into its GTM Viability dimension, and validation-report presents the value ladder as the revenue story in its Business Model section. No skill between here and the report re-benchmarks a price, and the first price a founder quotes on a sales call is whatever the value ladder said, as relayed through that section.

The LTV:CAC an investor eventually sees is this file's arithmetic carried through scorecard.json, so a tier priced on feel becomes, two artifacts later, a revenue projection nobody can trace back to a benchmark or a value calculation.

## What pricing.yaml Must Cover

### Competitor Pricing
What `competitors.csv` already holds, extended by direct research: pricing models (subscription, usage, onetime), price ranges (low to high tiers), free tier availability, and enterprise/custom pricing. Pricing pages give the list price; "[competitor] pricing page", "[competitor] plans comparison", and "[competitor] pricing reddit" searches surface what customers actually pay after discounts and overages, and both belong in the benchmark.

### Adjacent Market Pricing
What related categories charge, because the buyer's sense of a fair price is anchored there: similar solutions for different segments, different solutions for the same problem, and complementary products the buyer already pays for.

### Value Delivered
The customer's ROI, built from three questions:
- What's the current cost of the problem?
- What value does your solution deliver?
- What's the expected ROI multiple?

**Pricing Rule of Thumb**: Price at 10-20% of value delivered

The value figure states the assumption it rests on (hours saved, revenue recovered, headcount avoided), since the rule of thumb is only as good as the value estimate under it.

### Willingness-to-Pay Evidence
What customers have said or shown about what they will pay: competitor customer reviews mentioning price, Reddit/forum discussions about pricing, survey data on software spending, and industry benchmarks for the category. Two independent sources is the floor; a single enthusiastic thread is an anecdote.

### Value Ladder
The tiers the product will sell at:
1. **Free/Lead Magnet**: Acquisition driver
2. **Starter**: Entry-level conversion
3. **Pro/Growth**: Core revenue tier
4. **Enterprise**: High-value accounts

Each tier specifies:
- Features included/excluded
- Usage limits
- Price point
- Billing cycle

Not every product needs all four; a ladder with two well-separated tiers beats one with four that blur together. The Value Ladder Framework below gives typical ranges per tier.

The tiers are a ladder in the literal sense: read top to bottom, each rung carries a higher price and a larger offering than the one before it, which is the contract's validation rule and also what lets validation-report retell it as one ascending story. A rung that breaks the order is usually a different product wearing a tier label, a per-lead fee a third party pays sitting under the customer's own plans, for instance, and it belongs in a separate revenue line with its own buyer rather than as a fourth rung priced below the third. The ladder is checked for increasing price and increasing value before it is written, because the check costs nothing here and the contradiction cannot be recovered once scorecard-generator has read one number from it.

### Unit Economics
The four numbers the ladder implies:
- **ARPC**: Average Revenue Per Customer (monthly)
- **Estimated CAC**: Cost to acquire a customer
- **LTV:CAC Ratio**: Should be 3:1 or higher
- **Payback Period**: Months to recover CAC

LTV:CAC is arithmetic over fields already in the file, ARPC times gross margin times the customer lifetime the comment states, divided by the CAC listed, and the ratio appears once, in the `ltv_cac_ratio` field, with that formula and its inputs beside it. A ratio the comment works out to one value and the field reports as another, after an adjustment mentioned but never applied, hands scorecard-generator two numbers to choose from, so any adjustment goes into the inputs and the ratio is recomputed from them rather than corrected by hand at the end.

## How to Work

Competitor pricing, adjacent-market pricing, and willingness-to-pay evidence are three independent searches with no order among them. The value calculation depends only on the idea brief and the ICP. The value ladder is the synthesis of all four, and the unit economics follow from the ladder's prices, so those two are written last.

## Constraints

Competitor prices carry the URL and the date observed, because pricing pages change without notice. The value figure states the assumption it rests on. Every ladder tier names its price, its buyer, and what it excludes. At least two competitor benchmarks and two willingness-to-pay sources are cited. The recommendation names a pricing model from the options table below and gives its rationale in terms of the evidence gathered. The finished `pricing.yaml` conforms to `contracts/pricing.yaml`.

## What a strong pricing.yaml looks like

The test is whether a reader can see why Pro costs what it costs. A strong pricing file ties each tier to either a named competitor benchmark or a stated value calculation, and says which one it used; a weak one lists round numbers that feel right and a 3:1 LTV:CAC that was chosen rather than computed. The difference shows in the recommendation: "Pro at $79 because Competitor A charges $99 for a comparable tier and the ROI estimate supports 15% of $6,000 in annual value" can be argued with, while "Pro at $79" cannot.

The value ladder has to survive being summarised in one paragraph of validation_report.md and one number in scorecard.json, because that compressed form is all founders ever see of it.

## Output Format

Create `pricing.yaml` following the artifact contract in `contracts/pricing.yaml`.

Required sections:
- Competitor benchmarks (at least 2)
- Value ladder (at least 2 tiers)
- Unit economics (ARPC, CAC, LTV:CAC, payback)
- WTP evidence (at least 2 sources)
- Recommendation with rationale

## Working the Price

Competitor pricing pages, adjacent-category benchmarks and willingness-to-pay threads are separate lookups, so delegate them to sub-agents working in parallel and reconcile what comes back into the benchmark list. Two solid WTP data points that agree are enough evidence to set a tier, and once the tier prices stop moving as more anecdotes arrive, the extra searching is diminishing returns. A published list price is sourced, a price reconstructed from a customer's forum comment is an estimate, and enterprise pricing hidden behind a Contact Sales button stays unverified; each WTP evidence entry says which of the three it is.

Your judgment is wanted on the contrarian tier, because the price that looks too high often tests better than the safe one, and naming that possibility serves the founder more than centering the ladder on the competitor median. `pricing.yaml` is read downstream by gtm-channels, which plans around the unit economics and checks channel CAC against the ARPC set here, and by scorecard-generator's GTM Viability dimension, so an LTV:CAC ratio that was invented becomes a score someone trusts. Lead with the recommended price point and the one sentence of reasoning behind it, then the benchmarks that justify it.

The deliverable is `pricing.yaml`; drafting pricing-page copy or choosing a billing provider is not part of it. Before you finish, re-read the unit economics and confirm the payback period follows from the ARPC and CAC actually listed rather than from a remembered rule of thumb, that the LTV:CAC in the field is the value its own formula produces, and that the ladder's prices still rise from the first tier to the last.

## Research Query Templates

### Competitor Pricing
```text
"[competitor] pricing"
"[competitor] plans"
"[competitor] cost"
"[competitor] pricing page"
"[competitor] how much site:reddit.com"
```

### Industry Benchmarks
```text
"[category] software pricing benchmark"
"[category] average deal size"
"SaaS pricing best practices [category]"
```

### Willingness to Pay
```text
"would pay for [solution] site:reddit.com"
"[solution] worth the price"
"[alternative] too expensive"
"[category] budget survey"
```

### Value-Based Pricing
```text
"[problem] cost to business"
"[problem] ROI"
"[solution] saves time money"
```

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
