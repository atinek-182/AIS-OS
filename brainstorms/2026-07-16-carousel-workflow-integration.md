# Carousel Workflow Integration: Brainstorm / Discovery Notes
Date: 2026-07-16 · Goal: Tweak and integrate the ingested carousel system into Atinek's AIOS, comparing DALL-E prompt generation vs. programmatic HTML-to-Image rendering.

## Summary / key decisions
- **Scope & Method**: Approved the (Upgrade) workflow. We will unify the planning and design concepts into a programmatic pipeline. We will combine `/carousel-copy` (slide copywriter) and `/carousel-render` (formerly `/design-taste` prompts, now a programmatic template builder + viewport screenshot capture) into a unified automation.
- **CLI Options**: Approved 4 arguments for the `/carousel` command: `--topic`, `--style` (default: `cream`), `--slides` (default: `6`), and `--aspect` (default: `instagram-portrait`). Directory paths will be structured in `d:\AI-OS\brainstorms\temp_carousel/` (temporary HTML slides) and `d:\AI-OS\brainstorms\output_carousel/` (final slide PNG files).
- **Aesthetic Overlays**: Approved slide headers (step label top-left, page arrow top-right) and footers (branding tag `@zorixel` or progress line). Hook and CTA slides will have custom layout overrides.
- **Reference Layout Style**: We captured slides from `adarshxdesign`'s Instagram carousel showing a clean, modern design system: a vertical gradient background, bold condensed display headers, and a split "Before vs. After" card comparison visual metaphor. We will implement this split comparison as a standard template in our system!

## Q&A log
### Q1 — The Render Workflow Choice
- Asked: Keep DALL-E prompt workflow or upgrade to programmatic HTML-to-Image?
- Captured: The user chose (Upgrade): "Integrate /carousel-copy for slide planning, and adapt the /design-taste concept into /carousel-render — a unified command that generates the copy outline, translates it to HTML, spins up the background server, and screenshots the entire deck of PNGs in one go."

### Q2 — Unified Command CLI Options & Parameters
- Asked: Do you approve of the proposed command arguments (`--topic`, `--style`, `--slides`, `--aspect`) and output directory paths?
- Captured: The user approved.

### Q3 — Carousel-Specific Slide Furniture & Formatting
- Asked: Do you approve of adding slide headers/footers and hook/CTA specific layout overrides?
- Captured: The user approved.

### Q4 — Visual Analysis of IG Carousel Reference
- Asked: Let's look at the IG link provided for visual styles.
- Captured: Spun up Playwright and captured slides from `adarshxdesign`. Identified a key design pattern: split "Before vs. After" cards comparing bad and good design options. This visual metaphor is highly effective for design content and will be added as a preset template in our CSS framework.

## Open flags (pending input)
