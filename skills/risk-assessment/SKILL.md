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

## Quick Start

Given all prior artifacts, assess risks:
1. Identify risks across categories
2. Score by severity and likelihood
3. Develop mitigation strategies
4. Document must-be-true assumptions
5. Output `risks.md`

## Inputs Required

- All prior artifacts (aggregated context)
- Particularly: `mvp_spec.md`, `gtm_plan.md`, `competitors.csv`

## Step-by-Step Workflow

### Step 1: Review Prior Artifacts

Gather context from all prior work:
- Idea brief: Core assumptions
- Signals: Demand validation risks
- ICP: Customer understanding risks
- Competitors: Competitive risks
- Market size: Market risks
- Pricing: Revenue model risks
- MVP spec: Technical risks
- GTM: Go-to-market risks

### Step 2: Identify Risks by Category

For each category, brainstorm potential risks:

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

### Step 3: Score Each Risk

For each risk, assess:

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

### Step 4: Prioritize Critical Risks

Focus on high-score risks (Score ≥ 15):
- Document in detail
- Develop mitigation strategy
- Create contingency plan
- Assign ownership

### Step 5: Document Must-Be-True Assumptions

List the assumptions that must hold:
- From the idea brief
- From market research
- From technical planning
- From GTM strategy

For each, note how it could be validated.

### Step 6: Identify Constraints

Document known constraints:
- Budget limitations
- Timeline requirements
- Team capabilities
- Technology limitations
- Legal/regulatory bounds

### Step 7: Map Dependencies

Identify external dependencies:
- Third-party APIs
- Platform providers
- Data sources
- Partners
- Regulatory approvals

For each, note the risk if unavailable.

### Step 8: Generate Artifact

Create `risks.md` following the contract format.

## Workflow Checklist

```
Risk Assessment Progress:
- [ ] Prior artifacts reviewed
- [ ] Technical risks identified
- [ ] Market risks identified
- [ ] Execution risks identified
- [ ] Regulatory risks identified
- [ ] Financial risks identified
- [ ] Risks scored (severity × likelihood)
- [ ] Critical risks detailed with mitigation
- [ ] Must-be-true assumptions documented
- [ ] Constraints listed
- [ ] Dependencies mapped
- [ ] risks.md created
```

## Output Format

Create `risks.md` following the artifact contract in `contracts/risks.md`.

Required sections:
- Risk matrix table (all risks with scores)
- Critical risks detail (Score ≥ 15)
- Must-be-true assumptions
- Constraints
- Dependencies

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
