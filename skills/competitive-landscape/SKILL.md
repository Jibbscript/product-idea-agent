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

## Outcome

A finished `competitors.csv` names three to five direct competitors and two to three indirect alternatives, one row each, fills every profile field on positioning, pricing, product, and threat or marks it unknown, and closes with a judgment about how crowded the market is and where a new entrant could stand apart.

## Inputs Required

- `idea_brief.md` (from idea-brief-creator)
- Target market/segment context

## Who reads competitors.csv

pricing-wtp reads price_low and price_high as the floor and ceiling of its benchmark range; solution-wedge mines the weaknesses column for the gap to wedge into; market-sizing cross-checks its TAM against competitor revenue and customer counts; and scorecard-generator inverts threat_level into its Competitive Intensity dimension. Each of them trusts the column it reads.

That trust is the reason a blank cell is never neutral. A blank price column reaches an investor only through validation_report.md, by which point it has become a pricing recommendation with nothing under it; a weaknesses column that says "limited features" gives solution-wedge no gap to name.

## What competitors.csv Must Cover

### Direct Competitors
The companies a buyer would compare against this product in a purchasing decision: they solve the same core problem and target the same customer segment. The searches that surface them are "[problem] software", "[solution type] tool", and "[competitor name] alternatives", alongside listings on Product Hunt, G2, and Capterra. Three to five is the useful range; beyond that the profiles get thin and the intensity judgment gets no sharper.

### Indirect Alternatives
The adjacent solutions customers reach for today when no direct competitor fits: a different approach to the same problem, broader tools with relevant features, professional services alternatives, and DIY/manual approaches. The status quo is often the real competitor, which is why spreadsheets and consultants belong here as rows and not as footnotes.

### Per-Competitor Profile
The fields researched for every competitor and alternative, which map onto the CSV columns:

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

### Competitive Intensity
A single 1-10 reading of the market as a whole, informed by the number of well-funded competitors, market concentration (leaders vs fragmented), the rate of new entrants, and the level of feature parity:
- 1-2: Blue ocean, no direct competitors
- 3-4: Few competitors, clear gaps
- 5-6: Moderate competition, differentiation possible
- 7-8: Crowded, hard to differentiate
- 9-10: Red ocean, dominated by incumbents

### Feature Gaps
A feature matrix: the key features customers need, which competitors have each, and where coverage is thin. The interesting cells are the features everyone lacks, the features only leaders have, and emerging requirements nobody has addressed yet, because those are where a wedge can go.

### Differentiation Opportunities
The answer, grounded in the gaps and weaknesses above, to four questions:
- Where are competitors weak?
- What do customers complain about?
- What's changing in the market?
- What's possible now that wasn't before?

## How to Work

Each competitor profile is an independent research pass over one company, so profiles do not queue behind each other. Intensity, feature gaps, and differentiation are judgments over the completed set and cannot be made until the set exists. Enough is reached when a reader of the CSV could explain, for each row, why that company is or is not a threat.

## Constraints

Three to five direct competitors and two to three indirect alternatives appear as rows. Every profile field is populated or explicitly marked unknown, because a blank cell downstream reads as "not researched" while an unknown reads as "researched, not public". Pricing is recorded for every row that publishes it. Every row carries a threat_level on the 1-10 scale in the Threat Level Assessment table below. The finished `competitors.csv` conforms to `contracts/competitors.csv`.

## What a strong competitors.csv looks like

A positioning meeting is where this file gets used, and a founder has to be able to defend every row of it there. A strong landscape names, for each competitor, one weakness that a real customer complained about (with the review or thread it came from) rather than a weakness inferred from the feature list, and it separates direct from indirect so cleanly that a reader can tell which rows would appear on the same buyer's shortlist with no further explanation. Brand names with strengths that would fit any company in the category ("strong brand", "good UX"), beside a threat_level column filled in by feel, is the file that gets taken apart on its first row.

Every row carries a URL, because the file is only as useful as the fastest way to check it, and a threat score with no page behind it is an opinion in a numeric column.

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

## Working the Landscape

Each competitor's pricing page, funding history and review-site complaints are independent research, so spawn one sub-agent per competitor and let them work concurrently, then reconcile the returned rows into `competitors.csv`. Five competitors researched deeply beat fifteen researched shallowly, and how deep to go on any one of them scales with its threat level; a 3 rarely earns more than a visit to the pricing page. Funding amounts and employee counts enter the CSV only when a page states them, figures inferred from headcount patterns are marked as an estimate, and anything unverified stays labeled unverified rather than quietly filled in.

Steelman the strongest incumbent before assigning its threat level, because the counter-intuitive reading, that the category is crowded precisely because customers keep paying, is worth more to a founder than a tidy list of weaknesses. `competitors.csv` is read downstream by pricing-wtp, which benchmarks against the price_low and price_high columns, by solution-wedge, which hunts the feature gaps mapped here, and by scorecard-generator, which reads competitive intensity from it, so a competitor skipped now becomes a gap that was never really open. Lead with how contested the space is and who the real threat is, then the row-by-row detail.

The deliverable is `competitors.csv`; choosing the positioning response to these competitors is solution-wedge's work, so map the landscape and stop there. Before you finish, verify the numbers in both price columns resolve to a live pricing page and confirm no row's threat_level contradicts its own strengths field.

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
