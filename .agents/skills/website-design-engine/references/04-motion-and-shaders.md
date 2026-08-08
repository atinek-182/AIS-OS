---
title: 'Phase 4 Reference: Motion Engineering, Lenis, GSAP & WebGL Shaders (v4.0)'
domain: skill
summary: 'Motion intensity is established in Phase 0 Q&A. Every animation must serve a clear purpose (hierarchy, tactile feedback,
  spatial transition, narrative sequence): - **Dial 0–3 (Airy / Minimalist)**: Clean CSS hover transitions (`duration-200
  ease-out`'
critical_directives:
- Follow document guidance without bypassing established safeguards.
section_outline:
- 'Phase 4 Reference: Motion Engineering, Lenis, GSAP & WebGL Shaders (v4.0)'
- Motion Dialing Matrix (Dial 0 to 10)
- Lenis Smooth Momentum Scroll & RAF Sync
- Native CSS View Timeline Animation Offloading
- Interactive Radiant Shader HTML Protocol (`pbakaus/radiant`)
read_triggers:
- When working on skill in .agents/skills/website-design-engine/references/04-motion-and-shaders.md
- 'When reading context for Phase 4 Reference: Motion Engineering, Lenis, GSAP & WebGL Shaders (v4.0)'
tags:
- skill
- 04-motion-and-shaders
updated: '2026-08-08'
---

# Phase 4 Reference: Motion Engineering, Lenis, GSAP & WebGL Shaders (v4.0)

## Motion Dialing Matrix (Dial 0 to 10)

Motion intensity is established in Phase 0 Q&A. Every animation must serve a clear purpose (hierarchy, tactile feedback, spatial transition, narrative sequence):

- **Dial 0–3 (Airy / Minimalist)**: Clean CSS hover transitions (`duration-200 ease-out`), subtle press scale (`0.98`), native CSS View Timeline scroll reveals (`animation-timeline: view()`), zero heavy JS scroll hooks.
- **Dial 4–6 (Kinetic / Interactive)**: Lenis smooth momentum scroll, GSAP ScrollTrigger sticky-card stacks, horizontal scroll tracks, magnetic button cursors (`scale(1.03)` with `cubic-bezier(0.16, 1, 0.3, 1)`).
- **Dial 7–10 (Immersive / 3D Canvas)**: Three.js / React Three Fiber interactive 3D stages, Radiant WebGL GLSL shaders (`pbakaus/radiant`), audio-reactive visualizers, particle physics.

---

## Lenis Smooth Momentum Scroll & RAF Sync

When `MOTION_INTENSITY >= 4`, initialize Lenis momentum scrolling and sync with GSAP ScrollTrigger:

```typescript
import Lenis from '@studio-freight/lenis';
import { gsap } from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';

gsap.registerPlugin(ScrollTrigger);

export const initSmoothScroll = () => {
  const lenis = new Lenis({
    duration: 1.2,
    easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
    smoothWheel: true,
  });

  lenis.on('scroll', ScrollTrigger.update);

  gsap.ticker.add((time) => {
    lenis.raf(time * 1000);
  });

  gsap.ticker.lagSmoothing(0);
  return lenis;
};
```

---

## Native CSS View Timeline Animation Offloading

For simple scroll reveals, offload animation from main-thread JS to native CSS Scroll-Driven Animations:

```css
@keyframes reveal-up {
  from {
    opacity: 0;
    transform: translateY(40px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.scroll-reveal {
  animation: reveal-up linear both;
  animation-timeline: view();
  animation-range: entry 10% cover 30%;
}
```

---

## Interactive Radiant Shader HTML Protocol (`pbakaus/radiant`)

When a WebGL background or generative graphic is considered:
1. Ask the user: *"Would you like a WebGL shader background here? If yes, which shader from radiant-shaders.com gallery?"*
2. The user will place the HTML file into `reference/`.
3. Extract and adapt vertex/fragment shader programs and uniform controls directly from that HTML file into your WebGL canvas stage.

---

## GSAP ScrollTrigger Canonical Skeletons

### A. Sticky-Stack Scroll (Card Stack Effect)
```tsx
"use client";
import { useRef, useEffect } from "react";
import { gsap } from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";

gsap.registerPlugin(ScrollTrigger);

export function StickyStack({ cards }: { cards: React.ReactNode[] }) {
  const ref = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (!ref.current) return;
    const ctx = gsap.context(() => {
      const cardEls = gsap.utils.toArray<HTMLElement>(".stack-card");
      cardEls.forEach((card, i) => {
        if (i === cardEls.length - 1) return;
        ScrollTrigger.create({
          trigger: card,
          start: "top top",
          endTrigger: cardEls[cardEls.length - 1],
          end: "top top",
          pin: true,
          pinSpacing: false,
        });
        gsap.to(card, {
          scale: 0.92,
          opacity: 0.55,
          ease: "none",
          scrollTrigger: {
            trigger: cardEls[i + 1],
            start: "top bottom",
            end: "top top",
            scrub: true,
          },
        });
      });
    }, ref);
    return () => ctx.revert();
  }, []);

  return <div ref={ref}>{cards}</div>;
}
```

### B. Magnetic Hover Button Physics
```typescript
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
