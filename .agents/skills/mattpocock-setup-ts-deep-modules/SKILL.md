---
name: mattpocock-setup-ts-deep-modules
description: Setup TypeScript package deep module boundaries and dependency-cruiser isolation. Prevents illegal cross-imports and circular dependencies in TS codebases. Triggered via /mattpocock-setup-ts-deep-modules or naturally when configuring TS module boundaries.
argument-hint: '[optional_target_directory]'
---

# Matt Pocock TS Deep Modules & Boundary Engine (`/mattpocock-setup-ts-deep-modules`)

## ⚡ Overview & Tri-Mode Routing

Adapted from Matt Pocock's package structure tooling. Configures strict module boundaries, `exports` fields in `package.json`, and dependency-cruiser configs to enforce clean separation of concerns in TypeScript monorepos and multi-module apps.

Invokable via:
- **Slash Command**: `/mattpocock-setup-ts-deep-modules [dir]`
- **Dynamic Intent**: Triggered automatically when structuring TypeScript packages or eliminating circular dependencies.
- **Inter-Skill Calling**: Invoked by `/jsmastery-architect`, `/jsmastery-audit`, `/new-project`, and `/ingest-repo`.

---

## 🛡️ Package Isolation Rules

1. **Explicit Entrypoints**: Prevent internal file imports (`import { x } from 'pkg/dist/internal/x'`) by defining strict `exports` maps in `package.json`.
2. **Dependency Cruiser Safeguards**: Inject `dependency-cruiser.config.cjs` to enforce architectural layers (e.g. `domain` cannot import `ui`, `utils` cannot import `services`).
3. **No Circular Imports**: Fail lint/build checks immediately if circular dependencies are detected.

---

## 🔗 Inter-Skill Connections & Handoff Pipeline
- **Architecture Design**: Used during system setup by **`/jsmastery-architect`** and **`/new-project`**.
- **Code Audits**: Audited during release checks by **`/jsmastery-audit`**.
