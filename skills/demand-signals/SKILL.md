---
name: demand-signals
description: Researches demand signals including search trends, community discussions, and market interest indicators for product ideas. Use when validating whether real demand exists, researching market interest, or gathering community sentiment for a startup concept.
license: Apache-2.0
metadata:
  author: product-idea-agent
  pack: product-idea-agent
allowed-tools: Read Write WebSearch WebFetch Grep
---

# Demand Signals Research

Analyzes search trends, community discussions, and market interest indicators to validate demand for a product idea.

## Outcome

`signals.md` is the evidence file that says whether real people are already searching for, complaining about, or paying to solve the problem in the idea brief. A finished one pairs a search-trend table with community evidence from the platforms where the target audience actually talks, quotes those people directly, and ends in a 1-10 signal score that the evidence above it visibly supports.

## Inputs Required

- `idea_brief.md` in the project artifacts directory
- OR direct description of the product idea

## Who reads signals.md

scorecard-generator reads the 1-10 signal score straight into its Demand Signals dimension, which carries 15% of the composite; market-sizing reads the trend direction as a check on whether the TAM it finds elsewhere is growing or shrinking; and validation-report quotes the user quotes verbatim in its Customer Evidence section. None of the three re-runs a search.

That matters because a score with no URL behind it moves a GO/NO-GO verdict by exactly as much as a sourced one. An unsourced 8 is worse than an honest 4, since the 4 tells founders where the demand is thin and the 8 tells them nothing they can act on.

## What signals.md Must Cover

### Keywords
The vocabulary the research runs on, drawn from the idea brief: core problem keywords (3-5), solution keywords (2-3), and audience keywords (2-3). Problem keywords matter most because people search for their pain long before they search for a product category.

### Search Trend Evidence
For each keyword, the monthly volume, trend direction, and year-over-year change, gathered from "[keyword] Google Trends" or "[keyword] search volume" style queries. Keywords growing more than 50% year over year are strong signals and are called out as such; flat or declining interest is reported just as plainly, since a falling trend is a finding rather than a gap.

### Community Signals
What Reddit and forums show when queried with "[problem] site:reddit.com" and "[solution] frustration OR problem OR help": subreddit names, post counts, and the sentiment of the discussion. Active communities with recurring complaints are the strongest form of demand evidence short of purchase data.

### Platform-Specific Evidence
Whatever the platforms relevant to the ICP add beyond Reddit: tutorial and review content on YouTube, relevant Facebook Groups, complaints and wishes on Twitter/X, and related products on Product Hunt. Which platforms matter depends on where the audience lives, so a B2B developer tool and a consumer wellness app will draw on different mixes.

### Representative Quotes
Three to five direct quotes that demonstrate pain point severity, willingness to pay, current workarounds, or frustration with alternatives. Quotes are the evidence a later reader trusts most, which is why each carries its source URL and date.

### Signal Score
A single 1-10 score with the scale applied as written:
- 9-10: High volume, active communities, strong growth
- 7-8: Good signals, engaged communities
- 5-6: Moderate interest, niche communities
- 3-4: Limited signals, small audiences
- 1-2: No measurable demand

The score is a judgment on the evidence already gathered; the justification beside it points at the specific trend rows, communities, and quotes that produced it.

## How to Work

Keyword extraction feeds every search, so it comes first. The trends, community, and platform searches are independent of each other and their order does not matter. Quote collection happens naturally while reading community threads rather than as a separate pass. The score is the last thing written because it is a reading of everything above it, not a seventh search.

## Constraints

Every quote carries a source URL and a date. Every trend figure names the tool or query it came from. The signal score uses the stated 1-10 scale and is justified by the evidence above it rather than by general impressions of the market. Where a platform or query returns nothing, the file records that as insufficient data with low confidence instead of omitting the row, because an empty result is itself a signal about where demand is not. The finished `signals.md` conforms to `contracts/signals.md`.

## What a strong signals.md looks like

The bar for this file is that a reader can paste one of these searches and land on the same thread it quoted. What passes it is the provenance sitting next to each figure: the link and the date it was pulled beside every volume number, the subreddit and its post count in place of "active communities", and real users quoted in their own words with a link to the comment. "Strong interest" with no number, no source and no recency fails it, which means the score has to be taken on the researcher's word.

Recency is part of the bar: a 2019 thread with 400 upvotes says less about demand today than a 2024 thread with 40, so the date sits next to every count.

## Output Format

Create `signals.md` following the artifact contract in `contracts/signals.md`.

Required sections:
- Summary with overall signal strength
- Search trends table
- Community signals with platform breakdown
- Key quotes (direct evidence)
- Signal score (1-10)
- Sources with URLs

## Working the Signal Search

Keyword-volume lookups, Reddit threads, YouTube comments, Facebook Groups and Product Hunt launches are independent searches, so fan them out to sub-agents running in parallel and reconcile what they return into one trends table rather than walking the platforms one after another. Three subreddits repeating the same complaint is enough evidence for the community section and a fourth is diminishing returns, so the remaining search budget goes to the keywords whose trend direction is still ambiguous. Every volume figure in `signals.md` carries its provenance: sourced when a page states it, estimated when derived from a proxy keyword, unverified when only a forum post claims it, and a keyword whose volume could not be confirmed says so in its row instead of being rounded into a confident number.

The interesting finding is usually the non-obvious one, such as the adjacent community that turns out to hold the real buyer or the long-tail term growing while the category term stays flat, so a search that only confirms the founder's framing has not finished. `signals.md` is read by problem-segment when it ranks segments and by scorecard-generator, which lifts the 1-10 signal score straight into its Demand Signals dimension, so an unlabeled guess here propagates into the composite. Lead with the demand verdict in the summary, whether real and growing demand showed up, ahead of the keyword tables that support it.

The deliverable is `signals.md` and its sources; competitor feature teardowns and market sizing belong to later skills, so report the signals and stop there. Before you finish, re-read each key quote against its URL and confirm it says what the summary claims it says.

## Search Query Templates

### Google Trends
```text
"[keyword] trends"
"[keyword] search volume stats"
"[keyword] interest over time"
```

### Reddit Pain Points
```text
"[problem] site:reddit.com"
"help with [problem] site:reddit.com"
"[alternative] sucks site:reddit.com"
"looking for [solution type] site:reddit.com"
```

### Competitor Research
```text
"[competitor name] alternative"
"[competitor name] vs"
"[competitor name] review complaints"
```

### Willingness to Pay
```text
"would pay for [solution] site:reddit.com"
"[problem] worth paying site:reddit.com"
"looking to buy [solution]"
```

## Edge Cases

**No search data found:**
- Try broader keyword variations
- Check adjacent problem spaces
- Note as "insufficient data" with confidence: low

**Conflicting signals:**
- Report both positive and negative
- Weight recency (newer > older)
- Note the conflict in summary

**Rate limited:**
- Wait and retry with exponential backoff
- Fall back to cached/historical data if available
- Document limitations in output

**Non-English markets:**
- Note language/region limitations
- Search in target market language if possible
- Adjust confidence level accordingly

## References

- [signal_sources.md](references/signal_sources.md): Comprehensive list of demand signal sources
- [scoring_rubric.md](references/scoring_rubric.md): Detailed scoring methodology
