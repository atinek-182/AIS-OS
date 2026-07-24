# ⚡ Phase 4 Reference: Motion Engineering, GSAP & WebGL Shaders

## 1. Motion Strategy & Dial Gating

Apply animation ONLY when indicated by `MOTION_INTENSITY > 4`. Every animation must serve 1 of 4 functions:
1. **Hierarchy**: Drawing attention to primary element.
2. **Narrative Sequence**: Revealing content in story order.
3. **Tactile Feedback**: Confirming user interaction (press scale `0.98`).
4. **State Transition**: Explaining spatial origin of modals/drawers.

---

## 2. GSAP ScrollTrigger Canonical Skeletons

### A. Sticky-Stack Scroll (Card Stack Effect)
```tsx
"use client";
import { useRef, useEffect } from "react";
import { gsap } from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import { useReducedMotion } from "motion/react";

gsap.registerPlugin(ScrollTrigger);

export function StickyStack({ cards }: { cards: React.ReactNode[] }) {
  const ref = useRef<HTMLDivElement>(null);
  const reduce = useReducedMotion();

  useEffect(() => {
    if (reduce || !ref.current) return;
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
  }, [reduce]);

  return (
    <div ref={ref} className="relative">
      {cards.map((card, i) => (
        <div key={i} className="stack-card sticky top-0 min-h-[100dvh] flex items-center justify-center">
          {card}
        </div>
      ))}
    </div>
  );
}
```

### B. Horizontal-Pan Track (Vertical Scroll -> Horizontal Travel)
```tsx
"use client";
import { useRef, useEffect } from "react";
import { gsap } from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import { useReducedMotion } from "motion/react";

gsap.registerPlugin(ScrollTrigger);

export function HorizontalPan({ children }: { children: React.ReactNode }) {
  const wrap = useRef<HTMLDivElement>(null);
  const track = useRef<HTMLDivElement>(null);
  const reduce = useReducedMotion();

  useEffect(() => {
    if (reduce || !wrap.current || !track.current) return;
    const ctx = gsap.context(() => {
      const distance = track.current!.scrollWidth - window.innerWidth;
      gsap.to(track.current, {
        x: -distance,
        ease: "none",
        scrollTrigger: {
          trigger: wrap.current,
          start: "top top",
          end: () => `+=${distance}`,
          pin: true,
          scrub: 1,
          invalidateOnRefresh: true,
        },
      });
    }, wrap);
    return () => ctx.revert();
  }, [reduce]);

  return (
    <section ref={wrap} className="relative overflow-hidden">
      <div ref={track} className="flex h-[100dvh] items-center">
        {children}
      </div>
    </section>
  );
}
```

---

## 3. Motion/React State Rules & Anti-Patterns

- **NEVER use `useState` for Scroll/Pointer Physics**: Always use Motion's `useMotionValue` and `useTransform`. React state re-renders the component tree on every frame and causes severe jank on mobile devices.
- **Hardware Acceleration**: Animate ONLY `transform` (translate, scale, rotate) and `opacity`. Never animate `top`, `left`, `width`, `height`, or `margin`.
- **Forbidden Scroll Listener**: `window.addEventListener("scroll")` state updates are BANNED. Use Motion's `useScroll()` or GSAP's `ScrollTrigger`.
- **Marquee Limit**: Capped at max 1 marquee per page.
- **Reduced Motion Safety**: All animations MUST degrade gracefully to static layout when `prefers-reduced-motion: reduce` is active.

---

## 4. Three.js & WebGL Shader Fallbacks

When creating 3D canvases or custom GLSL shaders:
1. Always handle `webglcontextlost` events to restore the WebGL context.
2. Provide a 2D CSS background gradient/image fallback wrapper behind `<canvas>` so the page remains beautiful if WebGL is disabled or fails to initialize.
3. Pause WebGL render loop (`requestAnimationFrame`) when the canvas is not intersecting the active viewport (`IntersectionObserver`).
