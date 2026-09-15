# MVP Principles

Philosophy, frameworks, and anti-patterns for defining minimum viable products.

## The MVP Philosophy

### What MVP Really Means

**Minimum**: The smallest thing that...
**Viable**: ...delivers real value to real users
**Product**: ...as a complete experience (not a demo)

### Common Misconceptions

| Misconception | Reality |
|---------------|---------|
| MVP is a prototype | MVP is a real product customers use |
| MVP is low quality | MVP is high quality with limited scope |
| MVP is for testing | MVP is for learning AND generating value |
| MVP is version 0.1 | MVP is version 1.0 of a smaller vision |

### The Skateboard Model

Classic MVP progression:

```
❌ Wrong approach (parts of a car):
[Wheel] → [Chassis] → [Frame] → [Body] → [Car]
Each step delivers no value until the end

✅ Right approach (transportation value):
[Skateboard] → [Scooter] → [Bike] → [Motorcycle] → [Car]
Each step delivers complete value at different scales
```

## Feature Prioritization Frameworks

### MoSCoW Method

| Category | Criteria | Action |
|----------|----------|--------|
| **Must Have** | Product fails without it | Build for MVP |
| **Should Have** | Important but not critical | Phase 2 |
| **Could Have** | Nice to have | Backlog |
| **Won't Have** | Explicitly out of scope | Document |

### RICE Scoring

Score each feature:
- **R**each: How many users affected? (1-10)
- **I**mpact: How much does it help? (1-3)
- **C**onfidence: How sure are we? (0.5-1.0)
- **E**ffort: How much work? (person-weeks)

**Score = (Reach × Impact × Confidence) / Effort**

Prioritize by highest score.

### Value vs Complexity Matrix

```
                High Value
                    |
    Quick Wins      |     Major Projects
    [DO FIRST]      |     [PLAN CAREFULLY]
                    |
--------------------|--------------------
                    |
    Fill-ins        |     Time Sinks
    [DO LATER]      |     [AVOID]
                    |
                Low Value

        Low Effort ←——→ High Effort
```

## The Wedge Strategy

### Why Wedges Matter

You can't compete on everything at once. A wedge is:
- A focused point of differentiation
- An entry point into a larger market
- A defensible position to build from

### Types of Wedges

#### 1. Technology Wedge
New technology enables a better solution.

**Examples**:
- GPT-3 enables AI writing assistants
- WebGL enables browser-based 3D
- Edge computing enables real-time processing

**When to use**: Technology just became possible/accessible

#### 2. Experience Wedge
Dramatically better user experience.

**Examples**:
- Stripe's simple API vs. legacy payment processors
- Linear's speed vs. Jira's complexity
- Notion's flexibility vs. rigid alternatives

**When to use**: Incumbent products are clunky/frustrating

#### 3. Segment Wedge
Specialized for an underserved segment.

**Examples**:
- Gusto for SMB payroll (vs. ADP for enterprise)
- Webflow for designers (vs. WordPress for everyone)
- Brex for startups (vs. traditional corporate cards)

**When to use**: General solutions don't fit a specific need

#### 4. Price Wedge
Disruptive pricing enables new use cases.

**Examples**:
- Canva vs. Adobe (10x cheaper)
- Zoom vs. WebEx (free tier)
- Mailchimp vs. Marketo (pay-as-you-go)

**When to use**: High prices are blocking adoption

#### 5. Distribution Wedge
Unique access to customers.

**Examples**:
- Shopify apps (built-in distribution)
- Salesforce AppExchange
- Browser extensions

**When to use**: You have unique channel access

## Positioning Framework

### Positioning Statement Template

```
For [target customer]
Who [statement of need or opportunity]
[Product name] is a [product category]
That [key benefit/reason to buy]
Unlike [primary competitive alternative]
Our product [statement of primary differentiation]
```

### Example Positioning Statements

**Slack**:
For teams who need to communicate
Slack is a business communication platform
That makes work life simpler, more pleasant, and more productive
Unlike email
Slack reduces information overload with organized channels

**Notion**:
For teams who need to organize knowledge
Notion is an all-in-one workspace
That combines notes, wikis, and databases
Unlike separate tools for each function
Notion provides flexibility to build custom workflows

## MVP Anti-Patterns

### Anti-Pattern 1: Feature Creep
**Symptom**: "While we're at it, let's also add..."
**Solution**: Strict prioritization, say no more often

### Anti-Pattern 2: Premature Optimization
**Symptom**: Building for 10x scale before proving value
**Solution**: Build for 10 users first, scale when needed

### Anti-Pattern 3: Perfectionism
**Symptom**: Delaying launch until everything is perfect
**Solution**: Ship when core value works, iterate based on feedback

### Anti-Pattern 4: Building for Everyone
**Symptom**: Trying to serve all use cases
**Solution**: Pick one segment, delight them, then expand

### Anti-Pattern 5: Copycat MVP
**Symptom**: Just rebuilding competitor features
**Solution**: Focus on your unique wedge, not feature parity

### Anti-Pattern 6: Invisible MVP
**Symptom**: Building backend before any user-facing product
**Solution**: Build the thinnest vertical slice end-to-end

## Technical Approach Guidelines

### Technology Selection Criteria

| Factor | Weight | Questions |
|--------|--------|-----------|
| Team expertise | High | What do we know? |
| Time to market | High | How fast can we ship? |
| Scalability | Medium | Can it grow with us? |
| Ecosystem | Medium | Are there helpful tools/libraries? |
| Hiring | Low (for MVP) | Can we hire for this later? |

### Build vs Buy Decision Tree

```
Is this your core differentiator?
├── Yes → Build custom
└── No → Does a good solution exist?
    ├── Yes → Buy/integrate
    └── No → Is it complex?
        ├── Yes → Simplify requirements, then buy
        └── No → Build simple version
```

### Platform Selection

| Platform | Best For | Avoid For |
|----------|----------|-----------|
| Web | B2B, content, complex UI | Offline, hardware access |
| iOS | Consumer premium, payments | Low-price, global reach |
| Android | Global reach, emerging markets | Premium positioning |
| Desktop | Power users, local data | Casual users, mobile-first |
| API | Developer tools, integrations | Consumer products |

## Success Criteria Examples

### Validation Phase (Pre-Launch)
- 50 user interviews completed
- 100 email waitlist signups
- 5 letters of intent (LOIs)
- 3 design partners confirmed

### Launch Phase (First 90 Days)
- 1,000 signups
- 100 active weekly users
- 10 paying customers
- $1,000 MRR
- NPS > 30

### Growth Phase (First Year)
- 10,000 users
- 500 paying customers
- $50,000 MRR
- NRR > 100%
- CAC payback < 12 months
