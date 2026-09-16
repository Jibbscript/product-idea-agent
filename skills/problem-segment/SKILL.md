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

## Outcome

A finished `icp.yaml` names one primary customer segment, chosen on evidence from three to five candidates, with the runners-up recorded so the choice can be revisited. It carries the demographic or firmographic profile, the psychographics, the buying behaviors, and a problem-severity score whose evidence is written down next to it.

## Inputs Required

- `idea_brief.md` (from idea-brief-creator)
- `signals.md` (optional, enhances analysis)

## Who reads icp.yaml

Four skills take this file as input and none of them re-interviews a customer. market-sizing turns the segment definition into the percentages of its SAM formula; pricing-wtp reads the buyer context to decide who signs the cheque and which budget line it comes from; solution-wedge ranks jobs-to-be-done against the frustrations recorded here; and gtm-channels reads the information-sources field almost literally, treating each named blog, podcast and community as a candidate channel.

A segment defined loosely makes the SAM arithmetic meaningless two artifacts later, because a percentage is only a percentage of something you can name: "30% of small businesses" is not a number, "30% of US logistics firms with 50-200 employees" is.

## What icp.yaml Must Cover

### Candidate Segments
Three to five potential customer segments drawn from the idea brief, each answering:
- Who has this problem?
- Who has it most severely?
- Who has budget to solve it?

The list considers both obvious and non-obvious segments, because the segment a founder first names is often the one they know rather than the one that hurts most.

### Segment Characteristics
The profile gathered for each candidate segment:

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

### Psychographics
What the primary segment wants, what stands in their way, and what they value:

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

### Behaviors
How the segment discovers products and how it buys them:

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

### Problem Severity
A 1-10 severity score for the segment, built from:
- Frequency: How often does the problem occur?
- Impact: What's the cost/consequence?
- Urgency: How quickly must it be solved?
- Alternatives: How bad are current solutions?

The evidence behind the score sits beside it in the file, since scorecard-generator reads this number directly and needs to see what supports it.

### Segment Prioritization
The ranking of candidate segments by opportunity, weighing:
- Severity of problem (highest first)
- Ability to pay (consider budget)
- Accessibility (can you reach them?)
- Size (is it big enough?)

The top-ranked segment becomes the primary; the others are kept as secondary segments rather than discarded.

## How to Work

Characteristics, psychographics, and behaviors are three independent research passes over the same candidate list, and none of them waits on another. Severity scoring and prioritization need all three in hand, so prioritization is the one place order is forced.

## Constraints

Three to five candidate segments are compared before one is chosen. Severity is scored with cited evidence rather than asserted from intuition. The primary segment is named in the file with the runners-up kept as secondary segments (up to three) so a later pivot has somewhere to go. Demographics or firmographics are filled according to whether the buyer is a person or a company; when that is unclear, both are sketched and the ambiguity is noted. The finished `icp.yaml` conforms to `contracts/icp.yaml`.

## What a strong icp.yaml looks like

A salesperson handed this profile should know which list to buy and which title to call first. Every field in a strong profile is specific enough to be falsified with one interview, so the founder can tell within five conversations whether the segment was wrong; a weak profile describes a demographic nobody could look up ("tech-savvy professionals who value efficiency") and survives every interview unchanged, which is the failure rather than the success.

Read through validation_report.md, the profile is where investors see whether the founder knows the customer by name or only by category.

## Output Format

Create `icp.yaml` following the artifact contract in `contracts/icp.yaml`.

Required fields:
- Primary segment with full details
- Demographics or firmographics (depending on B2C/B2B)
- Psychographics (goals, frustrations, values)
- Behaviors (info sources, purchase triggers, objections)
- Problem severity score with evidence
- Secondary segments (optional, max 3)

## Working the Segment

Firmographics, community behavior and purchase-process research for each candidate segment are independent, so fan them out to one sub-agent per segment and compare the returned profiles side by side. The primary segment gets the deepest research, a full profile, while secondary segments need only enough evidence to rank them, since a sketch of the runners-up serves the downstream skills better than equal shallow coverage of five and effort past that point is detail they cannot use. The problem_severity score cites the evidence it came from, and where a segment's budget or approval process could not be confirmed the field reads unverified rather than carrying a plausible-sounding number.

Your judgment matters most on the non-obvious segment: the adjacent role that feels the pain harder than the one the brief names. `icp.yaml` is read by competitive-landscape, market-sizing and gtm-channels, and both the SAM multipliers and the channel shortlist descend from whichever segment is marked primary, so that segment is described well enough to narrow TAM to SAM and to say where those people spend time. Lead with who the customer is and how badly it hurts them, ahead of the demographic and firmographic detail.

The deliverable is `icp.yaml`; interviewing real customers or drafting outreach to them sits outside this skill. Before you finish, check the artifact against the brief: a severity score of 8 or higher with no quoted evidence behind it is the signal to go back.

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
