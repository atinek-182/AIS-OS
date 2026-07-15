---
name: carousel-render
description: Programmatically render slide HTML files into final PNG images using Playwright browser capture.
---

# Carousel Render Engine

You are the Zorixel AI Renderer. Your task is to compile a carousel markdown copy plan into individual HTML slides and screenshot them using the Playwright browser interface.

When this skill is invoked via `/carousel-render --file <path>` or triggered:

1. **Verify Input File**: Make sure the input markdown file (e.g., `d:\AI-OS\brainstorms\temp_carousel\copy.md`) exists.
2. **Run Compiler**: Execute the Python compiler script to generate the individual slide HTML files:
   `python d:\AI-OS\scripts\compile_carousel.py`
3. **Screenshot Loop**:
   - For each slide HTML file generated in `d:\AI-OS\brainstorms\temp_carousel/` (e.g., `slide_01.html`, `slide_02.html`, etc.):
     - Navigate the browser to the file URL:
       `file:///d:/AI-OS/brainstorms/temp_carousel/slide_01.html`
     - Set the browser viewport size to `1080` x `1350` (or target dimensions).
     - Wait 1000ms for layout and typography rendering.
     - Take a screenshot of the viewport and save it as `d:\AI-OS\brainstorms\output_carousel\slide_01.png`, etc.
4. **Clean Up**: Remove the temporary `.html` and `styles.css` files from `d:\AI-OS\brainstorms\temp_carousel/` to keep the workspace clean.
5. **Present Output**: Output the file paths of all generated PNG slides.

## Playwright Execution Protocol

Do NOT spawn a subagent. Call the `playwright` MCP tools directly in a loop:
1. `browser_navigate` with `url: "file:///d:/AI-OS/brainstorms/temp_carousel/slide_XX.html"`
2. `browser_resize` with `width: 1080, height: 1350`
3. `browser_take_screenshot` with `path: "d:\AI-OS\brainstorms\output_carousel\slide_XX.png"`
