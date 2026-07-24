# 🏛️ Phase 1 Reference: Macrostructures & Brand Systems

## 1. 21 Hallmark Macrostructure Archetypes

Select ONE macrostructure that fits the brief's subject matter. Do not default to hero -> 3-col feature -> CTA:

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

## 2. Zorixel & Studio Typography Rules

- **Nuqun**: Primary logo mark & signature brand brandmark.
- **Rosehot**: Primary display font for major headlines, titles, and hero statements.
- **Outfit**: Primary body font for clean readability, body paragraphs, and UI labels.
- **Geist / JetBrains Mono**: Monospace utility font for technical metrics, code, captions, and structural tags.

### Typography Discipline:
- **Hero Headline**: `text-4xl md:text-6xl lg:text-7xl tracking-tighter leading-none`.
- **Body Paragraphs**: `text-base text-zinc-400 leading-relaxed max-w-[65ch]`.
- **Sans Display Default**: Sans-serif display is default for modern/tech/creative briefs. Serif fonts (like `PP Editorial New`, `Tiempos`, `Cormorant`) are ONLY used if explicitly requested or for heritage editorial briefs.
- **No Mixed-Family Emphasis**: Use italic/bold of the SAME font family for emphasis. Never inject a random serif word into a sans headline.
- **Italic Descender Clearance**: When italic display text contains `y g j p q`, set minimum `leading-[1.1]` and `pb-1` to prevent clipping.

---

## 3. OKLCH Color Math & Palette Rotation

Always use locked CSS variable tokens or Tailwind OKLCH themes. Max 1 accent color per page:

```css
@theme {
  --color-bg: oklch(0.14 0.01 260);
  --color-surface: oklch(0.18 0.02 260);
  --color-border: oklch(0.25 0.02 260);
  --color-text-main: oklch(0.95 0.01 260);
  --color-text-muted: oklch(0.65 0.02 260);
  --color-accent: oklch(0.65 0.22 140); /* Emerald Pop */
}
```

### Banned Default Palettes:
- BANNED: Warm beige/cream background (`#f5f1ea`) + brass/clay accent (`#b08947`) as generic default.
- BANNED: Generic AI purple gradient slop (`#8b5cf6` glow over `#09090b`).

### Rotational Palette Families:
1. **Cold Luxury**: Silver-grey (`oklch(0.92 0.005 240)`) + smoke + chrome accent.
2. **Forest**: Deep forest (`oklch(0.20 0.04 150)`) + bone + amber accent.
3. **Black & Tan**: True off-black (`oklch(0.12 0.01 260)`) + crisp tan accent.
4. **Cobalt + Cream**: Deep saturated cobalt pop against cool neutral.
5. **Terracotta + Slate**: Rust accent against slate-grey structure.
6. **Pure Monochrome + Pop**: Off-black + off-white + 1 vibrant pop (Emerald, Electric Cyan, Hot Pink).
