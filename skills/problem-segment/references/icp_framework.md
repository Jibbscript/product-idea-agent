# ICP Framework

Comprehensive framework for defining ideal customer profiles.

## The ICP Canvas

### 1. Segment Definition

Start by answering:
- **Who** has this problem? (broad description)
- **What** are they trying to accomplish? (job to be done)
- **Why** is this hard for them? (root cause)
- **When** does the problem occur? (context/trigger)
- **Where** do they currently solve it? (alternatives)

### 2. Demographic/Firmographic Profile

#### B2C Template
```yaml
demographics:
  age_range: "25-45"
  gender: "60% female, 40% male"
  location: "US urban/suburban"
  income_level: "$75K-$150K household"
  education: "College degree+"
  life_stage: "Homeowner, 1-2 kids"
  tech_savviness: "Early majority"
```

#### B2B Template
```yaml
firmographics:
  company_size: "50-500 employees"
  industry: "SaaS, Technology"
  revenue: "$5M-$50M ARR"
  stage: "Series A to Series C"
  geography: "US, UK, DACH"

  roles:
    decision_maker: "VP Engineering, CTO"
    user: "Software Engineer, DevOps"
    influencer: "Team Lead, Architect"
    budget_holder: "CFO, VP Engineering"
```

### 3. Psychographic Profile

#### Goals (What they want)
- **Primary goal**: The main outcome they seek
- **Secondary goals**: Additional desired outcomes
- **Aspirational goals**: What success looks like long-term

#### Frustrations (What blocks them)
- **Current pain**: What's not working today
- **Past failures**: Solutions that didn't work
- **Fear**: What they're worried about

#### Values (What they prioritize)
- **Trade-offs**: Speed vs quality, cost vs features
- **Trust signals**: What makes them trust a solution
- **Deal breakers**: What would make them reject a solution

### 4. Behavioral Profile

#### Information Sources
- **Publications**: Blogs, newsletters, magazines
- **Social platforms**: LinkedIn, Twitter, Reddit, etc.
- **Communities**: Slack groups, Discord, forums
- **Events**: Conferences, webinars, meetups
- **Influencers**: Who they follow and trust

#### Purchase Triggers
- **Internal triggers**: New role, new project, growth pain
- **External triggers**: Market change, competitor action, funding
- **Timing**: End of quarter, budget cycle, planning season

#### Purchase Process
- **Discovery**: How they find solutions
- **Evaluation**: Criteria and process
- **Decision**: Who decides, approval process
- **Objections**: Common concerns raised

### 5. Problem Severity Assessment

#### Severity Score Components

| Factor | Weight | Questions to Answer |
|--------|--------|---------------------|
| Frequency | 25% | How often does this problem occur? |
| Impact | 35% | What's the cost when it happens? |
| Urgency | 20% | How quickly must it be resolved? |
| Alternatives | 20% | How poor are current solutions? |

#### Severity Score Scale

| Score | Label | Description |
|-------|-------|-------------|
| 9-10 | Hair on fire | Must solve immediately, high willingness to pay |
| 7-8 | Significant pain | Active problem-solving, budget available |
| 5-6 | Moderate frustration | Would like to solve, lower priority |
| 3-4 | Minor annoyance | Can live with current solution |
| 1-2 | Non-issue | Not really a problem for this segment |

### 6. Segment Prioritization Matrix

Rate each segment (1-5) on these dimensions:

| Segment | Severity | Ability to Pay | Accessibility | Size | Total |
|---------|----------|----------------|---------------|------|-------|
| Segment A | 5 | 4 | 3 | 4 | 16 |
| Segment B | 3 | 5 | 4 | 3 | 15 |
| Segment C | 4 | 2 | 5 | 5 | 16 |

**Prioritization factors:**
- **Severity**: How bad is the problem? (most important)
- **Ability to Pay**: Do they have budget?
- **Accessibility**: Can you reach them?
- **Size**: Is the segment large enough?

### 7. Negative Personas

Define who is NOT your customer:

- **Wrong size**: Too small (can't pay) or too large (need enterprise sales)
- **Wrong stage**: Too early (no budget) or too established (locked in)
- **Wrong industry**: Different regulatory or technical needs
- **Wrong geography**: Language, time zone, legal barriers

## ICP Validation Checklist

Before finalizing the ICP:

- [ ] Based on research, not assumptions
- [ ] Specific enough to identify real people
- [ ] Large enough to build a business
- [ ] Accessible through identifiable channels
- [ ] Has budget and authority to buy
- [ ] Problem severity is validated with evidence
- [ ] Negative personas defined

## Example: B2B SaaS ICP

```yaml
icp:
  version: "1.0"

  primary_segment:
    name: "Growth-Stage DevOps Teams"
    description: "DevOps engineers and platform teams at Series A-C
      startups who are scaling infrastructure but don't have dedicated
      SRE teams yet."

    firmographics:
      company_size: "50-300 employees"
      industry: "SaaS, Technology, FinTech"
      role_titles:
        - "DevOps Engineer"
        - "Platform Engineer"
        - "VP Engineering"
      tech_stack: "AWS/GCP, Kubernetes, Terraform"

    psychographics:
      goals:
        - "Ship faster without breaking production"
        - "Reduce on-call burden on small team"
        - "Meet SOC 2 compliance for enterprise sales"
      frustrations:
        - "Too many alerts, most are noise"
        - "Incident response is chaotic and undocumented"
        - "Can't hire fast enough to keep up with growth"
      values:
        - "Developer experience matters"
        - "Automation over manual processes"
        - "Open source when possible"

    behaviors:
      information_sources:
        - "Hacker News, r/devops, DevOps Weekly"
        - "KubeCon, DevOpsDays"
        - "Charity Majors, Kelsey Hightower"
      purchase_triggers:
        - "Major outage that cost revenue"
        - "New enterprise customer requiring SLAs"
        - "Team scaling from 5 to 15 engineers"
      objections:
        - "We can build this ourselves"
        - "Another tool to manage"
        - "Security/data concerns"

  problem_severity: 8
  problem_evidence: "Reddit threads show 2-3 posts/week about incident
    fatigue; 73% of SRE survey respondents report burnout"
```
