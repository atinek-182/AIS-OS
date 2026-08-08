---
title: 14 Node Editing
domain: architecture
summary: Add resizing and inline label editing to canvas nodes. - selected nodes should show resize handles
critical_directives:
- Follow document guidance without bypassing established safeguards.
section_outline:
- Implementation
- Scope Limits
- Check When Done
read_triggers:
- When working on architecture in references/six-file-context-methodology/creator-project-reference/feature-specs-library/14-node-editing.md
- When reading context for 14 Node Editing
tags:
- architecture
- 14-node-editing
updated: '2026-08-08'
---

Add resizing and inline label editing to canvas nodes.

## Implementation

1. Add resizing.
   - selected nodes should show resize handles
   - prevent nodes from being resized below a minimum size
   - keep resize handles subtle and consistent with the dark canvas UI

2. Add inline label editing.
   - keep the node label centered inside the node
   - double-click the center/label area of a node to edit its label
   - show placeholder text in the same centered position when the label is empty
   - keep editing smooth without causing layout shifts
   - show a textarea directly over the label while editing
   - update the label as users type
   - close editing on blur or `Escape`
   - prevent text editing interactions from dragging or panning the canvas

3. Keep all node updates connected to the existing collaborative canvas state.

## Scope Limits

- don't change shape rendering from the previous unit
- don't change the shape panel or drag preview
- don't change how dropped nodes are created
- keep this focused on resize and label editing only

## Check When Done

- Selected nodes show resize handles.
- Resizing updates node dimensions through the existing node state flow.
- Double-clicking a node opens inline label editing.
- Label editing updates node labels through the existing sync flow.
- Editing closes on blur or Escape.
- Text interactions do not trigger canvas drag or pan.
- `npm run build` passes without type errors.
