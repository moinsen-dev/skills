# Feature Matrix Template

## Instructions

This template helps you track feature status, priorities, and dependencies for goal-driven project navigation.

**How to use this template**:

1. Copy this template to your project
2. Fill in the Project Info section
3. List all features in the appropriate sections
4. Update status and progress as you work
5. Use with goal-navigator skill for prioritization guidance

**Feature Status Values**:
- ✅ **Completed** (100%): Feature is done, tested, and deployed
- 🚧 **In Progress** (1-99%): Currently being developed
- ⏳ **Planned** (0%): Not started, scheduled for current phase
- 💭 **Backlog**: Deferred to future phase/release

**MoSCoW Priority**:
- **M** = Must-Have (critical for MVP/current milestone)
- **S** = Should-Have (important but not critical)
- **C** = Could-Have (nice-to-have)
- **W** = Won't-Have (explicitly out of scope)

**Dependency Layer**:
- **Foundation** (F): Core infrastructure, data models, architecture
- **Validation** (V): Proves concept, core user workflows
- **Differentiation** (D): Unique features, competitive advantage
- **Polish** (P): UX improvements, refinements

**Complexity**:
- **S** (Small): < 1 day
- **M** (Medium): 1-3 days
- **L** (Large): 1+ weeks
- **XL** (Extra Large): Multiple weeks

---

## Project Information

**Project Name**: [Your Project Name]

**Current Phase**: [e.g., MVP, Beta, Version 1.0]

**Target Milestone**: [e.g., MVP Launch, Public Beta]

**Milestone Date**: [Target date]

**Team Size**: [Number of developers]

**Last Updated**: [Date]

---

## Summary Statistics

| Category | Count | % Complete |
|----------|-------|------------|
| Total Features | [X] | [X%] |
| Must-Have (M) | [X] | [X%] |
| Should-Have (S) | [X] | [X%] |
| Could-Have (C) | [X] | [X%] |
| Won't-Have (W) | [X] | N/A |

| Layer | % Complete |
|-------|------------|
| Foundation | [X%] |
| Validation | [X%] |
| Differentiation | [X%] |
| Polish | [X%] |

---

## Foundation Layer Features

Core infrastructure, data models, and architecture that everything else depends on.

| # | Feature | Status | Progress | Priority | Complexity | Dependencies | Notes |
|---|---------|--------|----------|----------|------------|--------------|-------|
| F-1 | [Feature name] | ⏳ | 0% | M | L | - | [Notes, blockers, or context] |
| F-2 | [Feature name] | 🚧 | 50% | M | M | F-1 | [Notes] |
| F-3 | [Feature name] | ✅ | 100% | S | M | - | [Notes] |

**Examples**:
- Data model definition (entities, relationships, schemas)
- Database setup (PostgreSQL, MongoDB, SQLite)
- Authentication system (JWT, OAuth, sessions)
- API architecture (REST, GraphQL, WebSocket)
- Core services (payment processing, file storage)
- Build system (webpack, vite, deployment pipeline)

---

## Validation Layer Features

Minimum features to demonstrate core value and validate assumptions with users.

| # | Feature | Status | Progress | Priority | Complexity | Dependencies | Notes |
|---|---------|--------|----------|----------|------------|--------------|-------|
| V-1 | [Feature name] | ⏳ | 0% | M | M | F-1, F-2 | [Notes] |
| V-2 | [Feature name] | 🚧 | 60% | M | L | F-3 | [Notes] |
| V-3 | [Feature name] | ⏳ | 0% | S | S | V-1 | [Notes] |

**Examples**:
- Core user workflows (onboarding, main task flow)
- Import/export functionality (get data in/out)
- Basic UI for primary features
- Essential interactions (create, read, update, delete)
- Minimum feature set for user testing

---

## Differentiation Layer Features

Unique features that set the product apart from competitors.

| # | Feature | Status | Progress | Priority | Complexity | Dependencies | Notes |
|---|---------|--------|----------|----------|------------|--------------|-------|
| D-1 | [Feature name] | ⏳ | 0% | M | XL | V-1, V-2 | [Notes] |
| D-2 | [Feature name] | ⏳ | 0% | S | L | F-2, V-1 | [Notes] |
| D-3 | [Feature name] | 💭 | 0% | C | M | D-1 | [Notes] |

**Examples**:
- AI-powered features (recommendations, automation)
- Novel interactions (voice, gesture, unique UX)
- Advanced workflows (automation, integrations)
- Performance advantages (10x faster, real-time)
- Unique integrations (proprietary APIs, exclusive data)

---

## Polish Layer Features

UX improvements, convenience features, and refinements.

| # | Feature | Status | Progress | Priority | Complexity | Dependencies | Notes |
|---|---------|--------|----------|----------|------------|--------------|-------|
| P-1 | [Feature name] | ⏳ | 0% | C | S | V-1 | [Notes] |
| P-2 | [Feature name] | 💭 | 0% | W | M | - | Deferred to Phase 2 |
| P-3 | [Feature name] | 🚧 | 20% | C | S | - | [Notes] |

**Examples**:
- Dark mode / themes
- Keyboard shortcuts
- Animation effects
- Loading states / skeleton screens
- Error message improvements
- Accessibility enhancements
- Performance optimizations

---

## Technical Spikes / Research

Investigations needed to de-risk assumptions or make architectural decisions.

| # | Spike | Status | Priority | Time Box | Decision Needed | Outcome |
|---|-------|--------|----------|----------|-----------------|---------|
| S-1 | [Spike name] | ⏳ | High | 1 day | [What you need to decide] | [Findings] |
| S-2 | [Spike name] | ✅ | Medium | 4 hours | [Decision] | [Outcome/decision made] |

**Examples**:
- Performance testing (can React Flow handle 500 nodes?)
- API evaluation (which voice API: OpenAI vs Google?)
- Library comparison (D3 vs Cytoscape vs React Flow?)
- Architecture decision (monolith vs microservices?)
- Integration feasibility (can we integrate with X API?)

---

## Risks & Assumptions

### High-Risk Items

| # | Risk | Impact | Likelihood | Mitigation Strategy | Status |
|---|------|--------|------------|---------------------|--------|
| R-1 | [Risk description] | High | Medium | [How to de-risk] | ⏳ |
| R-2 | [Risk description] | Medium | High | [Mitigation plan] | 🚧 |

**Examples**:
- Unvalidated core value prop ("users won't prefer visual > text")
- Technical uncertainty ("voice API may have high latency")
- Performance unknowns ("React Flow may not scale to 500 nodes")
- Integration risks ("third-party API may be unreliable")

### Key Assumptions

| # | Assumption | Validated? | Validation Method | Outcome |
|---|------------|------------|-------------------|---------|
| A-1 | [Assumption] | ⏳ | [How to validate] | [Result] |
| A-2 | [Assumption] | ✅ | [Method used] | [Confirmed / Rejected] |

**Examples**:
- "Users prefer visual PID > text PID" → Validate with user testing
- "Voice commands are essential" → Validate with user interviews
- "React Flow scales to 500 nodes" → Validate with performance test

---

## Blockers & Dependencies

### Current Blockers

| Feature | Blocked By | Impact | Resolution Plan |
|---------|------------|--------|-----------------|
| [Feature] | [What's blocking it] | [Impact description] | [How to unblock] |

**Examples**:
- Voice integration blocked by: No API decision made → Run spike this week
- User testing blocked by: No import feature → Build import UI first
- Collaboration blocked by: No auth system → Build auth first

### Dependency Chain

```
Foundation Layer:
├─ F-1: Data Model (✅ Complete)
│  ├─ Enables: V-1 (Import), V-2 (Visualization)
│  └─ Enables: F-2 (Persistence)
│
├─ F-2: Persistence (🚧 50% complete)
│  ├─ Blocked by: F-1 (Complete ✅)
│  └─ Enables: V-3 (Multi-session testing)
│
└─ F-3: AI API (✅ Complete)
   └─ Enables: D-1 (Voice), D-2 (Semantic Zoom)

Validation Layer:
├─ V-1: Import (⏳ Planned)
│  ├─ Depends on: F-1, F-2
│  └─ Enables: User testing
│
└─ V-2: Visualization (🚧 60% complete)
   ├─ Depends on: F-1
   └─ Enables: V-3 (Export)

Differentiation Layer:
├─ D-1: Voice (⏳ Planned)
│  ├─ Depends on: F-3, V-1, V-2
│  └─ Blocked by: API decision needed
│
└─ D-2: Semantic Zoom (⏳ Planned)
   ├─ Depends on: F-3, V-2
   └─ Requires: Caching strategy decision
```

---

## Notes & Context

### Product Vision
[Brief description of product vision and core value proposition]

### Current Sprint/Milestone Goals
[What you're trying to achieve in current sprint]

### Recent Decisions
- [Decision 1 and rationale]
- [Decision 2 and rationale]

### Open Questions
- [Question 1]
- [Question 2]

---

## Example: ThinkCanvas Feature Matrix

### Foundation Layer

| # | Feature | Status | Progress | Priority | Complexity | Dependencies | Notes |
|---|---------|--------|----------|----------|------------|--------------|-------|
| F-1 | Node/Edge Data Model | ✅ | 100% | M | M | - | Complete, tested |
| F-2 | SQLite Persistence | 🚧 | 30% | M | L | F-1 | In progress, blocked by schema migrations |
| F-3 | AI API Integration | ✅ | 100% | M | M | - | Using OpenAI API |
| F-4 | React Flow Setup | ✅ | 90% | M | M | F-1 | Works well, need performance testing |
| F-5 | WebSocket Connection | ✅ | 100% | M | M | - | Real-time updates working |

### Validation Layer

| # | Feature | Status | Progress | Priority | Complexity | Dependencies | Notes |
|---|---------|--------|----------|----------|------------|--------------|-------|
| V-1 | Import PID (Markdown) | ⏳ | 0% | M | M | F-1, F-2 | Planned for Week 3 |
| V-2 | Mind Map Visualization | ✅ | 60% | M | L | F-1, F-4 | Layout works, need styling |
| V-3 | AI Chat + Canvas Sync | 🚧 | 50% | M | L | F-3, V-2 | Chat works, sync partial |
| V-4 | Basic Node Editing | ✅ | 70% | M | M | V-2 | Add/edit works, delete buggy |
| V-5 | Export to Markdown | ⏳ | 0% | M | S | V-1 | Quick win after import |

### Differentiation Layer

| # | Feature | Status | Progress | Priority | Complexity | Dependencies | Notes |
|---|---------|--------|----------|----------|------------|--------------|-------|
| D-1 | Voice Commands | ⏳ | 0% | S | XL | F-3, V-3 | Blocked by API decision |
| D-2 | Dynamic Diagram Morphing | ⏳ | 0% | M | L | V-2, V-3 | Need multiple layouts first |
| D-3 | AI Semantic Zoom | 🚧 | 30% | M | L | F-3, V-2 | Summarization works, no caching |
| D-4 | Context-Aware Suggestions | ⏳ | 0% | S | M | V-3, D-3 | Defer to Phase 2 |

### Polish Layer

| # | Feature | Status | Progress | Priority | Complexity | Dependencies | Notes |
|---|---------|--------|----------|----------|------------|--------------|-------|
| P-1 | Dark Mode | ⏳ | 0% | C | S | - | Defer to post-MVP |
| P-2 | Keyboard Shortcuts | 🚧 | 10% | C | S | V-4 | Basic shortcuts only |
| P-3 | Animation Effects | ⏳ | 0% | W | M | - | Phase 2 |
| P-4 | Breadcrumb Navigation | ⏳ | 0% | C | S | V-2 | Quick win if time |

### Summary

- **Total Features**: 18
- **Completed**: 5 (28%)
- **In Progress**: 5 (28%)
- **Planned**: 8 (44%)

**Layer Progress**:
- Foundation: 90% (Strong foundation!)
- Validation: 40% (Need import + export)
- Differentiation: 10% (Mostly planned)
- Polish: 3% (Defer to post-MVP)

**Key Insight**: Foundation is strong, focus on Validation layer to enable user testing.
