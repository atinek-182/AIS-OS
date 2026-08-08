---
title: 09 Share Dialog
domain: architecture
summary: Add sharing to the workspace so project owners can invite collaborators by email. Add a `Share` button to the editor
  navbar that opens the share dialog.
critical_directives:
- Follow document guidance without bypassing established safeguards.
section_outline:
- Share Dialog
- Clerk User Data
- Implementation
- Check When Done
read_triggers:
- When working on architecture in references/six-file-context-methodology/creator-project-reference/feature-specs-library/09-share-dialog.md
- When reading context for 09 Share Dialog
tags:
- architecture
- 09-share-dialog
updated: '2026-08-08'
---

Add sharing to the workspace so project owners can invite collaborators by email.

## Share Dialog

Add a `Share` button to the editor navbar that opens the share dialog.

Owners can:

- invite collaborators by email
- view current collaborators
- remove collaborators
- copy the project link with temporary `Copied!` feedback

Collaborators can:

- view the collaborator list only
- not invite, remove, or manage access

## Clerk User Data

Collaborators are stored by email in the database.

Use Clerk Backend API to enrich collaborator emails with:

- display name
- avatar image

If a Clerk user is not found for an email, fall back to showing the email only.

## Implementation

Add the required API logic for:

- listing collaborators
- inviting collaborators
- removing collaborators

Enforce ownership server-side for invite and remove actions.

Do not add a local user table.

## Check When Done

- share dialog opens from the workspace
- owners can invite and remove collaborators
- collaborators see read-only access
- collaborator names/avatars load from Clerk when available
- `npm run build` passes
