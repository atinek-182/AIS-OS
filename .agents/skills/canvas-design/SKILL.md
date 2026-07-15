---
name: canvas-design
description: Use when generating original visual art, posters, social media graphics, Instagram carousel slides, YouTube banners, thumbnails, or logo/brand asset compositions.
---

# Canvas Design Router Skill

When this skill is triggered, you will compile an HTML layout using the brand design tokens and then use the `browser_subagent` to capture a pixel-perfect PNG image.

## Step-by-Step Execution Workflow

### 1. Settle Dimensions & Layout
Identify the target aspect ratio preset and layout style from the user's prompt (or choose the best fit):
* **Aspect Presets**:
  * `instagram-square` (1080 x 1080)
  * `instagram-portrait` (1080 x 1350)
  * `story-reel` (1080 x 1920)
  * `youtube-thumbnail` (1280 x 720)
  * `youtube-banner` (2560 x 1440)
  * `brand-logo` (800 x 800)
  * `brand-badge` (500 x 500)
* **Layout Formats**:
  * `editorial-quote`: Serif quotes on a cream canvas.
  * `code-showcase`: Monospace code block in a dark window.
  * `bento-features`: Grid blocks with cream background.
  * `full-bleed-callout`: Saturated coral backdrop with white display type.

### 2. Compile HTML Preview
1. Read the base HTML template at `d:\AI-OS\brain-aios\wiki\research\skills-library\canvas-design\template-base.html` using the `view_file` tool.
2. Read the stylesheet variables at `d:\AI-OS\brain-aios\wiki\research\skills-library\canvas-design\styles.css` using `view_file`.
3. Construct the HTML snippet representing the layout (incorporating the text, code, titles, and styles from the spec).
4. Replace the placeholder `<!-- LAYOUT_CONTENT_PLACEHOLDER -->` with your layout snippet.
5. Write the fully compiled file to `d:\AI-OS\brain-aios\wiki\research\skills-library\canvas-design\preview.html`. (Ensure the stylesheet link is relative and resolves).

### 3. Render and Capture PNG via Browser Subagent
Invoke the `browser_subagent` tool with the following tasks:
1. **Task Name**: `"Rendering Canvas Design"`
2. **Task Description**:
   * Navigate the browser to the local file URL: `file:///d:/AI-OS/brain-aios/wiki/research/skills-library/canvas-design/preview.html`
   * Resize the browser viewport window to the exact dimensions of the chosen preset (e.g. width=1080, height=1350).
   * Take a full-page screenshot of the rendered page.
   * Save the screenshot to: `d:/AI-OS/brainstorms/canvas_output.png`
3. **Recording Name**: `"canvas_render"`

### 4. Visual Self-Correction Loop
1. Call the `view_file` tool on `d:/AI-OS/brainstorms/canvas_output.png` to inspect the generated visual composition directly in your context window.
2. Check for visual bugs:
   * Is text truncated or wrapping awkwardly?
   * Are margins too narrow?
   * Is there poor color contrast or text overlap?
3. If bugs are found, modify the layout snippet in `preview.html` (adjusting padding, font sizes, or grid gaps) and call `browser_subagent` to capture a new screenshot.
4. Repeat until perfect.

### 5. Deliver
Return the path to the final image: `d:/AI-OS/brainstorms/canvas_output.png`. Show a short bulleted outline of the design rationale and annotations.
