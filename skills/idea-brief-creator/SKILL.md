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

## Outcome

A finished `idea_brief.md` states in plain language what the product does, who it is for, and what problem it solves, then commits to a one-sentence pitch, a short problem statement, a target-customer hypothesis, a solution hypothesis, the assumptions the idea depends on, and the metrics that would show it is working.

## Inputs Required

- Raw idea description (text, conversation, or notes)
- Optional: target market hints, problem observations, existing research

## What idea_brief.md Must Cover

### Core Concept
The brief opens with the three facts the rest of the pipeline hangs on:
- What the product/service does
- Who it's for (initial hypothesis)
- What problem it solves

When any of these is unclear from the user's input, a clarifying question is worth more than a guess, because every downstream skill inherits whatever is written here.

### One-Line Pitch
A single sentence carrying the value delivered, the target customer, and the key differentiator when one is known. The pattern "[Product] helps [customer] [achieve outcome] by [method]." fits most ideas; the test of a good pitch is that a stranger could repeat it back after hearing it once.

### Problem Statement
Two or three sentences that describe the pain point clearly, explain why existing solutions fall short, and hint at how severe and how frequent the problem is. Severity and frequency matter here because demand-signals and problem-segment will later test exactly those claims.

### Target Customer
The initial hypothesis about who has this problem most acutely, with whatever demographic or firmographic hints and behavioral indicators the input supports. This is a starting point for problem-segment, not a final ICP, so a narrow guess that can be tested beats a broad one that cannot.

### Solution Hypothesis
How the product solves the problem, its key capabilities or features at a high level, and why this approach might work where others have not. The reasoning matters as much as the feature list, since it is what solution-wedge will later sharpen into a wedge.

### Key Assumptions
Three to five assumptions that must be true for the idea to succeed, spanning the customer (do they have this problem?), the solution (will this solve it?), the market (will they pay?), and execution (can we build it?). Each is phrased so that research could show it to be false; an assumption nobody could disprove is not carrying any risk and does not belong on the list.

### Success Metrics
Two or three measurable outcomes, split between validation-phase metrics (signups, interviews, LOIs) and launch-phase metrics (users, revenue, retention). A metric earns its place when a number attached to it would change what the founder does next.

## How to Work

The pitch and the problem statement are both rewrites of the core concept, so neither can be finished until the concept is settled. The target customer, the assumptions, and the metrics each draw on the concept independently and need no particular order among themselves.

## Constraints

All seven elements above appear in the brief, since each one is an input a later skill reads by name. The pitch is one sentence. Every assumption is stated so that evidence could prove it false. Every metric is measurable rather than aspirational. Where the input leaves a section unknown, the section says so explicitly instead of filling the gap with a plausible guess, because everything in the brief is a hypothesis to be tested downstream and an honest unknown is more useful than a confident guess. The finished `idea_brief.md` conforms to `contracts/idea_brief.md`.

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

## Working the Brief

When the raw idea arrives with links, notes or a call transcript, hand the reading to sub-agents in parallel and keep composing the brief while they report back. The brief is finished once each of the seven fields holds one testable claim that could be handed to the next skill without a follow-up question, and more research here is diminishing returns, because demand-signals and problem-segment are the steps that test those claims against real evidence. The brief separates what the founder said from what you inferred, so an inference is marked as an inference; an assumption written as though it were established fact is exactly the failure this separation exists to prevent.

The most valuable thing you can add is the non-obvious reframing, the sharper problem hiding behind the one the founder described. `idea_brief.md` is read by every other skill in this pack before it does its own work, so a vague target customer here becomes a vague ICP, a vague market boundary and a vague scorecard. The one-line pitch is the headline and opens the brief, so a reader who stops after it still knows what is being built and for whom.

The deliverable is the drafted brief, so only ask the user when a gap genuinely blocks it, such as who hurts today and what they do instead, and draft the pitch, assumptions and metrics without asking. Before writing `idea_brief.md`, re-read the assumptions and confirm each one is falsifiable by a later step; anything that cannot be tested belongs in the problem statement instead.

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
