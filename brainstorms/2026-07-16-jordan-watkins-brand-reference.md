# Jordan Watkins Brand Reference & Playwright Tools: Brainstorm / Discovery Notes
Date: 2026-07-16 · Goal: Analyze jordanwatkins.xyz to extract brand references, design tools, and setup Playwright scripts for automated tool usage and brand building.

## Summary / key decisions
- **Reference Location:** Scraped files are stored in `second-brain-zorixel/wiki/research/jordan-watkins-reference/`.
- **Retention Policy:** Kept permanently in the workspace for design and tool reference.
- **Primary Objectives:**
  1. **Visual Reference & Vibe:** Used Playwright to visually navigate and inspect animations, illustrations, layouts, and cursor trails to capture the design essence. Saved screenshots locally.
  2. **Playwright Interactive MCP Usage:** Enabled local HTTP server on port 3000 to interact with the design tools visually or programmatically via Playwright.
- **Visual Vibe & Design System:**
  - **Colors:** Warm beige background (`#f1e9e7`), gray borders (`#cdc4c1`), forest green text (`#1a2d14` and `#37481c`), bold red accents (`#a82226`).
  - **Typography:** Vintage Serif header font (`Awesome Serif`), clean grotesque body/UI font (`Trip Sans`), and custom code font (`Trip Sans Mono`).
  - **Interaction Design:** Draggable elements with inertia (`hub-float.js`), hand-drawn character states switching (`character-rotate.js`), animated paper texture canvas (`paper-texture.js`), cursor particle trails (`pixel-canvas.js` and `cursor-trail.js`), and parallax floating vector icons.
  - **Layout:** Neobrutalist design with 1.5px solid dark green borders, offset flat shadows, sidebars on tools pages, and card-based navigation.

## Q&A log
### Q1 — Reference Scope & Storage
- **Asked:** Where should we store the scraped website files, and what is the primary objective of this reference for the Zorixel brand?
- **Captured:** 
  - Save scraped assets/files to `second-brain-zorixel/wiki/research/jordan-watkins-reference/`.
  - Use Playwright to actively navigate the site to capture the actual visual experience, animations, illustrations, cursor trails, and overall "vibe."
  - Enable using the site's tools visually inside the browser session so the user can review outputs.
- **Flags:** None.

### Q2 — Scraping & Asset Extraction Approach
- **Asked:** How should we implement the scraping of code files, assets, styles, and fonts, and what priority should we give to different sections of the website?
- **Captured:** 
  - Wrote a Node.js scraper script (`scripts/mirror-jordan-watkins.js`) to download all pages, design tool HTML files (all 17 tools), styles, scripts, illustrations, and font files.
  - Stored all scraped files under `second-brain-zorixel/wiki/research/jordan-watkins-reference/`.
  - Ran local visual exploration and analysis.
- **Flags:** None.

### Q3 — Automated Branding Candidate Generation
- **Asked:** How can we programmatically extract brand ideas (fonts and colors) for Zorixel using these scraped tools?
- **Captured:**
  - Started a background static server (`scripts/serve.js`) hosting the mirrored website on port 3000.
  - Executed a Playwright script targeting the local Typeface Picker and Color Palette Generator to input Zorixel parameters (Education, Creatives, Inspirational, Friendly/Creative/Bold).
  - Saved the matching candidates to `second-brain-zorixel/wiki/brand/candidates.md` with visual HTML block previews.
- **Flags:** None.

## Open flags (pending input)
- None. All initial discovery and setup phases are complete.
