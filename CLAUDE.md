# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is the **Anthropic Skills Repository** - a collection of example skills that demonstrate Claude's skills system capabilities. Skills are folders containing instructions, scripts, and resources that Claude loads dynamically to improve performance on specialized tasks.

The repository contains:
- **Example skills** (`skills/algorithmic-art`, `skills/artifacts-builder`, `skills/canvas-design`, `skills/mcp-builder`, `skills/slack-gif-creator`, `skills/webapp-testing`, etc.) - Open source (Apache 2.0)
- **Document skills** (`skills/document-skills/docx`, `skills/document-skills/pdf`, `skills/document-skills/pptx`, `skills/document-skills/xlsx`) - Source-available reference implementations
- **Meta skills** (`skills/skill-creator`, `skills/template-skill`) - Tools for creating new skills

## Architecture

### Skill Structure

Every skill follows the Agent Skills Spec defined in `agent_skills_spec.md`:

```
skill-name/
├── SKILL.md (required)
│   ├── YAML frontmatter (name, description, optional: license, allowed-tools, metadata)
│   └── Markdown instructions
├── scripts/ (optional) - Executable code for deterministic operations
├── references/ (optional) - Documentation loaded on-demand
└── assets/ (optional) - Files used in output (templates, icons, etc.)
```

### Progressive Disclosure Pattern

Skills use a three-level loading system to manage context efficiently:
1. **Metadata** (name + description) - Always in context (~100 words)
2. **SKILL.md body** - When skill triggers (<5k words)
3. **Bundled resources** - As needed by Claude (scripts may execute without loading into context)

### Plugin Marketplace Structure

The `.claude-plugin/marketplace.json` defines two plugin collections:
- **document-skills** - Production-grade document processing suite
- **example-skills** - Reference implementations for learning and inspiration

## Working with Skills

### Creating a New Skill

**DO NOT manually create skill folders.** The skill-creator skill provides guidance, but note:
- Reference `skills/template-skill/SKILL.md` for the basic structure
- YAML frontmatter requires `name` (hyphen-case) and `description` (when to use this skill)
- Skill name must match directory name
- Use imperative/infinitive form (verb-first instructions), not second person
- Write for another Claude instance to consume

### Skill Content Guidelines

**SKILL.md writing style:**
- Use imperative form: "To accomplish X, do Y" (not "You should do X")
- Be specific about when the skill should be used
- Include concrete examples of usage patterns
- Reference bundled resources so Claude knows they exist

**Bundled resources:**
- `scripts/` - For repeatedly rewritten code or deterministic operations (e.g., PDF rotation, Excel recalculation)
- `references/` - Documentation Claude should reference while working (schemas, API docs, policies)
- `assets/` - Files used in output, not loaded into context (templates, images, fonts)

### Document Skills Special Considerations

Document skills (`skills/document-skills/{docx,pdf,pptx,xlsx}`) contain production-grade patterns:
- Python scripts in `scripts/` for binary file operations
- Extensive reference documentation in separate `.md` files
- Complex workflows balancing formula preservation, formatting, and data integrity
- Example: `skills/document-skills/xlsx/recalc.py` uses LibreOffice for formula recalculation

## Testing Skills

When testing or using skills:
- Skills are designed for Claude.ai, Claude Code, and API usage
- In Claude Code, skills can be installed via the plugin marketplace
- Test with concrete, realistic examples that match the skill's intended use cases
- Iterate based on actual performance - notice struggles, update instructions

## Key Files

- `agent_skills_spec.md` - Official specification for skill structure
- `README.md` - Public documentation and installation instructions
- `.claude-plugin/marketplace.json` - Plugin marketplace configuration
- `skills/` - Directory containing all skill implementations
- `skills/skill-creator/SKILL.md` - Comprehensive guide for building effective skills
- `skills/template-skill/SKILL.md` - Minimal starting template

## Important Notes

- These are **reference examples**, not guaranteed to match production Claude behavior
- Document skills are **point-in-time snapshots**, not actively maintained
- Each skill is self-contained - no shared dependencies between skills
- Skills should focus on procedural knowledge that no model can fully possess
- Avoid generic development practices - focus on domain-specific workflows
