---
name: frontend-slides
description: This skill should be used when the user asks to "create HTML slides", "generate a presentation", "convert a PPT to HTML slides", "design slide deck", "make web slides", or "convert PPTX to web slides". Supports fixed-stage 16:9 layouts, custom styles, and Windows CLI scripts.
version: 1.0.0
---

# Frontend Slides Generator

Create zero-dependency, animation-rich HTML presentations that run entirely in the browser.

## Core Principles

1. **Zero Dependencies** — Produce single HTML files with inline CSS and JavaScript. Do not use npm, build tools, or frameworks.
2. **Show, Don't Tell** — Generate visual previews rather than forcing abstract choices. Let users choose by seeing.
3. **Distinctive Design** — Avoid generic "AI slop" aesthetics. Make custom-crafted, visually striking presentations.
4. **Progressive Disclosure** — Read style indexes first. Load detailed template files only after selection.
5. **Fixed 16:9 Stage (NON-NEGOTIABLE)** — Every presentation must use a fixed 1920×1080 design stage that scales uniformly to fit the browser viewport. Never reflow slide content.

---

## Operating Instructions

### Phase 1: Content Gathering

Ask the user all of the following questions in a single numbered prompt (or via interactive questions):

1. **Purpose**: Pitch deck, Teaching-Tutorial, Conference talk, or Internal presentation?
2. **Length**: Approximately how many slides (Short 5-10, Medium 10-20, Long 20+)?
3. **Content**: Is content ready (All content ready, Rough notes, or Topic only)?
4. **Density**: Low density (speaker-led: 1-3 bullets max, high negative space) or High density (reading-first: 4-8 bullets or structured grid cards)?

If images or logos are provided:
1. Scan the image directory for formats (`.png`, `.jpg`, `.svg`, `.webp`).
2. Evaluate each image's dimensions, colors, and content.
3. Incorporate images into the slide layout structure from the start (e.g. grid mockups, text-column pairs).

---

### Phase 2: Style Selection (Visual Discovery)

Provide the user with 3 distinct single-slide visual previews before generating the full presentation:

1. **Preview A (Safe Preset)**: Select from the light/dark presets in `STYLE_PRESETS.md` (e.g., Swiss Modern, Notebook Tabs, Paper & Ink).
2. **Preview B (Bold Template)**: Select a layout from `bold-template-pack/selection-index.json`.
3. **Preview C (Custom Wildcard)**: Propose a custom design tailored specifically to the presentation's theme. Do not use overused fonts (Inter, Arial) or cliched colors (purple gradients on white).

Save previews to `.frontend-slides/slide-previews/` as `style-a.html`, `style-b.html`, and `style-c.html`. Open each in the browser to let the user choose.

---

### Phase 3: Slide Deck Generation

Generate the full presentation by merging the content and chosen style:

1. **Apply Density Constraints**:
   * *Low density*: Generate more slides, large headings, statement quotes, and generous spacing.
   * *High density*: Use structured comparison tables, grid layouts, and brief explanations.
2. **Include Mandatory CSS**: Paste the full contents of `viewport-base.css` inside the HTML's `<style>` block.
3. **Add Presentation Controller JS**: Paste the presentation controller script from `html-template.md` for keyboard, touch, and scroll navigation.
4. **Enable Inline Editor**: Include the inline editing script from `html-template.md` to allow users to press `E` to edit text and `Ctrl+S` to save local changes.

---

### Phase 4: PPTX to HTML Conversion

When converting PowerPoint decks:

1. Install the Python pptx module if missing:
   ```powershell
   pip install python-pptx
   ```
2. Extract presentation slide content and images:
   ```powershell
   python scripts/extract-pptx.py <path-to-file.pptx> <output-directory>
   ```
3. Read the extracted `extracted-slides.json` file.
4. Run Phase 2 (Style Selection) to let the user select a theme, then compile the extracted content into the chosen HTML template.

---

### Phase 5: Exporting & Deploying

#### 1. Export as PDF
To print slides or generate static PDF handouts, run the export script (requires Node.js and Playwright):
```powershell
bash scripts/export-pdf.sh <path-to-presentation.html> [output.pdf]
```
For smaller file sizes, run with the `--compact` flag (resizes screenshots to 1280×720).

#### 2. Deploy to Vercel
To share slides via a live URL that works on mobile devices, run the deploy script:
```powershell
bash scripts/deploy.sh <path-to-presentation.html>
```

---

## Brand Customization Guidelines (Zorixel Editorial)

To generate decks specifically branded for **Zorixel**, override standard template presets with these parameters:

* **Background**: Warm linen off-white paper canvas background (`#fbfaf7`).
* **Text**: Dark editorial charcoal (`#141413`).
* **Highlight Accent**: Zorixel brand coral (`#ff6b4a`), used sparingly (under 10% screen space).
* **Typography**: Elegant display serif (e.g. Garamond, Fraunces) paired with clean monospace/sans-serif.
* **Layout Structure**: Comparison columns should float as crisp white panels (`#ffffff`) with highly diffused, soft shadows (`box-shadow: 0 20px 48px rgba(20, 20, 19, 0.04)`).
