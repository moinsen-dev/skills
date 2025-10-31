# LLM Optimization Guide for CLAUDE.md

This guide explains how to write CLAUDE.md files optimized for AI agent consumption.

## Core Principle: Context Efficiency

**CLAUDE.md is NOT documentation for humans.** It's instruction for AI agents.

### The Problem
- Long files → context bloat → degraded AI performance
- Verbose explanations → noise that obscures actionable rules
- Generic advice → AI already knows this

### The Solution
- Dense, structured information
- Pattern-matching over prose
- Actionable rules over explanations
- Focus on PROJECT-SPECIFIC decisions

## What to Include

### ✅ Tool CHOICES (not usage)
```markdown
❌ WRONG: "Use grep to search files. The syntax is grep 'pattern' files."
✅ RIGHT: "**Package Manager**: `pnpm` (not npm, not yarn)"
```

AI knows HOW to use grep. AI needs to know WHICH tool to use.

### ✅ Architectural PATTERNS
```markdown
❌ WRONG: "Clean Architecture separates concerns into layers..."
✅ RIGHT: "**Dependency Rule**: presentation → domain ← data
          ❌ domain cannot import from data or presentation"
```

Focus on the RULES and CONSTRAINTS, not explanations.

### ✅ Mandatory USAGE
```markdown
✅ "**Before creating UI**: Search atomic_components package first
   ```bash
   grep -r \"ComponentName\" packages/atomic_components/lib/
   ```"
```

### ✅ Anti-Patterns SPECIFIC to this project
```markdown
✅ "❌ NEVER: Create custom buttons (use atomic_components/atoms/button.dart)
   ❌ NEVER: Import UI in domain layer (violates Clean Architecture)"
```

### ✅ Quality GATES
```markdown
✅ "Task complete ONLY when:
   - [ ] `flutter analyze` shows no issues
   - [ ] All tests pass
   - [ ] No code duplication from internal packages"
```

## What to EXCLUDE

### ❌ Tool Usage Instructions
```markdown
❌ "To search files, use: grep 'pattern' files
   The -r flag searches recursively..."
```

AI knows this. Don't waste context.

### ❌ Folder Structure
```markdown
❌ "Project structure:
   src/
     components/
       atoms/
       molecules/
   ..."
```

Gets outdated immediately. AI can explore with glob/ls.

### ❌ Generic Best Practices
```markdown
❌ "Write clean code. Use meaningful variable names. Add comments."
```

AI already knows. Be PROJECT-SPECIFIC.

### ❌ Long Explanations
```markdown
❌ "Clean Architecture is a software design philosophy that emphasizes
   separation of concerns. The architecture is divided into layers, each
   with its own responsibility. The innermost layer contains business logic..."
```

Replace with dense rules:
```markdown
✅ "Clean Architecture layers:
   - domain/ → Pure business (no dependencies)
   - data/ → Repositories, APIs
   - presentation/ → UI, widgets
   Rule: domain imports nothing"
```

## Optimal Formats

### Checklists
```markdown
## Task Completion Criteria

- [ ] `flutter analyze` passes
- [ ] Tests pass
- [ ] Verified no code duplication
- [ ] Used atomic_components (not custom UI)
```

**Why**: Easy to parse, actionable, clear success criteria.

### Decision Trees
```markdown
## When to Create New UI

Need UI component?
├─ Exists in atomic_components? → Use it (STOP)
├─ Can compose from atoms/molecules? → Compose (STOP)
└─ Must create new? → Add to atomic_components (not app code)
```

**Why**: Algorithmic clarity, no ambiguity.

### Code Blocks with Examples
```markdown
## Import Pattern

❌ WRONG:
\`\`\`dart
import 'custom_button.dart';  // NO! Use atomic_components
\`\`\`

✅ CORRECT:
\`\`\`dart
import 'package:atomic_components/atomic_components.dart';
\`\`\`
```

**Why**: Shows exact patterns to match/avoid.

### Command Snippets
```markdown
## Search Before Creating

\`\`\`bash
# Check if component exists
grep -r "ButtonName" packages/atomic_components/lib/

# Check if entity exists
ls packages/app_layers/lib/entities/
\`\`\`
```

**Why**: Copy-pasteable, actionable, reduces errors.

### Tabular Rules
```markdown
| Decision | Choice | Alternative Rejected |
|----------|--------|---------------------|
| Package Manager | `pnpm` | npm, yarn |
| State Management | Riverpod | BLoC, Provider |
| Linter | `ruff` | flake8, pylint |
```

**Why**: Dense, scannable, pattern-matchable.

## Structure Guidelines

### Use Emojis for Visual Parsing
```markdown
## 🚨 Critical Requirements  → Immediate attention
## 🔧 Tool Decisions         → Configuration
## 🏗️ Architecture Rules     → Structure
## 📦 Mandatory Packages     → Dependencies
## 🚫 Anti-Patterns          → Never do this
## ✅ Checklist              → Success criteria
```

**Why**: Visual anchors for quick context retrieval.

### Keep Sections Short
- Each section: < 30 lines
- If longer: Split into subsections
- Use h3 (###) for subsections

### Lead with Action
```markdown
❌ "This section describes the testing approach we use..."
✅ "Before marking task complete, run: `npm test`"
```

Start with the ACTION, not the explanation.

## Anti-Patterns in CLAUDE.md Writing

### ❌ Storytelling
```markdown
"When we started this project, we evaluated several options for state management.
After careful consideration, we chose Riverpod because..."
```

**Fix**: "**State Management**: `Riverpod` (not BLoC, not Provider)"

### ❌ Educational Content
```markdown
"Atomic Design is a methodology created by Brad Frost. It breaks UI into
five distinct levels: atoms, molecules..."
```

**Fix**: "Atomic Design: atoms → molecules → organisms → templates"

### ❌ Conditional Uncertainty
```markdown
"You might want to consider using the atomic_components package if appropriate..."
```

**Fix**: "**MUST** use atomic_components. Search first: `grep -r ...`"

### ❌ Passive Voice
```markdown
"The components should be organized into folders..."
```

**Fix**: "Organize components: atoms/, molecules/, organisms/"

## Quality Check

Before finalizing CLAUDE.md, verify:

- [ ] Zero "how to use" instructions for standard tools
- [ ] No folder structure (unless critical to architecture rules)
- [ ] Every rule is PROJECT-SPECIFIC (not generic)
- [ ] Checklists/trees/code blocks used (not prose)
- [ ] File size < 500 lines (ideally < 300)
- [ ] Each section actionable (not explanatory)

## Examples

### ❌ Bad: Context-Heavy, Generic
```markdown
# Project Documentation

## Introduction
This project uses React for the frontend and follows modern best practices.
We believe in writing clean, maintainable code.

## Getting Started
To get started, first install dependencies. You can do this by running npm install.
This will download all packages listed in package.json...

## Code Quality
We use ESLint for linting. ESLint is a tool that analyzes your code...
```

**Problems**:
- Generic advice AI knows
- "How to" instructions
- Verbose explanations

### ✅ Good: Context-Efficient, Specific
```markdown
# Project Development Rules

## 🔧 Tool Decisions
- **Package Manager**: `pnpm` (not npm)
- **State**: Zustand (not Redux, not Context)
- **Linter**: ESLint (`pnpm lint` must pass)

## ✅ Task Complete When
- [ ] `pnpm lint` → No errors
- [ ] `pnpm test` → All pass
- [ ] Used `/src/components` (not custom)
```

**Benefits**:
- Specific tool choices
- Actionable commands
- Clear success criteria
- Minimal context usage

## Research Integration

When researching best practices for CLAUDE.md generation:

### Questions to Ask
1. "What are the specific anti-patterns for [architecture] in [tech stack]?"
2. "What are the mandatory package usage patterns in [tech stack] monorepos?"
3. "What quality gates should be enforced for [tech stack] projects?"

### How to Integrate
- Extract RULES (not tutorials)
- Convert to CHECKLISTS/TREES
- Make PROJECT-SPECIFIC
- Add to relevant section (Critical, Architecture, Anti-Patterns)

## Summary

**Write CLAUDE.md like you're configuring a linter:**
- Specific rules
- Clear violations
- Actionable fixes
- Zero ambiguity
- Minimal verbosity

NOT like you're teaching a junior developer.
