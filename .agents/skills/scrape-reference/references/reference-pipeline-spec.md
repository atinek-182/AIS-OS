# Ultimate Site DNA & Full-Code Ingestion Engine Pipeline Specification

This document provides the technical reference specification for the Ultimate Site DNA, Full-Code Mirroring, and Master Vault Reference Engine in AIOS.

---

## 🔒 Core Operational Principles

1. **Strict One-by-One Sequential Execution Guard:**
   - Process **EXACTLY ONE SITE AT A TIME**.
   - Complete site $N$ fully (source mirroring, video recordings, code extractions, master reference manual, vault indexing), present raw file links, update queue tracking, and **STOP**.
   - **NEVER proceed to site $N+1$ without explicit user command.**

2. **Unbounded Exhaustive Discovery & Non-Exhaustive Examples Rule:**
   - Any list of examples provided in instructions or prompts (e.g. *"navbars, buttons, heroes, GSAP, WebGL shaders"*) is strictly an illustrative sample, **NEVER a restrictive limit**.
   - The AI agent MUST proactively discover, extract, deconstruct, and document **EVERY SINGLE novel element, component, script, animation, shader, and interaction** present on the target website.
   - Dynamically create new subfolders (`code-extracts/[novel-feature]/`) for any newly discovered pattern (e.g., audio-reactive UI, 3D product customizer, fluid simulations, custom physics canvas).

---

## 1. Full Source & Media Mirroring Architecture (`mirror/`)

The ingestion script (`scripts/scrape_full_site_mirror.py`) intercepts network responses and DOM state to save 100% of the site's raw assets:

```
premium-frontend-experience-system/reference-inputs/sites/[site-slug]/
├── mirror/
│   ├── index.html                      # Complete page DOM markup
│   ├── en.html / locale.html           # Full localized page copies
│   ├── css/                            # All linked CSS stylesheets
│   ├── js/                             # All JS bundles & Web Worker scripts
│   ├── fonts/                          # Custom font files (.woff2, .ttf, .otf)
│   └── misc/                           # 3D Mesh Buffers (.buf, .glb, .gltf), Rive (.riv, .wasm), Splat Sorters
├── assets/
│   ├── wireframe.html                  # Hyper-Detailed Visual UI Wireframe HTML Blueprint
│   ├── wireframe.png                   # High-Resolution Visual Wireframe Screenshot (1440x1100)
│   ├── recording_[site-slug].webp      # Browser session interaction WebP video
│   ├── desktop_1920.png                # Ultra-wide desktop screenshot (1920x1080)
│   ├── laptop_1440.png                 # Laptop screenshot (1440x900)
│   ├── tablet_1024.png                 # Tablet landscape screenshot (1024x768)
│   ├── tablet_768.png                  # Tablet portrait screenshot (768x1024)
│   ├── mobile_375.png                  # Mobile screenshot (375x812)
│   ├── images/                         # PBR Material Maps (height, normal, specular, gobo, WebP/PNG)
│   └── videos/                         # Mirrored MP4, WebM background videos
└── code-extracts/
    ├── components/                     # Standalone React + TypeScript (.tsx) drop-in components
    ├── animations/                     # Raw GSAP timelines, Lenis math, inline scripts (.js)
    ├── shaders/                        # Raw WebGL / Three.js GLSL shaders (.glsl)
    └── styles/                         # OKLCH design tokens, keyframe animations, inline styles (.css)
```

---

## 2. Dynamic Unbounded Master Reference Manual (15+ Categories)

For every site, generate `premium-frontend-experience-system/vault-references/[site-slug]-granularity-master.md` covering **all 15 baseline categories + dynamic $N+$ categories for any novel site features**:

1. **Meta, SEO, & Favicons:** Viewport tags, OpenGraph WebP image ratios (`1200x630`), Twitter cards, Schema.org JSON-LD structured data, favicons (`32x32`, `256x256`).
2. **Preloader & Entrance System:** Percentage loading counter (`0%` -> `100%`), visit detection (`hasVisited`), scroll-locking physics (`--scrollbar-width = innerWidth - clientWidth`).
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

---

## 3. Dedicated Master Vault Reference Indexing

All site extractions are registered in the centralized vault index:

📄 **[`premium-frontend-experience-system/vault-references/INDEX.md`](file:///d:/AI-OS/premium-frontend-experience-system/vault-references/INDEX.md)**

---

## 4. Ultra-Exhaustive 10-Pillar Deep Analysis (`DEEP_ANALYSIS.md`) Standard

Every site MUST include `premium-frontend-experience-system/reference-inputs/sites/[site-slug]/DEEP_ANALYSIS.md` as an exhaustive 100+ line research document covering:
1. **Executive Summary & Studio/Award Pedigree:** Web search via `search_web` for studio background, Awwwards, FWA, CSSDA awards, client context, and case study details.
2. **Visual & Aesthetic Design Psychology:** Color contrast, OKLCH tokens, spatial density, dark/light theme switching, brand positioning.
3. **Typography Architecture & Micro-Kerning:** Font stacks, SplitText wrappers, baseline vertical rhythm formulas ($\text{fontSize} \times \text{lineHeight}$), special glyph compressing (e.g., `YakuHanJP`).
4. **Grid Math & Responsive Geometry:** 24 micro-column division, `--gw` ratio formulas, breakpoints, margin/gutter scales.
5. **Full-Stack Source Code & JavaScript Engineering:** Analysis of JS bundles (`prod-desktop.js`, `SplatsWorker-DSMxtdkh.js`), animation hooks (`.js-split-l`, `.js-inview`, `.flip`, `.js-clip`), Barba.js page routing, Alpine.js reactivity.
6. **WebGL Shader Pipeline & Canvas Math:** GLSL fragment shaders, uniforms (`uTime`, `uProgress`, `uMouse`), texture sampling, FPS optimization.
7. **Dynamic Interactive Widgets & Timezone/Audio Mechanics:** Real-time clock widgets, JST calculations, DOM hydration, kanji typography pairing, audio streams.
8. **UX Psychology & Micro-Interactions:** Difference blend mode cursor physics, SVG progress rings `getPointAtLength()`, slide index counters.
9. **Media & Preloading Pipeline:** MP4/WebM video preloading, CloudFront CDN routing, responsive image scaling.
10. **AIOS System Integration & Reusable Code Blueprints:** Direct links to runnable React components, CSS tokens, GSAP scripts, GLSL shaders.

