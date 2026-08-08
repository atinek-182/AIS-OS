---
title: 29 Spec Ui Integration
domain: architecture
summary: Integrate spec generation results into the editor so users can view, preview, and download specs from the existing
  ai sidebar specs tab. - in the right sidebar (Specs tab), show a list of specs for the current project
critical_directives:
- assume ProjectSpec only provides metadata, content must be fetched separately
section_outline:
- Implementation
- UI Details
- Scope Limits
- Notes
- Check When Done
read_triggers:
- When working on architecture in references/six-file-context-methodology/creator-project-reference/feature-specs-library/29-spec-ui-integration.md
- When reading context for 29 Spec Ui Integration
tags:
- architecture
- 29-spec-ui-integration
updated: '2026-08-08'
---

Integrate spec generation results into the editor so users can view, preview, and download specs from the existing ai sidebar specs tab.

### Implementation

1. Spec list

- in the right sidebar (Specs tab), show a list of specs for the current project
- fetch specs from the backend using the existing ProjectSpec API
- display:
  - createdAt
  - filename
- keep items simple and clickable

2. Preview modal

- open a modal when a spec is selected
- fetch the spec content through an existing endpoint (do not access Blob directly from the client)
- render content as Markdown
- include a close action and basic keyboard support

3. Download action

- add a download action for each spec (list item + modal)
- call the download endpoint
- let the browser handle the file download

### UI Details

- use existing sidebar layout, do not redesign
- use shadcn/ui components (Dialog, ScrollArea, Button)
- use existing colors and tokens from `global.css`
- follow `ui-context.md` for spacing and layout
- keep the list compact and scrollable

### Scope Limits

- do not implement backend logic
- do not fetch Blob URLs directly in the client
- do not store spec content in frontend state long-term
- do not redesign the sidebar or tabs
- do not add new global state

### Notes

- reuse existing fetch patterns used in the app
- assume ProjectSpec only provides metadata, content must be fetched separately

### Check When Done

- spec list loads for the current project
- modal shows rendered Markdown content
- download action triggers file download
- TypeScript and build pass
