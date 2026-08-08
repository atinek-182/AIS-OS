---
title: 07 Wire Editor Home
domain: architecture
summary: Wire the editor home sidebar and dialogs to the real project API. The editor home page is a server component.
critical_directives:
- Follow document guidance without bypassing established safeguards.
section_outline:
- Data Fetching
- '`useProjectActions`'
- Wiring
- Check When Done
read_triggers:
- When working on architecture in references/six-file-context-methodology/creator-project-reference/feature-specs-library/07-wire-editor-home.md
- When reading context for 07 Wire Editor Home
tags:
- architecture
- 07-wire-editor-home
updated: '2026-08-08'
---

Wire the editor home sidebar and dialogs to the real project API.

### Data Fetching

The editor home page is a server component.

Fetch owned and shared projects server-side using the existing project data helper and pass both lists to the sidebar.

No client-side fetching for initial load.

### `useProjectActions`

Create a hook in `hooks/` that manages dialog state and project mutations.

**Create**

- manage create dialog state
- manage project name input
- generate a short unique suffix
- slugify the name to create the room ID
- call `POST /api/projects`
- navigate to the new workspace

The project ID and Liveblocks room ID should stay aligned.

**Rename**

- store target project id + current name
- call `PATCH /api/projects/[id]`
- refresh on success

**Delete**

- store target project
- call `DELETE /api/projects/[id]`
- redirect to `/editor` if deleting the active workspace
- otherwise refresh

### Wiring

Connect the hook to the sidebar and dialogs.

- create dialog shows room ID preview
- rename dialog pre-fills current name
- delete dialog shows project name

### Check When Done

- sidebar uses real project data
- create navigates to workspace
- rename updates correctly
- delete refreshes or redirects correctly
- `npm run build` passes
