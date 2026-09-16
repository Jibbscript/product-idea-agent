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

## Quick Start

Given an idea brief, search for demand evidence:
1. Extract 5-10 keywords from the idea
2. Search Google Trends for interest patterns
3. Search Reddit for pain point discussions
4. Compile findings into `signals.md`

## Inputs Required

- `idea_brief.md` in the project artifacts directory
- OR direct description of the product idea

## Step-by-Step Workflow

### Step 1: Extract Keywords
Read the idea brief and identify:
- Core problem keywords (3-5)
- Solution keywords (2-3)
- Audience keywords (2-3)

### Step 2: Search Trends Research
For each keyword:
- Search "[keyword] Google Trends" or "[keyword] search volume"
- Note monthly volume, trend direction, YoY change
- Flag keywords with >50% YoY growth as strong signals

### Step 3: Community Signal Mining
Search Reddit and forums:
- Query: "[problem] site:reddit.com"
- Query: "[solution] frustration OR problem OR help"
- Note: subreddit names, post counts, sentiment

### Step 4: Platform-Specific Research
Check additional platforms relevant to the ICP:
- YouTube: Search for tutorial/review content
- Facebook Groups: Search for relevant communities
- Twitter/X: Search for complaints and wishes
- Product Hunt: Search for related products

### Step 5: Extract Key Quotes
Find 3-5 direct quotes that demonstrate:
- Pain point severity
- Willingness to pay
- Current workarounds
- Frustration with alternatives

### Step 6: Calculate Signal Score
Based on findings, score 1-10:
- 9-10: High volume, active communities, strong growth
- 7-8: Good signals, engaged communities
- 5-6: Moderate interest, niche communities
- 3-4: Limited signals, small audiences
- 1-2: No measurable demand

### Step 7: Compile Findings
Create `signals.md` using the artifact contract format.

## Workflow Checklist

Copy and track progress:
```
Demand Signals Progress:
- [ ] Keywords extracted from idea brief
- [ ] Google Trends data gathered
- [ ] Reddit discussions found
- [ ] Other platforms checked
- [ ] Key quotes extracted
- [ ] Signal strength scored
- [ ] signals.md created
```

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
- "[keyword] trends"
- "[keyword] search volume stats"
- "[keyword] interest over time"

### Reddit Pain Points
- "[problem] site:reddit.com"
- "help with [problem] site:reddit.com"
- "[alternative] sucks site:reddit.com"
- "looking for [solution type] site:reddit.com"

### Competitor Research
- "[competitor name] alternative"
- "[competitor name] vs"
- "[competitor name] review complaints"

### Willingness to Pay
- "would pay for [solution] site:reddit.com"
- "[problem] worth paying site:reddit.com"
- "looking to buy [solution]"

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
