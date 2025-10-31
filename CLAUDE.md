# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is the **Anthropic Skills Repository** - a collection of example skills that demonstrate Claude's skills system capabilities. Skills are folders containing instructions, scripts, and resources that Claude loads dynamically to improve performance on specialized tasks.

The repository contains:
- **Example skills** (`skills/algorithmic-art`, `skills/artifacts-builder`, `skills/brand-guidelines`, `skills/canvas-design`, `skills/claude-md-architect`, `skills/internal-comms`, `skills/mcp-builder`, `skills/slack-gif-creator`, `skills/theme-factory`, `skills/webapp-testing`) - Open source (Apache 2.0)
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
- **document-skills** - Production-grade document processing suite (docx, pdf, pptx, xlsx)
- **example-skills** - Reference implementations for learning and inspiration

**When adding new skills to marketplace:**
```bash
# 1. Add skill path to appropriate plugin in marketplace.json
# 2. Update plugin description if needed
# 3. Verify JSON is valid
cat .claude-plugin/marketplace.json | python3 -m json.tool > /dev/null && echo "Valid JSON"

# 4. Verify skill exists at specified path
# Example: if path is "./skills/my-skill", ensure skills/my-skill/SKILL.md exists
```

**Marketplace version:** Increment `metadata.version` when adding/removing skills

## Critical Rules

**Before creating/modifying skills:**
1. **Skill name MUST match directory name** (exact match, hyphen-case)
2. **YAML frontmatter is mandatory** (`name` and `description` required)
3. **Use skill-creator skill** - DO NOT manually create skill folders
4. **Test skills** before claiming they work

**Before claiming "production-ready":**
```bash
# Verify SKILL.md exists and has valid frontmatter
grep -A 2 "^---$" skills/YOUR-SKILL/SKILL.md

# Test skill loads properly in Claude Code
# (manual verification required)
```

## Working with Skills

### Creating a New Skill

**MANDATORY: Use the skill-creator skill** - DO NOT manually create folders.

**Required structure:**
- Reference `skills/template-skill/SKILL.md` for basic structure
- YAML frontmatter: `name` (hyphen-case) + `description` (when to use)
- Skill name = directory name (exact match)
- Use imperative form: "Do X" not "You should do X"
- Write for AI consumption, not humans

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

## Anti-Patterns

**❌ DO NOT:**
- Manually create skill folders without using skill-creator
- Use second-person writing ("you should") in SKILL.md - use imperative ("do this")
- Include generic development advice in skills (AI already knows best practices)
- Document "how to use" standard tools - focus on WHICH tools/patterns THIS project uses
- Create skills with names that don't match their directory names
- Skip YAML frontmatter validation before claiming skill is ready
- Add shared dependencies between skills - each must be self-contained

**✅ DO:**
- Use skill-creator for all new skills
- Write in imperative form for AI consumption
- Focus on domain-specific, procedural knowledge
- Test skills before claiming they work
- Keep skills self-contained with no cross-dependencies
- Reference bundled resources explicitly so Claude knows they exist

## Skill Completion Checklist

Before marking a skill as complete:

```bash
# [ ] SKILL.md exists with valid YAML frontmatter
grep -A 2 "^---$" skills/YOUR-SKILL/SKILL.md

# [ ] Skill name matches directory name
basename skills/YOUR-SKILL/

# [ ] If in marketplace.json, path is correct
grep "YOUR-SKILL" .claude-plugin/marketplace.json

# [ ] marketplace.json is valid JSON
cat .claude-plugin/marketplace.json | python3 -m json.tool > /dev/null

# [ ] Skills uses imperative form (not second-person)
# [ ] Skill tested in Claude Code (manual)
# [ ] No shared dependencies with other skills
```

## Important Notes

- These are **reference examples**, not guaranteed to match production Claude behavior
- Document skills are **point-in-time snapshots**, not actively maintained
- Each skill is self-contained - no shared dependencies between skills
- Skills should focus on procedural knowledge that no model can fully possess
- Avoid generic development practices - focus on domain-specific workflows
