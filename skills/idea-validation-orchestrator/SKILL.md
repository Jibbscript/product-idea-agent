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

## Who reads the eleven artifacts

The founder who asked for the validation reads validation_report.md and possibly nothing else. The other ten files are what a co-founder or an investor opens three months later, when the decision is revisited and the conversation that produced them is gone, which is why each artifact has to stand alone rather than referring back to anything said in the session: a phrase like "as we discussed" means nothing to the reader who opens icp.yaml cold.

## Progress and Resumption

A run's position is read from which artifacts already exist in the project directory, not from a copied checklist: if `icp.yaml` is on disk and conforms to its contract, steps 1-3 are done and step 4 is next. The pipeline groups into five phases, and the phase a run is in is the phase of the first missing artifact.

| Phase | Skills | Artifacts produced |
|-------|--------|--------------------|
| Discovery | idea-brief-creator, demand-signals | idea_brief.md, signals.md |
| Customer & Market | problem-segment, competitive-landscape, market-sizing | icp.yaml, competitors.csv, market_size.md |
| Strategy | pricing-wtp, solution-wedge, gtm-channels | pricing.yaml, mvp_spec.md, gtm_plan.md |
| Assessment | risk-assessment, scorecard-generator | risks.md, scorecard.json |
| Synthesis | validation-report | validation_report.md |

Reporting progress means naming the phase, the last artifact written, and the next skill to run; the final recommendation (GO / PIVOT / NO-GO) is reported once `scorecard.json` exists.

## How to Use This Skill

A run enters the pipeline in one of three ways, and the project directory decides which. When the request is an idea and nothing is on disk, the run is a full validation: idea-brief-creator writes `idea_brief.md` and each later skill takes the previous artifact as its input until `validation_report.md` exists. Clarifying questions belong before that first step, and only when the idea is too thin to brief - a single line with no hint of who it is for or what it replaces - because that is the last point at which a wrong guess costs nothing to correct; once there is enough to write the brief, the run proceeds.

When artifacts already exist, the run resumes where Progress and Resumption places it, whether the user says "Continue validation from step X" or simply asks for the validation again, and the existing files are read rather than regenerated so that finished work is not paid for twice. A pause is the same case seen from the other side: each artifact is written to disk as its step completes, so a run stopped at any point resumes from the directory in a later session with nothing to note down. When a later finding undercuts an earlier artifact, such as a competitor found in step 4 that changes the segment chosen in step 3, the earlier file is rewritten and the steps that read it are re-run, since the pipeline only holds together while every artifact is current.

When the request names one analysis - "just run competitive analysis for this idea" - only that skill runs and only its artifact is written, with the inputs it depends on read from disk when they exist and drawn from the request when they do not.

## Working the Pipeline

The user is not watching each step, so reversible actions that follow from the original request - reading an artifact, running the next skill in the chain, redrafting a section - proceed without asking, and the user is consulted only when a decision genuinely changes the scope of the validation, such as which of two segments to treat as primary. Steps that do not depend on each other can run concurrently, so once `icp.yaml` exists, competitive-landscape and market-sizing are independent and belong in parallel sub-agents rather than a serialized pipeline. How deep each step goes scales with what is at stake: a quick feasibility check runs steps one through four shallowly, while an investment-readiness pass goes deeper on market-sizing and pricing-wtp. Not every idea needs all eleven steps, so the judgment call is where to stop; a NO-GO already obvious from `competitors.csv` is worth surfacing rather than spending two more hours confirming it.

Each step's artifact is what the next step reads, with `signals.md` read by problem-segment and `icp.yaml` read by competitive-landscape, market-sizing and gtm-channels, so a thin artifact early is a thin artifact everywhere after it. Progress is audited against what was actually written, so when a skill produced nothing, say so plainly rather than reporting the step as done.

Your final message is the founder's first look at hours of work, so the first sentence carries the verdict and the composite score, and what follows re-grounds a reader who saw none of the intermediate artifacts, spelling terms out rather than reusing shorthand built up while working. Before declaring the validation complete, re-read the artifact directory and confirm that either all eleven files exist or the final message states plainly which steps were skipped and why, and, when both exist, that the verdict in `scorecard.json` matches what `validation_report.md` states.

## What a strong validation run looks like

The test is whether a reader could reconstruct the verdict from the eleven artifacts without the transcript. Files that each make sense opened cold, with the weak dimensions stated as plainly as the strong ones, pass it, so that founders coming back to it can see why it said PIVOT and what has changed since. A good conversation and thin files fail it: a brief that quotes the chat, a signals file with no URLs, a scorecard whose evidence strings say "see discussion".

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

## Output Summary

At the end of complete validation, you'll have:
- **11 artifacts** documenting your research
- **Validation scorecard** with 7-dimension scoring
- **GO/PIVOT/NO-GO recommendation**
- **Actionable next steps**

Given an idea description, the pipeline runs to completion and returns the report; the validation begins as soon as there is an idea to work from.

## References

- [workflow_guide.md](references/workflow_guide.md): Detailed workflow guidance
