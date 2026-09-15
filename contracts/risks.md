# Artifact Contract: risks.md

## Purpose
Documents risks, constraints, dependencies, and mitigation strategies.

## Producer
- `risk-assessment` skill

## Consumers
- `scorecard-generator`
- `validation-report`

## Schema

```markdown
# Risk Assessment

## Risk Matrix

| Risk | Category | Severity | Likelihood | Score | Mitigation |
|------|----------|----------|------------|-------|------------|
| [risk] | [category] | [1-5] | [1-5] | [S×L] | [strategy] |

## Critical Risks (Score >= 15)

### [Risk 1]
- **Description**: [detailed description of the risk]
- **Impact if realized**: [consequences to the business]
- **Mitigation strategy**: [how to reduce likelihood or impact]
- **Contingency**: [backup plan if risk materializes]

### [Risk 2]
- **Description**: [detailed description]
- **Impact if realized**: [consequences]
- **Mitigation strategy**: [approach]
- **Contingency**: [backup plan]

## Must-Be-True Assumptions
1. [Assumption]: [how to validate]
2. [Assumption]: [how to validate]
3. [Assumption]: [how to validate]

## Constraints
- [Constraint 1]: [implication for execution]
- [Constraint 2]: [implication for execution]

## Dependencies
- [Dependency 1]: [risk if unavailable]
- [Dependency 2]: [risk if unavailable]
```

## Field Definitions

| Field | Required | Description |
|-------|----------|-------------|
| Risk Matrix | Yes | All identified risks with scores |
| Critical Risks | Yes | Detailed analysis of high-score risks |
| Must-Be-True Assumptions | Yes | At least 3 key assumptions |
| Constraints | Yes | At least 2 execution constraints |
| Dependencies | Yes | At least 2 external dependencies |

## Risk Categories

| Category | Examples |
|----------|----------|
| Technical | API dependencies, scalability, security |
| Market | Competition, demand shifts, timing |
| Execution | Team gaps, timeline, budget |
| Regulatory | Compliance, licensing, data privacy |
| Financial | Funding, runway, unit economics |

## Scoring Guide

### Severity (1-5)
| Score | Impact |
|-------|--------|
| 1 | Negligible - Minor inconvenience |
| 2 | Low - Some rework required |
| 3 | Medium - Significant delay or cost |
| 4 | High - Major pivot required |
| 5 | Critical - Existential threat |

### Likelihood (1-5)
| Score | Probability |
|-------|-------------|
| 1 | Rare - <10% chance |
| 2 | Unlikely - 10-25% chance |
| 3 | Possible - 25-50% chance |
| 4 | Likely - 50-75% chance |
| 5 | Almost Certain - >75% chance |

### Risk Score Interpretation
- **1-5**: Low priority, monitor
- **6-10**: Medium priority, plan mitigation
- **11-15**: High priority, active mitigation required
- **16-25**: Critical, address before proceeding
