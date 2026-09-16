---
name: scorecard-generator
description: Calculates validation scores across multiple dimensions to produce an opportunity scorecard. Use when summarizing validation findings into actionable metrics, making go/no-go decisions, or comparing ideas.
license: Apache-2.0
metadata:
  author: product-idea-agent
  pack: product-idea-agent
allowed-tools: Read Write
---

# Scorecard Generator

Calculates multi-dimensional validation scores and generates opportunity scorecards.

## Outcome

`scorecard.json` carries seven dimension scores, each with the evidence that produced it, combined by fixed weights into a 0-100 composite, a revenue-potential band, and a GO / PIVOT / NO-GO recommendation with rationale and next steps.

## Inputs Required

- All prior artifacts:
  - `idea_brief.md`
  - `signals.md`
  - `icp.yaml`
  - `competitors.csv`
  - `market_size.md`
  - `pricing.yaml`
  - `mvp_spec.md`
  - `gtm_plan.md`
  - `risks.md`

## Who reads scorecard.json

validation-report lifts the verdict into the first line of the report and the dimension table into its section 7, and idea-validation-orchestrator reports the composite as the outcome of the whole run. For most readers the composite number is the validation, since the founder reads the verdict and the investor reads the table, and few of either open the nine artifacts behind them.

The evidence string on each dimension therefore matters more than the digit next to it, because an evidence string that does not name the artifact and the figure it came from leaves the verdict unfalsifiable, and a verdict nobody can argue with is a verdict nobody trusts.

## What scorecard.json Must Cover

### Evidence
The metric each artifact contributes, pulled before any scoring starts:

| Artifact | Key Metrics to Extract |
|----------|------------------------|
| signals.md | Signal strength score, search volumes |
| icp.yaml | Problem severity score |
| competitors.csv | Number of competitors, threat levels |
| market_size.md | TAM, SAM, CAGR |
| pricing.yaml | Unit economics, LTV:CAC |
| mvp_spec.md | Technical complexity |
| gtm_plan.md | Channel viability |
| risks.md | Critical risk count |

### Dimension Scores
Each dimension rated 1-10 on its own anchors, with the evidence recorded beside the number:

#### Problem Severity (Weight: 20%)
From `icp.yaml` problem_severity score:
- 9-10: Hair-on-fire problem, active spending to solve
- 7-8: Significant pain, some existing solutions
- 5-6: Moderate frustration, workarounds exist
- 3-4: Minor inconvenience
- 1-2: Nice-to-have, not a real problem

#### Demand Signals (Weight: 15%)
From `signals.md` signal score:
- 9-10: High search volume, active communities, strong growth
- 7-8: Good signals, engaged communities
- 5-6: Moderate interest, niche communities
- 3-4: Limited signals, small audiences
- 1-2: No measurable demand

#### Competitive Intensity (Weight: 10%)
From `competitors.csv`:
- 1-2: Blue ocean, no direct competitors (good)
- 3-4: Few competitors, clear differentiation possible
- 5-6: Moderate competition, gaps exist
- 7-8: Crowded market, hard to differentiate
- 9-10: Red ocean, dominated by incumbents (bad)

**Note**: For this dimension, LOWER is BETTER.

#### Market Size (Weight: 15%)
From `market_size.md`:
- 9-10: TAM > $10B, SAM > $1B
- 7-8: TAM $1-10B, SAM $100M-1B
- 5-6: TAM $100M-1B, SAM $10-100M
- 3-4: TAM $10-100M, niche market
- 1-2: TAM < $10M, very small market

#### Execution Difficulty (Weight: 15%)
From `mvp_spec.md` and `risks.md`:
- 1-2: Simple app, proven tech, solo buildable (good)
- 3-4: Standard complexity, small team needed
- 5-6: Moderate complexity, some novel components
- 7-8: Complex system, specialized skills required
- 9-10: Frontier technology, major R&D required (bad)

**Note**: For this dimension, LOWER is BETTER.

#### GTM Viability (Weight: 15%)
From `gtm_plan.md` and `pricing.yaml`:
- 9-10: Clear channels, low CAC, viral potential
- 7-8: Good channels available, reasonable CAC
- 5-6: Some channels, moderate CAC
- 3-4: Limited channels, high CAC
- 1-2: No clear path to customers

#### Timing (Weight: 10%)
From `signals.md`, `market_size.md`, and context:
- 9-10: Perfect timing - enabling tech just matured
- 7-8: Good timing - market ready, trends supportive
- 5-6: Neutral - no major headwinds or tailwinds
- 3-4: Challenging - market not ready or shifting away
- 1-2: Bad timing - too early or too late

### Composite Score
The weighted combination, computed with the arithmetic shown in the file:

```
Composite = (
  Problem Severity × 0.20 +
  Demand Signals × 0.15 +
  (11 - Competitive Intensity) × 0.10 +  # Invert
  Market Size × 0.15 +
  (11 - Execution Difficulty) × 0.15 +   # Invert
  GTM Viability × 0.15 +
  Timing × 0.10
) × 10
```

Result is 0-100.

### Revenue Potential
A band derived from market size and unit economics:
- `$$$` ($10M+ ARR potential): Large SAM, strong economics
- `$$` ($1M-$10M ARR potential): Medium SAM, viable economics
- `$` ($100K-$1M ARR potential): Small SAM or challenging economics

### Recommendation
The verdict the composite and the dimension floor together imply:

**GO** (Score ≥ 65 AND no dimension below 4):
- Proceed with development
- Strong overall opportunity
- Manageable risks

**PIVOT** (Score 50-64 OR 1-2 dimensions below 4):
- Opportunity exists but needs adjustment
- Address weak areas before proceeding
- Consider narrowing scope or segment

**NO-GO** (Score < 50 OR 3+ dimensions below 4):
- Insufficient opportunity
- Critical gaps in multiple areas
- Recommend exploring different ideas

The dimension floor exists because a high composite can hide a single disqualifying dimension; when that happens the rationale says so rather than letting the average speak.

### Next Steps
Two or three immediate actions that follow from the verdict: execution priorities for GO, the specific weaknesses to address for PIVOT, alternative directions to explore for NO-GO.

## How to Work

The seven dimensions are independent readings of artifacts already on disk and can be scored in any order. The only dependency chain is:
1. All seven dimension scores, each with its evidence
2. The composite, from the weights above
3. The recommendation, from the composite and the dimension floor

Revenue potential reads market_size.md and pricing.yaml directly and does not wait on the composite.

## Constraints

Every dimension score cites the artifact and the specific figure or line that supports it. The composite is computed from the stated weights with the arithmetic shown, so a reader can recompute it. A dimension with no evidence in any artifact is recorded as unscored with the reason, rather than given a middling default that would quietly distort the composite. The revenue band and the recommendation each carry a rationale in terms of the evidence. Next steps are concrete enough to act on this week. The finished `scorecard.json` conforms to `contracts/scorecard.json`.

## What a strong scorecard.json looks like

Each dimension score has to stand or fall on its own, so a reader can disagree with one of them without rejecting the whole scorecard. That takes an evidence string per dimension that points back at the artifact and the figure it came from ("Market Size 6: SAM $45M per market_size.md bottom-up estimate, confidence medium"), so that a founder who thinks the SAM is wrong knows which file to reopen and what a corrected score would do to the composite. Seven numbers, a composite and a verdict, with evidence strings that restate the scale ("moderate competition"), fall short, since there is nothing in them to disagree with. The composite is shown with its arithmetic because a 64 has to be checkable as a 64 and not a rounding that crossed the GO threshold.

## Output Format

Create `scorecard.json` following the artifact contract in `contracts/scorecard.json`.

Required fields:
- version, idea_name, evaluated_date
- All 7 dimension scores with evidence
- composite_score and calculation_method
- revenue_potential with indicator and range
- recommendation with verdict, rationale, and next_steps

## Working the Score

Reading the nine artifacts is fast, so what is worth delegating here is the judgment rather than the file access - sub-agents can each argue one dimension's score from its own evidence in parallel while you hold the weighting consistent across all seven. Scoring is arithmetic over evidence already gathered, so effort is proportional to disagreement; dimensions where the artifacts conflict deserve the deliberation and the rest read straight off the bands. A dimension whose primary input artifact is missing but whose evidence survives in another artifact is scored with its confidence marked unverified rather than filled in from a general impression of the idea.

A composite can hide a disqualifying dimension, and the counter-intuitive case of a 68 built on a Demand Signals 3 is worth saying plainly instead of reporting the verdict the formula produced. `scorecard.json` is read by validation-report, which reprints this verdict and rationale almost verbatim as its headline, so the rationale is written for a founder deciding rather than for the model that produced it, and a thin evidence field becomes an unsupported claim in the final document. Lead with the verdict and the composite; the seven dimension scores are the support, not the opening.

The deliverable is `scorecard.json`; going back to re-research a dimension that scored badly is not this skill's move, and neither is adjusting the weights to reach a preferred verdict. Before writing `scorecard.json`, verify the numbers by recomputing the composite from the seven weighted scores and showing the formula with the actual values substituted.

## Scoring Calibration

### Cross-Check Scores

Ensure consistency:
- High problem severity should correlate with strong demand signals
- High competitive intensity may indicate validated market
- Large market should align with multiple viable channels

### Adjust for Context

Consider:
- B2B vs B2C dynamics
- Industry-specific norms
- Founder/team advantages
- Timing of research (market may have changed)

## Edge Cases

**Missing artifacts:**
- Score based on available evidence
- Note lower confidence for affected dimensions
- Recommend gathering missing data

**Conflicting evidence:**
- Document the conflict
- Use more conservative score
- Note in evidence field

**Borderline scores:**
- Err toward lower score unless strong evidence
- Document reasoning
- Flag for validation

**All high scores:**
- Sanity check assumptions
- May indicate bias or insufficient research
- Validate with external perspective

## References

- [scoring_model.md](references/scoring_model.md): Detailed scoring methodology
