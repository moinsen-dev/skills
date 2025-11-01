# Dependency Mapping Framework

## Overview

Dependency Mapping is a sequencing framework that organizes features into hierarchical layers based on their dependencies and impact on the product. This framework helps teams understand what must be built first and what can be built later.

**Core Principle**: Build in layers, where each layer depends on the previous layer's stability.

## The Four Layers

### Layer 1: Foundation (Must Work First)

**Definition**: Core infrastructure, data models, and architectural decisions that everything else depends on. If the foundation is unstable, everything built on top will be unstable.

**Characteristics**:
- **Blocking**: All other features depend on these
- **Stability required**: Must be solid before building on top
- **Hard to change**: Changes require refactoring everything
- **Low user visibility**: Users don't directly see these, but feel their absence
- **Technical debt risk**: Cutting corners here compounds over time

**Examples**:
- **Data models**: User schema, product schema, core entities
- **Infrastructure**: Database setup, API architecture, authentication system
- **Core services**: Payment processing, file storage, caching layer
- **Architecture decisions**: Monolith vs microservices, SQL vs NoSQL, REST vs GraphQL
- **Developer tools**: Build system, deployment pipeline, testing framework

**Questions to Identify Foundation**:
- "If this breaks, does everything else break?"
- "How many features depend on this working correctly?"
- "How hard would it be to change this later?"
- "Is this an architectural decision or implementation detail?"

**Red Flags** (might not be Foundation):
- ❌ "This is technically complex" (complexity ≠ foundational)
- ❌ "We need this eventually" (timing matters)
- ❌ "This is important to users" (that's Validation or Differentiation)

**Example: Visual PID Tool (ThinkCanvas)**

Foundation Layer:
- ✅ Node/Edge data model (defines how PIDs are structured)
- ✅ React Flow integration (core visualization library)
- ✅ AI chat API integration (enables all AI features)
- ✅ WebSocket connection (real-time updates)
- ✅ Basic persistence (SQLite setup, save/load logic)

**Why these are Foundation**:
- Data model: Every feature needs to know how PIDs are structured
- React Flow: All visualization features depend on this working
- AI API: All intelligent features (semantic zoom, voice, commands) depend on this
- WebSocket: Real-time updates for all features
- Persistence: Multi-session workflows depend on data surviving restarts

### Layer 2: Validation (Proves Concept)

**Definition**: Minimum features required to demonstrate the core value proposition and validate key assumptions with real users.

**Characteristics**:
- **Value demonstration**: Users can see the "why" behind the product
- **Assumption testing**: Validates core beliefs (users want this, tech works, concept is better than alternatives)
- **MVP-ready**: Enough to launch and get feedback
- **User-facing**: Visible, usable features
- **Risk reduction**: Proves viability before investing in full build

**Examples**:
- **Core workflows**: Import data → visualize → export (proves end-to-end)
- **Unique features**: The "aha!" moment that shows value
- **Basic interactions**: Enough UI to test the concept
- **Simple use cases**: Cover the primary user journey
- **Feedback mechanisms**: Ways to learn from users

**Questions to Identify Validation**:
- "What's the minimum set of features to prove this concept works?"
- "What do users need to experience the 'aha!' moment?"
- "What assumptions are we testing with real users?"
- "Can we launch with just Foundation + Validation?"

**Validation vs Foundation**:
- Foundation: What the product is built on (technical)
- Validation: What users experience to understand value (functional)

**Example: Visual PID Tool (ThinkCanvas)**

Validation Layer:
- ✅ Import PID from markdown (get user data in)
- ✅ Mind map visualization (show visual representation)
- ✅ AI chat with canvas sync (demonstrate AI manipulation)
- ✅ Basic node editing (add/edit/delete nodes)
- ✅ Export to markdown (get data out)

**Why these are Validation**:
- Import → visualize → export proves "visual PID > text PID" assumption
- AI chat + canvas sync proves "AI can help shape PIDs visually"
- Basic editing proves users can manipulate visual PIDs
- Together, these demonstrate core value proposition

**What's NOT Validation** (even if valuable):
- ❌ Voice commands (Interface choice, not core value)
- ❌ Multiple diagram layouts (Enhancement, not proof of concept)
- ❌ Dark mode (Polish, doesn't validate concept)

### Layer 3: Differentiation (The Unique Magic)

**Definition**: Features that set the product apart from competitors and define its unique identity. These are the "wow" features that make users choose your product over alternatives.

**Characteristics**:
- **Competitive advantage**: "We're the only ones who..."
- **Unique value**: Not available elsewhere
- **Innovation**: Novel approach or technology
- **Brand identity**: What you're known for
- **Strategic**: Defines market positioning

**Examples**:
- **Unique workflows**: Novel ways of accomplishing tasks
- **Advanced AI**: Capabilities competitors don't have
- **Performance**: 10x faster/better than alternatives
- **Integration**: Unique ecosystem connections
- **Experience**: Delightful interactions that define the brand

**Questions to Identify Differentiation**:
- "Why would users choose us over [competitor]?"
- "What can we do that no one else can?"
- "What makes this uniquely valuable?"
- "What's our unfair advantage?"

**Differentiation vs Validation**:
- Validation: Proves the basic concept works
- Differentiation: Proves we're better than alternatives

**Example: Visual PID Tool (ThinkCanvas)**

Differentiation Layer:
- ✅ Voice-driven interface (speak → UI morphs)
- ✅ Dynamic diagram morphing (mind map → Kanban based on conversation)
- ✅ AI semantic zoom with auto-summarization
- ✅ Context-aware AI suggestions (knows when to prompt for missing sections)
- ✅ Smooth visualization transitions

**Why these are Differentiation**:
- Voice + UI morphing: No other PID tool has this
- Dynamic diagram selection: Adapts to user's thinking mode
- AI semantic zoom: Intelligent abstraction levels
- Together: "Feel like working with invisible expert consultant"

**What's NOT Differentiation** (even if important):
- ❌ Export to PDF (Table stakes, not unique)
- ❌ Dark mode (Everyone has this)
- ❌ Keyboard shortcuts (Expected, not differentiating)

### Layer 4: Polish (Makes It Delightful)

**Definition**: Improvements that enhance user experience, add convenience, and make the product feel professional, but don't change the core functionality.

**Characteristics**:
- **UX refinement**: Smoother, faster, prettier
- **Convenience**: Shortcuts, preferences, customization
- **Aesthetics**: Visual design, animations, branding
- **Edge cases**: Handling rare scenarios gracefully
- **Quality of life**: Small improvements that add up

**Examples**:
- **UI polish**: Animations, loading states, error messages
- **Personalization**: Themes, preferences, customization
- **Shortcuts**: Keyboard shortcuts, quick actions
- **Performance**: Optimizations, caching
- **Accessibility**: Screen reader support, keyboard navigation

**Questions to Identify Polish**:
- "Does this change what the product does, or how it feels?"
- "Would users notice if this is missing on day 1?"
- "Can we add this after launch without impacting core experience?"
- "Is this about functionality or refinement?"

**When to Build Polish**:
- ✅ After Foundation, Validation, and Differentiation are stable
- ✅ When user feedback identifies specific pain points
- ✅ When quick wins boost morale or momentum
- ⏳ Not before proving core concept

**Example: Visual PID Tool (ThinkCanvas)**

Polish Layer:
- ⏳ Dark mode (visual preference)
- ⏳ Keyboard shortcuts (power user feature)
- ⏳ Animation effects (visual polish)
- ⏳ Breadcrumb navigation (convenience)
- ⏳ Diagram templates (quick start)
- ⏳ Undo/redo (quality of life)

**Why these are Polish**:
- Users can accomplish everything without these
- Nice refinements that improve experience
- Can be added iteratively based on feedback
- Don't change core value proposition

## Applying Dependency Mapping

### Step 1: List All Features

Start with comprehensive feature list from PID/PRD or feature matrix.

### Step 2: Identify Dependencies

For each feature, ask:
1. "What must exist before this can work?"
2. "What does this enable or unblock?"
3. "How many features depend on this?"

Map dependencies:
```
Feature A (Persistence)
├─ Blocks: Multi-session workflows
├─ Blocks: User accounts
└─ Blocks: Collaboration

Feature B (Import markdown)
├─ Depends on: Data model
├─ Enables: User testing
└─ Enables: Visualization features

Feature C (Voice commands)
├─ Depends on: AI API integration
├─ Depends on: Command parsing
└─ Optional enhancement to chat commands
```

### Step 3: Categorize by Layer

**Foundation** (must work first):
- Has many dependencies from other features
- Foundational technology or architecture
- Hard to change later

**Validation** (proves concept):
- Depends on Foundation
- Demonstrates core value to users
- Minimum viable feature set

**Differentiation** (unique magic):
- Depends on Foundation + Validation
- Sets product apart from competitors
- Strategic advantage

**Polish** (makes it delightful):
- Depends on everything else being stable
- Enhances experience, doesn't change functionality
- Can be added anytime

### Step 4: Sequence Work

Build in order:
1. **Foundation first**: Get infrastructure stable
2. **Validation next**: Prove concept works
3. **Differentiation after validation**: Build unique features
4. **Polish last**: Refine experience

Within each layer, prioritize by:
- Impact (what unlocks the most value?)
- Risk (what has highest uncertainty?)
- Quick wins (what's fast and valuable?)

### Example: ThinkCanvas Sequencing

**Week 1-2: Foundation**
- ✅ Data model stabilization
- ✅ SQLite persistence setup
- ✅ AI API integration testing
- ✅ React Flow configuration

**Goal**: Stable foundation to build on

**Week 3-4: Validation**
- ✅ Import markdown UI
- ✅ Mind map visualization
- ✅ AI chat with canvas sync
- ✅ Basic export

**Goal**: Prove "visual PID > text PID" with 5 users

**Week 5-7: Differentiation**
- ✅ Voice command integration (if validation succeeds)
- ✅ Dynamic diagram morphing
- ✅ AI semantic zoom
- ✅ Context-aware suggestions

**Goal**: Demonstrate unique value vs competitors

**Week 8+: Polish**
- ⏳ Dark mode
- ⏳ Keyboard shortcuts
- ⏳ Animations
- ⏳ Performance optimizations

**Goal**: Refine experience based on user feedback

## Common Patterns

### Pattern 1: Parallel Foundation Work

**Scenario**: Multiple foundation pieces can be built simultaneously.

**Strategy**:
- Identify independent foundation pieces
- Parallelize work across team members
- Define clear interfaces/contracts
- Integrate when stable

**Example**:
```
Week 1 (Parallel):
├─ Developer A: Data model + persistence
├─ Developer B: AI API integration
└─ Developer C: React Flow setup

Week 2 (Integration):
└─ All: Integrate components, fix interface issues
```

### Pattern 2: Validation Before Differentiation

**Scenario**: Uncertain whether differentiation feature is valued by users.

**Strategy**:
- Build minimum Validation layer first
- Test with 5-10 users
- Validate assumptions
- Only build Differentiation if validated

**Example**:
```
Assumption: "Users want voice commands"

Validation Approach:
1. Build chat-based commands first (Week 3)
2. Test with 10 users (Week 4)
3. Ask: "Would you pay more for voice instead of chat?"
4. Decide: If 8+ say yes → build voice (Week 5)
           If <5 say yes → defer voice, focus elsewhere
```

### Pattern 3: Quick Polish for Momentum

**Scenario**: Team morale low, need visible wins.

**Strategy**:
- Identify 1-2 quick Polish items (< 1 day each)
- Sprinkle into sprint alongside Foundation/Validation work
- Boost morale without derailing priorities

**Example**:
```
Week 2 Sprint:
├─ Foundation: SQLite persistence (3 days)
├─ Validation: Import UI (2 days)
└─ Polish: Dark mode (0.5 days) ← Quick win

Result: Foundation/Validation progresses, team sees visible improvement
```

### Pattern 4: Technical Spikes for Risky Foundation

**Scenario**: Foundation choice has high uncertainty (performance, scalability, integration).

**Strategy**:
- Run time-boxed technical spike (0.5-2 days)
- Test riskiest assumption
- Make informed decision
- Avoid wasted effort

**Example**:
```
Risk: "React Flow can't handle 500 nodes"

Spike (2 hours):
1. Create synthetic 500-node PID
2. Load into React Flow
3. Measure FPS, memory, render time
4. Decide:
   - If performance acceptable → proceed with React Flow
   - If performance poor → research alternatives (D3, Cytoscape)

Value: 2 hours prevents weeks of wasted work on wrong foundation
```

## Integration with MoSCoW

**MoSCoW** = What to build (business priority)
**Dependency Mapping** = When to build it (technical sequence)

**Combined Framework**:

```
Foundation Layer:
├─ Persistence (Must-Have) → Build first
├─ Authentication (Should-Have) → Build second
└─ Analytics (Could-Have) → Defer to Phase 2

Validation Layer:
├─ Import PID (Must-Have) → Build third
├─ Export multiple formats (Should-Have) → Build fourth
└─ Diagram templates (Could-Have) → Defer

Differentiation Layer:
├─ Voice commands (Should-Have) → Build fifth (if validated)
└─ AI semantic zoom (Must-Have) → Build sixth

Polish Layer:
├─ Dark mode (Could-Have) → Build seventh (or defer)
└─ Keyboard shortcuts (Could-Have) → Defer to Phase 2
```

**Process**:
1. **Categorize** by Dependency Layer (Foundation → Validation → Differentiation → Polish)
2. **Prioritize** within each layer using MoSCoW (Must → Should → Could → Won't)
3. **Sequence** work by layer, then priority within layer
4. **Validate** assumptions before committing to Differentiation features

## Gap Analysis Using Dependency Mapping

**Goal**: Identify what's missing in each layer to reach project goals.

**Process**:

1. **Map current state** to layers:
```
Foundation Layer: 80% complete
├─ ✅ Data model (100%)
├─ ✅ AI API (100%)
├─ ⏳ Persistence (30%)
└─ ✅ React Flow (90%)

Validation Layer: 40% complete
├─ ⏳ Import PID (0%)
├─ ✅ Visualization (60%)
├─ ✅ AI chat (50%)
└─ ⏳ Export (0%)

Differentiation Layer: 10% complete
├─ ⏳ Voice (0%)
├─ ⏳ Diagram morphing (0%)
└─ ⏳ Semantic zoom (30%)

Polish Layer: 5% complete
├─ ⏳ Dark mode (0%)
└─ ⏳ Shortcuts (10%)
```

2. **Identify blockers** in each layer:
```
Foundation Gaps:
- ⚠️ Persistence incomplete → Blocks multi-session testing

Validation Gaps:
- ⚠️ Import missing → Can't test with real user data
- ⚠️ Export missing → Can't save work

Differentiation Gaps:
- ⚠️ All features 0-30% done → Can't demonstrate unique value

Polish Gaps:
- ✅ Acceptable for MVP
```

3. **Prioritize gaps**:
```
Week 1 Priority: Foundation Gaps
└─ Complete persistence (blocks Validation testing)

Week 2 Priority: Validation Gaps
├─ Build import UI
└─ Build basic export

Week 3+ Priority: Differentiation Gaps
└─ After Validation proven, build unique features
```

## Anti-Patterns

### Anti-Pattern 1: Polish Before Validation

**Problem**: Building dark mode before proving core concept works.

**Why it's wrong**:
- Wastes time on features users may never use
- Delays validation of core assumptions
- If concept fails, polish is wasted effort

**Solution**: Always build Foundation → Validation → Differentiation → Polish

### Anti-Pattern 2: Differentiation Before Foundation

**Problem**: Building voice commands before persistence works.

**Why it's wrong**:
- Voice depends on AI API (Foundation)
- Can't test multi-session voice usage without persistence
- Unstable foundation makes Differentiation buggy

**Solution**: Ensure Foundation is stable before building advanced features

### Anti-Pattern 3: Skipping Validation

**Problem**: Building all Differentiation features without validating core concept.

**Why it's wrong**:
- May build wrong features (users don't want them)
- Wastes resources on unvalidated assumptions
- Delays learning what users actually need

**Solution**: Build minimum Validation layer, test with users, then build Differentiation

### Anti-Pattern 4: Everything is Foundation

**Problem**: Marking 80% of features as "foundational" to justify building them first.

**Why it's wrong**:
- Delays user testing and feedback
- Increases risk (building without validation)
- Confuses "technically interesting" with "foundational"

**Solution**: Apply strict criteria: "How many features block if this doesn't exist?"

## Summary

**Dependency Mapping Benefits**:
- ✅ Provides clear sequencing rationale
- ✅ Identifies blockers early
- ✅ Prevents building on unstable foundation
- ✅ Balances technical dependencies with user value
- ✅ Reduces wasted effort on wrong features

**Four Layers**:
1. **Foundation**: What everything else depends on (infrastructure, data models, architecture)
2. **Validation**: What proves the concept works (core workflows, MVP features)
3. **Differentiation**: What makes you unique (competitive advantages, innovation)
4. **Polish**: What makes it delightful (UX refinements, convenience, aesthetics)

**Key Principle**: Build in layers. Each layer must be stable before building the next.

**Best Practice**: Combine with MoSCoW for comprehensive prioritization (what + when to build).
