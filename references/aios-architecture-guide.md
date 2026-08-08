# AIOS System Architecture & Vault Guide

## Core Architectural Layout
- `brain-aios/`: General AI OS hub, personal task tracking, system workflows, and operational logs.
  - `brain-aios/wiki/checklists/master-task-list.md`: Canonical source of truth for task status.
  - `brain-aios/wiki/sops/`: Operational SOPs and guides.
- `second-brain-zorixel/`: ZORIXEL brand research, content production drafts, scripts, and target audience insights.
- `zorixel-brand-os/`: Master brand identity, positioning reports, and assets.
- `projects/`: Web application projects, landing pages, slide compilers, and client codebases.
- `context/`: Business intakes, connections registry, operator priorities.
- `references/`: Design matrices, component vaults, brand identity guides, API documentation.
- `decisions/log.md`: Append-only record of system decisions.
- `MEMORY.md`: Persistent memory logging cross-session learnings.
- `hot.md`: Transient session cache for active focus.

## Universal 5 Master Graphify Operating Patterns
1. **Query-First Discovery Gate**: Run `python scripts/aios_deep_search.py "<topic>"` or `graphify query` before manual grep.
2. **Shortest Path & Dependency Tracer**: Run `graphify path` during domain modeling or refactoring.
3. **God-Node & Security Audit Gate**: Run `graphify explain` during security or architecture audits.
4. **Post-Modification Graph Update & Diff**: Run `graphify update .` to keep knowledge graph hubs fresh.
5. **Multi-Vault Hub Routing**: Route graph queries to `root`, `brain`, `zorixel`, or `frontend` hubs.
