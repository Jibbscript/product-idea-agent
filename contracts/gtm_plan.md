# Artifact Contract: gtm_plan.md

## Purpose
Documents go-to-market strategy including channels, tactics, and launch plan.

## Producer
- `gtm-channels` skill

## Consumers
- `risk-assessment`
- `scorecard-generator`
- `validation-report`

## Schema

```markdown
# Go-to-Market Plan

## Channel Strategy

### Primary Channels
| Channel | CAC Est. | Volume | Priority |
|---------|----------|--------|----------|
| [channel] | $[X] | [high/med/low] | 1 |
| [channel] | $[X] | [high/med/low] | 2 |
| [channel] | $[X] | [high/med/low] | 3 |

### Channel Details

#### [Channel 1 Name]
- **Why**: [rationale based on ICP presence]
- **Tactics**: [specific approaches]
- **Metrics**: [what to track]
- **Budget**: [estimated spend]

#### [Channel 2 Name]
- **Why**: [rationale]
- **Tactics**: [specific approaches]
- **Metrics**: [what to track]
- **Budget**: [estimated spend]

## Launch Strategy

### Pre-Launch
- [Activity 1]: [purpose and timing]
- [Activity 2]: [purpose and timing]

### Launch
- [Activity 1]: [purpose]
- [Activity 2]: [purpose]

### Post-Launch
- [Activity 1]: [purpose and timing]
- [Activity 2]: [purpose and timing]

## Growth Loops
- **Loop 1**: [description of viral/network/content effect]
- **Loop 2**: [description of second growth mechanism]

## Partnerships
[Potential partners and integration opportunities]

## 90-Day Milestones
- **Day 30**: [milestone with target metric]
- **Day 60**: [milestone with target metric]
- **Day 90**: [milestone with target metric]
```

## Field Definitions

| Field | Required | Description |
|-------|----------|-------------|
| Primary Channels | Yes | At least 3 channels prioritized |
| Channel Details | Yes | Deep dive on top 2 channels |
| CAC Estimate | Yes | Per-channel acquisition cost |
| Launch Strategy | Yes | Pre, during, and post-launch activities |
| Growth Loops | Yes | At least 1 growth mechanism |
| 90-Day Milestones | Yes | Measurable targets |

## Channel Categories

### Acquisition Channels
- **Content**: SEO, blog, YouTube, podcasts
- **Paid**: Google Ads, Meta Ads, LinkedIn Ads
- **Social**: Twitter/X, LinkedIn, Reddit, TikTok
- **Community**: Forums, Discord, Slack groups
- **Partnerships**: Affiliates, integrations, co-marketing
- **Product-Led**: Viral loops, referral programs
- **Outbound**: Cold email, sales development

### Prioritization Criteria
1. Where does ICP spend time?
2. What's the CAC relative to LTV?
3. Can it scale beyond initial traction?
4. Do you have expertise or unfair advantages?
