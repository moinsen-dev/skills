# MoSCoW Prioritization Framework

## Overview

MoSCoW is a prioritization technique used to reach a common understanding about the importance of features, requirements, or deliverables. The acronym stands for:

- **M**ust have
- **S**hould have
- **C**ould have
- **W**on't have (this time)

This framework helps teams focus on delivering maximum value within constraints by explicitly categorizing features by priority.

## Categories Explained

### Must-Have (Critical for Success)

**Definition**: Features absolutely essential for the product to function or deliver its core value proposition.

**Criteria for Must-Have**:
- ✅ Without this, the product cannot launch or is useless
- ✅ Legal/regulatory requirement (compliance, safety, privacy)
- ✅ Core differentiator - what makes this product unique
- ✅ Foundational dependency - blocks all other features
- ✅ Non-negotiable business requirement

**Examples**:
- For an e-commerce site: Product catalog, shopping cart, checkout, payment processing
- For a visual PID tool: Visualization display, PID import, basic editing
- For a social network: User profiles, friend connections, posting
- For a SaaS app: Authentication, data persistence, core workflow

**Questions to Ask**:
- "Can we launch without this?"
- "Does the product still deliver value without this?"
- "Is this legally required?"
- "Does this define what makes us different from competitors?"

**Red Flags** (might not actually be Must-Have):
- ❌ "This would be nice to have" → Could-Have
- ❌ "Users might want this" → Should-Have (validate first)
- ❌ "We've always had this" → Challenge assumption
- ❌ "It's easy to build" → Ease doesn't determine priority

### Should-Have (Important but Not Critical)

**Definition**: Features that are important and valuable but not absolutely essential for launch. Product can function without them, but with reduced effectiveness.

**Criteria for Should-Have**:
- ✅ Significant value add, enhances core experience
- ✅ High user demand or expected by users
- ✅ Competitive parity (competitors have it, users expect it)
- ✅ Improves efficiency or usability meaningfully
- ✅ Reduces risk or future technical debt

**Examples**:
- For an e-commerce site: Product reviews, wishlist, order history
- For a visual PID tool: Multiple diagram layouts, export to multiple formats
- For a social network: Direct messaging, notifications, photo albums
- For a SaaS app: Team collaboration, advanced search, audit logs

**Questions to Ask**:
- "Does this significantly enhance the core value?"
- "Would users be disappointed if this is missing?"
- "Does this give us competitive parity?"
- "Can we launch first and add this later based on feedback?"

**Distinction from Must-Have**:
- Must-Have: "We cannot launch without this"
- Should-Have: "We should have this for a strong launch, but can add it later if needed"

### Could-Have (Nice-to-Have)

**Definition**: Features that would be nice additions but have minimal impact if left out. These are desirable but not necessary.

**Criteria for Could-Have**:
- ✅ Small improvement to user experience
- ✅ Nice polish or convenience feature
- ✅ Low cost to implement if time permits
- ✅ Minor differentiation, not core to value prop
- ✅ Aesthetic improvements, branding touches

**Examples**:
- For an e-commerce site: Dark mode, product comparison tool, gift wrapping
- For a visual PID tool: Themes/skins, animation effects, keyboard shortcuts
- For a social network: Custom emoji, profile themes, post scheduling
- For a SaaS app: Dashboard widgets, custom reports, email digests

**Questions to Ask**:
- "Would users notice if this is missing?"
- "Is this polish or substance?"
- "Can we add this in a future update without impact?"
- "Does this meaningfully move metrics (engagement, retention, revenue)?"

**When to Promote to Should-Have**:
- User research shows strong demand
- Competitive pressure (everyone else has it)
- Low effort, high delight (quick win)

### Won't-Have (Explicitly Out of Scope)

**Definition**: Features explicitly deferred to a future release or permanently out of scope. Important to document to manage expectations.

**Criteria for Won't-Have**:
- ✅ Not aligned with current milestone goals
- ✅ Too complex/risky for current scope
- ✅ Requires dependencies not yet built
- ✅ Low ROI for current phase
- ✅ Future innovation, not current need

**Examples**:
- For an e-commerce site (MVP): Mobile app, AR try-on, live chat support
- For a visual PID tool (MVP): Real-time collaboration, mobile, plugin marketplace
- For a social network (MVP): Video calls, stories, marketplace
- For a SaaS app (MVP): SSO, enterprise features, white-labeling

**Questions to Ask**:
- "Why are we saying no to this?"
- "When might we revisit this?"
- "What would need to change for this to become Must/Should?"

**Benefits of Explicit Won't-Have**:
- Prevents scope creep
- Manages stakeholder expectations
- Focuses team on priorities
- Provides clear roadmap for future phases

## Applying MoSCoW to Features

### Step 1: List All Features

Start with comprehensive list from PID/PRD:
```
1. User authentication
2. Product catalog
3. Shopping cart
4. Payment processing
5. Product reviews
6. Wishlist
7. Dark mode
8. Mobile app
9. AR try-on
10. Live chat support
```

### Step 2: Apply Decision Criteria

For each feature, ask:
1. **Can we launch without this?**
   - No → Must-Have
   - Yes → Continue to question 2

2. **Does this significantly enhance core value?**
   - Yes → Should-Have
   - No → Continue to question 3

3. **Is this a nice improvement but not essential?**
   - Yes → Could-Have
   - No → Won't-Have

### Step 3: Categorize Features

```markdown
**Must-Have (Critical for MVP)**:
1. User authentication - Required for accounts
2. Product catalog - Core functionality
3. Shopping cart - Essential workflow
4. Payment processing - Required to sell

**Should-Have (Important Enhancement)**:
1. Product reviews - High user value, competitive parity
2. Wishlist - Requested feature, enhances retention

**Could-Have (Nice Polish)**:
1. Dark mode - Nice UX improvement, low priority

**Won't-Have (Deferred to Phase 2)**:
1. Mobile app - Too complex for MVP
2. AR try-on - High risk, unclear ROI
3. Live chat support - Resource intensive, can add later
```

### Step 4: Validate Categories

Review with team/stakeholders:
- "Do we agree these Must-Haves are truly required for launch?"
- "Are we comfortable deferring the Won't-Haves?"
- "Should any Should-Haves be promoted to Must-Have based on business needs?"

## Common Pitfalls

### Everything is Must-Have

**Problem**: Team marks 80% of features as Must-Have, defeating the purpose of prioritization.

**Solution**:
- Apply strict criteria: "Can we launch without this?"
- Set target distribution: Aim for 20-30% Must-Have, 30-40% Should-Have, 20-30% Could-Have, 20-30% Won't-Have
- Force trade-offs: "If we only had time for 5 features, which 5?"

### Confusing Ease with Priority

**Problem**: Marking easy features as Must-Have because "it's quick to build."

**Solution**:
- Ease affects sequencing (when to build), not priority (whether to build)
- A quick Could-Have is still less important than a hard Must-Have
- Use separate complexity scoring (S/M/L) alongside MoSCoW

### Ignoring Dependencies

**Problem**: Marking a feature Must-Have when its dependency is Could-Have.

**Solution**:
- Map dependencies first
- If Feature B depends on Feature A, B cannot have higher priority than A
- Use Dependency Mapping framework alongside MoSCoW

### Scope Creep Over Time

**Problem**: Could-Haves get promoted to Must-Haves mid-sprint without justification.

**Solution**:
- Document why each feature is in its category
- Require formal review to change categories
- Revisit MoSCoW analysis at each milestone, not mid-sprint

## MoSCoW in Practice

### Example 1: Visual PID Tool (ThinkCanvas)

**Must-Have (20% of features)**:
- Visual PID display (mind map layout)
- AI chat integration with canvas
- Import PID from markdown
- Basic persistence (save/load)
- Node editing (add/edit/delete)

**Rationale**: Without these, it's not a "visual PID tool" - it's just a text editor. These define the core value proposition.

**Should-Have (35% of features)**:
- Export to multiple formats (markdown, PNG, PDF)
- Multiple diagram layouts (Kanban, sticky notes)
- Semantic zoom (AI-generated summaries)
- Voice commands
- Search functionality

**Rationale**: These significantly enhance the experience and prove differentiation, but MVP can launch with chat-only commands and one export format.

**Could-Have (25% of features)**:
- Dark mode
- Keyboard shortcuts
- Animation effects
- Breadcrumb navigation
- Diagram templates

**Rationale**: Nice polish that improves UX but doesn't change core value. Can be added based on user feedback.

**Won't-Have (20% of features)**:
- Real-time collaboration
- Mobile app
- Plugin marketplace
- Version history
- Team management

**Rationale**: Too complex for MVP, unclear demand, can validate core concept first before investing in these.

### Example 2: Mid-Sprint Re-Evaluation

**Scenario**: Team is 60% through MVP sprint. User research shows voice commands are highly desired.

**Question**: Should "Voice commands" be promoted from Should-Have to Must-Have?

**Analysis**:
- ✅ **Evidence**: User interviews show 8/10 users request voice
- ✅ **Value**: Core differentiator, competitive advantage
- ⚠️ **Risk**: Not yet proven technically, could be buggy
- ⚠️ **Timeline**: Would delay MVP by 2 weeks

**Decision Process**:
1. Can we launch without voice and add it in v1.1? → Yes
2. Would users still pay for chat-only version? → 6/10 said yes
3. Is 2-week delay acceptable for business? → No, need to launch by deadline

**Recommendation**: Keep as Should-Have, launch MVP with chat, add voice in v1.1 (4 weeks post-launch).

## Integration with Other Frameworks

### MoSCoW + Dependency Mapping

**Dependency Mapping** categorizes by sequence (Foundation → Validation → Differentiation → Polish).

**MoSCoW** categorizes by business priority (Must → Should → Could → Won't).

**Combined Usage**:
1. Use Dependency Mapping to identify what CAN be built (sequence)
2. Use MoSCoW to identify what SHOULD be built (priority)
3. Intersection = Recommended roadmap

**Example**:
```
Foundation Layer:
├─ Persistence (Must-Have) → Build Week 1
├─ Authentication (Should-Have) → Build Week 2
└─ Analytics (Could-Have) → Defer to Phase 2

Validation Layer:
├─ Import PID (Must-Have) → Build Week 1
└─ Export multiple formats (Should-Have) → Build Week 3

Differentiation Layer:
├─ Voice commands (Should-Have) → Build Week 4
└─ AI semantic zoom (Must-Have) → Build Week 2
```

**Outcome**: Sequence work by dependency layer, prioritize within each layer by MoSCoW.

### MoSCoW + ICE Score

**ICE Score** = Impact × Confidence ÷ Ease (quantitative prioritization).

**MoSCoW** = Qualitative categorization.

**Combined Usage**:
1. Use MoSCoW to filter scope (only Must + Should considered for MVP)
2. Use ICE Score to sequence within Must-Have and Should-Have categories

**Example**:
```
Must-Have Features:
├─ Persistence (Impact: 9, Confidence: 90%, Ease: 3 days) → ICE: 270
├─ Import PID (Impact: 10, Confidence: 80%, Ease: 2 days) → ICE: 400 ← Build first
└─ AI integration (Impact: 10, Confidence: 60%, Ease: 5 days) → ICE: 120

Should-Have Features:
├─ Voice commands (Impact: 8, Confidence: 40%, Ease: 7 days) → ICE: 46
└─ Export formats (Impact: 6, Confidence: 90%, Ease: 1 day) → ICE: 540 ← Quick win
```

**Outcome**: Build high-ICE Must-Haves first, sprinkle in high-ICE Should-Haves for momentum.

## Summary

**MoSCoW Framework Benefits**:
- ✅ Forces explicit prioritization
- ✅ Manages scope and expectations
- ✅ Provides clear rationale for decisions
- ✅ Prevents scope creep
- ✅ Aligns team on what matters

**Key Principles**:
- Must-Have = "Cannot launch without"
- Should-Have = "Important but can add later"
- Could-Have = "Nice polish"
- Won't-Have = "Explicitly deferred"

**Best Practice**:
- Aim for 20-30% Must-Have to avoid everything being critical
- Document rationale for each category
- Revisit at each milestone, not mid-sprint
- Combine with Dependency Mapping for sequencing
