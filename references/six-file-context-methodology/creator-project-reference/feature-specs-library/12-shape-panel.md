---
title: 12 Shape Panel
domain: architecture
summary: Add a bottom shape panel so users can drag shapes onto the canvas and create new nodes. 1. Add a floating pill-shaped
  toolbar at the bottom-center of the canvas.
critical_directives:
- Follow document guidance without bypassing established safeguards.
section_outline:
- Implementation
- Check When Done
read_triggers:
- When working on architecture in references/six-file-context-methodology/creator-project-reference/feature-specs-library/12-shape-panel.md
- When reading context for 12 Shape Panel
tags:
- architecture
- 12-shape-panel
updated: '2026-08-08'
---

Add a bottom shape panel so users can drag shapes onto the canvas and create new nodes.

## Implementation

1. Add a floating pill-shaped toolbar at the bottom-center of the canvas.

2. Add draggable icon buttons for these shapes:
   - rectangle
   - diamond
   - circle
   - pill
   - cylinder
   - hexagon

3. When dragging a shape, include the shape name and default size in the drag payload.

   Use sensible default sizes:
   - rectangles should be wider than tall
   - circles should be square
   - diamonds should be slightly larger so labels have room

4. Add `dragover` and `drop` handling to the canvas wrapper.

5. On drop:
   - read the dragged shape payload
   - convert the screen position to canvas coordinates using React Flow
   - create a new node at that position
   - use an empty label
   - use the default node color
   - use the dragged shape value

6. Generate each node ID using the shape name, timestamp, and a counter.

7. Add a basic renderer for the custom canvas node type so new nodes are visible.

   For this unit, render every shape as a simple bordered rectangle with the label centered. Shape-specific visuals will be added later.

## Check When Done

- Shape drag payload includes the correct shape and size data.
- Drop logic creates new canvas nodes with the expected shape data.
- New nodes use the custom canvas node type.
- `npm run build` passes without type errors.
