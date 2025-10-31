# Architectural Patterns for CLAUDE.md

This reference documents common architectural patterns and how to express them in CLAUDE.md format (context-efficient, rule-based).

## Clean Architecture

### Detection Indicators
- Folders: `domain/`, `data/`, `presentation/` OR `core/`, `infrastructure/`, `ui/`
- Dependency direction: outer layers depend on inner
- Domain layer has no external dependencies

### CLAUDE.md Rules Template

```markdown
## 🏗️ Clean Architecture Rules

**Layers**:
- `domain/` → Pure business logic (no external dependencies)
- `data/` → Repositories, data sources, API clients
- `presentation/` → UI, state management, widgets

**Dependency Rule**: presentation → domain ← data

**Violations**:
❌ domain importing from data or presentation
❌ domain depending on Flutter/UI frameworks
❌ Entities with UI logic

**Before creating**:
\`\`\`bash
# Check layer
ls lib/domain/entities/  # Business entities
ls lib/data/repositories/  # Data access
ls lib/presentation/pages/  # UI
\`\`\`
```

### Common Anti-Patterns
```markdown
❌ WRONG: UI import in domain
\`\`\`dart
// domain/entities/user.dart
import 'package:flutter/material.dart';  // NO!
\`\`\`

❌ WRONG: Data source in presentation
\`\`\`dart
// presentation/pages/home.dart
final api = ApiClient();  // NO! Use repository from domain
\`\`\`

✅ CORRECT: Pure domain entity
\`\`\`dart
// domain/entities/user.dart
class User {
  final String id;
  final String email;
  // No Flutter, no API dependencies
}
\`\`\`
```

## Feature-First Architecture

### Detection Indicators
- Folder: `features/` or `modules/`
- Each feature is self-contained
- Features may have internal layering

### CLAUDE.md Rules Template

```markdown
## 🏗️ Feature-First Architecture

**Structure**: Each feature is self-contained

\`\`\`
features/
  auth/
    domain/
    data/
    presentation/
  profile/
    ...
shared/  → Code used across features
\`\`\`

**Rules**:
- Features must NOT import from other features
- Shared code goes in `shared/` or `core/`
- Each feature has own tests

**Before creating**:
\`\`\`bash
# Check if feature exists
ls lib/features/

# Check shared code
ls lib/shared/ lib/core/
\`\`\`
```

## Atomic Design

### Detection Indicators
- Folders: `atoms/`, `molecules/`, `organisms/`, `templates/`, `pages/`
- Component composition hierarchy
- Often in component library or UI package

### CLAUDE.md Rules Template

```markdown
## 🏗️ Atomic Design Pattern

**Hierarchy**: atoms → molecules → organisms → templates → pages

- `atoms/` → Basic UI elements (buttons, inputs, icons)
- `molecules/` → Simple combinations (search bar = input + button)
- `organisms/` → Complex sections (header with nav + user menu)
- `templates/` → Page layouts
- `pages/` → Actual screens with data

**Mandatory Rule**: Build UP the hierarchy (never skip levels)

**Before creating UI**:
\`\`\`bash
# Search existing atoms
ls packages/atomic_components/lib/atoms/

# Search molecules
grep -r "ComponentName" packages/atomic_components/lib/molecules/

# Search organisms
find packages/atomic_components/lib/organisms/ -name "*.dart"
\`\`\`

**Decision Tree**:
\`\`\`
Need UI component?
├─ Atom exists? → Use it (STOP)
├─ Can compose molecules from atoms? → Compose (STOP)
├─ Can compose organism from molecules? → Compose (STOP)
└─ Must create new? → Add to appropriate level
\`\`\`
```

### Common Anti-Patterns
```markdown
❌ WRONG: Custom button (atom exists)
\`\`\`dart
ElevatedButton(
  style: ButtonStyle(...),  // NO! Use atomic button
  child: Text('Click'),
)
\`\`\`

❌ WRONG: Duplicate organism
\`\`\`dart
// Recreating app bar that exists in organisms/
\`\`\`

✅ CORRECT: Import and use
\`\`\`dart
import 'package:atomic_components/atoms/button.dart';

AtomicButton(
  text: 'Click',
  variant: ButtonVariant.primary,
)
\`\`\`
```

## Monorepo / Multi-Package

### Detection Indicators
- Folder: `packages/` or `modules/`
- Multiple `pubspec.yaml` / `package.json` files
- Internal package dependencies

### CLAUDE.md Rules Template

```markdown
## 📦 Monorepo Structure

**Internal Packages**:
\`\`\`bash
packages/
  atomic_components/  → UI library (MANDATORY)
  app_layers/         → Domain entities (MANDATORY)
  core_utils/         → Shared utilities
\`\`\`

**Rule**: Always check internal packages BEFORE creating new code

**Search workflow**:
\`\`\`bash
# 1. Check UI components
grep -r "ComponentName" packages/atomic_components/lib/

# 2. Check entities
ls packages/app_layers/lib/entities/

# 3. Check utilities
grep -r "functionName" packages/core_utils/lib/
\`\`\`

**Anti-Pattern**:
❌ Creating functionality that exists in internal package
❌ Duplicating entities from app_layers
❌ Custom UI when atomic_components has it
```

## Layered Architecture (Traditional)

### Detection Indicators
- Folders: `controllers/`, `services/`, `repositories/`, `models/`
- OR: `api/`, `business/`, `data/`, `ui/`
- Clear horizontal layers

### CLAUDE.md Rules Template

```markdown
## 🏗️ Layered Architecture

**Layers** (top to bottom):
1. `controllers/` → Handle requests, coordinate
2. `services/` → Business logic
3. `repositories/` → Data access
4. `models/` → Data structures

**Rules**:
- Upper layer can call lower layer
- Lower layer CANNOT call upper layer
- Services contain NO data access code (use repositories)

**Before creating**:
\`\`\`bash
# Check existing services
ls src/services/

# Check repositories
ls src/repositories/
\`\`\`
```

## MVC (Model-View-Controller)

### Detection Indicators
- Folders: `models/`, `views/`, `controllers/`
- Framework: Rails, Laravel, ASP.NET

### CLAUDE.md Rules Template

```markdown
## 🏗️ MVC Pattern

**Structure**:
- `models/` → Database entities, business logic
- `views/` → Templates, UI rendering
- `controllers/` → Request handling, coordination

**Rules**:
- Fat models, skinny controllers
- No business logic in views
- No direct database access in controllers

**Before creating controller action**:
\`\`\`bash
# Check if model has method
grep -r "methodName" app/models/

# Check if action exists
grep -r "def action_name" app/controllers/
\`\`\`
```

## Hexagonal / Ports & Adapters

### Detection Indicators
- Folders: `core/`, `adapters/`, `ports/`
- Interface-based design
- Dependency inversion

### CLAUDE.md Rules Template

```markdown
## 🏗️ Hexagonal Architecture

**Structure**:
- `core/` → Business logic (no dependencies)
- `ports/` → Interfaces (in/out)
- `adapters/` → Implementations (API, DB, UI)

**Dependency Rule**: Adapters depend on ports, NOT vice versa

**Rules**:
- Core defines ports (interfaces)
- Adapters implement ports
- Core never imports from adapters

\`\`\`
core/ → defines ports/IUserRepository
adapters/database/ → implements IUserRepository
adapters/api/ → implements IUserService
\`\`\`
```

## Domain-Driven Design (DDD)

### Detection Indicators
- Folders: `domain/`, `application/`, `infrastructure/`
- Subdirs: `entities/`, `value_objects/`, `aggregates/`, `repositories/`
- Rich domain models

### CLAUDE.md Rules Template

```markdown
## 🏗️ Domain-Driven Design

**Layers**:
- `domain/` → Entities, value objects, aggregates (pure logic)
- `application/` → Use cases, services
- `infrastructure/` → DB, APIs, external systems

**Rules**:
- Domain is pure (no framework dependencies)
- Aggregates enforce invariants
- Repositories work with aggregates (not entities)

**Before creating entity**:
\`\`\`bash
# Check existing entities
ls src/domain/entities/

# Check value objects
ls src/domain/value_objects/
\`\`\`
```

## Repository Pattern

### Key Rules for CLAUDE.md

```markdown
## 📦 Repository Pattern Rules

**Repositories abstract data access**

**Rules**:
- One repository per aggregate root / entity
- Repositories return domain entities (not DB models)
- No business logic in repositories

**Before creating repository**:
\`\`\`bash
# Check if repository exists
ls lib/data/repositories/
grep -r "Repository" lib/data/repositories/
\`\`\`

❌ WRONG: Business logic in repository
\`\`\`python
class UserRepository:
    def validate_and_save(user):  # NO! Validation is business logic
        ...
\`\`\`

✅ CORRECT: Pure data access
\`\`\`python
class UserRepository:
    def save(user):  # Simple CRUD
        ...
\`\`\`
```

## Service Layer Pattern

### Key Rules for CLAUDE.md

```markdown
## 🔧 Service Layer Rules

**Services contain business logic**

**Rules**:
- Services coordinate between repositories
- Services enforce business rules
- Services are stateless

**Before creating service**:
\`\`\`bash
# Check existing services
ls lib/domain/services/
grep -r "Service" lib/domain/
\`\`\`

**Pattern**:
\`\`\`dart
class UserService {
  final UserRepository _repo;

  Future<void> registerUser(email, password) {
    // 1. Validate (business rule)
    // 2. Create entity
    // 3. Save via repository
  }
}
\`\`\`
```

## Generating Architecture Sections

### When Detecting an Architecture

1. **Identify pattern** from folder structure
2. **Extract rules** (dependency directions, constraints)
3. **Create decision tree** (when to use what)
4. **Document anti-patterns** (common violations)
5. **Add search commands** (verify before creating)

### Template Structure

```markdown
## 🏗️ Architecture Rules

**Pattern**: [Name]

**Structure**:
[Folder layout with descriptions]

**Rules**:
- [Dependency rule]
- [Constraint rule]
- [Mandatory workflow]

**Before creating [component]**:
\`\`\`bash
[Search commands]
\`\`\`

**Decision Tree**:
[When to do what]

**Anti-Patterns**:
❌ [Common violation]
✅ [Correct approach]
```

## Research Prompts for Architectural Patterns

When researching best practices for a detected architecture:

### Questions
1. "What are the mandatory rules for [architecture] in [tech stack]?"
2. "What are common violations of [architecture pattern]?"
3. "What are the dependency constraints in [architecture]?"
4. "How to organize [specific feature] in [architecture]?"

### Extract for CLAUDE.md
- ✅ Rules and constraints
- ✅ Common violations (anti-patterns)
- ✅ Decision trees
- ❌ Theoretical explanations
- ❌ History or philosophy
