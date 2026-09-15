---
name: problem-segment
description: Defines ideal customer profile (ICP), validates problem severity, and segments the market. Use when determining who has the problem, how urgently they need a solution, or when building customer personas.
license: Apache-2.0
metadata:
  author: product-idea-agent
  pack: product-idea-agent
allowed-tools: Read Write WebSearch WebFetch
---

# Problem Segment Analysis

Defines ideal customer profiles and validates problem severity through research and segmentation.

## Quick Start

Given an idea brief, define the ICP:
1. Identify potential customer segments
2. Research segment characteristics
3. Assess problem severity per segment
4. Prioritize segments by opportunity
5. Output `icp.yaml`

## Inputs Required

- `idea_brief.md` (from idea-brief-creator)
- `signals.md` (optional, enhances analysis)

## Step-by-Step Workflow

### Step 1: Identify Potential Segments
From the idea brief, list 3-5 potential customer segments:
- Who has this problem?
- Who has it most severely?
- Who has budget to solve it?

Consider both obvious and non-obvious segments.

### Step 2: Research Segment Characteristics

For each segment, gather:

**Demographics (B2C):**
- Age range
- Gender distribution
- Location/geography
- Income level
- Education level

**Firmographics (B2B):**
- Company size (employees)
- Industry/vertical
- Revenue range
- Role titles (decision maker, user, influencer)
- Technology stack

### Step 3: Define Psychographics

For the primary segment, research:

**Goals:**
- What are they trying to achieve?
- What does success look like?
- What are their aspirations?

**Frustrations:**
- What's blocking them?
- What do they complain about?
- What workarounds do they use?

**Values:**
- What do they prioritize?
- What trade-offs do they make?
- What brands/products do they trust?

### Step 4: Map Behaviors

Research how this segment:

**Finds information:**
- What blogs/publications do they read?
- What podcasts do they listen to?
- What communities are they in?
- Who do they follow?

**Makes purchases:**
- What triggers a purchase decision?
- Who influences the decision?
- What objections do they raise?
- What's their budget/approval process?

### Step 5: Assess Problem Severity

Score problem severity (1-10) based on:
- Frequency: How often does the problem occur?
- Impact: What's the cost/consequence?
- Urgency: How quickly must it be solved?
- Alternatives: How bad are current solutions?

Document evidence for the score.

### Step 6: Prioritize Segments

Rank segments by opportunity:
- Severity of problem (highest first)
- Ability to pay (consider budget)
- Accessibility (can you reach them?)
- Size (is it big enough?)

### Step 7: Generate ICP Artifact

Create `icp.yaml` following the contract format.

## Workflow Checklist

```
Problem Segment Progress:
- [ ] Potential segments identified (3-5)
- [ ] Demographics/firmographics researched
- [ ] Psychographics defined (goals, frustrations)
- [ ] Behaviors mapped (info sources, purchase triggers)
- [ ] Problem severity scored with evidence
- [ ] Segments prioritized
- [ ] icp.yaml created
```

## Output Format

Create `icp.yaml` following the artifact contract in `contracts/icp.yaml`.

Required fields:
- Primary segment with full details
- Demographics or firmographics (depending on B2C/B2B)
- Psychographics (goals, frustrations, values)
- Behaviors (info sources, purchase triggers, objections)
- Problem severity score with evidence
- Secondary segments (optional, max 3)

## Research Query Templates

### Finding Demographics
- "[segment] demographics statistics"
- "[segment] survey data"
- "who uses [competitor]"

### Finding Pain Points
- "[segment] biggest challenges"
- "[role] frustrations site:reddit.com"
- "[segment] problems with [current solution]"

### Finding Information Sources
- "best [topic] blogs for [segment]"
- "[segment] podcasts"
- "[role] communities"

### Finding Purchase Behavior
- "how [segment] buys [category]"
- "[segment] software purchasing process"
- "[role] decision making"

## Edge Cases

**Multiple valid segments:**
- Choose the one with highest severity + ability to pay
- Document others as secondary segments
- Note potential for expansion later

**B2B vs B2C unclear:**
- Look for signals of who pays (individual vs company)
- Consider prosumer segments
- May need to define both

**No clear segment data:**
- Use analogous markets for estimates
- Note low confidence
- Recommend primary research (interviews)

**International markets:**
- Note regional differences
- Consider localization needs
- May have different ICPs per region

## References

- [icp_framework.md](references/icp_framework.md): Detailed ICP framework and templates
