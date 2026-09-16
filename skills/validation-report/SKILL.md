---
name: validation-report
description: Generates comprehensive validation report synthesizing all research and analysis. Use when creating a final deliverable summarizing the product validation, preparing for stakeholder review, or documenting validation findings.
license: Apache-2.0
metadata:
  author: product-idea-agent
  pack: product-idea-agent
allowed-tools: Read Write
---

# Validation Report Generator

Generates comprehensive validation reports synthesizing all research and analysis.

## Quick Start

Given all prior artifacts and scorecard, generate report:
1. Aggregate findings from all artifacts
2. Write executive summary
3. Structure section narratives
4. Include key data and visualizations
5. Add recommendations and next steps
6. Output `validation_report.md`

## Inputs Required

- All prior artifacts
- `scorecard.json` (from scorecard-generator) - required

## Step-by-Step Workflow

### Step 1: Review All Artifacts

Gather and review:
- `idea_brief.md` - The core concept
- `signals.md` - Demand validation
- `icp.yaml` - Customer definition
- `competitors.csv` - Competitive landscape
- `market_size.md` - Market opportunity
- `pricing.yaml` - Revenue model
- `mvp_spec.md` - Product scope
- `gtm_plan.md` - Go-to-market strategy
- `risks.md` - Risk assessment
- `scorecard.json` - Validation scores

### Step 2: Write Executive Summary

Create a 3-5 paragraph summary covering:
- The idea and its core value proposition
- Key validation findings (strongest and weakest areas)
- Overall recommendation (GO/PIVOT/NO-GO)
- Critical next steps

This should be readable in 2 minutes and convey the essential decision.

### Step 3: Structure Main Sections

Organize the report into logical sections:

1. **The Opportunity**
   - Problem statement
   - Target customer overview
   - Market size summary

2. **Validation Evidence**
   - Demand signals findings
   - Competitive landscape summary
   - Customer evidence (quotes, data)

3. **The Solution**
   - MVP scope
   - Differentiation strategy
   - Technical approach

4. **Business Model**
   - Pricing strategy
   - Unit economics
   - Revenue projections

5. **Go-to-Market**
   - Channel strategy
   - Launch plan
   - Growth mechanics

6. **Risks & Mitigations**
   - Critical risks
   - Key assumptions
   - Mitigation strategies

7. **Scorecard**
   - Dimension scores (table)
   - Composite score
   - Recommendation rationale

8. **Recommendations & Next Steps**
   - Immediate actions
   - Key milestones
   - Resources needed

### Step 4: Add Supporting Data

Include key data points:
- Market size figures (TAM/SAM/SOM)
- Demand signal metrics
- Competitor comparison highlights
- Pricing benchmarks
- Risk matrix summary

### Step 5: Create Visualizations (Text-Based)

Add text-based diagrams where helpful:
- Scorecard dimension chart
- Market positioning map
- Timeline overview
- Artifact flow diagram

### Step 6: Write Recommendations

Based on the scorecard verdict:

**For GO:**
- Immediate execution priorities
- Key milestones to hit
- Resources to secure
- Risks to monitor

**For PIVOT:**
- What specifically needs to change
- How to validate the pivot
- Timeline for re-assessment

**For NO-GO:**
- Key learnings from this validation
- Alternative directions to explore
- What would need to change to reconsider

### Step 7: Generate Artifact

Create `validation_report.md` with professional formatting.

## Workflow Checklist

```
Validation Report Progress:
- [ ] All artifacts reviewed
- [ ] Scorecard analyzed
- [ ] Executive summary written
- [ ] Opportunity section complete
- [ ] Validation evidence section complete
- [ ] Solution section complete
- [ ] Business model section complete
- [ ] Go-to-market section complete
- [ ] Risks section complete
- [ ] Scorecard section complete
- [ ] Recommendations written
- [ ] Document formatted and polished
- [ ] validation_report.md created
```

## Output Format

Create `validation_report.md` with this structure:

```markdown
# Product Validation Report: [Idea Name]

**Generated**: [Date]
**Recommendation**: [GO / PIVOT / NO-GO]
**Composite Score**: [XX/100]

---

## Executive Summary

[3-5 paragraphs summarizing the validation]

---

## 1. The Opportunity

### Problem Statement
[From idea brief]

### Target Customer
[From ICP]

### Market Size
[From market sizing]

---

## 2. Validation Evidence

### Demand Signals
[From signals analysis]

### Competitive Landscape
[From competitive analysis]

### Customer Evidence
[Key quotes and data]

---

## 3. The Solution

### MVP Scope
[From MVP spec]

### Differentiation
[From solution wedge]

### Technical Approach
[From MVP spec]

---

## 4. Business Model

### Pricing Strategy
[From pricing analysis]

### Unit Economics
[From pricing analysis]

---

## 5. Go-to-Market

### Channel Strategy
[From GTM plan]

### Launch Plan
[From GTM plan]

---

## 6. Risks & Mitigations

### Critical Risks
[From risk assessment]

### Key Assumptions
[From risk assessment]

---

## 7. Scorecard

| Dimension | Score | Evidence |
|-----------|-------|----------|
| Problem Severity | X/10 | [summary] |
| ... | ... | ... |

**Composite Score**: XX/100
**Verdict**: [GO/PIVOT/NO-GO]

---

## 8. Recommendations & Next Steps

### Immediate Actions
1. [Action item]
2. [Action item]
3. [Action item]

### Key Milestones
[Timeline or milestone list]

### Resources Needed
[Team, budget, tools]

---

## Appendix

- Link to detailed artifacts
- Additional data tables
- Methodology notes
```

## Working the Report

Lead with the verdict: the first sentence after the title says GO, PIVOT or NO-GO and why, ahead of any section narrative. This report ends the chain and is read by people who saw none of the work, so vocabulary built up across ten artifacts is either re-introduced here or left out. The eight section narratives are independent writing tasks over artifacts that are already final, so delegate them to sub-agents in parallel and spend your own attention on the executive summary that has to hold them together.

Section depth is proportional to the verdict's drivers, so the dimensions that produced GO, PIVOT or NO-GO earn the detail, and a section with nothing decision-relevant in it can be three sentences. Every figure in the report traces to the artifact it came from, and where an artifact was missing or its number unverified the report says so instead of smoothing over the gap. The most valuable paragraph is usually the one naming what would change the verdict, and a surprising finding that contradicts the composite belongs in the summary rather than an appendix.

The deliverable is `validation_report.md` assembled from the existing artifacts, so re-running research or revising a scorecard dimension mid-write is out of scope; note the gap and stop there. Before you finish, re-read the executive summary on its own: it should stand without the rest of the document and contradict nothing in the scorecard table.

## Writing Guidelines

### Tone
- Professional but accessible
- Data-driven with clear conclusions
- Actionable, not academic

### Length
- Executive summary: 300-500 words
- Full report: 2,000-4,000 words
- Aim for scannable with clear headings

### Evidence
- Cite specific numbers
- Include direct quotes where impactful
- Reference source artifacts

## Edge Cases

**Incomplete artifacts:**
- Note what's missing
- Adjust confidence accordingly
- Recommend gathering missing data

**Conflicting findings:**
- Acknowledge the conflict
- Explain implications
- Recommend resolution approach

**Borderline recommendation:**
- Be transparent about close call
- Highlight deciding factors
- Provide conditional guidance

## References

- [report_template.md](references/report_template.md): Full report template
