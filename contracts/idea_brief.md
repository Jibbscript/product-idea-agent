# Artifact Contract: idea_brief.md

## Purpose
Captures a structured startup/product idea hypothesis for validation.

## Producer
- `idea-brief-creator` skill

## Consumers
- `demand-signals`
- `problem-segment`
- `competitive-landscape`
- All downstream skills (via inheritance)

## Schema

```markdown
# Idea Brief: [Working Title]

## One-Line Pitch
[Single sentence value proposition - what it does and for whom]

## Problem Statement
[2-3 sentences describing the pain point being addressed]

## Target Customer
[Initial customer segment hypothesis - who has this problem]

## Solution Hypothesis
[Proposed solution approach - how you'll solve it]

## Key Assumptions
1. [Assumption requiring validation]
2. [Assumption requiring validation]
3. [Assumption requiring validation]

## Success Metrics
- [Metric 1 with target]
- [Metric 2 with target]

## Created
[YYYY-MM-DD]

## Status
[Draft | In Validation | Validated | Pivoted | Abandoned]
```

## Field Definitions

| Field | Required | Description |
|-------|----------|-------------|
| Working Title | Yes | Short name for the idea (3-7 words) |
| One-Line Pitch | Yes | Single sentence value proposition |
| Problem Statement | Yes | 2-3 sentences on the pain point |
| Target Customer | Yes | Initial segment hypothesis |
| Solution Hypothesis | Yes | How the product solves the problem |
| Key Assumptions | Yes | 3+ assumptions to validate |
| Success Metrics | Yes | 2+ measurable outcomes |
| Created | Yes | ISO date format |
| Status | Yes | One of the allowed values |

## Validation Rules

1. Working Title must be unique within the project
2. One-Line Pitch must be under 150 characters
3. Key Assumptions must have at least 3 items
4. Status must be one of: Draft, In Validation, Validated, Pivoted, Abandoned
