---
name: mattpocock-to-tickets
description: Decompose technical specs into atomic execution tickets. Creates independent, verifiable developer tasks with clear Definition of Done (DoD). Triggered via /mattpocock-to-tickets or naturally when breaking down specs into tasks.
argument-hint: '[spec_file_or_path]'
---

# Matt Pocock Spec-to-Tickets Engine (`/mattpocock-to-tickets`)

## ⚡ Overview & Tri-Mode Routing

Converts technical design contracts (`SPEC.md` or build specs) into atomic, independent engineering tickets ready for developer execution, based on Matt Pocock's workflow.

Invokable via:
- **Slash Command**: `/mattpocock-to-tickets [spec_path]`
- **Dynamic Intent**: Triggered automatically when decomposing specs into atomic task items.
- **Inter-Skill Calling**: Invoked by `/new-project`, `/website-design-engine`, `/mattpocock-to-spec`, and `/jsmastery-scope`.

---

## 🎟️ Ticket Decomposition Rules

1. **Atomic & Independent**: Each ticket represents a single unit of work (e.g. 30-90 minutes of coding) that can be verified independently.
2. **Sequential Dependencies**: Explicitly declare blockers (`Blocked by: Ticket #X`).
3. **Verifiable DoD**: Every ticket MUST have an explicit, testable Definition of Done.

---

## 📄 Ticket Template Output

```markdown
### Ticket [ID]: [Title]
- **Description**: [What needs to be implemented]
- **Target Files**: [List of specific files to touch]
- **Dependencies**: [Blocked by Ticket IDs or None]
- **Definition of Done**:
  - [ ] Code implemented matching type signatures in SPEC
  - [ ] Unit/Integration test written and passing
  - [ ] Zero TypeScript or linter errors
```

---

## 🔗 Inter-Skill Connections & Handoff Pipeline
- **Upstream Specs**: Receives technical contracts from **`/mattpocock-to-spec`**, **`/jsmastery-architect`**, and **`/jsmastery-scope`**.
- **Execution & Testing**: Hands off task items to **`/do`**, **`/test-driven-development`**, and **`/verify-design`**.
