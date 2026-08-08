---
title: 02 Editor Chrome
domain: architecture
summary: we need the base chrome components that frame every editor screen — the top navbar and the left sidebar shell. These
  will be reused and extended in every chapter that follows. Create `components/editor/editor-navbar.tsx`.
critical_directives:
- Follow document guidance without bypassing established safeguards.
section_outline:
- Editor Navbar
- Project Sidebar
- Dialog Pattern
- Check when done
read_triggers:
- When working on architecture in references/six-file-context-methodology/creator-project-reference/feature-specs-library/02-editor-chrome.md
- When reading context for 02 Editor Chrome
tags:
- architecture
- 02-editor-chrome
updated: '2026-08-08'
---

we need the base chrome components that frame every editor screen — the top navbar and the left sidebar shell. These will be reused and extended in every chapter that follows.

### Editor Navbar

Create `components/editor/editor-navbar.tsx`.

Requirements:

- fixed-height top navbar
- left, center, and right sections
- left section contains sidebar toggle button
- use `PanelLeftOpen` / `PanelLeftClose` icons based on sidebar state
- right section stays empty for now
- dark background with subtle bottom border

---

### Project Sidebar

Create `components/editor/project-sidebar.tsx`.

Requirements:

- sidebar should float above the editor canvas
- opening it should not push page content
- slides in from the left
- accepts `isOpen` prop
- header with `Projects` title + close button
- shadcn `Tabs`:
  - My Projects
  - Shared
- both tabs show empty placeholder state
- full-width `New Project` button at the bottom with `Plus` icon

---

### Dialog Pattern

Use the existing color tokens from `globals.css` for dialog styling.

Support:

- title
- description
- footer actions

Do not build actual dialogs yet.

### Check when done

- new components compile without TypeScript errors
- no lint errors
- dialog pattern is ready for future use
