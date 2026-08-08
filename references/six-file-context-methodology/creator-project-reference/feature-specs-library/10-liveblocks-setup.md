---
title: 10 Liveblocks Setup
domain: architecture
summary: Set up the realtime collaboration infrastructure using Liveblocks. Configure the `liveblocks.config.ts` at the project
  root.
critical_directives:
- Follow document guidance without bypassing established safeguards.
section_outline:
- Configuration
- Presence
- UserMeta
- Liveblocks Client
- Auth Route
read_triggers:
- When working on architecture in references/six-file-context-methodology/creator-project-reference/feature-specs-library/10-liveblocks-setup.md
- When reading context for 10 Liveblocks Setup
tags:
- architecture
- 10-liveblocks-setup
updated: '2026-08-08'
---

Set up the realtime collaboration infrastructure using Liveblocks.

## Configuration

Configure the `liveblocks.config.ts` at the project root.

Define:

### Presence

- cursor position
- `isThinking` boolean

### UserMeta

- user ID
- display name
- avatar URL
- cursor color

## Liveblocks Client

Create a cached Liveblocks node client in `lib`.

Add a helper that deterministically maps a user ID to a consistent color from a fixed palette.

## Auth Route

Create `POST /api/liveblocks-auth`.

Use the project ID as the Liveblocks room ID.

This route must:

1. require Clerk authentication
2. verify project access using the existing access helper
3. ensure the Liveblocks room exists (create only if needed)
4. return a session token with:
   - user name
   - avatar
   - generated cursor color

Return `403` for unauthorized project access.

## Dependencies

All required Liveblocks packages are already installed.

## Check When Done

- `liveblocks.config.ts` defines Presence and UserMeta
- Liveblocks client is cached
- auth route verifies project access
- user metadata is attached to sessions
- `npm run build` passes
