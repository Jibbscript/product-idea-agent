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

## Outcome

`mvp_spec.md` is a scoped first version of the product, a chosen technical approach, and a one-sentence wedge that says why this product wins against the alternatives in `competitors.csv`. A finished spec is as notable for what it leaves out as for what it includes, since everything cut from v1 is listed as cut rather than quietly dropped.

## Inputs Required

- `idea_brief.md` (from idea-brief-creator)
- `competitors.csv` (from competitive-landscape) - for gap identification
- `icp.yaml` (from problem-segment) - for prioritization

## Who reads mvp_spec.md

gtm-channels lifts the positioning statement out of this file into its messaging and reads the platform choice to know which surface the launch lands on; risk-assessment reads the technical approach and the build-versus-buy decisions to find the technical risks; and validation-report describes the product from this file alone, without going back to the brief. None of them fills in a gap this spec leaves open.

That is why a platform choice left as "web or mobile, to be decided" reappears two skills later as an Execution Difficulty that scorecard-generator cannot score: risk-assessment has no stack to assess, so the dimension gets a guess.

## What mvp_spec.md Must Cover

### User Jobs
The jobs the target customer is hiring the product to do, drawn from the idea brief and the ICP:
- **Functional jobs**: Tasks the user is trying to complete
- **Emotional jobs**: How they want to feel
- **Social jobs**: How they want to be perceived

Each job is weighed by frequency (how often do they do this?), importance (how critical is it?), and satisfaction with current solutions (opportunity for improvement). The highest-priority job is the one the MVP is built around.

### MVP Scope
For each priority job, a decision about whether it is essential for the first paying customer, deferrable to v2, or explicitly excluded, expressed as:
- **P0 (Must Have)**: Product doesn't work without these
- **P1 (Should Have)**: Important but not launch-blocking
- **Won't Have**: Explicitly out of scope for v1

The "breadth vs depth" test settles most borderline calls:
- Breadth: Many features, basic implementation
- Depth: Few features, exceptional implementation
- **Recommendation**: Choose depth for MVP

### Technical Approach
The implementation strategy, decided along three axes:

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

The Build vs Buy Framework under MVP Principles below is the tiebreaker: custom work goes to the differentiator, everything else is bought.

### The Wedge
What makes this product different, in one sentence, using the positioning statement format:

For [target customer] who [need], [product name] is a [category] that [key benefit]. Unlike [alternatives], we [key differentiator].

The wedge is one of these types, and the spec names which:
- **Technology wedge**: New tech enables better solution
- **Experience wedge**: Dramatically better UX
- **Segment wedge**: Specialized for underserved segment
- **Price wedge**: Disruptive pricing model
- **Distribution wedge**: Unique channel access

### Competitive Advantage
What would be hard for competitors to copy once the product exists:
- Proprietary data or algorithms
- Network effects
- Switching costs
- Ecosystem/integrations
- Brand/trust
- Team expertise

A wedge gets a product in the door; the advantage is what keeps it there, and a spec that has the first without the second says so plainly.

### Success Criteria
Measurable targets across three horizons:
- **Validation metrics**: Signups, interviews, LOIs
- **Launch metrics**: Users, revenue, retention
- **Quality metrics**: NPS, completion rates

## How to Work

User jobs bound the scope, so they come first. Technical approach, the wedge, and competitive advantage are three readings of the same scope and need no order among them. Success criteria follow once scope and wedge are settled, because a target only means something against a defined product. The spec is done when a founder could hand it to an engineer and a designer and get the same v1 back from both.

## Constraints

The wedge is one sentence in the positioning format above. Everything cut from v1 is listed under Won't Have rather than omitted silently, so the reader knows it was considered. Every P0 feature ties back to a named user job. Success criteria are numeric and time-boxed. The finished `mvp_spec.md` conforms to `contracts/mvp_spec.md`.

## What a strong mvp_spec.md looks like

The test is whether an engineer could estimate a first sprint from it and a marketer could write a landing page from it, using the same document, without either asking a question the other would answer differently. A strong spec passes because the P0 list is short enough to ship and the Won't Have list is as specific as the P0 list; an unstated exclusion is the scope that creeps back in during the first sprint, since nobody can point to the line that ruled it out. A weak spec lists features, never says what is deliberately out, and describes the platform as a menu.

The Won't Have list is the clearest evidence a reader gets that the founder knows what the product is, and it is the founder who has to live with the cut.

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
