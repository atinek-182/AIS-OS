---
title: 08 Editor Workspace Shell
domain: architecture
summary: Build the `/editor/[roomId]` workspace shell with server-side access checks. No canvas logic yet. `/editor/[roomId]`
  must be a server component.
critical_directives:
- Follow document guidance without bypassing established safeguards.
section_outline:
- Access
- Access Helpers
- Layout
- Scope
- Check When Done
read_triggers:
- When working on architecture in references/six-file-context-methodology/creator-project-reference/feature-specs-library/08-editor-workspace-shell.md
- When reading context for 08 Editor Workspace Shell
tags:
- architecture
- 08-editor-workspace-shell
updated: '2026-08-08'
---

Build the `/editor/[roomId]` workspace shell with server-side access checks. No canvas logic yet.

## Access

`/editor/[roomId]` must be a server component.

Before rendering:

- unauthenticated users redirect to `/sign-in`
- users without project access see `AccessDenied`
- non-existent projects also show `AccessDenied`

Create `components/editor/access-denied.tsx` with:

- centered layout
- lock icon
- short message
- link back to `/editor`

## Access Helpers

Create `lib/project-access.ts` with helpers for:

- getting current Clerk identity: `userId` + primary email
- checking project access by owner or collaborator

## Layout

Build a full-viewport workspace layout with:

- top navbar showing the project name
- navbar actions: share button and AI sidebar toggle
- existing `ProjectSidebar` on the left
- current room highlighted in the sidebar
- central canvas placeholder with dark background and centered message
- right sidebar placeholder for future AI chat

The canvas area should fill the remaining space.

## Scope

Do not add real canvas logic, Liveblocks, AI chat, or sharing behavior yet.

## Check When Done

- `/editor/[roomId]` builds successfully
- access helper exists outside the page component
- `AccessDenied` is used for missing or unauthorized projects
- workspace layout renders with current project context
- no TypeScript errors
