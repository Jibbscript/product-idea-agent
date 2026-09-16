<!-- Parent: ../AGENTS.md -->
<!-- Generated: 2026-09-15 | Updated: 2026-09-15 -->

# demand-signals

## Purpose
Pipeline step 2. Extracts 5–10 keywords from the idea brief, researches search-trend volume and direction plus community discussion (Reddit, forums, Product Hunt), and writes `signals.md` with a 1–10 signal score and confidence level.

## Key Files

| File | Description |
|------|-------------|
| `SKILL.md` | 147 lines. Extract keywords → search trends → community signals → key quotes → score. Tools: `Read Write WebSearch WebFetch Grep` |
| `references/signal_sources.md` | Catalogue of where to look: Google Trends, Reddit, Product Hunt, Hacker News, app stores, with URLs and what each is good for |
| `references/scoring_rubric.md` | How the 1–10 signal score is computed as a weighted average of component scores (search, community, growth) |

## Inputs / Outputs
- **Reads**: `idea_brief.md`, or a direct idea description
- **Writes**: `signals.md` per `contracts/signals.md`
- **Downstream**: `market-sizing`, `scorecard-generator` (feeds the `demand_signals` dimension), `validation-report`

## For AI Agents

### Working In This Directory
- Keywords with >50% YoY growth are flagged as strong signals; that threshold is in `SKILL.md` and `scoring_rubric.md`, change both.
- Edge cases handled: no search data (broaden, mark low confidence), conflicting signals (report both, weight recency), rate limits (backoff, document), non-English markets (note limits).
- The optional Google / Reddit API keys in `.env.example` are for this skill. Nothing in the workflow requires them; keep the no-key path working.

### Testing Requirements
- Run on `t1-energy-audit` and compare against `expected_outputs/signals.md`. Check every claim in Search Trends and Community Signals has a URL in Sources.

### Common Patterns
- Direct quotes from community posts are kept short and attributed with a link; `rubric.yaml` scores quote accuracy.
- Output summary states Overall Signal Strength (Strong / Moderate / Weak) and Confidence (High / Medium / Low) before the detail.

## Dependencies

### Internal
- `contracts/signals.md`, `contracts/idea_brief.md`

### External
- Claude Code `WebSearch` / `WebFetch`

<!-- MANUAL: Any manually added notes below this line are preserved on regeneration -->
