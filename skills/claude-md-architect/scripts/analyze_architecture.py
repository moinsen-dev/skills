#!/usr/bin/env python3
"""
Architecture Pattern Analyzer
Detects architectural patterns and design decisions in a codebase.
Outputs JSON for consumption by CLAUDE.md generator.
"""

import json
import os
import re
from pathlib import Path
from typing import Dict, List, Any


class ArchitectureAnalyzer:
    """Analyzes project structure to detect architectural patterns"""

    def __init__(self, project_root: str):
        self.project_root = Path(project_root)
        self.results = {
            "tech_stack": None,
            "architecture_pattern": None,
            "design_patterns": [],
            "layer_structure": {},
            "mandatory_packages": [],
            "key_insights": []
        }

    def analyze(self) -> Dict[str, Any]:
        """Run full architecture analysis"""
        self.detect_tech_stack()
        self.detect_architecture_pattern()
        self.detect_design_patterns()
        self.detect_layer_structure()
        self.detect_mandatory_packages()
        return self.results

    def detect_tech_stack(self):
        """Detect primary technology stack"""
        # Flutter/Dart
        if (self.project_root / "pubspec.yaml").exists():
            self.results["tech_stack"] = "flutter"
            return

        # React/TypeScript/JavaScript
        package_json = self.project_root / "package.json"
        if package_json.exists():
            try:
                with open(package_json) as f:
                    pkg = json.load(f)
                    deps = {**pkg.get("dependencies", {}), **pkg.get("devDependencies", {})}
                    if "react" in deps:
                        self.results["tech_stack"] = "react"
                    elif "next" in deps:
                        self.results["tech_stack"] = "nextjs"
                    elif "@angular/core" in deps:
                        self.results["tech_stack"] = "angular"
                    elif "vue" in deps:
                        self.results["tech_stack"] = "vue"
                    else:
                        self.results["tech_stack"] = "nodejs"
                    return
            except:
                pass

        # Python
        if any((self.project_root / f).exists() for f in ["requirements.txt", "pyproject.toml", "setup.py", "Pipfile"]):
            self.results["tech_stack"] = "python"
            return

        # Go
        if (self.project_root / "go.mod").exists():
            self.results["tech_stack"] = "go"
            return

        # Rust
        if (self.project_root / "Cargo.toml").exists():
            self.results["tech_stack"] = "rust"
            return

        self.results["tech_stack"] = "unknown"

    def detect_architecture_pattern(self):
        """Detect primary architectural pattern"""
        stack = self.results["tech_stack"]

        if stack == "flutter":
            self._detect_flutter_architecture()
        elif stack in ["react", "nextjs", "vue", "angular"]:
            self._detect_frontend_architecture()
        elif stack == "python":
            self._detect_python_architecture()
        else:
            self.results["architecture_pattern"] = "unknown"

    def _detect_flutter_architecture(self):
        """Detect Flutter-specific architecture"""
        # Check for Clean Architecture
        lib_path = self.project_root / "lib"
        if not lib_path.exists():
            return

        subdirs = [d.name for d in lib_path.iterdir() if d.is_dir()]

        # Clean Architecture indicators
        clean_arch_markers = {"domain", "data", "presentation"}
        if clean_arch_markers.issubset(set(subdirs)):
            self.results["architecture_pattern"] = "clean_architecture"
            self.results["key_insights"].append("Clean Architecture with domain/data/presentation layers")
            return

        # Feature-first
        if "features" in subdirs:
            self.results["architecture_pattern"] = "feature_first"
            self.results["key_insights"].append("Feature-first organization")
            return

        # Check for packages (monorepo)
        packages_path = self.project_root / "packages"
        if packages_path.exists():
            package_dirs = [d.name for d in packages_path.iterdir() if d.is_dir()]
            self.results["architecture_pattern"] = "monorepo"
            self.results["key_insights"].append(f"Monorepo with {len(package_dirs)} packages")

            # Check for atomic design
            if any("atomic" in p.lower() or "components" in p.lower() for p in package_dirs):
                self.results["design_patterns"].append("atomic_design")
                self.results["key_insights"].append("Atomic Design pattern detected")

    def _detect_frontend_architecture(self):
        """Detect React/Vue/Angular architecture"""
        src_path = self.project_root / "src"
        if not src_path.exists():
            return

        subdirs = [d.name for d in src_path.iterdir() if d.is_dir()]

        # Component-based architecture
        if "components" in subdirs:
            self.results["architecture_pattern"] = "component_based"

            # Check for atomic design
            comp_path = src_path / "components"
            comp_subdirs = [d.name for d in comp_path.iterdir() if d.is_dir()]
            atomic_markers = {"atoms", "molecules", "organisms", "templates"}
            if atomic_markers.intersection(set(comp_subdirs)):
                self.results["design_patterns"].append("atomic_design")
                self.results["key_insights"].append("Atomic Design pattern detected")

        # Feature-based
        if "features" in subdirs:
            self.results["architecture_pattern"] = "feature_based"
            self.results["key_insights"].append("Feature-based organization")

    def _detect_python_architecture(self):
        """Detect Python architecture patterns"""
        # Check for common patterns
        subdirs = [d.name for d in self.project_root.iterdir() if d.is_dir() and not d.name.startswith('.')]

        # Django
        if "manage.py" in [f.name for f in self.project_root.iterdir()]:
            self.results["architecture_pattern"] = "django_mvt"
            return

        # Flask/FastAPI patterns
        if any(pattern in subdirs for pattern in ["api", "routes", "endpoints"]):
            if "models" in subdirs and "services" in subdirs:
                self.results["architecture_pattern"] = "layered"
                return

    def detect_design_patterns(self):
        """Detect additional design patterns"""
        # Already partially detected in architecture detection
        pass

    def detect_layer_structure(self):
        """Detect and document layer structure"""
        stack = self.results["tech_stack"]
        arch = self.results["architecture_pattern"]

        if stack == "flutter" and arch == "clean_architecture":
            lib_path = self.project_root / "lib"
            self.results["layer_structure"] = {
                "domain": "Business logic and entities (no external dependencies)",
                "data": "Repositories, data sources, models",
                "presentation": "UI, widgets, state management"
            }

        # Add more layer structures for other architectures as needed

    def detect_mandatory_packages(self):
        """Detect packages that must be used (monorepo internal packages)"""
        stack = self.results["tech_stack"]

        if stack == "flutter":
            packages_path = self.project_root / "packages"
            if packages_path.exists():
                for pkg_dir in packages_path.iterdir():
                    if pkg_dir.is_dir() and (pkg_dir / "pubspec.yaml").exists():
                        self.results["mandatory_packages"].append({
                            "name": pkg_dir.name,
                            "path": str(pkg_dir.relative_to(self.project_root))
                        })


def main():
    import sys

    if len(sys.argv) < 2:
        print("Usage: analyze_architecture.py <project_root>", file=sys.stderr)
        sys.exit(1)

    project_root = sys.argv[1]
    analyzer = ArchitectureAnalyzer(project_root)
    results = analyzer.analyze()

    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
