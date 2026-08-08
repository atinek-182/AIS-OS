---
title: Architecture Context
domain: architecture
summary: 'title: Architecture Context summary: ''title: Architecture Context summary: ''''title: Architecture Context summary:
  ''''''''| Layer     | Technology                  |'
critical_directives:
- Follow document guidance without bypassing established safeguards.
section_outline:
- Architecture Context
- Stack
- System Boundaries
- Storage Model
- Auth and Access Model
read_triggers:
- When working on architecture in references/six-file-context-methodology/6-file-context-templates/context/architecture.md
- When reading context for Architecture Context
tags:
- architecture
- architecture
updated: '2026-08-08'
---

---
title: Architecture Context
domain: architecture
summary: 'title: Architecture Context summary: ''title: Architecture Context summary: ''''| Layer     | Technology                  |
  Role   | | --------- | ---------------------------'''
critical_directives:
- Follow document guidance without bypassing established safeguards.
section_outline:
- Architecture Context
- Stack
- System Boundaries
- Storage Model
- Auth and Access Model
read_triggers:
- When working on architecture in references/six-file-context-methodology/6-file-context-templates/context/architecture.md
- When reading context for Architecture Context
tags:
- architecture
- architecture
updated: '2026-08-08'
---

---
title: Architecture Context
domain: architecture
summary: 'title: Architecture Context summary: ''| Layer     | Technology                  | Role   | | --------- | ---------------------------'
critical_directives:
- Follow document guidance without bypassing established safeguards.
section_outline:
- Architecture Context
- Stack
- System Boundaries
- Storage Model
- Auth and Access Model
read_triggers:
- When working on architecture in references/six-file-context-methodology/6-file-context-templates/context/architecture.md
- When reading context for Architecture Context
tags:
- architecture
- architecture
updated: '2026-08-08'
---

---
title: Architecture Context
domain: architecture
summary: '| Layer     | Technology                  | Role   | | --------- | ---------------------------
  | ------ |'
critical_directives:
- Follow document guidance without bypassing established safeguards.
section_outline:
- Architecture Context
- Stack
- System Boundaries
- Storage Model
- Auth and Access Model
read_triggers:
- When working on architecture in references/six-file-context-methodology/6-file-context-templates/context/architecture.md
- When reading context for Architecture Context
tags:
- architecture
- architecture
updated: '2026-08-08'
---

# Architecture Context

## Stack

| Layer     | Technology                  | Role   |
| --------- | --------------------------- | ------ |
| Framework | [e.g. Next.js + TypeScript] | [Role] |
| UI        | [e.g. Tailwind + shadcn/ui] | [Role] |
| Auth      | [e.g. Clerk]                | [Role] |
| Database  | [e.g. Prisma + PostgreSQL]  | [Role] |
| [Layer]   | [Technology]                | [Role] |

## System Boundaries

- `[folder]` — [What this folder owns and is responsible for]
- `[folder]` — [What this folder owns and is responsible for]
- `[folder]` — [What this folder owns and is responsible for]
- `[folder]` — [What this folder owns and is responsible for]

## Storage Model

- **[Storage type e.g. Database]**: [What lives here —
  e.g. metadata, ownership, relationships]
- **[Storage type e.g. Blob/File Storage]**: [What lives
  here — e.g. generated files, media, large artifacts]

## Auth and Access Model

- [How authentication works — e.g. Every user signs in
  via Clerk]
- [How ownership works — e.g. Every project has a single
  owner]
- [How access control works — e.g. Only the owner or a
  collaborator can mutate project resources]

## Invariants

1. [Rule the codebase must never violate — e.g. Request
   handlers do not run long-lived background work]
2. [Invariant two]
3. [Invariant three]
4. [Invariant four]
