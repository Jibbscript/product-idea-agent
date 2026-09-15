# Risk Categories Framework

Detailed frameworks for identifying and assessing risks by category.

## Risk Category Deep Dives

### Technical Risks

#### Common Technical Risks

| Risk | Description | Typical Severity |
|------|-------------|------------------|
| Technology uncertainty | Core technology may not work | High (4-5) |
| Integration complexity | APIs may not behave as expected | Medium (3) |
| Scalability limits | Architecture may not scale | Medium-High (3-4) |
| Security vulnerabilities | Data breaches, exploits | High (4-5) |
| Performance issues | Slow, unreliable experience | Medium (3) |
| Technical debt | Shortcuts create future problems | Low-Medium (2-3) |
| Dependency failures | Third-party services go down | Medium (3) |

#### Technical Risk Assessment Questions

1. **Feasibility**: Has anyone built this before?
2. **Complexity**: How many moving parts?
3. **Dependencies**: What external services are required?
4. **Expertise**: Do we have the skills in-house?
5. **Scalability**: Will architecture handle 10x growth?
6. **Security**: What attack surfaces exist?
7. **Maintenance**: How complex to operate?

#### Technical Risk Mitigation Patterns

| Risk | Mitigation |
|------|------------|
| Technology uncertainty | Prototype early, fail fast |
| Integration complexity | Mock APIs, robust error handling |
| Scalability limits | Design for scale, monitor early |
| Security vulnerabilities | Security audit, penetration testing |
| Dependency failures | Fallbacks, circuit breakers |

### Market Risks

#### Common Market Risks

| Risk | Description | Typical Severity |
|------|-------------|------------------|
| Demand overestimation | Market smaller than projected | High (4-5) |
| Competition | Incumbents or new entrants compete | Medium-High (3-4) |
| Timing | Too early or too late | High (4) |
| Segment shift | ICP changes or moves | Medium-High (3-4) |
| Commoditization | Race to bottom on pricing | Medium (3) |
| Platform risk | Dependent on platform that changes | High (4-5) |

#### Market Risk Assessment Questions

1. **Validation**: Is demand proven or assumed?
2. **Competition**: Who could eat our lunch?
3. **Timing**: Why now vs. 2 years ago?
4. **Alternatives**: What else could customers do?
5. **Trends**: Is the market growing or shrinking?
6. **Platforms**: Are we dependent on gatekeepers?

#### Market Risk Mitigation Patterns

| Risk | Mitigation |
|------|------------|
| Demand overestimation | Validate with real customers before building |
| Competition | Find defensible wedge, move fast |
| Timing | Monitor leading indicators |
| Segment shift | Maintain customer feedback loops |
| Platform risk | Diversify channels, own customer relationship |

### Execution Risks

#### Common Execution Risks

| Risk | Description | Typical Severity |
|------|-------------|------------------|
| Team gaps | Missing critical skills | High (4) |
| Founder conflict | Co-founder disputes | High (5) |
| Key person risk | Dependent on one person | High (4) |
| Scope creep | Building too much | Medium (3) |
| Timeline slippage | Taking longer than planned | Medium (3) |
| Quality issues | Shipping buggy product | Medium-High (3-4) |
| Burnout | Team exhaustion | Medium-High (3-4) |

#### Execution Risk Assessment Questions

1. **Team**: Do we have all needed skills?
2. **Leadership**: Is there clear ownership?
3. **Scope**: Is scope clearly defined and managed?
4. **Timeline**: Is the timeline realistic?
5. **Process**: Do we have effective workflows?
6. **Morale**: Is the team sustainable?

#### Execution Risk Mitigation Patterns

| Risk | Mitigation |
|------|------------|
| Team gaps | Hire, partner, or acquire skills |
| Key person risk | Cross-train, document knowledge |
| Scope creep | Strict prioritization, say no often |
| Timeline slippage | Buffer time, early warning metrics |
| Quality issues | Testing, code review, monitoring |
| Burnout | Sustainable pace, breaks, boundaries |

### Regulatory Risks

#### Common Regulatory Risks

| Risk | Description | Typical Severity |
|------|-------------|------------------|
| Compliance gaps | Not meeting requirements | High (4-5) |
| Licensing needs | Required certifications | Medium-High (3-4) |
| Data privacy | GDPR, CCPA, etc. | High (4) |
| Industry-specific | HIPAA, PCI, etc. | High (4-5) |
| IP issues | Patent/trademark conflicts | High (4) |
| Liability | Legal exposure | High (4-5) |

#### Regulatory Risk by Industry

| Industry | Key Regulations |
|----------|-----------------|
| Healthcare | HIPAA, FDA, state licensing |
| Finance | SOX, PCI-DSS, state money transmission |
| Education | FERPA, COPPA, accessibility |
| General SaaS | GDPR, CCPA, SOC 2 |
| AI/ML | Emerging AI regulations, bias laws |

#### Regulatory Risk Mitigation Patterns

| Risk | Mitigation |
|------|------------|
| Compliance gaps | Early legal consultation, compliance tools |
| Data privacy | Privacy by design, consent management |
| Industry-specific | Industry expertise, certifications |
| IP issues | Freedom-to-operate search, IP counsel |
| Liability | Terms of service, insurance |

### Financial Risks

#### Common Financial Risks

| Risk | Description | Typical Severity |
|------|-------------|------------------|
| Runway shortage | Run out of money | Critical (5) |
| Unit economics | CAC/LTV doesn't work | High (4-5) |
| Pricing failure | Can't charge enough | High (4) |
| Churn | Can't retain customers | High (4) |
| Cash flow | Timing of in/outflows | High (4) |
| Fundraising | Can't raise when needed | High (4-5) |

#### Financial Health Indicators

| Metric | Healthy | Warning | Critical |
|--------|---------|---------|----------|
| Runway | >12 mo | 6-12 mo | <6 mo |
| LTV:CAC | >3:1 | 2-3:1 | <2:1 |
| CAC Payback | <12 mo | 12-18 mo | >18 mo |
| Monthly Burn | Decreasing | Stable | Increasing |
| Churn | <5% annually | 5-10% | >10% |

#### Financial Risk Mitigation Patterns

| Risk | Mitigation |
|------|------------|
| Runway shortage | Raise early, cut costs, revenue focus |
| Unit economics | Channel optimization, pricing adjustment |
| Churn | Onboarding, success team, product fixes |
| Cash flow | Payment terms, annual billing incentives |
| Fundraising | Build relationships early, hit milestones |

## Risk Prioritization Matrix

### Scoring Grid

```
                    Likelihood
           1    2    3    4    5
         ┌────┬────┬────┬────┬────┐
       5 │  5 │ 10 │ 15 │ 20 │ 25 │ ← Critical
       4 │  4 │  8 │ 12 │ 16 │ 20 │
Severity │────┼────┼────┼────┼────│
       3 │  3 │  6 │  9 │ 12 │ 15 │
       2 │  2 │  4 │  6 │  8 │ 10 │
       1 │  1 │  2 │  3 │  4 │  5 │ ← Low
         └────┴────┴────┴────┴────┘
```

### Response by Score

| Score | Priority | Response |
|-------|----------|----------|
| 16-25 | Critical | Address immediately, blocker for proceeding |
| 11-15 | High | Develop mitigation plan, assign owner |
| 6-10 | Medium | Monitor, include in planning |
| 1-5 | Low | Accept, review periodically |

## Risk Register Template

```markdown
| ID | Risk | Category | Severity | Likelihood | Score | Owner | Status |
|----|------|----------|----------|------------|-------|-------|--------|
| R1 | [description] | Technical | 4 | 3 | 12 | [name] | Mitigating |
| R2 | [description] | Market | 5 | 2 | 10 | [name] | Monitoring |
```

## Assumption Tracking

### Assumption Categories

1. **Customer Assumptions**
   - They have this problem
   - They're actively trying to solve it
   - They'll pay $X for a solution

2. **Product Assumptions**
   - This solution will work
   - We can build it with these resources
   - It will be differentiated enough

3. **Market Assumptions**
   - Market is this size
   - It's growing at this rate
   - We can capture X% share

4. **Business Model Assumptions**
   - CAC will be approximately $X
   - LTV will be approximately $Y
   - We can reach customers via these channels

### Assumption Validation Methods

| Method | Cost | Speed | Confidence |
|--------|------|-------|------------|
| Customer interviews | Low | Fast | Medium |
| Surveys | Low | Fast | Low-Medium |
| Landing page test | Low | Medium | Medium |
| Prototype test | Medium | Medium | High |
| Pilot/Beta | High | Slow | High |
| Full launch | High | Slow | Highest |
