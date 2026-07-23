# Figma Micrographics Assets: Brainstorm / Discovery Notes
Date: 2026-07-19 · Goal: Plan the replication and generation of micrographic design assets from Figma into reusable HTML/CSS/React components.

## Summary / key decisions
- **Figma Authentication**: Personal Access Token (PAT) retrieved from MCP configuration and added to `.env` file as `FIGMA_ACCESS_TOKEN`.
- **Target Folder**: `d:\AI-OS\projects\For AIOS\Micrographics\`. (Note: `projects/For AIOS` is a Windows directory junction pointing to `D:\projects\For AIOS`).
- **Asset Formats**: Each of the 50 frames will be exported as a raw SVG, a standalone HTML/CSS file, and a parameterized React JSX component.
- **Editability**: Code assets will be structured with clean, semantic variables (CSS variables or React props) to make text, colors, fonts, and styles easily customizable.
- **Typography**: Import Google Fonts used in the Figma designs (`42Dot Sans`, `IBM Plex Mono`, `Instrument Serif`, `Pinyon Script`, etc.) directly in HTML/React code.
- **Symbol Extraction**: Extract independent symbols, vectors, geometric shapes, and icons as standalone reusable SVGs in a `symbols/` folder.

## Q&A log
### Q1 — Figma Access & Personal Access Token (PAT)
- Asked: Where is the Figma PAT stored or how should we configure it?
- Captured: The user added the Figma PAT in the global MCP configuration under the `figma` server env. Token configured in `.env` as `FIGMA_ACCESS_TOKEN`.

- Flags: None

### Q2 — Target Folder & Asset Delivery Format
- Asked: Where should we create the folder in the workspace, and what is your preference for the asset formats?
- Captured: The user specified creating the folder inside the directory junction `projects/For AIOS/Micrographics/`. They want each asset stored as a raw SVG and as code (standalone files) so they can edit colors, styles, fonts, and text easily.
- Flags: None

### Q3 — Typography, Colors & Symbol Extraction
- Asked: How should typography, colors, and reusable symbols (icons/infographics) be handled and customized?
- Captured: Use Google Fonts for custom typography. Bind colors to CSS variables/React props. Extract all individual icons, symbols, and geometric patterns used in the frames as separate standalone SVG files in a `symbols/` directory, allowing them to be reused anywhere.
- Flags: None

## Open flags (pending input)
- None

## adversarial roast council

### Stances & Persona Feedback

#### 1. The Contrarian (Red Team)
- **Stance**: RESHAPE (Score: 6/10)
- **Feedback**: Figma's default SVG exporter frequently converts text elements into outlined vector paths (`<path d="...">`). If that happens, the SVGs are completely uneditable in code, destroying the goal. Re-creating all 50 frames as custom HTML/CSS layouts manually is a recipe for weeks of alignment bugs. We need a compiler script that parses the JSON tree to extract the actual text strings and dimensions, then layers HTML/CSS text nodes over the SVGs to ensure perfect editability.

#### 2. The Expansionist (Bull)
- **Stance**: GO (Score: 9/10)
- **Feedback**: 50 micrographics templates are a content engine. This is a massive unlock for Zorixel's visual brand and social feed. It creates a reusable asset marketplace that can also be packaged as a commercial product later.

#### 3. The Logician (First principles)
- **Stance**: RESHAPE (Score: 7/10)
- **Feedback**: Do not copy-paste code for 50 files. Write a central build/compiler script in Python. Let it read `figma_file.json`, iterate through nodes `001` to `050`, map children recursively, and output `001.svg`, `001.html`, and `001.jsx`. This guarantees consistency, cuts down implementation time by 90%, and makes corrections instant.

#### 4. The Researcher (Evidence)
- **Stance**: GO (Score: 8/10)
- **Feedback**: Competitors like Jordan Watkins or premium agencies use structured geometric overlays and mini-badges extensively. SVGs and clean CSS code blocks are highly sought after by vibe coders and frontend developers. High real-world demand.

#### 5. The Buyer (Voice of customer)
- **Stance**: GO (Score: 8/10)
- **Feedback**: "I want to copy-paste these cards into my landing pages and just edit the text in VS Code or change the main color. If I have to go back to Figma to change a title, this package is useless to me. Keep the code super clean and variable-driven."

---

## THE VERDICT: RESHAPE
Confidence: High

**The call in one line:** Reshape the plan to build an automated python compiler script (`scripts/compile_micrographics.py`) that handles the Figma SVG downloads, parses text/typography coordinates from the JSON document, and programmatically generates the 50 editable HTML, JSX, and raw SVG files.

**Why:** Direct SVG exports from Figma lose text tag editability. Layering real, styled HTML text elements over base SVG background templates via absolute positioning maps exactly to the user's need for inline code editability. A compiler script eliminates manual labor and guarantees perfect accuracy.

**Biggest risk:** Special text shapes, rotations, or overlapping text paths that are hard to align mathematically in CSS.
**Biggest upside:** A scalable generator script that can be used on any future Figma frame package.

**Money read:** Zero cost to build. Time-to-delivery is 1-2 days using a compiler script vs. weeks of manual code replication.

**The cheapest 48-hour test:** Export Figma Frame `001` and `006` raw SVGs and JSON data. Write a minimal python parser to output an HTML overlay and a JSX file. Verify the text layers align perfectly in a Playwright screenshot.

**If RESHAPE:** Programmatic Figma-to-Code parser rather than manual file creation.

**Council Scores:** Contrarian 6/10 · Expansionist 9/10 · Logician 7/10 · Researcher 8/10 · Buyer 8/10
