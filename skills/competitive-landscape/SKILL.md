---
name: competitive-landscape
description: Maps competitive landscape including direct competitors, alternatives, and market gaps. Use when understanding who else solves this problem, identifying differentiation opportunities, or analyzing competitive threats.
license: Apache-2.0
metadata:
  author: product-idea-agent
  pack: product-idea-agent
allowed-tools: Read Write WebSearch WebFetch Grep
---

# Competitive Landscape Analysis

Maps competitors, alternatives, and market gaps to identify differentiation opportunities.

## Quick Start

Given an idea brief, map the competitive landscape:
1. Search for direct competitors
2. Identify indirect alternatives
3. Analyze positioning and pricing
4. Map feature coverage gaps
5. Output `competitors.csv`

## Inputs Required

- `idea_brief.md` (from idea-brief-creator)
- Target market/segment context

## Step-by-Step Workflow

### Step 1: Identify Direct Competitors
Search for companies solving the same problem:
- "[problem] software"
- "[solution type] tool"
- "[competitor name] alternatives"
- Check Product Hunt, G2, Capterra

List companies that:
- Solve the same core problem
- Target the same customer segment
- Would be compared in a buying decision

### Step 2: Identify Indirect Alternatives
Find adjacent solutions customers might use:
- Different approach to same problem
- Broader tools with relevant features
- Professional services alternatives
- DIY/manual approaches

### Step 3: Analyze Each Competitor

For each competitor, research:

**Basic Info:**
- Company name and URL
- Year founded
- Funding status/amount
- Employee count (LinkedIn)

**Positioning:**
- Target customer
- Key value proposition
- Market position (leader/challenger/niche)

**Pricing:**
- Pricing model (subscription, usage, onetime)
- Price range (low to high tier)
- Free tier availability

**Product:**
- Key features (5-10)
- Strengths (2-3)
- Weaknesses (2-3)
- Technology/platform

### Step 4: Assess Competitive Intensity

Calculate overall competitive intensity:
- Number of well-funded competitors
- Market concentration (leaders vs fragmented)
- Rate of new entrants
- Feature parity level

Score 1-10:
- 1-2: Blue ocean, no direct competitors
- 3-4: Few competitors, clear gaps
- 5-6: Moderate competition, differentiation possible
- 7-8: Crowded, hard to differentiate
- 9-10: Red ocean, dominated by incumbents

### Step 5: Map Feature Gaps

Create a feature matrix:
- List key features customers need
- Map which competitors have each feature
- Identify underserved areas

Look for:
- Features everyone lacks
- Features only leaders have
- Emerging requirements not yet addressed

### Step 6: Identify Differentiation Opportunities

Based on gaps and weaknesses:
- Where are competitors weak?
- What do customers complain about?
- What's changing in the market?
- What's possible now that wasn't before?

### Step 7: Generate Artifact

Create `competitors.csv` following the contract format.

## Workflow Checklist

```
Competitive Analysis Progress:
- [ ] Direct competitors identified (3-5)
- [ ] Indirect alternatives listed (2-3)
- [ ] Basic info gathered for each
- [ ] Pricing models documented
- [ ] Key features mapped
- [ ] Strengths/weaknesses analyzed
- [ ] Threat levels assigned
- [ ] competitors.csv created
```

## Output Format

Create `competitors.csv` following the artifact contract in `contracts/competitors.csv`.

Required columns:
- name, url, category (direct/indirect/alternative)
- pricing_model, price_low, price_high
- founded, funding
- key_features (semicolon-separated)
- strengths, weaknesses (semicolon-separated)
- market_position (leader/challenger/niche/emerging)
- threat_level (1-10)

## Research Query Templates

### Finding Competitors
- "[problem] software"
- "[solution] tool 2024"
- "best [category] tools"
- "[competitor] alternatives"
- "[competitor] vs"

### Review Sites
- "site:g2.com [category]"
- "site:capterra.com [solution]"
- "site:producthunt.com [problem]"

### Pricing Research
- "[competitor] pricing"
- "[competitor] plans"
- "[competitor] cost"

### Weakness Research
- "[competitor] review complaints"
- "[competitor] cons reddit"
- "[competitor] problems"
- "[competitor] switching from"

### Funding/Company Info
- "[competitor] crunchbase"
- "[competitor] funding"
- "[competitor] linkedin employees"

## Threat Level Assessment

| Score | Threat Level | Criteria |
|-------|--------------|----------|
| 9-10 | Critical | Well-funded leader, strong brand, could easily copy |
| 7-8 | High | Established player, good product, active development |
| 5-6 | Medium | Capable competitor, some weaknesses exploitable |
| 3-4 | Low | Weaker execution, niche focus, limited resources |
| 1-2 | Minimal | Outdated, poorly maintained, or very different focus |

## Edge Cases

**No direct competitors found:**
- This is a red flag - validate that demand exists
- Look harder for indirect alternatives
- Consider why no one has solved this

**Too many competitors:**
- Focus on top 5-7 most relevant
- Group similar competitors
- Prioritize by threat level

**Competitor information sparse:**
- Use LinkedIn for employee counts
- Check press releases
- Look at customer case studies
- Note data limitations

**Fast-moving market:**
- Note date of research
- Flag if landscape is changing rapidly
- Identify emerging players

## References

- [analysis_framework.md](references/analysis_framework.md): Detailed competitive analysis framework
