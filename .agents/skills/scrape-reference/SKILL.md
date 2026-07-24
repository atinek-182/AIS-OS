---
name: scrape-reference
description: Ultimate site DNA ingestion, full-code mirroring, dot-to-dot web analysis, and vault reference indexing engine. Intercepts and mirrors full site source (HTML, CSS, JS bundles, fonts, videos, GLSL shaders), extracts raw GSAP/animation code (.js), synthesizes drop-in React components (.tsx), records visual WebP session videos, and creates dot-to-dot 14-category master reference manuals in vault-references/.
argument-hint: [website URL]
---

# Ultimate Scrape Reference Skill (Full-Code Mirroring & Dot-to-Dot Vault Reference Engine)

Use this skill whenever given a website URL (or list of URLs) to execute full site source code mirroring, video/screenshot visual capture, raw GSAP/animation code extraction, drop-in React component synthesis, dot-to-dot micro/macro decision analysis, and indexing into `premium-frontend-experience-system/vault-references/`.

For complete technical specifications, network interceptor schemas, and deep architectural rules, see [reference-pipeline-spec.md](references/reference-pipeline-spec.md).

---

## 🔒 Mandatory Operational Rules

1. **Strict Sequential Execution Guard (One-by-One Only):**
   - When processing a list of URLs (e.g. 18-site queue), process **EXACTLY ONE SITE AT A TIME**.
   - Finish site $N$ completely (mirroring, visual assets, code extraction, dot-to-dot analysis, vault indexing), present the summary and raw file links, update `INGESTION_QUEUE.md` and `brainstorms/`, and **STOP**.
   - **DO NOT start site $N+1$ until the user explicitly commands "Proceed to next site" or equivalent.**

2. **Full Source, 3D Assets & Media Mirroring (`mirror/`):**
   - Run `python scripts/scrape_full_site_mirror.py [URL] [SITE_SLUG]` to intercept and download 100% of the target site's raw assets:
     - `index.html` (complete page DOM markup)
     - Linked CSS stylesheets (`mirror/css/`) and inline styles (`code-extracts/styles/inline-styles.css`)
     - JS bundles (`mirror/js/`) and inline scripts (`code-extracts/animations/inline-scripts.js`)
     - Custom font files (`mirror/fonts/` `.woff2`, `.ttf`, `.otf`)
     - **3D Mesh Buffers, Splats & Models:** (`mirror/misc/` `.buf`, `.glb`, `.gltf`, `.splat`, `.ksplat`, `.ply`, `.obj`, `.sog`)
     - **Vector Animation & Engine Runtimes:** (`mirror/misc/` `.riv`, `.wasm`, `.json`)
     - **PBR Material Maps, Gobos & Images:** (`assets/images/` normal maps, height maps, specular maps, environmental textures, WebP/AVIF assets)
     - Images, SVGs, MP4/WebM videos (`assets/`)
   - Capture 5 responsive viewport screenshots: `desktop_1920.png`, `laptop_1440.png`, `tablet_768.png`, etc.
   - Record WebP browser interaction session video (`recording_[site-slug].webp`).
   - **Hyper-Detailed Visual UI/UX Wireframe Blueprint (`assets/wireframe.html` & `assets/wireframe.png`):** Generate a hyper-detailed, section-by-section visual wireframe HTML page and Playwright screenshot (`wireframe.png`) containing actual site headlines, copy outlines, navigation controls, 3D WebGL canvas boxes, scrollytelling card grids, interactive prompt widgets, component specification tags, and technical annotations (GSAP parameters, CSS flex/grid math, backdrop blur filters, and scroll thresholds).

3. **Raw Code Extraction (`code-extracts/`):**
   - Extract raw, runnable code files:
     - `code-extracts/components/` — Standalone React + TypeScript (`.tsx`) components (e.g. `Nav.tsx`, `Hero.tsx`, `MagneticButton.tsx`, `Card.tsx`)
     - `code-extracts/animations/` — Exact GSAP timelines, `ScrollTrigger` pin ranges, Lenis easing functions, motion smoothness math, magnetic cursor scripts (`.js`)
     - `code-extracts/shaders/` — Raw WebGL / Three.js GLSL vertex & fragment shader files (`.glsl`)
     - `code-extracts/styles/` — OKLCH design tokens, CSS keyframe animations (`.css`)

4. **Dynamic Unbounded Master Reference Manual (15+ Categories):**
   - Create `premium-frontend-experience-system/vault-references/[site-slug]-granularity-master.md` analyzing **all micro & macro web decision categories (15 baseline categories + dynamic N+ categories for any novel site features)**:
     1. **Meta, SEO, & Favicons:** Viewport tags, OpenGraph image ratios (`1200x630`), Schema.org JSON-LD structured data, favicons (`32x32`, `256x256`).
     2. **Preloader & Entrance System:** Percentage counter (`0%` -> `100%`), visit detection (`hasVisited`), scroll-locking physics (`--scrollbar-width = innerWidth - clientWidth`).
     3. **Navigation & Header System:** Fixed positioning, backdrop blur, hide/reveal directional scroll delta thresholds (`>40px`), link hover underline `clip-path`.
     4. **Cursor & Pointer Physics:** Mobile/touch detection, magnetic pull formulas ($\Delta X, \Delta Y$), inner vs outer target elastic spring easing (`ease: "elastic.out(1, 0.3)"`).
     5. **Typography & Text Rendering:** Fluid `clamp()` font-size math, line-height ratios, SplitText lines/words/chars, ARIA accessibility attributes (`aria="none"` on split wrappers).
     6. **OKLCH Color Tokens & Theme Engine:** Token formulas, contrast switching DOM triggers (`[bg="color"]`, `[bg="light"]`, `[bg="dark"]`).
     7. **Hero Section Architecture:** Full-screen viewport hero, kinetic word reveal stagger, floating scroll indicator bounce keyframes.
     8. **Scrollytelling & Parallax Engine:** Parallax image transform math (`yPercent: -20 -> 20`), text character highlight opacity scrub (`0.1 -> 1.0`), section snap debounce timers (`40ms`).
     9. **Interactive UI Widgets & Cards:** Benefit cards, tab morphing, load-more array slicing, marquee ticker velocity scaling.
     10. **Drag-along-Path SVG Slider:** `getPointAtLength()` curve tracking and progress interpolation.
     11. **Proximity-Based Interactive Map Pins:** Euclidean distance formula calculation ($\sqrt{\Delta x^2 + \Delta y^2}$).
     12. **Audio & Soundscape UI System:** Audio stream initialization, volume fade in/out (`0 -> 0.25`), Web Audio visualizer bars loop.
     13. **Modals, CTAs, & Form Mechanics:** 3D Y-axis card flip form submit animation (`rotateY: 0 -> -180`), input regex sanitization (`[^\d+\-]`).
     14. **Footer & Page Transition System:** Scroll scale zoom (`scale: 2 -> 1`), Barba.js 20x12 dither grid page transitions, WebGL/ScrollTrigger memory cleanup.
     15. **3D Models, Rive Runtimes & Motion Physics Inventory:** Intercepted 3D geometry buffers (`.buf`, `.glb`, `.gltf`), Gaussian Splat depth sorters (`.wasm`), Rive vector files (`.riv`), PBR texture maps, GSAP timeline code, and Lenis scroll smoothness parameters.

5. **Central Vault Indexing (`vault-references/INDEX.md`):**
   - Register the site in `premium-frontend-experience-system/vault-references/INDEX.md` with links to raw mirrored HTML, raw JS bundles, 3D model buffers, inline scripts, stylesheets, `.tsx` components, `.js` animation scripts, `.glsl` shaders, and visual media assets.

6. **Unbounded Exhaustive Discovery & Non-Exhaustive Examples Rule:**
   - **Examples Are Non-Exhaustive Samples:** Any example list provided in instructions (e.g., "nav, hero, buttons, GSAP, Lenis, WebGL, 3D models") is strictly an illustrative baseline sample, NEVER a restrictive boundary.
   - **Proactive Site Exploration:** Every website has its own unique tech stack, custom components, novel scripts, canvas shaders, SVG physics, or interaction models. The AI agent MUST proactively inspect, discover, extract, and document **EVERY SINGLE novel element, component, script, animation, shader, 3D model, Rive file, and interaction** present on that specific website — even if not explicitly named in an example list.
   - **Dynamic Custom Subfolders:** If a target features a novel technology or pattern (e.g., audio-reactive UI, 3D product customizer, fluid simulations, custom physics canvas, WebRTC, drag physics), create a dedicated subfolder/section for it automatically (`code-extracts/[novel-feature]/`).

7. **Mandatory Web Research & 10-Pillar Ultra-Exhaustive Deep Analysis (`DEEP_ANALYSIS.md`):**
   - For EVERY ingested site, perform web research via `search_web` to retrieve studio background, Awwwards/FWA/CSSDA awards, client context, and case study details.
   - Write `premium-frontend-experience-system/reference-inputs/sites/[site-slug]/DEEP_ANALYSIS.md` as a comprehensive 10-pillar research document (100+ lines). Short 20-30 line summaries or placeholders are STRICTLY FORBIDDEN.
   - The 10 mandatory pillars are:
     1. Executive Summary & Studio/Award Pedigree
     2. Visual & Aesthetic Design Psychology
     3. Typography Architecture & Micro-Kerning
     4. Grid Math & Responsive Geometry
     5. Full-Stack Source Code & JavaScript Engineering
     6. WebGL Shader Pipeline & Canvas Math
     7. Dynamic Interactive Widgets & Timezone/Audio Mechanics
     8. UX Psychology & Micro-Interactions
     9. Media & Preloading Pipeline
     10. AIOS System Integration & Reusable Code Blueprints



---

## 📂 Output Directory Architecture

For target site `[site-slug]`:
- `premium-frontend-experience-system/reference-inputs/sites/[site-slug]/`
  - `mirror/` — Raw mirrored source files (`index.html`, `en.html`, `css/`, `js/`, `fonts/`)
  - `assets/` — Visual media (`recording_[site-slug].webp`, 5 viewport screenshots, site videos)
  - `code-extracts/`
    - `components/` — Standalone React + TypeScript (`.tsx`) drop-in components
    - `animations/` — Raw GSAP timelines, Lenis scroll setups, physics math (`.js`)
    - `shaders/` — Raw WebGL / Three.js GLSL vertex & fragment shaders (`.glsl`)
    - `styles/` — OKLCH design tokens, CSS keyframes, inline styles (`.css`)
   - `site-dna.md` — 5-layer site DNA report with embedded code blocks and file links
   - `DEEP_ANALYSIS.md` — Ultra-exhaustive 10-pillar architectural & web research analysis (studio pedigree, awards, design psychology, typography micro-kerning, grid math, JS bundle engineering, GLSL shader math, timezone/clock mechanics, cursor physics, and reusable code blueprints). MUST NOT be a brief summary or short placeholder.
- `premium-frontend-experience-system/vault-references/`
  - `INDEX.md` — Central vault reference index
  - `[site-slug]-granularity-master.md` — 14-category dot-to-dot master reference manual
