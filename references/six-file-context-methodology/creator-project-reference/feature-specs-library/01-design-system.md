---
title: 01 Design System
domain: architecture
summary: Read `AGENTS.md` and `context/ui-context.md` before starting. We're adding the design system and UI primitive components.
critical_directives:
- Follow document guidance without bypassing established safeguards.
section_outline:
- Check when done
read_triggers:
- When working on architecture in references/six-file-context-methodology/creator-project-reference/feature-specs-library/01-design-system.md
- When reading context for 01 Design System
tags:
- architecture
- 01-design-system
updated: '2026-08-08'
---

Read `AGENTS.md` and `context/ui-context.md` before starting.

We're adding the design system and UI primitive components.

Install and configure `shadcn/ui`.

Add these shadcn components:

- Button
- Card
- Dialog
- Input
- Tabs
- Textarea
- ScrollArea

Do not modify the generated `components/ui/*` files after installation.

Also Install `lucide-react`.

Create `lib/utils.ts` with a reusable `cn()` helper for merging Tailwind classes.

Ensure all components match the existing dark theme in `globals.css`.

### Check when done

- All components import without errors
- `cn()` works properly
- No default light styling appears
