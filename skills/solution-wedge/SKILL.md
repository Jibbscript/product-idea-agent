---
name: solution-wedge
description: Defines MVP scope, technical approach, and key differentiation strategy. Use when determining what to build first, scoping an MVP, or positioning against alternatives.
license: Apache-2.0
metadata:
  author: product-idea-agent
  pack: product-idea-agent
allowed-tools: Read Write WebSearch
---

# Solution Wedge Definition

Defines MVP scope, technical approach, and differentiation strategy.

## Quick Start

Given prior artifacts, define the solution:
1. Identify critical user jobs to address
2. Define minimum feature set for MVP
3. Specify technical approach
4. Articulate differentiation
5. Output `mvp_spec.md`

## Inputs Required

- `idea_brief.md` (from idea-brief-creator)
- `competitors.csv` (from competitive-landscape) - for gap identification
- `icp.yaml` (from problem-segment) - for prioritization

## Step-by-Step Workflow

### Step 1: Map User Jobs

From the idea brief and ICP, identify:
- **Functional jobs**: Tasks the user is trying to complete
- **Emotional jobs**: How they want to feel
- **Social jobs**: How they want to be perceived

Prioritize by:
- Frequency (how often do they do this?)
- Importance (how critical is it?)
- Satisfaction with current solutions (opportunity for improvement)

### Step 2: Define MVP Scope

For each priority job, determine:
- Is it essential for first paying customer?
- Can we defer it to v2?
- Should we explicitly exclude it?

Categorize features:
- **P0 (Must Have)**: Product doesn't work without these
- **P1 (Should Have)**: Important but not launch-blocking
- **Won't Have**: Explicitly out of scope for v1

Apply the "breadth vs depth" test:
- Breadth: Many features, basic implementation
- Depth: Few features, exceptional implementation
- **Recommendation**: Choose depth for MVP

### Step 3: Specify Technical Approach

Define the implementation strategy:

**Platform choice:**
- Web (desktop-first, mobile-responsive, PWA)
- Mobile (iOS, Android, cross-platform)
- Desktop (native, Electron)
- API-first (headless, integrations)

**Technology stack:**
- Frontend framework
- Backend language/framework
- Database
- Infrastructure/hosting

**Build vs Buy decisions:**
- What components to build custom?
- What to use off-the-shelf?
- What third-party services to integrate?

### Step 4: Articulate the Wedge

Define what makes you different:

**Positioning statement format:**
For [target customer] who [need], [product name] is a [category] that [key benefit]. Unlike [alternatives], we [key differentiator].

**Types of wedges:**
- **Technology wedge**: New tech enables better solution
- **Experience wedge**: Dramatically better UX
- **Segment wedge**: Specialized for underserved segment
- **Price wedge**: Disruptive pricing model
- **Distribution wedge**: Unique channel access

### Step 5: Identify Competitive Advantage

What's hard for competitors to copy?
- Proprietary data or algorithms
- Network effects
- Switching costs
- Ecosystem/integrations
- Brand/trust
- Team expertise

### Step 6: Define Success Criteria

Set measurable targets:
- **Validation metrics**: Signups, interviews, LOIs
- **Launch metrics**: Users, revenue, retention
- **Quality metrics**: NPS, completion rates

### Step 7: Generate Artifact

Create `mvp_spec.md` following the contract format.

## Workflow Checklist

```
Solution Wedge Progress:
- [ ] User jobs mapped and prioritized
- [ ] MVP scope defined (P0, P1, Won't Have)
- [ ] Technical approach specified
- [ ] Differentiation articulated
- [ ] Competitive advantage identified
- [ ] Success criteria defined
- [ ] mvp_spec.md created
```

## Output Format

Create `mvp_spec.md` following the artifact contract in `contracts/mvp_spec.md`.

Required sections:
- Product vision (north star)
- MVP scope (P0, P1, Won't Have)
- Technical approach (platform, stack, dependencies)
- Differentiation and positioning statement
- Timeline (phases with milestones)
- Success criteria
- Open questions

## Working the Wedge

Platform options, build-versus-buy components and competitor gap research are separable, so delegate them to sub-agents working concurrently while you keep shaping the P0 list yourself. The technical approach needs enough detail for a builder to start rather than an architecture document, so once the stack choice stops changing the P0 list, further design work is diminishing returns. A claimed gap in a competitor's product is only as good as its source, so gaps confirmed on a live product or pricing page are marked sourced and the rest are flagged unverified rather than scoping an MVP around a rumor.

The interesting question in scoping is which beloved feature to cut, and one contrarian Won't Have with a reason attached is worth more than a longer P0 list. `mvp_spec.md` is read downstream by gtm-channels for positioning and by risk-assessment for technical risk, so a P0 item left vague resurfaces as a risk nobody can score. Lead with the wedge itself, one sentence on what gets built first and why it wins, ahead of the feature tables.

The deliverable is `mvp_spec.md`; writing code, choosing a repository layout or standing up infrastructure is not part of this skill. Before you finalize, verify the draft against the ICP so that every P0 feature maps to a job the primary segment actually named.

## Research Query Templates

### Technical Research
- "[category] tech stack 2024"
- "[problem] API"
- "[solution] implementation"
- "best [technology] for [use case]"

### Competitor Gap Analysis
- "[competitor] missing features site:reddit.com"
- "[competitor] wish list"
- "[competitor] compared to"

### Market Positioning
- "[category] positioning examples"
- "[category] differentiation"
- "how to position against [competitor]"

## MVP Principles

### The "Mom Test" for Features
Would a customer's mom understand why this feature matters?
- If yes → likely P0
- If needs explanation → likely P1
- If technical/internal → likely Won't Have

### The "One Sentence" Test
Can you describe the MVP in one sentence?
- "It lets you [action] in [context]"
- If you need "and" → you might be building too much

### The "10x" Rule
Is this feature 10x better than alternatives?
- If 10x → include in MVP
- If 2x → consider deferring
- If same → skip unless table stakes

### Build vs Buy Framework

| Build Custom | Buy/Integrate |
|--------------|---------------|
| Core differentiator | Commodity functionality |
| Competitive advantage | Time-to-market critical |
| Unique requirements | Standard implementation |
| Control required | Cost-effective alternative |

## Edge Cases

**Too many must-haves:**
- Force rank P0 features
- Ask: "Would users pay with only this subset?"
- Consider multiple MVP phases

**No clear differentiator:**
- Focus on segment specialization
- Consider execution/experience wedge
- May need to rethink idea

**Technical uncertainty:**
- Flag as risk
- Prototype before committing
- Consider phased approach

**Platform uncertainty:**
- Start with highest-impact platform
- Design for eventual multi-platform
- Don't try to launch everywhere at once

## References

- [mvp_principles.md](references/mvp_principles.md): MVP philosophy and anti-patterns
