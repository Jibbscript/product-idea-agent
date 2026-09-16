---
name: market-sizing
description: Estimates total addressable market (TAM), serviceable addressable market (SAM), and serviceable obtainable market (SOM) with growth projections. Use when quantifying the market opportunity, sizing an investment, or validating market potential.
license: Apache-2.0
metadata:
  author: product-idea-agent
  pack: product-idea-agent
allowed-tools: Read Write WebSearch WebFetch
---

# Market Sizing Analysis

Estimates TAM/SAM/SOM market sizes with methodology and growth projections.

## Outcome

A finished `market_size.md` gives a TAM, SAM, and SOM for a precisely bounded market, each figure carrying its method, its source, and its date, with growth rates and an honest confidence rating. The numbers matter less than the chain of reasoning between them, because a reader who can follow TAM to SAM to SOM can correct any single figure that turns out wrong.

## Inputs Required

- `idea_brief.md` (from idea-brief-creator)
- `icp.yaml` (from problem-segment) - critical for SAM calculation
- `competitors.csv` (optional, helps validate estimates)

## Who reads market_size.md

gtm-channels reads the SAM to scale its channel plan, scorecard-generator maps the TAM and SAM onto the $10B and $1B bands of its Market Size dimension at 15% of the composite, and validation-report carries the figure into the section an investor turns to first. None of the three re-derives the number; they take it as given.

What makes the figure usable is the method behind it. An investor discounts a TAM they cannot reconstruct, and a founder who cannot defend the multiplication in a meeting loses the room on the second question, so the arithmetic is the deliverable and the dollar figure is a by-product of it.

## What market_size.md Must Cover

### Market Boundaries
A precise statement of what market is being sized: the problem category, the customer segment, the geographic scope, and the time horizon. "B2B SaaS compliance automation for US fintech startups" is the level of specificity that works; "compliance software" is not, since every figure downstream inherits the vagueness of the boundary.

### TAM
TAM = Total market if you captured 100% of the opportunity

**Top-Down Approach:**
1. Search for industry reports: "[industry] market size"
2. Find credible sources (Statista, IBISWorld, Gartner, etc.)
3. Note the methodology and date
4. Extract market size and CAGR

**Bottom-Up Approach:**
1. Estimate number of potential customers
2. Multiply by average revenue per customer
3. Cross-reference with top-down sources

Both approaches appear when sources allow, because agreement between them is the strongest evidence a TAM figure can have and disagreement is the first thing a skeptical reader will ask about.

### SAM
SAM = Portion of TAM you can actually serve

The ICP supplies the constraints that narrow TAM:
- Geographic constraints (% in target regions)
- Segment constraints (% matching ICP)
- Technology constraints (% addressable by your approach)
- Price point constraints (% who can afford you)

**Formula:**
SAM = TAM × Geographic % × Segment % × Technology % × Price %

Each percentage is stated with the assumption or source behind it, so the arithmetic can be checked and any one factor revised.

### SOM
SOM = Realistic market capture in target timeframe

The capture assumption reflects competitive intensity (more competitors = lower SOM), go-to-market capability, brand awareness trajectory, and sales cycle length.

**Typical SOM ranges:**
- Year 1: 0.1% - 1% of SAM for startups
- Year 3: 1% - 5% of SAM with traction
- Year 5: 5% - 15% of SAM as established player

### Growth Rates
For each level (TAM, SAM, SOM): the CAGR with its source and period, the drivers behind the growth, and any constraints or headwinds that could slow it.

### Confidence
A rating of the whole estimate on this scale:
- **High**: Multiple credible sources, recent data, validated assumptions
- **Medium**: 2-3 sources, some assumptions, reasonable methodology
- **Low**: Limited sources, old data, significant assumptions

The rating names which figure is weakest and why, since that is what a reader will want to shore up first.

## How to Work

Boundaries are fixed before any number is researched; a figure found for the wrong market is worse than no figure. The sizing itself is a genuine narrowing chain:
1. TAM from industry sources
2. SAM by applying the ICP constraints to TAM
3. SOM by applying capture assumptions to SAM

That chain fixes how the figures derive from each other, not how any one of them is researched, because each figure can be triangulated from several sources at once. Growth rates and the confidence judgment sit outside that chain and can be gathered alongside it. The Sizing Methods section below shows both calculation paths worked through.

## Constraints

Every figure names its source or is labelled an estimate with the assumption that produced it. SAM is derived from TAM under the ICP constraints, and SOM from SAM under stated capture assumptions, so that SAM ≤ TAM and SOM ≤ SAM hold by construction. CAGR is stated with its period and its source. At least two credible independent sources are cited, and when they conflict both figures are reported with the conservative one carried forward. The finished `market_size.md` conforms to `contracts/market_size.md`.

## What a strong market_size.md looks like

Any step in the chain accepts a reader's own percentage and hands back their own number. A strong estimate does that by showing the multiplication line by line, from the industry figure through each ICP constraint to the SAM, with the bottom-up count beside it even when the two disagree, because the disagreement is where the uncertainty actually lives. "$4.2B TAM" behind one link and no method fails, which means nobody downstream can tell whether the link said $4.2B or whether $4.2B is what was left after an unstated haircut.

When the top-down and bottom-up figures differ by more than 2x, the gap is the finding: report both, state which one the SAM uses, and name what would have to be true for the other to be right.

## Output Format

Create `market_size.md` following the artifact contract in `contracts/market_size.md`.

Required sections:
- Executive summary
- TAM with methodology and source
- SAM with constraints applied
- SOM with assumptions
- Market dynamics (drivers, constraints, trends)
- Confidence assessment
- Sources (minimum 2 citations)

## Working the Numbers

The top-down industry-report search and the bottom-up customer-count build are independent derivations, so run them as parallel sub-agents and triangulate the two results instead of letting the first figure found anchor the second. Enough evidence for a TAM is two sources that agree without sharing a syndicated origin; a third report restating the same figure is diminishing returns. A TAM is sourced when a named report states it and estimated when built from a customer count times an average contract value, and any multiplier in the SAM formula that could not be corroborated is marked as an assumption in the methodology line so a reader can see which factor is load-bearing.

Between a sourced figure and an estimated one sits the derived share: a source publishes its numbers in buckets, homes by decade built or firms by employee band, and the share the sizing needs is a sum of some of them. That sum is done in the artifact itself, with each bucket's boundary quoted as the source labels it and the addition written out beside the result, because the failure mode is quiet: a bucket recalled as 1980-1999 when the source says 2000-2009 yields a share that looks plausible, carries through TAM and SAM without objection, and is wrong by ten points in every artifact downstream. Quoting the boundaries before summing is what catches it, since a boundary written next to the year the share is supposed to cut at either fits or visibly does not, and a share recomputed from the quoted buckets rather than carried over from a first reading of the report is one a reader can check from the file alone.

The second-order question deserves its own sentence, what would change the verdict, because a SAM that collapses if the geographic constraint is wrong matters more than another decimal place. `market_size.md` is consumed by gtm-channels for scale planning and by scorecard-generator's Market Size dimension, whose bands turn the SAM figure directly into a 1-10 score without re-deriving anything. Lead with the SAM and its confidence level in the executive summary, since that pair is what a founder acts on.

The deliverable is `market_size.md` with its methodology and citations; revisiting pricing or the ICP to make the SOM look better is outside this skill. Before you finalize the file, sanity-check the arithmetic chain end to end by multiplying the stated constraints against the TAM and confirming the product equals the SAM written down, and re-add any bucket-derived share from the boundaries quoted in the file rather than from memory of the source.

## Research Query Templates

### Finding TAM Data
```text
"[industry] market size 2024"
"[industry] market report"
"[industry] TAM analysis"
"site:statista.com [industry]"
"[industry] market forecast CAGR"
```

### Finding Segment Data
```text
"[segment] number of companies"
"[segment] industry statistics"
"how many [customer type] in [region]"
```

### Validating Estimates
```text
"[competitor] revenue"
"[competitor] customers"
"[industry] average deal size"
```

## Sizing Methods

### Top-Down Method
Start with total market, narrow down:

```
Industry Market Size: $50B (from report)
    × Geographic constraint (US only): 40% → $20B
    × Segment constraint (SMB only): 30% → $6B
    × Technology constraint (cloud-native): 50% → $3B
= SAM: $3B
```

### Bottom-Up Method
Start with unit economics, scale up:

```
Number of target companies: 100,000
    × Addressable by solution: 50% → 50,000
    × Would consider buying: 20% → 10,000
    × Average deal size: $10,000/year
= SAM: $100M
```

### Triangulation
Use both methods and reconcile:
- If they're close (within 2x), take the average
- If they differ significantly, investigate why
- Note the range and confidence

## Edge Cases

**No market reports exist:**
- Use bottom-up calculation
- Reference adjacent markets
- Note lower confidence
- Recommend primary research

**Market in flux:**
- Note rapid change
- Provide range estimates
- Track leading indicators
- Update frequently

**Conflicting sources:**
- Report both figures
- Favor more recent/credible sources
- Note the discrepancy
- Use conservative estimate

**Very small market:**
- This is a valid finding
- Consider if market is growing
- Note if product could expand TAM
- Be realistic about opportunity

## References

- [sizing_methods.md](references/sizing_methods.md): Detailed sizing methodologies and examples
