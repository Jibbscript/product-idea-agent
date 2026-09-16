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

## Outcome

`gtm_plan.md` is a plan for reaching the ICP that names one primary channel, ranks the supporting ones, estimates what a customer costs to acquire through each, and lays out a launch sequence with 90-day milestones.

## Inputs Required

- `idea_brief.md` (from idea-brief-creator)
- `icp.yaml` (from problem-segment) - where customers are
- `market_size.md` (from market-sizing) - for scale planning
- `mvp_spec.md` (from solution-wedge) - for positioning

## Who reads gtm_plan.md

risk-assessment reads this plan for the go-to-market risks (a single channel, a CAC that only works at scale, a launch that depends on one partner); scorecard-generator turns the channel shortlist into its GTM Viability dimension at 15% of the composite; and validation-report carries the launch strategy into its Go-to-Market section. This plan reaches whoever is being asked for money only through validation_report.md and through GTM Viability in scorecard.json; what they see is whether a founder knows where to start on Monday.

That is why a plan listing eight channels scores no better than one listing three: the dimension measures whether the first move has been chosen, so the eight-channel version reads as a plan not yet made.

## What gtm_plan.md Must Cover

### Customer Presence
Where the ICP actually is, which decides which channels are even candidates. The map covers where target customers:
- **Discover products**: Search engines, social media, word of mouth
- **Consume content**: Blogs, podcasts, newsletters, YouTube
- **Engage professionally**: LinkedIn, conferences, communities
- **Make purchases**: Direct, through marketplaces, via partners

### Channel Options
The candidate channels, drawn from this catalogue and filtered by customer presence:

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

### Channel Evaluation
Each candidate scored on four criteria:
- **ICP Presence**: Are your customers there? (1-5)
- **CAC Efficiency**: Cost to acquire? (1-5, lower is better)
- **Scalability**: Can it grow? (1-5)
- **Team Fit**: Do you have expertise? (1-5)

The top 3-5 channels carry forward, with one named as primary.

### CAC Per Channel
A cost-to-acquire estimate for each channel that carried forward, researched through:
- "[channel] customer acquisition cost [category]"
- "[competitor] marketing strategy"
- "average CAC [channel] B2B/B2C"

Benchmarks are adjusted for the specific situation: higher for crowded categories, lower for strong product-market fit, and varying by geography and segment. Each figure is labelled sourced, estimated, or unverified, because adjusting a published benchmark turns it into an estimate and the label is how the reader tells the two apart.

### Growth Loops
The self-reinforcing mechanisms the plan relies on, of these shapes:

**Viral Loop:**
User → Invites Friends → Friends Become Users → Repeat

**Content Loop:**
Content → SEO Traffic → Users → User-Generated Content → More SEO

**Paid Loop:**
Revenue → Reinvest in Ads → More Users → More Revenue

**Sales Loop:**
Customer → Case Study → Credibility → More Customers

A plan without a loop is a plan that buys every customer; the loop is what makes growth compound.

### Launch Sequence
The plan's launch plays, in the order they happen in the market:

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

### 90-Day Milestones
Dated, measurable targets:
- Day 30: [specific metric]
- Day 60: [specific metric]
- Day 90: [specific metric]

## How to Work

Customer presence determines which channels are even candidates, so it is mapped before channels are evaluated. Evaluation and CAC estimation are two passes over the same candidate list and can be done together. Growth loops depend on the product and the primary channel. The launch sequence and milestones are written once a primary channel is chosen, because a launch plan for an undecided channel is a list of options, not a plan.

## Constraints

The plan names one primary channel rather than ranking five equally. Every CAC figure is labelled sourced, estimated, or unverified and carries its source when it has one. The 90-day milestones are dated and measurable. The channel table covers 3-5 channels and the top 2-3 get a deep dive, matching the sections the contract expects. The finished `gtm_plan.md` conforms to `contracts/gtm_plan.md`.

## What a strong gtm_plan.md looks like

This plan earns its name when a founder can start the first channel this week on the budget they actually have. A strong plan names three channels, gives a CAC estimate for each with the benchmark it came from, and says why the ICP is there (the subreddit, the conference, the newsletter, by name), with the first channel marked as first and the Day 30 number that would show it working. A weak plan gives CAC as "varies", which means a reader can only guess what happens on Monday, and so could the founder.

The launch sequence weighs most with investors, since a launch with a waitlist number and a date is a commitment and one without is a hope.

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

Your judgment is what separates a channel list from a plan, so name the one channel that is non-obvious for this ICP and say what would change your mind about the primary. `gtm_plan.md` is read by risk-assessment, which needs to see where the plan could fail, and by scorecard-generator's GTM Viability dimension, so a channel listed without conviction becomes a score that overstates the path to customers. Lead with the primary channel and the first ninety days, then the evaluation that got you there.

The deliverable is `gtm_plan.md`; creating accounts, drafting ad copy or contacting communities is outside it. Before you finish, re-read the channel table against `pricing.yaml`: a CAC that exceeds a year of ARPC is arithmetic to catch here rather than after launch.

## Research Query Templates

### Finding ICP Channels
```text
"where do [customer segment] spend time online"
"[industry] marketing channels"
"[customer type] communities"
```

### CAC Research
```text
"[channel] CAC [industry]"
"[category] customer acquisition cost benchmark"
"average [channel] CPC [industry]"
```

### Competitor GTM
```text
"how [competitor] acquired customers"
"[competitor] marketing strategy"
"[competitor] growth case study"
```

### Channel Best Practices
```text
"[channel] best practices [category]"
"how to market [product type]"
"[channel] for startups"
```

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
