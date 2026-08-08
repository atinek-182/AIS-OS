# Phase 1 Reference: Macrostructures, Token Extraction & Brand Systems (v4.0)

## 21 Hallmark Macrostructure Archetypes

Select ONE macrostructure archetype that fits the brief's subject matter. Do not default to standard hero -> 3-column feature -> CTA:

1. **Asymmetric Editorial**: Off-center hero, wide display typography, generous whitespace, staggered content blocks.
2. **Bento Showcase**: Asymmetric grid tiles with varied cell spans, mixed media, and high-density visual storytelling.
3. **Fullscreen Canvas / WebGL Stage**: Interactive 3D/GLSL background canvas with floating minimalist UI controls.
4. **Split-Screen Studio**: 50/50 sticky split; left column pins narrative copy, right column scrolls interactive assets.
5. **Kinetic Type Focus**: Massive display typography as primary visual anchor, scroll-driven text scaling.
6. **Monolithic Hero**: Dominant single-focus image or video hero with micro-overlay controls and hidden drawer nav.
7. **Minimal Dock**: Floating pill navigation, ultra-airy layout, high-contrast typography, zero card borders.
8. **Broadside Newspaper**: Dense multi-column grid, hairline borders, mono captions, editorial precision.
9. **Horizontal Pan Showcase**: Vertical scroll hijacked to horizontal track for portfolio projects or product walkthroughs.
10. **Sticky Stack Narrative**: Card stack on scroll; cards stack and shrink as user scrolls vertically down the page.
11. **Dark Tech Terminal**: Monospace accents, neon status indicators, command palette UI, dense telemetry metrics.
12. **Bento Hero Integration**: Hero section itself is an integrated multi-tile bento grid containing live widgets.
13. **Editorial Magazine Split**: Serif/display typography, drop caps, multi-column articles, pull quotes, rich captions.
14. **Floating Glass Layers**: Layered frosted glass panels over ambient mesh/aurora background.
15. **Brutalist Grid**: Raw thick borders, sharp zero-radius containers, high-contrast monochrome, bold typography.
16. **Product Stage / 3D Viewer**: Centered 3D product interactive canvas with floating spec callouts.
17. **App-Native Showcase**: Floating phone/tablet mockup stage with live interactive component preview.
18. **Launch Manifesto**: Center-aligned typography-first narrative flow with subtle scroll reveals.
19. **Interactive Playground**: Integrated live controls (sliders, swatches, toggles) driving instant UI preview.
20. **Color Block Story**: Sequential full-viewport color block transitions on scroll.
21. **Asymmetric Gallery**: Staggered masonry layout for creative media, photography, or case studies.

---

## Design Token Extraction & OKLCH Theme Architecture

Map all visual DNA into Tailwind CSS v4 `@theme` custom properties in `index.css`:

```css
@theme {
  --color-bg-primary: oklch(0.12 0.01 250);     /* Deep Obsidian Ink */
  --color-bg-surface: oklch(0.18 0.015 250 / 0.8); /* Glass Surface Layer */
  --color-border: oklch(0.25 0.02 250);
  --color-text-main: oklch(0.98 0.005 250);
  --color-text-muted: oklch(0.65 0.01 250);
  --color-accent-emerald: oklch(0.78 0.18 145);  /* Vibrant Emerald Pop */
  --color-accent-indigo: oklch(0.72 0.19 250);   /* Electric Indigo Glow */
  --font-logo: "Nuqun", sans-serif;
  --font-display-hero: "Havock", sans-serif;
  --font-display-sub: "Rosehot", sans-serif;
  --font-body: "Outfit", sans-serif;
  --font-mono: "Geist Mono", monospace;
}

/* 3% SVG Noise Overlay Texture */
.noise-bg {
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.8' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)' opacity='0.03'/%3E%3C/svg%3E");
}
```

---

## Brand Typography Safety Rules

- **Nuqun**: Signature brandmark logo typeface.
- **Havock**: Primary display typography for hero headlines and big middle titles.
  - **Safety Rule (Rule 1.14)**: Headlines larger than `64px` in `Havock` REQUIRE explicit `line-height: 1.28` and minimum `margin-bottom: 28px` to prevent multi-line text collisions.
- **Rosehot**: Editorial display typography for subheadings and section titles.
- **Outfit**: Primary body text for paragraphs, descriptions, and UI labels.
- **Geist Mono / JetBrains Mono**: Monospace font for telemetry, metrics, code, and structural tags.
