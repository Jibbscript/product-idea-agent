---
name: idea-validation-orchestrator
description: Orchestrates full product idea validation workflow from initial concept to final report. Use when running complete validation, coordinating multiple validation steps, or when unsure which specific validation skill to use.
license: Apache-2.0
metadata:
  author: product-idea-agent
  pack: product-idea-agent
allowed-tools: Read Write WebSearch WebFetch Grep Edit
---

# Idea Validation Orchestrator

Orchestrates the complete product idea validation workflow.

## Quick Start

To run a complete validation:
1. Tell me about your product idea
2. I'll guide you through all 11 validation steps
3. We'll generate a comprehensive validation report

Or specify a starting point:
- "Start from demand signals" (if you already have an idea brief)
- "Just run competitive analysis" (for a single step)

## Complete Workflow

The full validation pipeline consists of 11 steps:

```
Step 1: idea-brief-creator      → idea_brief.md
    ↓
Step 2: demand-signals          → signals.md
    ↓
Step 3: problem-segment         → icp.yaml
    ↓
Step 4: competitive-landscape   → competitors.csv
    ↓
Step 5: market-sizing           → market_size.md
    ↓
Step 6: pricing-wtp             → pricing.yaml
    ↓
Step 7: solution-wedge          → mvp_spec.md
    ↓
Step 8: gtm-channels            → gtm_plan.md
    ↓
Step 9: risk-assessment         → risks.md
    ↓
Step 10: scorecard-generator    → scorecard.json
    ↓
Step 11: validation-report      → validation_report.md
```

## Progress Tracker

Copy this checklist to track your validation progress:

```
Product Validation Progress: [Idea Name]
Started: [Date]

Phase 1: Discovery
- [ ] Step 1: Create idea brief (idea-brief-creator)
      Output: idea_brief.md

- [ ] Step 2: Research demand signals (demand-signals)
      Output: signals.md

Phase 2: Customer & Market
- [ ] Step 3: Define ICP (problem-segment)
      Output: icp.yaml

- [ ] Step 4: Map competitors (competitive-landscape)
      Output: competitors.csv

- [ ] Step 5: Size market (market-sizing)
      Output: market_size.md

Phase 3: Strategy
- [ ] Step 6: Research pricing (pricing-wtp)
      Output: pricing.yaml

- [ ] Step 7: Define MVP (solution-wedge)
      Output: mvp_spec.md

- [ ] Step 8: Plan GTM (gtm-channels)
      Output: gtm_plan.md

Phase 4: Assessment
- [ ] Step 9: Assess risks (risk-assessment)
      Output: risks.md

- [ ] Step 10: Generate scorecard (scorecard-generator)
      Output: scorecard.json

Phase 5: Synthesis
- [ ] Step 11: Compile report (validation-report)
      Output: validation_report.md

Validation Complete: [ ]
Final Recommendation: [GO / PIVOT / NO-GO]
```

## How to Use This Skill

### Full Validation Run

Say: "Help me validate my startup idea for [description]"

I will:
1. Start with the idea brief
2. Guide you through each step
3. Ask clarifying questions as needed
4. Generate all artifacts
5. Produce the final validation report

### Partial Validation

If you've already completed some steps:

Say: "I already have an idea brief and demand signals. Continue from step 3."

I will:
1. Review your existing artifacts
2. Continue from the specified step
3. Complete the remaining workflow

### Single Step

If you only need one specific analysis:

Say: "Just run competitive analysis for [idea]"

I will:
1. Run only that specific skill
2. Generate the relevant artifact

## Working the Pipeline

The user is not watching each step, so reversible actions that follow from the original request - reading an artifact, running the next skill in the chain, redrafting a section - proceed without asking, and the user is consulted only when a decision genuinely changes the scope of the validation, such as which of two segments to treat as primary. Steps that do not depend on each other can run concurrently, so once `icp.yaml` exists, competitive-landscape and market-sizing are independent and belong in parallel sub-agents rather than a serialized pipeline. How deep each step goes scales with what is at stake: a quick feasibility check runs steps one through four shallowly, while an investment-readiness pass goes deeper on market-sizing and pricing-wtp. Not every idea needs all eleven steps, so the judgment call is where to stop; a NO-GO already obvious from `competitors.csv` is worth surfacing rather than spending two more hours confirming it.

Each step's artifact is what the next step reads, with `signals.md` read by problem-segment and `icp.yaml` read by competitive-landscape, market-sizing and gtm-channels, so a thin artifact early is a thin artifact everywhere after it. Progress is audited against what was actually written: a step counts as complete when its artifact exists on disk, and when a skill produced nothing, say so plainly rather than reporting the step as done.

Your final message is the founder's first look at hours of work, so the first sentence carries the verdict and the composite score, and what follows re-grounds a reader who saw none of the intermediate artifacts, spelling terms out rather than reusing shorthand built up while working. Before declaring the validation complete, re-read the artifact directory and confirm all eleven files exist and that the verdict in `scorecard.json` matches what `validation_report.md` states.

## Artifact Locations

All artifacts are saved in the current project directory:

```
./
├── idea_brief.md
├── signals.md
├── icp.yaml
├── competitors.csv
├── market_size.md
├── pricing.yaml
├── mvp_spec.md
├── gtm_plan.md
├── risks.md
├── scorecard.json
└── validation_report.md
```

## Validation Timeline

Typical time for complete validation:

| Phase | Steps | Estimated Time |
|-------|-------|----------------|
| Discovery | 1-2 | 15-30 min |
| Customer & Market | 3-5 | 30-45 min |
| Strategy | 6-8 | 30-45 min |
| Assessment | 9-10 | 15-30 min |
| Synthesis | 11 | 15-20 min |
| **Total** | 1-11 | **2-3 hours** |

*Times assume active participation and available web access.*

## What to Prepare

For best results, have ready:
- Initial idea description (even rough is fine)
- Any existing research or notes
- Target market hypotheses
- Known competitors (if any)
- Budget/resource constraints (if known)

## Common Workflows

### New Idea Exploration
Full 11-step validation for a fresh concept.

### Pivot Assessment
Start from existing brief, re-run market/competitive analysis.

### Investment Readiness
Complete validation with emphasis on market sizing and financials.

### Quick Feasibility Check
Run steps 1-4 only for initial signal validation.

### Competitive Deep Dive
Focus on steps 3-4 (ICP + competitors) for positioning strategy.

## Handling Pauses

If you need to pause the validation:
1. Note which step you're on
2. Artifacts are saved automatically
3. Resume by saying "Continue validation from step X"

## Tips for Best Results

1. **Be specific about your idea** - The more detail, the better the analysis

2. **Share existing research** - If you have customer interviews, competitor notes, etc.

3. **Ask questions** - If any step is unclear or you want to go deeper

4. **Iterate** - It's okay to revisit earlier steps based on later findings

5. **Trust the process** - Each step builds on the previous ones

## Output Summary

At the end of complete validation, you'll have:
- **11 artifacts** documenting your research
- **Validation scorecard** with 7-dimension scoring
- **GO/PIVOT/NO-GO recommendation**
- **Actionable next steps**

Given an idea description, the pipeline runs to completion and returns the report; the validation begins as soon as there is an idea to work from.

## References

- [workflow_guide.md](references/workflow_guide.md): Detailed workflow guidance
