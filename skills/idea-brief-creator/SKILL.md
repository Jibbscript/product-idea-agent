---
name: idea-brief-creator
description: Creates or refines a structured startup/product idea brief from initial concept. Use when starting product validation, capturing a new idea, structuring an opportunity hypothesis, or when asked to help with a startup idea.
license: Apache-2.0
metadata:
  author: product-idea-agent
  pack: product-idea-agent
allowed-tools: Read Write Edit
---

# Idea Brief Creator

Creates structured idea briefs that serve as the foundation for product validation workflows.

## Quick Start

Transform a raw idea into a structured brief:
1. Gather the initial concept from the user
2. Ask clarifying questions to fill gaps
3. Structure into the idea brief format
4. Output `idea_brief.md`

## Inputs Required

- Raw idea description (text, conversation, or notes)
- Optional: target market hints, problem observations, existing research

## Step-by-Step Workflow

### Step 1: Extract Core Concept
From the user's input, identify:
- What the product/service does
- Who it's for (initial hypothesis)
- What problem it solves

If any of these are unclear, ask clarifying questions.

### Step 2: Craft One-Line Pitch
Create a single sentence that captures:
- The value delivered
- The target customer
- The key differentiator (if known)

Format: "[Product] helps [customer] [achieve outcome] by [method]."

### Step 3: Define Problem Statement
Write 2-3 sentences that:
- Describe the pain point clearly
- Explain why existing solutions fall short
- Hint at the severity/frequency of the problem

### Step 4: Identify Target Customer
Capture initial hypothesis about:
- Who has this problem most acutely
- Demographic or firmographic hints
- Behavioral indicators

### Step 5: Document Solution Hypothesis
Describe:
- How the product solves the problem
- Key capabilities or features (high-level)
- Why this approach might work

### Step 6: List Key Assumptions
Identify 3-5 assumptions that must be true for success:
- About the customer (do they have this problem?)
- About the solution (will this solve it?)
- About the market (will they pay?)
- About execution (can we build it?)

### Step 7: Define Success Metrics
Suggest 2-3 measurable outcomes:
- Validation-phase metrics (signups, interviews, LOIs)
- Launch-phase metrics (users, revenue, retention)

### Step 8: Generate Artifact
Create `idea_brief.md` following the contract format.

## Workflow Checklist

Copy and track progress:
```
Idea Brief Progress:
- [ ] Core concept extracted
- [ ] One-line pitch crafted
- [ ] Problem statement defined
- [ ] Target customer identified
- [ ] Solution hypothesis documented
- [ ] Key assumptions listed
- [ ] Success metrics defined
- [ ] idea_brief.md created
```

## Output Format

Create `idea_brief.md` in the project directory following the contract at `contracts/idea_brief.md`.

Required sections:
- Working Title
- One-Line Pitch
- Problem Statement
- Target Customer
- Solution Hypothesis
- Key Assumptions (3+ items)
- Success Metrics (2+ items)
- Created date
- Status (set to "Draft")

## Edge Cases

**Vague idea input:**
- Ask specific questions: "Who has this problem?" "How are they solving it today?"
- Offer examples to ground the discussion
- It's okay to create a draft brief with explicit unknowns marked

**Multiple ideas in one:**
- Suggest focusing on one core idea
- If user insists, create separate briefs for each
- Help prioritize which to validate first

**Solution-first thinking:**
- Gently redirect to problem-first framing
- Ask "What problem does this solve?" and "For whom?"
- Reframe features as jobs-to-be-done

**Existing product/company:**
- Adapt brief to focus on new feature or pivot
- Reference existing context where relevant
- Adjust assumptions to account for known factors

## References

- [brief_template.md](references/brief_template.md): Detailed template with field guidance
- [examples.md](references/examples.md): Sample idea briefs for reference
