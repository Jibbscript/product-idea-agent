---
name: gtm-channels
description: Identifies go-to-market channels and customer acquisition strategies. Use when planning how to reach customers, designing growth strategies, or evaluating marketing channels.
license: Apache-2.0
metadata:
  author: product-idea-agent
  pack: product-idea-agent
allowed-tools: Read Write WebSearch WebFetch
---

# Go-to-Market Channels

Identifies acquisition channels, growth strategies, and launch plans.

## Quick Start

Given prior artifacts, plan the GTM:
1. Research where ICP spends time
2. Identify viable acquisition channels
3. Estimate CAC per channel
4. Design growth loops
5. Output `gtm_plan.md`

## Inputs Required

- `idea_brief.md` (from idea-brief-creator)
- `icp.yaml` (from problem-segment) - where customers are
- `market_size.md` (from market-sizing) - for scale planning
- `mvp_spec.md` (from solution-wedge) - for positioning

## Step-by-Step Workflow

### Step 1: Map Customer Presence

From the ICP, identify where target customers:
- **Discover products**: Search engines, social media, word of mouth
- **Consume content**: Blogs, podcasts, newsletters, YouTube
- **Engage professionally**: LinkedIn, conferences, communities
- **Make purchases**: Direct, through marketplaces, via partners

### Step 2: Identify Channel Options

For each channel category, list options:

**Content Channels:**
- SEO / Organic search
- Content marketing / Blog
- YouTube / Video
- Podcasts

**Paid Channels:**
- Google Ads / Search
- Meta Ads (Facebook/Instagram)
- LinkedIn Ads
- Display / Programmatic

**Social Channels:**
- Twitter/X
- LinkedIn organic
- Reddit
- TikTok
- Communities (Discord, Slack)

**Direct Channels:**
- Cold email
- Outbound sales
- Events / Conferences
- Webinars

**Product-Led Channels:**
- Referral programs
- Viral loops
- Freemium conversion
- Marketplace listings

### Step 3: Evaluate Each Channel

Score channels on:
- **ICP Presence**: Are your customers there? (1-5)
- **CAC Efficiency**: Cost to acquire? (1-5, lower is better)
- **Scalability**: Can it grow? (1-5)
- **Team Fit**: Do you have expertise? (1-5)

Prioritize top 3-5 channels.

### Step 4: Estimate CAC Per Channel

Research typical CAC for your category:
- "[channel] customer acquisition cost [category]"
- "[competitor] marketing strategy"
- "average CAC [channel] B2B/B2C"

Adjust for your specific situation:
- Higher for crowded categories
- Lower for strong product-market fit
- Varies by geography and segment

### Step 5: Design Growth Loops

Identify self-reinforcing growth mechanisms:

**Viral Loop:**
User → Invites Friends → Friends Become Users → Repeat

**Content Loop:**
Content → SEO Traffic → Users → User-Generated Content → More SEO

**Paid Loop:**
Revenue → Reinvest in Ads → More Users → More Revenue

**Sales Loop:**
Customer → Case Study → Credibility → More Customers

### Step 6: Plan Launch Sequence

**Pre-Launch (4-8 weeks before):**
- Waitlist building
- Community seeding
- Content creation
- Partner outreach

**Launch:**
- Product Hunt / directory submissions
- PR / announcements
- Paid campaign burst
- Community engagement

**Post-Launch:**
- Onboarding optimization
- Retention focus
- Channel optimization
- Scale what works

### Step 7: Define 90-Day Milestones

Set measurable targets:
- Day 30: [specific metric]
- Day 60: [specific metric]
- Day 90: [specific metric]

### Step 8: Generate Artifact

Create `gtm_plan.md` following the contract format.

## Workflow Checklist

```
GTM Planning Progress:
- [ ] Customer presence mapped
- [ ] Channel options identified
- [ ] Channels evaluated and prioritized
- [ ] CAC estimated per channel
- [ ] Growth loops designed
- [ ] Launch sequence planned
- [ ] 90-day milestones defined
- [ ] gtm_plan.md created
```

## Output Format

Create `gtm_plan.md` following the artifact contract in `contracts/gtm_plan.md`.

Required sections:
- Primary channels table (3-5 channels)
- Channel details (top 2-3 with deep dive)
- Launch strategy (pre, during, post)
- Growth loops
- 90-day milestones

## Working the Channel Mix

CAC benchmarks, community mapping and competitor go-to-market teardowns are independent lookups, so fan out one sub-agent per channel under consideration and reconcile their estimates into the channel table. Depth belongs to the top two or three channels, while the rest of the list needs only enough evidence to justify not choosing it; research past that is spend the plan cannot use. CAC is the easiest number in this plan to invent, so a benchmark from a published report is sourced, a figure derived from a competitor's spend is an estimate, and a channel with neither carries unverified beside its number.

Your judgment is what separates a channel list from a plan, so name the one channel that is non-obvious for this ICP and say what would change your mind about the primary. `gtm_plan.md` is read by risk-assessment for go-to-market risk and by scorecard-generator's GTM Viability dimension, so a channel listed without conviction becomes a score that overstates the path to customers. Lead with the primary channel and the first ninety days, then the evaluation that got you there.

The deliverable is `gtm_plan.md`; creating accounts, drafting ad copy or contacting communities is outside it. Before you finish, re-read the channel table against `pricing.yaml`: a CAC that exceeds a year of ARPC is arithmetic to catch here rather than after launch.

## Research Query Templates

### Finding ICP Channels
- "where do [customer segment] spend time online"
- "[industry] marketing channels"
- "[customer type] communities"

### CAC Research
- "[channel] CAC [industry]"
- "[category] customer acquisition cost benchmark"
- "average [channel] CPC [industry]"

### Competitor GTM
- "how [competitor] acquired customers"
- "[competitor] marketing strategy"
- "[competitor] growth case study"

### Channel Best Practices
- "[channel] best practices [category]"
- "how to market [product type]"
- "[channel] for startups"

## Channel Playbook Snippets

### SEO/Content (6-12 month ramp)
- Create 10-20 pillar pages for core keywords
- Target long-tail keywords for quick wins
- Build topical authority over time
- Expected: 10-30% of traffic at scale

### LinkedIn (B2B)
- Personal brand building by founder
- Thoughtful comments on ICP content
- Original posts 3-5x/week
- Direct outreach to warm connections

### Product Hunt Launch
- Build community pre-launch
- Line up supporters for launch day
- Prepare for traffic spike
- Have onboarding ready

### Paid Search
- Start with exact match keywords
- Small budget to test ([$500-2K]/month)
- Optimize landing pages for conversion
- Scale what hits target CAC

## Edge Cases

**No clear channel stands out:**
- Default to content + community for B2B
- Default to paid social for B2C
- Test multiple channels with small budgets

**Highly competitive channels:**
- Look for second-tier alternatives
- Consider partnerships instead
- Focus on differentiation in messaging

**Limited budget:**
- Prioritize organic/low-cost channels
- Focus on community and referrals
- Consider design partners for validation

**Enterprise sales:**
- Direct sales likely primary channel
- Content for demand generation
- Events and conferences
- Longer timeline expected

## References

- [channel_playbooks.md](references/channel_playbooks.md): Detailed channel strategies
