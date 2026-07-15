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
3. **Start Background server**: Run a background local HTTP task to serve templates:
   `python -m http.server 8000 --directory d:/AI-OS/brainstorms/temp_carousel/`
4. **Screenshot Loop**:
   - For each slide HTML file generated in `d:\AI-OS\brainstorms\temp_carousel/` (e.g., `slide_01.html`, `slide_02.html`, etc.):
     - Navigate the browser to the localhost URL:
       `http://localhost:8000/slide_01.html`
     - Set the browser viewport size to `1080` x `1350` (Instagram Portrait).
     - Wait 1000ms for layout and typography rendering.
     - Take a screenshot of the viewport and save it as `d:\AI-OS\brainstorms\output_carousel\slide_01.png`, etc.
5. **Clean Up & Terminate**:
   - Kill the background Python server task via `manage_task`.
   - Remove the temporary `.html` and `styles.css` files from `d:\AI-OS\brainstorms\temp_carousel/` to keep the workspace clean.
6. **Present Output**: Output the file paths of all generated PNG slides.

## Playwright Execution Protocol

Do NOT spawn a subagent. Call the `playwright` MCP tools directly in a loop:
1. `browser_navigate` with `url: "http://localhost:8000/slide_XX.html"`
2. `browser_resize` with `width: 1080, height: 1350`
3. `browser_take_screenshot` with `path: "d:\AI-OS\brainstorms\output_carousel\slide_XX.png"`
