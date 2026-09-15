# Artifact Contract: signals.md

## Purpose
Documents demand signals including search trends, community discussions, and market interest indicators.

## Producer
- `demand-signals` skill

## Consumers
- `market-sizing`
- `scorecard-generator`
- `validation-report`

## Schema

```markdown
# Demand Signals Report

## Summary
- **Overall Signal Strength**: [Strong | Moderate | Weak]
- **Confidence Level**: [High | Medium | Low]

## Search Trends
| Keyword | Monthly Volume | Trend | YoY Change |
|---------|---------------|-------|------------|
| [keyword] | [volume] | [↑/↓/→] | [%] |

## Community Signals

### Reddit
| Subreddit | Members | Relevant Posts | Sentiment |
|-----------|---------|----------------|-----------|
| r/[sub] | [n] | [n] | [Positive/Negative/Mixed] |

### Other Platforms
[Facebook Groups, YouTube, Forums, etc.]

## Key Quotes
> "[Direct quote from community]" - Source

## Signal Score: [1-10]

## Sources
- [URL with retrieval date]
```

## Field Definitions

| Field | Required | Description |
|-------|----------|-------------|
| Overall Signal Strength | Yes | Strong, Moderate, or Weak |
| Confidence Level | Yes | High, Medium, or Low |
| Search Trends table | Yes | At least 3 keywords analyzed |
| Reddit section | Yes | At least 1 subreddit researched |
| Key Quotes | Yes | At least 2 direct quotes |
| Signal Score | Yes | Integer 1-10 |
| Sources | Yes | At least 3 URLs with dates |

## Scoring Rubric

| Score | Signal Strength | Criteria |
|-------|-----------------|----------|
| 9-10 | Very Strong | High search volume (>10K/mo), active communities (>100K members), strong YoY growth (>50%) |
| 7-8 | Strong | Moderate volume (1K-10K), engaged communities (10K-100K), positive growth (20-50%) |
| 5-6 | Moderate | Some volume (100-1K), niche communities, stable or slight growth |
| 3-4 | Weak | Low volume (<100), few discussions, declining or flat trends |
| 1-2 | Very Weak | Minimal signals, no community presence, negative trends |
