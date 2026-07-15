# Canvas Design Skill Setup: Brainstorm / Discovery Notes
Date: 2026-07-16 · Goal: Design and implement a Canvas Design skill for generating social media graphics and visual compositions.

## Summary / key decisions
- **Scope & Method**: The user selected Option 1: Canvas Design. We will design a custom canvas-design skill that enables Atinek's AIOS to programmatically create original static visual assets (posters, social graphics, custom SVGs) and save them as high-quality PNGs or PDFs.
- **Canvas Presets**: Approved 4 core presets (Instagram Square, Instagram Portrait, Story/Reel, YouTube Thumbnail) and requested additional presets for YouTube Banners (2560x1440px), Instagram Carousels (multi-slide grids), and Brand Assets (logo/badge sizes).
- **Aesthetic**: Use `Temporary brand design.md` styling variables as a temporary default brand design, mapping cream backgrounds, coral colors, Cormorant Garamond serif fonts, and glassmorphism elements.
- **Decoupled Architecture**: Put the brand specs, HTML templates, and rendering scripts in `d:\AI-OS\brain-aios\wiki\research\skills-library\canvas-design/`, and place a lightweight active skill in `.agents/skills/canvas-design/`.
- **Dynamic Activation & Verification**: The skill will auto-trigger on design phrases and use a visual self-correction loop, rendering the HTML via Playwright, viewing the image, and auto-correcting any layout issues before outputting.
- **Visual Design Skills Synergy**: Utilize global design assets and skills like `impeccable`, `frontend-design`, and `ui-ux-pro-max` to ensure premium visual taste.

## Q&A log
### Q1 — Goal & Tech Stack Definition
- Asked: How should we implement Canvas Design (e.g. SVG generators, image models, or HTML-to-screenshot pipelines)?
- Captured: The user wants to set up the Canvas Design skill. We recommend using a modern HTML-to-Image pipeline: the AI generates clean, responsive HTML/CSS designs (utilizing vector SVGs, gradients, and custom web typography), and uses Playwright to take a high-resolution screenshot (PNG) of the rendered page.

### Q2 — Target Layout Dimensions & Presets
- Asked: Do you approve of the proposed presets (instagram-square, instagram-portrait, story-reel, youtube-thumbnail)?
- Captured: The user approved the 4 presets and added requirements for:
  - `youtube-banner` (2560 x 1440 px).
  - `instagram-carousel` (ability to generate multiple linked slides side-by-side or sequentially).
  - `brand-assets` (preset dimensions for logos, icon packs, and badges).

### Q3 — Aesthetic & Brand Styling Configuration
- Asked: Since the brand visual identity is Undecided in the docs, should we implement a default premium dark/sleek theme?
- Captured: The user requested to use their downloaded `Temporary brand design.md` from the Downloads folder as a temporary brand identity spec for now.

### Q4 — Structure and Automation of the Canvas Generator
- Asked: Do you approve of the proposed automated template + render script layout?
- Captured: The user approved the structure, and requested further improvements and dynamic execution (auto-triggering on user requests without manual slash command calling).

### Q5 — Dynamic Activation & Visual Self-Correction Loop
- Asked: How can we improve the generator further and run it dynamically?
- Captured: The user approved the visual self-correction loop (taking a screenshot and inspecting/tweaking it automatically), the layout template registry, and the dynamic triggering. The user also specified integrating existing design skills (`impeccable`, `frontend-design`, `ui-ux-pro-max`) and noted they will provide a carousel skill later.

## Open flags (pending input)
