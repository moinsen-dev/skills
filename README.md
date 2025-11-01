# Skills

Skills are folders of instructions, scripts, and resources that Claude loads dynamically to improve performance on specialized tasks. Skills teach Claude how to complete specific tasks in a repeatable way, whether that's creating documents with your company's brand guidelines, analyzing data using your organization's specific workflows, or automating personal tasks.

For more information, check out:
- [What are skills?](https://support.claude.com/en/articles/12512176-what-are-skills)
- [Using skills in Claude](https://support.claude.com/en/articles/12512180-using-skills-in-claude)
- [How to create custom skills](https://support.claude.com/en/articles/12512198-creating-custom-skills)
- [Equipping agents for the real world with Agent Skills](https://anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)

# About This Repository

This repository is **based on Anthropic's original [example skills repository](https://github.com/anthropics/anthropic-skills)**, but has been restructured and reorganized to follow a more semantic, domain-focused approach to skill organization.

## What Changed

**Original Structure:**
- `document-skills` - Document processing
- `example-skills` - Everything else (mixed domains)

**New Structure:**
- **`product-management`** - Strategic product development skills
- **`development`** - Software development tools
- **`design`** - Visual and creative design skills
- **`communication`** - Internal/external communication tools
- **`document-processing`** - Document manipulation skills

This reorganization makes it easier to:
- ✅ Find skills by functional domain
- ✅ Scale the collection as new skills are added
- ✅ Understand skill purpose at a glance
- ✅ Follow Anthropic's patterns while maintaining better organization

## Original vs. Extended

This repository includes:
- ✅ All original Anthropic example skills (restructured by domain)
- ✅ All Anthropic document-processing skills (docx, pdf, pptx, xlsx)
- ✨ New community-contributed skills (like `goal-navigator`)

The skills are open source (Apache 2.0 License). The document-processing skills are source-available reference implementations that demonstrate advanced patterns for working with complex file formats.

**Note:** These are reference examples for inspiration and learning. They showcase general-purpose capabilities rather than organization-specific workflows or sensitive content.

## Disclaimer

**These skills are provided for demonstration and educational purposes only.** While some of these capabilities may be available in Claude, the implementations and behaviors you receive from Claude may differ from what is shown in these examples. These examples are meant to illustrate patterns and possibilities. Always test skills thoroughly in your own environment before relying on them for critical tasks.

# Skills by Category

## Product Management

Strategic product development skills for planning, prioritization, and decision-making.

- **product-shaper** - Interactive PRD generator that captures ideas through guided conversation, using empathy-first thinking and ruthless simplification
- **goal-navigator** - Strategic consultant that analyzes project state (PID/PRD, feature matrices) and provides data-driven recommendations on what to build next

## Development

Software development tools for building applications, testing, and developer workflows.

- **mcp-builder** - Guide for creating high-quality MCP servers to integrate external APIs and services (Python FastMCP or Node/TypeScript SDK)
- **claude-md-architect** - Analyzes project architecture and generates context-efficient CLAUDE.md files optimized for AI agent consumption
- **skill-creator** - Comprehensive guide for creating effective skills that extend Claude's capabilities
- **artifacts-builder** - Build complex claude.ai HTML artifacts using React, Tailwind CSS, and shadcn/ui components
- **webapp-testing** - Test local web applications using Playwright for UI verification and debugging

## Design

Visual and creative design skills for art generation, styling, and brand consistency.

- **canvas-design** - Create beautiful visual art in .png and .pdf formats using design philosophy
- **algorithmic-art** - Create generative art using p5.js with seeded randomness, flow fields, and particle systems
- **theme-factory** - Style artifacts with 10 pre-set professional themes or generate custom themes on-the-fly
- **brand-guidelines** - Apply Anthropic's official brand colors and typography to artifacts

## Communication

Internal and external communication tools for writing, formatting, and visual messaging.

- **internal-comms** - Write internal communications like status reports, leadership updates, newsletters, FAQs, and incident reports
- **slack-gif-creator** - Create animated GIFs optimized for Slack's size constraints with composable animation primitives

## Document Processing

Advanced document manipulation skills for working with complex file formats and binary data.

- **xlsx** - Create, edit, and analyze Excel spreadsheets with support for formulas, formatting, data analysis, and visualization
- **docx** - Create, edit, and analyze Word documents with support for tracked changes, comments, formatting preservation, and text extraction
- **pptx** - Create, edit, and analyze PowerPoint presentations with support for layouts, templates, charts, and automated slide generation
- **pdf** - Comprehensive PDF manipulation toolkit for extracting text and tables, creating new PDFs, merging/splitting documents, and handling forms

**Important Note:** Document-processing skills are point-in-time snapshots from Anthropic and are not actively maintained. They are primarily intended as reference examples to illustrate advanced patterns for complex skills.

# Installation & Usage

## Claude Code

You can register this repository as a Claude Code Plugin marketplace by running:

```bash
/plugin marketplace add <your-github-username>/skills
```

Then, to install a specific category of skills:

1. Select `Browse and install plugins`
2. Select `anthropic-agent-skills`
3. Choose a category:
   - `product-management`
   - `development`
   - `design`
   - `communication`
   - `document-processing`
4. Select `Install now`

Alternatively, directly install a plugin category via:

```bash
/plugin install product-management@anthropic-agent-skills
/plugin install development@anthropic-agent-skills
/plugin install design@anthropic-agent-skills
/plugin install communication@anthropic-agent-skills
/plugin install document-processing@anthropic-agent-skills
```

After installing a plugin category, you can use the skills by mentioning them. For instance:

```
"Use the goal-navigator skill to help me prioritize features for my MVP"
"Use the PDF skill to extract form fields from path/to/file.pdf"
"Use the product-shaper skill to create a PRD for my new idea"
```

## Claude.ai

The original Anthropic example skills are available to paid plans in Claude.ai.

To use skills from this repository or upload custom skills, follow the instructions in [Using skills in Claude](https://support.claude.com/en/articles/12512180-using-skills-in-claude#h_a4222fa77b).

## Claude API

You can use pre-built skills and upload custom skills via the Claude API. See the [Skills API Quickstart](https://docs.claude.com/en/api/skills-guide#creating-a-skill) for more.

# Creating a Custom Skill

Skills are simple to create - just a folder with a `SKILL.md` file containing YAML frontmatter and instructions. Here's the basic structure:

```markdown
---
name: my-skill-name
description: A clear description of what this skill does and when to use it
---

# My Skill Name

[Add your instructions here that Claude will follow when this skill is active]

## Examples
- Example usage 1
- Example usage 2

## Guidelines
- Guideline 1
- Guideline 2
```

The frontmatter requires only two fields:
- `name` - A unique identifier for your skill (lowercase, hyphens for spaces)
- `description` - A complete description of what the skill does and when to use it

The markdown content contains the instructions, examples, and guidelines that Claude will follow.

**For comprehensive guidance on creating effective skills**, use the `skill-creator` skill included in this repository's `development` category, or see [How to create custom skills](https://support.claude.com/en/articles/12512198-creating-custom-skills).

# Contributing

Contributions are welcome! If you've created a skill that could benefit others:

1. Fork this repository
2. Add your skill to the appropriate category folder (or propose a new category)
3. Follow the skill creation guidelines from `skill-creator`
4. Submit a pull request with a clear description

Please ensure your skill:
- Has a clear, specific purpose
- Includes a well-written `SKILL.md` with proper frontmatter
- Follows the patterns demonstrated in existing skills
- Is properly tested and validated

# License

This project is licensed under the **Apache License 2.0** - see the [LICENSE](LICENSE) file for details.

The original Anthropic example skills are also Apache 2.0 licensed. Document-processing skills are source-available reference implementations.

# Attribution

Based on the original [Anthropic Skills Repository](https://github.com/anthropics/anthropic-skills) by Anthropic. Restructured and extended by the community to provide better organization and additional capabilities.

# Partner Skills

Skills are a great way to teach Claude how to get better at using specific pieces of software. As we see awesome example skills from partners, we may highlight some of them here:

- **Notion** - [Notion Skills for Claude](https://www.notion.so/notiondevs/Notion-Skills-for-Claude-28da4445d27180c7af1df7d8615723d0)
