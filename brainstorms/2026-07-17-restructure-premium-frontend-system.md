# Restructure Premium Frontend Experience System: Brainstorm / Discovery Notes
Date: 2026-07-17 · Goal: Redesign and streamline the Premium Frontend Experience System, reducing duplication and bloat across files, creating strong Obsidian link connections, defining improved workflows and custom skills, and building a more cohesive system.

## Summary / key decisions
- Discovery session initiated on 2026-07-17.
- **Modularity Preserved**: Rejected collapsing directories into single files. Retain the modularity of subdirectories (`workflows/`, `references/`, `design-briefs/`, `assets-briefs/`, `source-registries/`) to protect research and workflow details, but clean up duplicate text, update broken links, and maximize inter-linking.
- **GSD & Superpowers Plan Alignment**: Agreed to upgrade planning templates (e.g. New Project Brief and Design Direction) to match modern Superpowers/GSD specs. This includes incorporating structured `implementation_plan.md` sections for User Review, Open Questions, Proposed Changes with file statuses (`[NEW]`, `[MODIFY]`), and comprehensive multi-viewport Visual QA validation loops with Playwright audits.
- **Dynamic Skill Triggering**: Custom skills (`/new-project` and `/design-direction`) will be implemented as active workspace commands. We will configure prompt patterns in `AGENTS.md` and guidelines in rules to dynamically trigger/recommend these scripts/commands during the project lifecycle.
- **Deduplication & Cross-Linking**: Briefs, asset files, and approved libraries will be stripped of repeating context blocks and status definitions, pointing instead to their parent README files. Every file will feature a standard `## Connections` block utilizing relative Obsidian `[[WikiLink]]` bracket structures to form a dense web of navigation.



## Q&A log
### Q1 — Directory & File Architecture
- Asked: How should we restructure the folders and files of the Premium Frontend Experience System?
- Captured: The user wants to retain separate modular files in subdirectories (workflows, design briefs, asset briefs, references, source registries) to preserve deep research. We should focus on resolving internal duplication, repairing outdated links (like references to deleted files), and adding rich inter-document links.
- Flags: None

### Q2 — Upgrading the Plan Templates (Old Style vs. New Style)
- Asked: What does the "old style plan" represent, and how do you want the "new style plan" templates to look?
- Captured: The user agreed to upgrade the planning templates to match modern Superpowers and GSD plan structures (`implementation_plan.md` with explicit sections, file changes, and strict multi-viewport visual QA verification criteria).
- Flags: None

### Q3 — Automated Skills & Slash Commands
- Asked: To make the workflows easier and reduce manual effort, what new custom skills or automations should we build?
- Captured: The user approved the creation of `/new-project` and `/design-direction` active workspace skills, and refining `/verify-design`. The user wants these skills to be dynamic and trigger automatically (or be recommended) whenever a new project starts or key actions occur.
- Flags: None

### Q4 — Streamlining Subdirectory Content & Obsidian Linkages
- Asked: Since we are keeping the modular subfolders and files, how should we clean up their inner content to remove the heavy duplication of definitions, rules, and templates?
- Captured: The user approved stripping the redundant Project Context blocks from the briefs, removing repeated status/source values from the asset and library files, linking them back to their respective folder READMEs, and establishing a dense web of cross-references (such as a `## Connections` header at the top of each file) using Obsidian relative bracket links (`[[WikiLink]]`).
- Flags: None

## Open flags (pending input)
