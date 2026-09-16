---
name: risk-assessment
description: Identifies risks, constraints, and dependencies for a product idea. Use when assessing what could go wrong, identifying blockers, or evaluating execution risks.
license: Apache-2.0
metadata:
  author: product-idea-agent
  pack: product-idea-agent
allowed-tools: Read Write WebSearch
---

# Risk Assessment

Identifies risks, constraints, dependencies, and mitigation strategies.

## Outcome

`risks.md` holds every material risk to the idea, scored on severity and likelihood, with the critical ones worked through to a mitigation and a contingency, plus the assumptions that must hold, the constraints the team operates under, and the external dependencies that could fail. A finished assessment reads the eight artifacts before it and turns each one's weak spots into named risks.

## Inputs Required

- All prior artifacts (aggregated context)
- Particularly: `mvp_spec.md`, `gtm_plan.md`, `competitors.csv`

## What risks.md Must Cover

### Evidence From Prior Artifacts
Where each risk came from, since every prior artifact carries its own kind of risk:
- Idea brief: Core assumptions
- Signals: Demand validation risks
- ICP: Customer understanding risks
- Competitors: Competitive risks
- Market size: Market risks
- Pricing: Revenue model risks
- MVP spec: Technical risks
- GTM: Go-to-market risks

### Risk Categories
Risks surfaced under each of the five categories, or an explicit note that a category does not apply and why:

**Technical Risks:**
- Technology uncertainty
- Integration dependencies
- Scalability challenges
- Security vulnerabilities
- Data/privacy concerns

**Market Risks:**
- Demand doesn't materialize
- Competition intensifies
- Market size overestimated
- Timing is wrong
- Segment shifts

**Execution Risks:**
- Team gaps
- Resource constraints
- Timeline overruns
- Scope creep
- Quality issues

**Regulatory Risks:**
- Compliance requirements
- Licensing needs
- Data regulations (GDPR, CCPA)
- Industry-specific rules
- Liability exposure

**Financial Risks:**
- Funding runway
- Unit economics don't work
- CAC too high
- Churn too high
- Cash flow timing

The Risk Identification Questions below are the prompts for each category.

### Risk Scoring
Every risk carries both numbers on these scales:

**Severity (1-5):**
- 1 = Negligible: Minor inconvenience
- 2 = Low: Some rework needed
- 3 = Medium: Significant delay or cost
- 4 = High: Major pivot required
- 5 = Critical: Existential threat

**Likelihood (1-5):**
- 1 = Rare: <10% chance
- 2 = Unlikely: 10-25% chance
- 3 = Possible: 25-50% chance
- 4 = Likely: 50-75% chance
- 5 = Almost Certain: >75% chance

**Risk Score = Severity × Likelihood**

### Critical Risks
The risks scoring 15 or higher, each written up in detail with a mitigation strategy, a contingency plan, and an owner, using the Mitigation Strategy Template below. These are the risks the validation report will lead with, so the write-up is where the depth goes.

### Must-Be-True Assumptions
The assumptions the whole plan rests on, gathered from the idea brief, market research, technical planning, and GTM strategy, each paired with how it could be validated. An assumption with no way to test it is a risk in disguise and is scored as one.

### Execution Constraints
The known limits the team is working inside: budget limitations, timeline requirements, team capabilities, technology limitations, and legal/regulatory bounds. Constraints are not risks, but they decide which mitigations are affordable.

### Dependencies
The external things the plan cannot control (third-party APIs, platform providers, data sources, partners, regulatory approvals), each with the risk if it becomes unavailable.

## How to Work

The five categories are independent sweeps over the prior artifacts and can be worked in any order. The sequenced part is short:
1. Scoring, which needs the full risk list
2. Prioritization into critical risks, which needs the scores
3. Mitigation write-ups, which need the critical set

Assumptions, constraints, and dependencies are gathered alongside the category sweeps rather than after them.

## Constraints

Every one of the five categories is covered or explicitly recorded as not applicable with the reason. Every risk carries both a severity and a likelihood on the stated 1-5 scales, and the risk matrix table shows their product. Every critical risk (score of 15 or more) carries a mitigation and a contingency. Must-be-true assumptions each name a validation method. Dependencies each state what breaks if they fail. The finished `risks.md` conforms to `contracts/risks.md`.

## Output Format

Create `risks.md` following the artifact contract in `contracts/risks.md`.

Required sections:
- Risk matrix table (all risks with scores)
- Critical risks detail (Score ≥ 15)
- Must-be-true assumptions
- Constraints
- Dependencies

## Working the Risk Register

Regulatory research, third-party dependency checks and competitor-response scenarios are independent investigations, so run them as parallel sub-agents. Detail is proportional to score, so risks at 15 or above earn a full mitigation and contingency, while cataloguing every low-score risk at the same length buries the ones that matter. Likelihood scores are judgments and should read as judgments, so a regulatory requirement confirmed by a named rule cites that rule while a risk resting on a market belief is marked as an assumption.

The risk that matters is usually the one absent from the category list, so ask what would change the verdict if it landed next quarter and write down the second-order consequence rather than the first. `risks.md` is consumed by scorecard-generator, which counts critical risks into Execution Difficulty, and by validation-report's risk section, so a risk softened here softens the final recommendation too, and an assessment that finds nothing is a finding to be suspicious of. Lead with the risk that could end this, not with the matrix.

The deliverable is `risks.md`; mitigating the risks by rescoping the MVP or rewriting the GTM plan belongs to whoever acts on the report, so record them and stop there. Before you finish, re-read the must-be-true assumptions against the earlier artifacts and confirm none was already contradicted by the demand or pricing evidence.

## Risk Identification Questions

### Technical
- What's the hardest technical challenge?
- What third-party services are we dependent on?
- What could make this 10x harder than expected?
- What's our biggest technical unknown?

### Market
- What if demand is 50% lower than expected?
- What if our biggest competitor copies us?
- What if the market shifts during development?
- What if our timing is off by 2 years?

### Execution
- What team skills are we missing?
- What's most likely to slip?
- What could block progress?
- What if key team members leave?

### Regulatory
- What regulations apply to this space?
- What licenses or certifications are needed?
- What data privacy requirements exist?
- What liability exposure do we have?

### Financial
- How long is our runway?
- What if CAC is 2x our estimate?
- What if churn is 2x our estimate?
- What's our break-even timeline?

## Mitigation Strategy Template

For each critical risk:

```
### [Risk Name]

**Description**: [What exactly is the risk]

**Impact if realized**: [What happens if this occurs]

**Current status**: [How confident are we this won't happen]

**Mitigation strategy**:
1. [Proactive step to reduce likelihood]
2. [Proactive step to reduce impact]
3. [Early warning indicators]

**Contingency plan**:
- If this happens, we will [backup plan]

**Owner**: [Who is responsible for monitoring]

**Review cadence**: [How often to reassess]
```

## Edge Cases

**Too many risks identified:**
- Focus on top 10-15 highest scores
- Group similar risks
- Note lower risks as "monitored"

**Risks seem manageable:**
- Good! Document why
- Note confidence level
- Still prepare contingencies

**Existential risks found:**
- Flag prominently
- Recommend addressing before proceeding
- Consider if idea should pivot

**Regulatory uncertainty:**
- Flag as high risk
- Recommend legal consultation
- Note compliance timeline needs

## References

- [risk_categories.md](references/risk_categories.md): Detailed risk category frameworks
