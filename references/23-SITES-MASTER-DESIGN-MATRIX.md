---
title: 23-Sites Master Design System & Blueprint Matrix
domain: architecture
summary: '*Synthesized from 23 award-winning reference sites: Active Theory, Obys Agency, Locomotive Agency, Merci Michel,
  Resn, Oryzo AI, Trionn Agency, Ashley Brooke, Detroit Paris, Gehry Getty, Sondaven, and more.* | Section Type | Signature
  Patterns & Layo'
critical_directives:
- Follow document guidance without bypassing established safeguards.
section_outline:
- 23-Sites Master Design System & Blueprint Matrix
- 🏛️ 1. Section Taxonomy & Macrostructures
- 🎨 2. Color Tokens & OKLCH Theme Architecture
- ⚡ 3. Motion Math & Physics Hooks
- GSAP ScrollTrigger Inertia Formula
read_triggers:
- When working on architecture in references/23-SITES-MASTER-DESIGN-MATRIX.md
- When reading context for 23-Sites Master Design System & Blueprint Matrix
tags:
- architecture
- 23-SITES-MASTER-DESIGN-MATRIX
updated: '2026-08-08'
---

# 23-Sites Master Design System & Blueprint Matrix

*Synthesized from 23 award-winning reference sites: Active Theory, Obys Agency, Locomotive Agency, Merci Michel, Resn, Oryzo AI, Trionn Agency, Ashley Brooke, Detroit Paris, Gehry Getty, Sondaven, and more.*

---

## 🏛️ 1. Section Taxonomy & Macrostructures

| Section Type | Signature Patterns & Layout Formulas | Primary Reference Sites |
|---|---|---|
| **Nav Header** | Floating glassmorphism pill, minimal sticky header, expand-on-scroll drawer, magnetic menu triggers | `oryzo-ai`, `grids-obys-agency`, `trionn-agency` |
| **Hero Stage** | Fullscreen 3D canvas background, split-screen typographic punch, video texture masks, interactive WebGL particle nodes | `active-theory`, `resn-corn-revolution`, `merci-michel` |
| **Bento Grid** | Modular 3x3 grid, variable aspect ratios (1x1, 2x1, 2x2), hover spotlight borders, noise background overlays | `oryzo-ai`, `outfit-hello-hello`, `locomotive-agency` |
| **Stage / Canvas** | Embedded Three.js/WebGL viewport, custom shader uniform controls, mouse-driven tilt & distortion | `active-theory`, `gehry-getty`, `merci-michel` |
| **Proof & Metrics** | Infinite horizontal marquee ticker, high-contrast statistic counters, client logo grid with grayscale-to-color hover | `detroit-paris`, `champions-4-good`, `sondaven` |
| **Footer Stage** | Massive brand headline, multi-column sitemap, dark mode contrast anchor, dynamic local time indicator | `grids-obys-agency`, `locomotive-agency`, `truck-n-roll` |

---

## 🎨 2. Color Tokens & OKLCH Theme Architecture

- **Dark Mode Anchor Palette**:
  - Background: `oklch(0.12 0.01 250)` (Deep Obsidian Ink)
  - Surface Card: `oklch(0.18 0.015 250 / 0.8)` (Subtle Glass Layer)
  - Primary Accent: `oklch(0.78 0.18 145)` (Vibrant Emerald Spark)
  - Secondary Accent: `oklch(0.72 0.19 250)` (Electric Indigo Glow)
  - Text Primary: `oklch(0.98 0.005 250)` (Clean Pure White)
  - Text Muted: `oklch(0.65 0.01 250)` (Muted Slate Fog)

- **Noise & Texture System**:
  - SVG noise overlay filter (`feTurbulence baseFrequency="0.8" numOctaves="3"`), 3% opacity.

---

## ⚡ 3. Motion Math & Physics Hooks

### GSAP ScrollTrigger Inertia Formula
```typescript
// ScrollTrigger Smooth Inertia Hook
export const useInertiaScroll = (targetRef: React.RefObject<HTMLElement>) => {
  useEffect(() => {
    if (!targetRef.current) return;
    gsap.fromTo(
      targetRef.current,
      { y: 60, opacity: 0 },
      {
        y: 0,
        opacity: 1,
        duration: 1.2,
        ease: "power3.out",
        scrollTrigger: {
          trigger: targetRef.current,
          start: "top 85%",
          toggleActions: "play none none reverse",
        },
      }
    );
  }, [targetRef]);
};
```

### Magnetic Hover Cursor Formula
```typescript
// Magnetic Button Effect
export const useMagnetic = (ref: React.RefObject<HTMLElement>, strength = 0.3) => {
  const handleMouseMove = (e: MouseEvent) => {
    if (!ref.current) return;
    const { left, top, width, height } = ref.current.getBoundingClientRect();
    const x = (e.clientX - (left + width / 2)) * strength;
    const y = (e.clientY - (top + height / 2)) * strength;
    gsap.to(ref.current, { x, y, duration: 0.4, ease: "power2.out" });
  };
  const handleMouseLeave = () => {
    if (!ref.current) return;
    gsap.to(ref.current, { x: 0, y: 0, duration: 0.6, ease: "elastic.out(1, 0.3)" });
  };
  return { handleMouseMove, handleMouseLeave };
};
```

---

## 📂 4. 23-Site Component Mapping

All 300+ extracted components are indexed in `references/23-sites-matrix.json` and queryable via `python scripts/design_synthesis_engine.py search-pattern <query>`.
