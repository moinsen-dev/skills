#!/usr/bin/env python3
"""
Decision Detector
Identifies tool choices, framework decisions, and conventions.
These are the "WHICH tool to use" decisions that AI needs to know.
"""

import json
import os
import re
from pathlib import Path
from typing import Dict, List, Any


class DecisionDetector:
    """Detects project decisions and tool choices"""

    def __init__(self, project_root: str):
        self.project_root = Path(project_root)
        self.decisions = {
            "package_manager": None,
            "state_management": None,
            "testing_framework": None,
            "linter": None,
            "formatter": None,
            "quality_tools": [],
            "key_dependencies": [],
            "conventions": []
        }

    def analyze(self) -> Dict[str, Any]:
        """Run full decision detection"""
        tech_stack = self._detect_tech_stack()

        if tech_stack == "flutter":
            self._analyze_flutter_decisions()
        elif tech_stack in ["react", "nextjs", "vue"]:
            self._analyze_frontend_decisions()
        elif tech_stack == "python":
            self._analyze_python_decisions()
        elif tech_stack == "nodejs":
            self._analyze_nodejs_decisions()

        return self.decisions

    def _detect_tech_stack(self) -> str:
        """Quick tech stack detection"""
        if (self.project_root / "pubspec.yaml").exists():
            return "flutter"
        elif (self.project_root / "package.json").exists():
            try:
                with open(self.project_root / "package.json") as f:
                    pkg = json.load(f)
                    deps = {**pkg.get("dependencies", {}), **pkg.get("devDependencies", {})}
                    if "react" in deps:
                        return "react"
                    elif "next" in deps:
                        return "nextjs"
                    elif "vue" in deps:
                        return "vue"
                    return "nodejs"
            except:
                pass
        elif any((self.project_root / f).exists() for f in ["requirements.txt", "pyproject.toml"]):
            return "python"
        return "unknown"

    def _analyze_flutter_decisions(self):
        """Analyze Flutter project decisions"""
        pubspec_path = self.project_root / "pubspec.yaml"

        try:
            import yaml
            with open(pubspec_path) as f:
                pubspec = yaml.safe_load(f)
        except ImportError:
            # Fallback: simple text parsing
            with open(pubspec_path) as f:
                pubspec_text = f.read()
                self._parse_flutter_text(pubspec_text)
                return

        # Package manager (always pub/flutter pub for Flutter)
        self.decisions["package_manager"] = "flutter_pub"

        # State management
        deps = {**pubspec.get("dependencies", {}), **pubspec.get("dev_dependencies", {})}

        state_mgmt_libs = {
            "flutter_riverpod": "Riverpod",
            "riverpod": "Riverpod",
            "flutter_bloc": "BLoC",
            "bloc": "BLoC",
            "provider": "Provider",
            "get": "GetX",
            "mobx": "MobX"
        }

        for lib, name in state_mgmt_libs.items():
            if lib in deps:
                self.decisions["state_management"] = name
                break

        # Testing
        if "flutter_test" in deps:
            self.decisions["testing_framework"] = "flutter_test"
            self.decisions["quality_tools"].append("flutter test")

        if "integration_test" in deps:
            self.decisions["quality_tools"].append("integration_test")

        # Linter/Analyzer
        analysis_options = self.project_root / "analysis_options.yaml"
        if analysis_options.exists():
            self.decisions["linter"] = "flutter_analyze"
            self.decisions["quality_tools"].append("flutter analyze")

            # Check for strict linting
            try:
                with open(analysis_options) as f:
                    analysis_text = f.read()
                    if "flutter_lints" in analysis_text or "lints" in analysis_text:
                        self.decisions["conventions"].append("Uses flutter_lints for strict analysis")
            except:
                pass

        # Key architectural dependencies
        important_deps = ["go_router", "dio", "hive", "sqflite", "firebase_core", "freezed", "json_serializable"]
        for dep in important_deps:
            if dep in deps:
                self.decisions["key_dependencies"].append(dep)

    def _parse_flutter_text(self, pubspec_text: str):
        """Fallback text-based parsing for Flutter pubspec.yaml"""
        # State management
        if "riverpod" in pubspec_text:
            self.decisions["state_management"] = "Riverpod"
        elif "bloc" in pubspec_text:
            self.decisions["state_management"] = "BLoC"
        elif "provider" in pubspec_text:
            self.decisions["state_management"] = "Provider"

        # Testing
        if "flutter_test" in pubspec_text:
            self.decisions["testing_framework"] = "flutter_test"

    def _analyze_frontend_decisions(self):
        """Analyze React/Next.js/Vue decisions"""
        package_json_path = self.project_root / "package.json"

        try:
            with open(package_json_path) as f:
                pkg = json.load(f)
        except:
            return

        deps = {**pkg.get("dependencies", {}), **pkg.get("devDependencies", {})}

        # Package manager detection
        if (self.project_root / "pnpm-lock.yaml").exists():
            self.decisions["package_manager"] = "pnpm"
        elif (self.project_root / "yarn.lock").exists():
            self.decisions["package_manager"] = "yarn"
        elif (self.project_root / "package-lock.json").exists():
            self.decisions["package_manager"] = "npm"
        elif (self.project_root / "bun.lockb").exists():
            self.decisions["package_manager"] = "bun"

        # State management (React)
        state_mgmt = {
            "redux": "Redux",
            "@reduxjs/toolkit": "Redux Toolkit",
            "zustand": "Zustand",
            "jotai": "Jotai",
            "recoil": "Recoil",
            "mobx": "MobX",
            "@tanstack/react-query": "React Query"
        }

        for lib, name in state_mgmt.items():
            if lib in deps:
                self.decisions["state_management"] = name
                break

        # Testing
        testing_libs = {
            "jest": "Jest",
            "vitest": "Vitest",
            "@testing-library/react": "React Testing Library",
            "cypress": "Cypress",
            "playwright": "Playwright"
        }

        frameworks = []
        for lib, name in testing_libs.items():
            if lib in deps:
                frameworks.append(name)

        if frameworks:
            self.decisions["testing_framework"] = " + ".join(frameworks)

        # Linter
        if "eslint" in deps:
            self.decisions["linter"] = "ESLint"

        # Formatter
        if "prettier" in deps:
            self.decisions["formatter"] = "Prettier"

        # TypeScript
        if "typescript" in deps:
            self.decisions["conventions"].append("TypeScript for type safety")

    def _analyze_python_decisions(self):
        """Analyze Python project decisions"""
        # Package manager
        if (self.project_root / "uv.lock").exists():
            self.decisions["package_manager"] = "uv"
        elif (self.project_root / "poetry.lock").exists():
            self.decisions["package_manager"] = "poetry"
        elif (self.project_root / "Pipfile").exists():
            self.decisions["package_manager"] = "pipenv"
        elif (self.project_root / "requirements.txt").exists():
            self.decisions["package_manager"] = "pip"

        # Testing
        if (self.project_root / "pytest.ini").exists() or self._check_pyproject_tool("pytest"):
            self.decisions["testing_framework"] = "pytest"
        elif self._check_file_contains("unittest"):
            self.decisions["testing_framework"] = "unittest"

        # Linter
        if self._check_pyproject_tool("ruff"):
            self.decisions["linter"] = "ruff"
        elif self._check_pyproject_tool("flake8"):
            self.decisions["linter"] = "flake8"
        elif self._check_pyproject_tool("pylint"):
            self.decisions["linter"] = "pylint"

        # Formatter
        if self._check_pyproject_tool("black"):
            self.decisions["formatter"] = "black"
        elif self._check_pyproject_tool("ruff"):
            if not self.decisions["formatter"]:
                self.decisions["formatter"] = "ruff format"

        # Type checker
        if self._check_pyproject_tool("mypy"):
            self.decisions["quality_tools"].append("mypy")

    def _analyze_nodejs_decisions(self):
        """Analyze Node.js project decisions"""
        package_json_path = self.project_root / "package.json"

        try:
            with open(package_json_path) as f:
                pkg = json.load(f)
        except:
            return

        deps = {**pkg.get("dependencies", {}), **pkg.get("devDependencies", {})}

        # Package manager
        if (self.project_root / "pnpm-lock.yaml").exists():
            self.decisions["package_manager"] = "pnpm"
        elif (self.project_root / "yarn.lock").exists():
            self.decisions["package_manager"] = "yarn"
        elif (self.project_root / "bun.lockb").exists():
            self.decisions["package_manager"] = "bun"
        else:
            self.decisions["package_manager"] = "npm"

        # Testing
        if "jest" in deps:
            self.decisions["testing_framework"] = "Jest"
        elif "mocha" in deps:
            self.decisions["testing_framework"] = "Mocha"
        elif "vitest" in deps:
            self.decisions["testing_framework"] = "Vitest"

        # Linter
        if "eslint" in deps:
            self.decisions["linter"] = "ESLint"

        # Formatter
        if "prettier" in deps:
            self.decisions["formatter"] = "Prettier"

        # TypeScript
        if "typescript" in deps:
            self.decisions["conventions"].append("TypeScript for type safety")

    def _check_pyproject_tool(self, tool: str) -> bool:
        """Check if tool is configured in pyproject.toml"""
        pyproject = self.project_root / "pyproject.toml"
        if not pyproject.exists():
            return False

        try:
            with open(pyproject) as f:
                content = f.read()
                return f"[tool.{tool}]" in content or f'"{tool}"' in content
        except:
            return False

    def _check_file_contains(self, text: str) -> bool:
        """Check if any Python file contains text"""
        for py_file in self.project_root.rglob("*.py"):
            if py_file.stat().st_size > 100000:  # Skip large files
                continue
            try:
                with open(py_file) as f:
                    if text in f.read():
                        return True
            except:
                pass
        return False


def main():
    import sys

    if len(sys.argv) < 2:
        print("Usage: detect_decisions.py <project_root>", file=sys.stderr)
        sys.exit(1)

    project_root = sys.argv[1]
    detector = DecisionDetector(project_root)
    results = detector.analyze()

    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
