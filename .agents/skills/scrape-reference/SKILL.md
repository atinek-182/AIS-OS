---
name: scrape-reference
description: Scrape, mirror, and analyze a website for brand or premium frontend reference. Runs local servers to bypass Playwright file restrictions, outputs detailed design audits, runs user Q&A/roasts, and updates design vaults.
---

# Scrape Reference Skill

Use this skill whenever the user provides a website URL to extract design tokens, layouts, fonts, animations, asset hierarchies, or to run Playwright browser tests on the site's tools.

## Phase 1: Clarification & Setup (Do FIRST)

1. **Reference Type Check:**
   - If not specified by the user, ask: *"Is this website for a brand reference (Zorixel vault) or a premium frontend design reference?"*
2. **Retention Policy Check:**
   - Ask the user: *"Should the mirrored files stay forever in our AIOS folders, or should they be deleted after we extract the analysis, screenshots, and design tokens?"*
3. **Storage Mapping:**
   - For **Brand References**: Save files under `second-brain-zorixel/wiki/research/[site-slug]/`.
   - For **Premium Design References**: Save files under `premium-frontend-experience-system/reference-inputs/[site-slug]/`.

## Phase 2: Mirroring & Local Server Deployment

1. **Mirroring Engine:**
   - Write a Node.js scraper script in the `scripts/` directory (e.g. `scripts/mirror-[site-slug].js`) to recursively or explicitly download:
     - HTML pages (including main landing, subpages, and utility tools).
     - CSS stylesheets (extracting base configurations, theme variables, layout styling).
     - JS scripts (targeting custom components, web components, GSAP/ScrollTrigger/Three.js routines).
     - Fonts (WOFF2/WOFF formats self-hosted on the page).
     - Image assets (PNG, JPEG, SVG, WebP) and 3D models.
2. **Local HTTP Server:**
   - *Constraint:* Playwright MCP blocks the `file:` protocol for security, which prevents direct rendering of local HTML pages.
   - *Solution:* Run the workspace static server at `scripts/serve.js` in the background, passing the target reference folder path as the argument:
     ```powershell
     node scripts/serve.js <absolute-path-to-mirrored-folder> 3000
     ```
   - Use the `run_command` tool to launch the background task.

## Phase 3: Visual & Code Analysis via Playwright

1. **Visual Capture:**
   - Use Playwright MCP tools to navigate to `http://localhost:[port]/` to load the local mirror.
   - Capture screenshots of the landing page, tools, or transitions at multiple viewports.
2. **Technical Auditing:**
   - Use `browser_run_code_unsafe` to inspect running states:
     - Check console errors, console logs, and performance metrics.
     - Extract DOM elements, inline CSS variables, GSAP timelines, and Three.js canvas bindings.
3. **Create Analysis Document:**
   - Save a markdown analysis file (`analysis.md`) in the reference folder containing:
     - **Visual Style & Vibe:** Neobrutalist, editorial, minimalist, etc.
     - **Color Tokens:** CSS custom properties/hex codes.
     - **Typography Hierarchy:** Display, body, and mono font pairings.
     - **Motion Language:** ScrollTriggers, page transitions, custom cursors, parallax math.
     - **Assets:** PNGs, SVGs, and asset links.

## Phase 4: AIOS System Adaptation

1. **System Self-Improvement:**
   - Run the `/improve-system` skill to ingest findings from the visual audit.
   - Update `premium-frontend-experience-system/POLICIES.md` or `DESIGN_DIRECTION.md` to incorporate newly discovered UI/UX techniques (e.g. elastic cursors, granular canvas noise, or custom spring animations).
2. **Update User Context:**
   - Log user feedback, visual preferences, and mindset shifts to `MEMORY.md` and `brain-aios/wiki/experiences/`.
3. **Brand Candidacy & Roast Loop:**
   - If the site contains design tools (like palette generators or font pickers), write a Playwright extraction script to run candidates for the user's brand (e.g. Zorixel).
   - Write candidates to `second-brain-zorixel/wiki/brand/candidates.md`.
   - Direct the user to run `/grill-me` or `/roast` to finalize selections.

## Phase 5: Cleanup (Based on Retention Choice)
- If the user selected to delete the mirrored site after extraction, run command-line cleanup on the raw HTML/CSS/JS/asset mirror directory, leaving only the `analysis.md` and screenshots behind.
