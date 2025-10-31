---
name: claude-md-architect
description: This skill should be used when creating or updating CLAUDE.md files for software projects. It analyzes project architecture, detects tool choices, and generates context-efficient CLAUDE.md files optimized for AI agent consumption. Use when user requests "generate CLAUDE.md", "analyze project patterns", "create development guidelines", or "document project rules for AI".
---

# CLAUDE.md Architect

Generate LLM-optimized CLAUDE.md files that improve AI agent performance through context-efficient, rule-based project documentation.

## Overview

This skill analyzes software projects and generates CLAUDE.md files specifically optimized for AI agent consumption. Unlike human documentation, CLAUDE.md files focus on:

- **Tool CHOICES** (which tool to use, not how to use it)
- **Architectural PATTERNS** (rules and constraints, not explanations)
- **Mandatory WORKFLOWS** (what must be done, not suggestions)
- **Anti-PATTERNS** (what to never do in this project)
- **Context EFFICIENCY** (dense, structured, actionable)

**Key Principle**: CLAUDE.md is instruction for AI agents, NOT documentation for humans. Long explanations hurt AI performance by bloating context.

## When to Use This Skill

### Primary Use Cases

1. **"Generate a CLAUDE.md for this project"**
   - New projects needing development guidelines
   - Inherited projects without documentation
   - Onboarding AI agents to existing codebases

2. **"Update CLAUDE.md - project has changed"**
   - New packages added
   - Architecture evolved
   - Tool choices changed

3. **"Analyze this project's patterns"**
   - Understand architectural decisions
   - Document development philosophy
   - Create consistency rules

4. **"Research best practices for this stack"**
   - Find anti-patterns for specific architecture
   - Discover quality gates for tech stack
   - Learn mandatory patterns

## Workflow

### Mode 1: Generate New CLAUDE.md

**Step 1: Analyze Project**

Run architecture and decision detection:

```bash
# Analyze architecture
python3 scripts/analyze_architecture.py /path/to/project > arch.json

# Detect tool decisions
python3 scripts/detect_decisions.py /path/to/project > decisions.json
```

**Step 2: Interactive Discovery**

Ask user clarifying questions:

- **Mandatory packages**: "I detected these internal packages: X, Y. Are these mandatory to use?"
- **Quality gates**: "Should `flutter analyze` show zero warnings, or are some acceptable?"
- **Anti-patterns**: "Are there specific patterns developers keep recreating incorrectly?"
- **Development philosophy**: "Is there a specific workflow (e.g., template-first, test-first)?"

**Step 3: Research (if requested)**

If user wants best practices researched:

```
"Research anti-patterns for Clean Architecture in Flutter"
"Research quality gates for React + TypeScript projects"
"Research monorepo package usage patterns"
```

Use WebSearch to find:
- Anti-patterns for this architecture + tech stack
- Quality standards and linting rules
- Common violations and how to prevent them

**Important**: Extract RULES not tutorials. Convert research to checklists/decision trees.

**Step 4: Generate CLAUDE.md**

```bash
python3 scripts/generate_claude_md.py arch.json decisions.json "ProjectName" > CLAUDE.md
```

**Step 5: Review and Refine**

Review generated CLAUDE.md with user:
- Read the generated sections
- Ask: "Does this match your development philosophy?"
- Ask: "Any critical rules missing?"
- Ask: "Any anti-patterns to add?"

**Step 6: Optimize for LLM**

Before finalizing, check against `references/llm_optimization_guide.md`:

- [ ] No "how to use" instructions for standard tools?
- [ ] No folder structure (unless architectural rule)?
- [ ] All rules PROJECT-SPECIFIC (not generic)?
- [ ] Uses checklists/trees/code blocks (not prose)?
- [ ] File size < 500 lines?

### Mode 2: Update Existing CLAUDE.md

**Step 1: Analyze Current State**

```bash
# Re-analyze project
python3 scripts/analyze_architecture.py /path/to/project > arch_new.json
python3 scripts/detect_decisions.py /path/to/project > decisions_new.json
```

**Step 2: Detect Changes**

```bash
# Update CLAUDE.md
python3 scripts/update_claude_md.py CLAUDE.md arch_new.json decisions_new.json > CLAUDE_updated.md
```

The update script will output detected changes to stderr.

**Step 3: Review Changes**

Show user what changed:
- "Detected new package: X"
- "Updated linter from Y to Z"
- "Added mandatory package: A"

Ask: "Do these changes look correct?"

**Step 4: Preserve Custom Sections**

The updater preserves custom sections. Ask user:
- "Are there manual sections you added that should be kept?"
- Review updated file to ensure nothing lost

### Mode 3: Research Best Practices

When user requests research:

**Step 1: Identify Research Topic**

From analysis results:
- Architecture pattern (Clean Architecture, Feature-First, etc.)
- Tech stack (Flutter, React, Python, etc.)
- Specific concern (testing, state management, etc.)

**Step 2: Focused Research**

Use WebSearch with specific queries:

```
"[Architecture] anti-patterns in [TechStack]"
"[TechStack] [Pattern] common mistakes"
"[Architecture] best practices [TechStack] 2025"
"Quality gates for [TechStack] projects"
```

**Step 3: Extract Rules**

From research, extract:
- ✅ Specific rules and constraints
- ✅ Common violations (anti-patterns)
- ✅ Quality gates and checks
- ❌ NOT tutorials or explanations

**Step 4: Convert to CLAUDE.md Format**

Transform findings into:
- Checklists for quality gates
- Decision trees for workflows
- Code blocks showing violations vs correct usage
- Bash commands for verification

Reference: `references/llm_optimization_guide.md` for formatting patterns

## Reference Materials

### For Writing CLAUDE.md

Read `references/llm_optimization_guide.md` to understand:
- What to include (tool choices, patterns, rules)
- What to exclude (folder structure, tool usage, generic advice)
- Optimal formats (checklists, decision trees, code blocks)
- Anti-patterns in CLAUDE.md writing

### For Architecture Documentation

Read `references/architectural_patterns.md` for:
- Common architecture patterns (Clean, Feature-First, Atomic Design, etc.)
- How to document each pattern for AI consumption
- Architecture-specific anti-patterns
- Research prompts for each architecture type

## Key Principles

### 1. Context Efficiency Over Completeness

```markdown
❌ BAD: "Clean Architecture is a software design philosophy created by Robert C. Martin.
        It emphasizes separation of concerns through layered architecture..."

✅ GOOD: "**Dependency Rule**: presentation → domain ← data
         ❌ domain cannot import from data or presentation"
```

### 2. Tool CHOICES, Not Usage

```markdown
❌ BAD: "Use grep to search files. Syntax: grep 'pattern' files..."

✅ GOOD: "**Package Manager**: `pnpm` (not npm, not yarn)"
```

AI knows HOW to use tools. Document WHICH tools to use.

### 3. Project-Specific Rules Only

```markdown
❌ BAD: "Write clean code with meaningful variable names..."

✅ GOOD: "**Before creating UI**: Search atomic_components first
         ```bash
         grep -r 'Component' packages/atomic_components/lib/
         ```"
```

Generic advice wastes context. Focus on THIS project's rules.

### 4. No Folder Structure

```markdown
❌ BAD: "Project structure:
         src/
           components/
             atoms/
             molecules/
         ..."
```

Folder structure gets outdated immediately. AI can explore with glob/ls. Only document structure if it's an architectural RULE.

### 5. Actionable Over Explanatory

```markdown
❌ BAD: "This section describes our testing approach..."

✅ GOOD: "Before marking complete: `flutter test` must pass"
```

Lead with ACTION, not explanation.

## Common Scenarios

### Scenario: Flutter Clean Architecture + Monorepo

```bash
# Analysis detects:
- Architecture: Clean Architecture (domain/data/presentation)
- Design Pattern: Atomic Design (atoms/molecules/organisms)
- Packages: atomic_components, app_layers (mandatory)
- State Management: Riverpod
- Quality: flutter_analyze strict mode

# Generated CLAUDE.md includes:
- Critical Requirement: flutter analyze must show zero warnings
- Tool Decisions: Riverpod (not BLoC), flutter pub (package manager)
- Architecture Rules: Dependency directions, layer constraints
- Mandatory Packages: Check atomic_components before UI, use app_layers entities
- Workflow: Template-first approach, search before create
- Anti-Patterns: UI in domain, custom widgets when atomic exists
- Checklist: Analyze passes, no duplication, tests pass
```

### Scenario: React + TypeScript Monorepo

```bash
# Analysis detects:
- Architecture: Component-based with features
- State Management: Zustand
- Package Manager: pnpm
- Linter: ESLint, Formatter: Prettier
- Testing: Jest + React Testing Library

# Generated CLAUDE.md includes:
- Critical Requirement: pnpm lint must pass with zero errors
- Tool Decisions: pnpm (not npm), Zustand (not Redux), ESLint + Prettier
- Architecture Rules: Component composition, feature isolation
- Workflow: Check components library first, compose before creating
- Anti-Patterns: State in components (use Zustand), duplicated components
- Checklist: Lint passes, tests pass, TypeScript compiles
```

### Scenario: Python with Clean Architecture

```bash
# Analysis detects:
- Architecture: Layered (api/business/data)
- Package Manager: uv
- Testing: pytest
- Linter: ruff
- Formatter: ruff format

# Generated CLAUDE.md includes:
- Critical Requirement: ruff check must pass
- Tool Decisions: uv (not pip), pytest, ruff (linter + formatter)
- Architecture Rules: Service layer patterns, repository pattern
- Workflow: Check services/repositories before creating
- Anti-Patterns: Business logic in API layer, direct DB access from services
- Checklist: ruff passes, pytest passes, type hints added
```

## Interactive Questions to Ask

### Always Ask

1. **"I've analyzed the project. Here's what I found: [summary]. Does this match your understanding?"**
2. **"Are there critical rules I should include? (e.g., zero tolerance policies, mandatory workflows)"**
3. **"Are there anti-patterns developers keep making that should be documented?"**
4. **"Should I research best practices for [architecture + tech stack]?"**

### Conditional Questions

**If monorepo/packages detected:**
- "Are these internal packages mandatory to use?"
- "What should happen if someone creates functionality that already exists in a package?"

**If linter detected:**
- "Should linting pass with zero warnings, or are some warnings acceptable?"

**If testing framework detected:**
- "Should tests be required before marking tasks complete?"

**If architecture detected but unclear:**
- "I see [folders]. Is this [architecture pattern]?"
- "What are the dependency rules between these layers?"

## Anti-Patterns to Avoid

### ❌ Generating Outdated Content

```markdown
Don't document folder structure:
❌ src/components/atoms/Button.tsx
❌ src/components/molecules/SearchBar.tsx

Gets outdated immediately.
```

### ❌ Generic Development Advice

```markdown
Don't include:
❌ "Write meaningful variable names"
❌ "Add comments to explain complex logic"
❌ "Follow SOLID principles"

AI already knows this.
```

### ❌ Tool Usage Instructions

```markdown
Don't explain how to use tools:
❌ "Use grep to search. Syntax: grep [options] pattern [files]"

Document WHICH tool:
✅ "**Search Tool**: `grep` (not `ack`, not `ag`)"
```

### ❌ Long Explanations

```markdown
Don't write paragraphs:
❌ "Atomic Design is a methodology for creating design systems. It was created
    by Brad Frost and provides a framework for..."

Write rules:
✅ "Atomic Design: atoms → molecules → organisms → templates
   Rule: Build UP the hierarchy (never skip levels)"
```

## Scripts Reference

All scripts output JSON for easy consumption and chaining.

### analyze_architecture.py

```bash
python3 scripts/analyze_architecture.py /path/to/project
```

**Output**:
```json
{
  "tech_stack": "flutter|react|python|...",
  "architecture_pattern": "clean_architecture|feature_first|...",
  "design_patterns": ["atomic_design", ...],
  "layer_structure": {...},
  "mandatory_packages": [...],
  "key_insights": [...]
}
```

### detect_decisions.py

```bash
python3 scripts/detect_decisions.py /path/to/project
```

**Output**:
```json
{
  "package_manager": "pnpm|npm|uv|pip|...",
  "state_management": "Riverpod|Redux|...",
  "testing_framework": "pytest|jest|...",
  "linter": "ruff|eslint|...",
  "formatter": "prettier|black|...",
  "quality_tools": [...],
  "key_dependencies": [...],
  "conventions": [...]
}
```

### generate_claude_md.py

```bash
python3 scripts/generate_claude_md.py arch.json decisions.json "ProjectName"
```

Generates complete CLAUDE.md optimized for AI consumption.

### update_claude_md.py

```bash
python3 scripts/update_claude_md.py existing_CLAUDE.md arch.json decisions.json
```

Updates existing CLAUDE.md, preserving custom sections.

## Success Criteria

A successful CLAUDE.md file:

- [ ] File size < 500 lines (ideally < 300)
- [ ] Zero "how to use" instructions for standard tools
- [ ] No folder structure (unless architectural rule)
- [ ] Every rule is PROJECT-SPECIFIC
- [ ] Uses checklists/trees/code blocks (minimal prose)
- [ ] Clear quality gates (what must pass)
- [ ] Specific anti-patterns documented
- [ ] Actionable "before creating X" commands
- [ ] Tool choices explicitly stated

## Examples

See `references/llm_optimization_guide.md` for detailed examples of:
- Good vs bad CLAUDE.md sections
- Context-efficient formatting
- Anti-patterns in documentation

## Remember

**CLAUDE.md is configuration for AI agents, not documentation for humans.**

Write it like configuring a linter:
- Specific rules
- Clear violations
- Actionable fixes
- Zero ambiguity
- Minimal verbosity
