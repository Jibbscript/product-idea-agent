# Artifact Contract: mvp_spec.md

## Purpose
Documents MVP scope, technical approach, and differentiation strategy.

## Producer
- `solution-wedge` skill

## Consumers
- `gtm-channels`
- `risk-assessment`
- `validation-report`

## Schema

```markdown
# MVP Specification

## Product Vision
[1-2 sentence north star - what this becomes at scale]

## MVP Scope

### Must Have (P0)
1. [Feature]: [Description] - [User Job Addressed]
2. [Feature]: [Description] - [User Job Addressed]
3. [Feature]: [Description] - [User Job Addressed]

### Should Have (P1)
1. [Feature]: [Description]
2. [Feature]: [Description]

### Won't Have (v1)
- [Feature] - [Reason for exclusion]
- [Feature] - [Reason for exclusion]

## Technical Approach
- **Platform**: [web/mobile/desktop/API]
- **Stack**: [technology choices with rationale]
- **Dependencies**: [external services, APIs, libraries]
- **Build vs Buy**: [key decisions on components]

## Differentiation
[What makes this different from alternatives - the "wedge"]

### Competitive Advantage
[Specific advantage that is hard to replicate]

### Positioning Statement
For [target customer] who [need], [product name] is a [category] that [key benefit]. Unlike [alternatives], we [key differentiator].

## Timeline
- **Phase 1** ([duration]): [deliverables]
- **Phase 2** ([duration]): [deliverables]
- **MVP Launch**: [target milestone, not date]

## Success Criteria
- [Metric 1]: [target value]
- [Metric 2]: [target value]

## Open Questions
1. [Question requiring further research or decision]
2. [Question requiring further research or decision]
```

## Field Definitions

| Field | Required | Description |
|-------|----------|-------------|
| Product Vision | Yes | 1-2 sentence north star |
| Must Have (P0) | Yes | 3-5 essential features |
| Should Have (P1) | Yes | 2-4 important but deferrable features |
| Won't Have | Yes | Features explicitly excluded |
| Platform | Yes | Primary deployment target |
| Stack | Yes | Key technology choices |
| Dependencies | Yes | External services required |
| Differentiation | Yes | Clear wedge vs alternatives |
| Positioning Statement | Yes | Follows template format |
| Timeline | Yes | Phased approach with milestones |
| Success Criteria | Yes | 2+ measurable outcomes |

## Feature Prioritization Guidelines

### P0 (Must Have) Criteria
- Without this, the product doesn't work
- Directly addresses the core pain point
- Required for first paying customer

### P1 (Should Have) Criteria
- Significantly improves experience
- Addresses secondary pain points
- Differentiates from free alternatives

### Won't Have Criteria
- Nice to have but not essential for MVP
- Complex to build relative to value
- Can be added post-launch based on feedback
