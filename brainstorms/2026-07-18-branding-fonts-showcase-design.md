# Design Spec: Branding Fonts Showcase Deck for ZORIXEL
Date: 2026-07-18 · Goal: Design and implement a premium, interactive, zero-dependency HTML presentation deck that showcases four branding routes for ZORIXEL using 13 local font files.

## Visual Concept
A single 1920×1080 design stage presentation. Each of the four routes has its own layout grid, color palette, typographic scaling, and design mood, preventing templated AI-slop appearance. The presentation is interactive, supporting keyboard navigation, slide transition effects, and live in-browser text editing.

---

## 1. Brand Route Systems

### Route A: Modern Futuristic (AI & Tech Vibe)
*   **Palette:** Background: Deep Carbon Black (`#090b10`), Text: Arctic White (`#f0f4f8`), Accents: Electric Teal (`#00f5c4`), Steel Blue (`#4a5768`).
*   **Fonts:** Header: `Bezmiar`, Subhead: `LunaObscura`, Body/UI: `Nuqun`.
*   **Layout:** 1px stroke lines, asymmetric screens, mono metadata tags, modern telemetry.

### Route B: Elegant & Premium (Design-First Vibe)
*   **Palette:** Background: Deep Charcoal Gray (`#111111`), Text: Linen Off-White (`#f5f5f7`), Accent: Terracotta-Coral (`#df5d4b`).
*   **Fonts:** Header: `Rosehot`, Subhead: `Malvides`, Body/UI: `Nuqun`.
*   **Layout:** Editorial text frames, offset quote blocks, generous whitespace, soft shadows.

### Route C: Bold & Social-First (High Energy Vibe)
*   **Palette:** Background: Jet Black (`#000000`), Text: Stark White (`#ffffff`), Accent: Safety Orange (`#ff5500`).
*   **Fonts:** Header: `Grith` / `SunsetHeavyNarrow`, Subhead: `Nighthawk`, Body/UI: `Nuqun`.
*   **Layout:** 2px bold solid borders, massive typography overlays, content cards, high energy.

### Route D: Quirky / Creative Experimental (Indie Vibe)
*   **Palette:** Background: Deep Forest Green (`#0c2117`), Text: Sage Green White (`#ecf4f0`), Accent: Pale Mint (`#7df9be`).
*   **Fonts:** Header: `Vixa`, Subhead: `Kalamayka`, Body/UI: `Orbix`.
*   **Layout:** Overlapping card modules, organic silhouettes, playful grid structures.

---

## 2. Slide Structure
The deck will contain 19 slides:

*   **Slide 1: Title Slide** — "ZORIXEL / Typography Brand Exploration"
*   **Slide 2: Font Directory** — Map of the 13 local fonts, weights, and categories
*   **Slide 3-6: Route A (Modern Futuristic)**
    *   Slide 3: Vibe Sheet (Palette, keywords, style guides)
    *   Slide 4: Logo Playgrounds ("ZORIXEL" & "ZORIXEL AI" in Bezmiar/LunaObscura)
    *   Slide 5: Card UI (Course / AI Tool telemetry card using Route A styles)
    *   Slide 6: Poster Banner ("RETHINK DESIGN IN THE AGE OF AI" with abstract dark geometric photography)
*   **Slide 7-10: Route B (Elegant & Premium)**
    *   Slide 7: Vibe Sheet
    *   Slide 8: Logo Playgrounds (Elegant serif "ZORIXEL" wordmark)
    *   Slide 9: Content Card (Instagram carousel layout)
    *   Slide 10: Poster Banner ("CRAFTING THE FUTURE OF THE WEB" with minimalist architecture photography)
*   **Slide 11-14: Route C (Bold & Social-First)**
    *   Slide 11: Vibe Sheet
    *   Slide 12: Logo Playgrounds (High-impact bold typography wordmark)
    *   Slide 13: Social Card (YouTube thumbnail and video player layout)
    *   Slide 14: Poster Banner ("DESIGN WITHOUT SLOP" statement)
*   **Slide 15-18: Route D (Quirky & Creative)**
    *   Slide 15: Vibe Sheet
    *   Slide 16: Logo Playgrounds (Playful experimental wordmark)
    *   Slide 17: Interactive Card (Bohemian card grid)
    *   Slide 18: Poster Banner ("VIBE CODING AND ART" forest graphic)
*   **Slide 19: Interactive Comparison & Voting**
    *   A grid comparison of all 4 routes with dynamic local voting UI.

---

## 3. Technical Requirements
- **Local Fonts Loading:** Loaded using CSS `@font-face` referencing extracted `.otf` and `.ttf` files in `fonts/`.
- **Keyboard Navigation:** Left/Right arrows, Space, PageUp/PageDown.
- **Stage Scaling:** Fixed 1920×1080 stage scaled uniformly to the browser viewport using CSS transform.
- **Interactive Inline Editor:** Press `E` to toggle edit mode, allowing text blocks to have `contenteditable="true"` for copy reviews.
- **Background Images:** Rich Unsplash photos loaded via CDN with matching parameters.

## 4. Verification Plan
- **Local Browser Review:** Verify the presentation loads local fonts correctly.
- **Playwright Console Audit:** Verify no console errors (missing fonts or broken script execution).
- **Layout Checks:** Verify 1920×1080 stage scales correctly on desktop and mobile viewports.
- **Contrast Check:** Verify WCAG AA compliance for text content.
