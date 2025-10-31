#!/usr/bin/env python3
"""
CLAUDE.md Generator
Generates LLM-optimized CLAUDE.md files from analysis data.
Focuses on context efficiency, structured patterns, and actionable rules.
"""

import json
import sys
from pathlib import Path
from typing import Dict, Any, List


class ClaudeMdGenerator:
    """Generates CLAUDE.md optimized for LLM consumption"""

    def __init__(self, architecture_data: Dict, decisions_data: Dict, project_name: str = None):
        self.arch = architecture_data
        self.decisions = decisions_data
        self.project_name = project_name or "Project"
        self.sections = []

    def generate(self) -> str:
        """Generate complete CLAUDE.md content"""
        self.sections = []

        self._add_header()
        self._add_critical_requirements()
        self._add_tool_decisions()
        self._add_architecture_rules()

        if self.arch.get("mandatory_packages"):
            self._add_mandatory_packages()

        self._add_development_workflow()
        self._add_anti_patterns()
        self._add_quality_checklist()
        self._add_quick_reference()

        return "\n\n".join(self.sections)

    def _add_header(self):
        """Add document header"""
        tech = self.arch.get("tech_stack", "Unknown").title()
        arch = self.arch.get("architecture_pattern", "").replace("_", " ").title()

        header = f"# {self.project_name} Development Rules"

        if arch:
            header += f"\n\n**ARCHITECTURE**: {arch}"
        if tech != "Unknown":
            header += f"\n**TECH STACK**: {tech}"

        self.sections.append(header)

    def _add_critical_requirements(self):
        """Add zero-tolerance quality rules"""
        section = "## 🚨 Critical Requirements\n\n### Zero Tolerance Policy"

        # Add quality command based on tech stack
        quality_cmd = self._get_quality_command()
        if quality_cmd:
            section += f"\n```bash\n{quality_cmd}  # MUST show: \"No issues found!\"\n```"

        section += "\n- **NO WARNINGS** - Fix immediately, no exceptions"
        section += "\n- **NO ERRORS** - Code must compile cleanly"
        section += "\n- **NO INCOMPLETE TASKS** - Run quality checks before marking done"

        self.sections.append(section)

    def _get_quality_command(self) -> str:
        """Get the quality check command for the tech stack"""
        stack = self.arch.get("tech_stack")

        if stack == "flutter":
            return "flutter analyze"
        elif stack == "python":
            linter = self.decisions.get("linter")
            if linter == "ruff":
                return "ruff check ."
            elif linter:
                return f"{linter.lower()} ."
            return "# Configure linter"
        elif stack in ["react", "nextjs", "vue", "nodejs"]:
            if self.decisions.get("linter") == "ESLint":
                return "npm run lint"  # or pnpm/yarn based on package manager
        return None

    def _add_tool_decisions(self):
        """Add tool choice section - WHICH tools to use"""
        section = "## 🔧 Tool Decisions\n\n"
        section += "**These are the tools chosen for this project. Use these, not alternatives:**\n"

        decisions_map = {
            "package_manager": "Package Manager",
            "state_management": "State Management",
            "testing_framework": "Testing",
            "linter": "Linter",
            "formatter": "Code Formatter"
        }

        items = []
        for key, label in decisions_map.items():
            value = self.decisions.get(key)
            if value:
                items.append(f"- **{label}**: `{value}`")

        if self.decisions.get("quality_tools"):
            tools = ", ".join(f"`{t}`" for t in self.decisions["quality_tools"])
            items.append(f"- **Quality Tools**: {tools}")

        if items:
            section += "\n".join(items)
        else:
            section += "*No specific tool decisions detected*"

        self.sections.append(section)

    def _add_architecture_rules(self):
        """Add architecture-specific rules"""
        arch = self.arch.get("architecture_pattern")
        if not arch:
            return

        section = "## 🏗️ Architecture Rules\n\n"

        if arch == "clean_architecture":
            section += self._clean_architecture_rules()
        elif arch == "monorepo":
            section += self._monorepo_rules()
        elif arch == "feature_first" or arch == "feature_based":
            section += self._feature_first_rules()
        elif arch == "component_based":
            section += self._component_based_rules()
        else:
            section += f"**Pattern**: {arch.replace('_', ' ').title()}\n\n"
            section += "*Document specific architectural rules and constraints*"

        # Add design patterns
        if self.arch.get("design_patterns"):
            section += "\n\n### Design Patterns\n"
            for pattern in self.arch["design_patterns"]:
                if pattern == "atomic_design":
                    section += "\n**Atomic Design**: Build UI from atoms → molecules → organisms → templates"

        self.sections.append(section)

    def _clean_architecture_rules(self) -> str:
        """Rules for Clean Architecture"""
        return """**Clean Architecture Layers**:

```
domain/     → Pure business logic (no external dependencies)
data/       → Repositories, data sources, API clients
presentation/ → UI, widgets, state management
```

**Dependency Rule**:
- ✅ presentation → domain ← data
- ❌ domain cannot depend on data or presentation
- ❌ Never import UI code into domain layer"""

    def _monorepo_rules(self) -> str:
        """Rules for monorepo structure"""
        return """**Monorepo Structure**:

This project uses multiple packages. Always check if functionality exists in a package before creating new code.

**Package Discovery**:
```bash
# List available packages
ls packages/

# Search for functionality across packages
grep -r "search_term" packages/*/lib/
```"""

    def _feature_first_rules(self) -> str:
        """Rules for feature-first architecture"""
        return """**Feature-First Organization**:

Each feature is self-contained with its own:
- UI components
- Business logic
- Data layer
- Tests

**Rule**: Keep feature code isolated. Shared code goes in `core/` or `shared/`."""

    def _component_based_rules(self) -> str:
        """Rules for component-based architecture"""
        return """**Component-Based Architecture**:

UI is built from reusable components.

**Before creating a component**:
```bash
# Search existing components
find src/components -name "*.tsx" -o -name "*.jsx"
grep -r "ComponentName" src/components/
```"""

    def _add_mandatory_packages(self):
        """Add mandatory package usage rules"""
        section = "## 📦 Mandatory Package Usage\n\n"
        section += "**These internal packages MUST be used. Never duplicate their functionality:**\n\n"

        for pkg in self.arch["mandatory_packages"]:
            name = pkg["name"]
            section += f"### {name}\n"
            section += f"**Location**: `{pkg['path']}`\n\n"
            section += f"**Search before creating**:\n"
            section += f"```bash\n"
            section += f"# Check what exists in {name}\n"
            section += f"ls {pkg['path']}/lib/\n"
            section += f"grep -r \"search_term\" {pkg['path']}/lib/\n"
            section += f"```\n\n"

        self.sections.append(section)

    def _add_development_workflow(self):
        """Add development workflow section"""
        section = "## 🔄 Development Workflow\n\n"

        # Add architecture-specific workflow
        arch = self.arch.get("architecture_pattern")

        if self.arch.get("mandatory_packages"):
            section += "### Starting Any Task\n\n"
            section += "**Step 1**: Search existing packages\n```bash\n"
            for pkg in self.arch["mandatory_packages"]:
                section += f"grep -r \"functionality\" {pkg['path']}/lib/\n"
            section += "```\n\n"
            section += "**Step 2**: Reuse existing code\n"
            section += "**Step 3**: Only create new code if nothing exists\n\n"

        # Add testing workflow
        if self.decisions.get("testing_framework"):
            section += "### Before Completing Task\n\n"
            section += "```bash\n"

            quality_cmd = self._get_quality_command()
            if quality_cmd:
                section += f"{quality_cmd}  # Must pass\n"

            test_cmd = self._get_test_command()
            if test_cmd:
                section += f"{test_cmd}  # Must pass\n"

            section += "```\n"

        self.sections.append(section)

    def _get_test_command(self) -> str:
        """Get test command for the tech stack"""
        stack = self.arch.get("tech_stack")
        test_framework = self.decisions.get("testing_framework")

        if stack == "flutter":
            return "flutter test"
        elif stack == "python":
            if test_framework == "pytest":
                return "pytest"
            return "python -m unittest"
        elif stack in ["react", "nextjs", "nodejs"]:
            pm = self.decisions.get("package_manager", "npm")
            return f"{pm} test"
        return None

    def _add_anti_patterns(self):
        """Add anti-patterns section"""
        section = "## 🚫 Anti-Patterns (Never Do This)\n\n"

        # Architecture-specific anti-patterns
        arch = self.arch.get("architecture_pattern")

        if arch == "clean_architecture":
            section += "### Clean Architecture Violations\n\n"
            section += "```dart\n"
            section += "// ❌ WRONG: UI import in domain layer\n"
            section += "import 'package:flutter/material.dart';  // NO! Domain must be pure\n\n"
            section += "// ❌ WRONG: Data source in presentation\n"
            section += "final api = ApiClient();  // NO! Use repository from domain\n\n"
            section += "// ✅ CORRECT: Pure domain entity\n"
            section += "class User {\n"
            section += "  final String id;\n"
            section += "  // No Flutter, no API dependencies\n"
            section += "}\n"
            section += "```\n\n"

        # Package-specific anti-patterns
        if self.arch.get("mandatory_packages"):
            section += "### Code Duplication\n\n"
            for pkg in self.arch["mandatory_packages"]:
                section += f"```bash\n"
                section += f"# ❌ WRONG: Recreating functionality from {pkg['name']}\n"
                section += f"# Always search first:\n"
                section += f"grep -r \"ClassName\" {pkg['path']}/lib/\n"
                section += f"```\n\n"

        self.sections.append(section)

    def _add_quality_checklist(self):
        """Add quality checklist"""
        section = "## ✅ Task Completion Checklist\n\n"
        section += "**Task is ONLY complete when ALL items pass:**\n\n"

        items = []

        # Quality command
        quality_cmd = self._get_quality_command()
        if quality_cmd:
            items.append(f"- [ ] `{quality_cmd}` shows no issues")

        # Tests
        test_cmd = self._get_test_command()
        if test_cmd:
            items.append(f"- [ ] `{test_cmd}` all pass")

        # Generic checks
        items.append("- [ ] No warnings in IDE")
        items.append("- [ ] No TODO/FIXME in new code")

        # Architecture-specific checks
        if self.arch.get("mandatory_packages"):
            items.append("- [ ] Verified no code duplication from internal packages")

        if items:
            section += "\n".join(items)

        section += "\n\n**If ANY item fails → Task incomplete**"

        self.sections.append(section)

    def _add_quick_reference(self):
        """Add quick reference commands"""
        section = "## 🔍 Quick Reference Commands\n\n"

        # Package search
        if self.arch.get("mandatory_packages"):
            section += "### Search Internal Packages\n```bash\n"
            for pkg in self.arch["mandatory_packages"]:
                section += f"# Search {pkg['name']}\n"
                section += f"grep -ri \"search_term\" {pkg['path']}/lib/\n"
            section += "```\n\n"

        # Quality checks
        section += "### Quality Checks\n```bash\n"

        quality_cmd = self._get_quality_command()
        if quality_cmd:
            section += f"# Run linter\n{quality_cmd}\n\n"

        test_cmd = self._get_test_command()
        if test_cmd:
            section += f"# Run tests\n{test_cmd}\n\n"

        # Formatter
        formatter = self.decisions.get("formatter")
        if formatter:
            if formatter == "Prettier":
                pm = self.decisions.get("package_manager", "npm")
                section += f"# Format code\n{pm} run format\n\n"
            elif formatter == "black":
                section += "# Format code\nblack .\n\n"
            elif self.arch.get("tech_stack") == "flutter":
                section += "# Format code\ndart format lib/\n\n"

        section += "```"

        self.sections.append(section)


def main():
    if len(sys.argv) < 4:
        print("Usage: generate_claude_md.py <arch_json> <decisions_json> <project_name>", file=sys.stderr)
        sys.exit(1)

    arch_file = sys.argv[1]
    decisions_file = sys.argv[2]
    project_name = sys.argv[3]

    with open(arch_file) as f:
        arch_data = json.load(f)

    with open(decisions_file) as f:
        decisions_data = json.load(f)

    generator = ClaudeMdGenerator(arch_data, decisions_data, project_name)
    claude_md = generator.generate()

    print(claude_md)


if __name__ == "__main__":
    main()
