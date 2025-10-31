#!/usr/bin/env python3
"""
CLAUDE.md Updater
Updates existing CLAUDE.md when project changes are detected.
Preserves user customizations while updating auto-generated sections.
"""

import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple


class ClaudeMdUpdater:
    """Updates existing CLAUDE.md with new analysis data"""

    def __init__(self, existing_claude_md: str, arch_data: Dict, decisions_data: Dict):
        self.existing = existing_claude_md
        self.arch = arch_data
        self.decisions = decisions_data
        self.sections = self._parse_sections(existing_claude_md)

    def _parse_sections(self, content: str) -> Dict[str, str]:
        """Parse CLAUDE.md into sections"""
        sections = {}
        current_section = None
        current_content = []

        for line in content.split("\n"):
            # Match ## Section headers
            match = re.match(r"^##\s+(.+)$", line)
            if match:
                if current_section:
                    sections[current_section] = "\n".join(current_content)
                current_section = match.group(1)
                current_content = [line]
            else:
                current_content.append(line)

        # Add last section
        if current_section:
            sections[current_section] = "\n".join(current_content)

        return sections

    def update(self) -> Tuple[str, List[str]]:
        """Update CLAUDE.md and return (updated_content, changes_made)"""
        changes = []

        # Update tool decisions if changed
        if self._tool_decisions_changed():
            self._update_tool_decisions()
            changes.append("Updated tool decisions (package manager, linter, etc.)")

        # Update quality commands
        if self._quality_commands_changed():
            self._update_quality_commands()
            changes.append("Updated quality check commands")

        # Update mandatory packages
        if self._mandatory_packages_changed():
            self._update_mandatory_packages()
            changes.append("Updated mandatory package list")

        # Reconstruct document
        updated = self._reconstruct()
        return updated, changes

    def _tool_decisions_changed(self) -> bool:
        """Check if tool decisions section needs updating"""
        tool_section = self.sections.get("🔧 Tool Decisions")
        if not tool_section:
            return True

        # Check if any decision is different from what's documented
        pm = self.decisions.get("package_manager")
        if pm and pm not in tool_section:
            return True

        sm = self.decisions.get("state_management")
        if sm and sm not in tool_section:
            return True

        return False

    def _update_tool_decisions(self):
        """Update tool decisions section"""
        section = "## 🔧 Tool Decisions\n\n"
        section += "**These are the tools chosen for this project. Use these, not alternatives:**\n\n"

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

        if items:
            section += "\n".join(items)

        self.sections["🔧 Tool Decisions"] = section

    def _quality_commands_changed(self) -> bool:
        """Check if quality commands need updating"""
        critical_section = self.sections.get("🚨 Critical Requirements")
        if not critical_section:
            return True

        # Check if quality command matches current setup
        quality_cmd = self._get_quality_command()
        if quality_cmd and quality_cmd not in critical_section:
            return True

        return False

    def _update_quality_commands(self):
        """Update quality check commands"""
        critical_section = self.sections.get("🚨 Critical Requirements", "")

        quality_cmd = self._get_quality_command()
        if quality_cmd:
            # Replace the code block in Zero Tolerance Policy
            pattern = r"```bash\n.*?```"
            replacement = f"```bash\n{quality_cmd}  # MUST show: \"No issues found!\"\n```"

            if re.search(pattern, critical_section):
                critical_section = re.sub(pattern, replacement, critical_section, count=1)
            else:
                # Add if not present
                lines = critical_section.split("\n")
                # Insert after "### Zero Tolerance Policy"
                for i, line in enumerate(lines):
                    if "Zero Tolerance Policy" in line:
                        lines.insert(i + 1, replacement)
                        break
                critical_section = "\n".join(lines)

            self.sections["🚨 Critical Requirements"] = critical_section

    def _get_quality_command(self) -> str:
        """Get quality command for tech stack"""
        stack = self.arch.get("tech_stack")

        if stack == "flutter":
            return "flutter analyze"
        elif stack == "python":
            linter = self.decisions.get("linter")
            if linter == "ruff":
                return "ruff check ."
            elif linter:
                return f"{linter.lower()} ."
        elif stack in ["react", "nextjs", "vue", "nodejs"]:
            if self.decisions.get("linter"):
                pm = self.decisions.get("package_manager", "npm")
                return f"{pm} run lint"

        return None

    def _mandatory_packages_changed(self) -> bool:
        """Check if mandatory packages have changed"""
        current_packages = self.arch.get("mandatory_packages", [])
        if not current_packages:
            return False

        pkg_section = self.sections.get("📦 Mandatory Package Usage")
        if not pkg_section:
            return True

        # Check if all packages are documented
        for pkg in current_packages:
            if pkg["name"] not in pkg_section:
                return True

        return False

    def _update_mandatory_packages(self):
        """Update mandatory packages section"""
        packages = self.arch.get("mandatory_packages", [])
        if not packages:
            return

        section = "## 📦 Mandatory Package Usage\n\n"
        section += "**These internal packages MUST be used. Never duplicate their functionality:**\n\n"

        for pkg in packages:
            name = pkg["name"]
            section += f"### {name}\n"
            section += f"**Location**: `{pkg['path']}`\n\n"
            section += f"**Search before creating**:\n"
            section += f"```bash\n"
            section += f"grep -r \"search_term\" {pkg['path']}/lib/\n"
            section += f"```\n\n"

        self.sections["📦 Mandatory Package Usage"] = section

    def _reconstruct(self) -> str:
        """Reconstruct CLAUDE.md from sections"""
        # Order sections logically
        section_order = [
            "header",  # Special: everything before first ##
            "🚨 Critical Requirements",
            "🔧 Tool Decisions",
            "🏗️ Architecture Rules",
            "📦 Mandatory Package Usage",
            "🔄 Development Workflow",
            "🚫 Anti-Patterns (Never Do This)",
            "✅ Task Completion Checklist",
            "🔍 Quick Reference Commands"
        ]

        output = []

        # Add header (content before first section)
        lines = self.existing.split("\n")
        header_lines = []
        for line in lines:
            if line.startswith("## "):
                break
            header_lines.append(line)

        if header_lines:
            output.append("\n".join(header_lines).strip())

        # Add sections in order
        for section_key in section_order:
            if section_key == "header":
                continue

            content = self.sections.get(section_key)
            if content:
                output.append(content.strip())

        # Add any custom sections not in the order
        for section_key, content in self.sections.items():
            if section_key not in section_order:
                output.append(content.strip())

        return "\n\n".join(output)


def main():
    if len(sys.argv) < 4:
        print("Usage: update_claude_md.py <existing_claude_md> <arch_json> <decisions_json>", file=sys.stderr)
        sys.exit(1)

    claude_md_file = sys.argv[1]
    arch_file = sys.argv[2]
    decisions_file = sys.argv[3]

    with open(claude_md_file) as f:
        existing_content = f.read()

    with open(arch_file) as f:
        arch_data = json.load(f)

    with open(decisions_file) as f:
        decisions_data = json.load(f)

    updater = ClaudeMdUpdater(existing_content, arch_data, decisions_data)
    updated_content, changes = updater.update()

    if changes:
        print("# Changes Made:", file=sys.stderr)
        for change in changes:
            print(f"  - {change}", file=sys.stderr)
        print(file=sys.stderr)

    print(updated_content)


if __name__ == "__main__":
    main()
