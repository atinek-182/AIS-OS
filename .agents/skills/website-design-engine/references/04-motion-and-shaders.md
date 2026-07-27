# ⚡ Phase 4 Reference: Motion Engineering, GSAP & WebGL Shaders

## 1. Motion Dialing Matrix (Dial 0 to 10)

Motion intensity is established in Phase 0 Q&A. Every animation must serve a clear purpose (hierarchy, tactile feedback, spatial transition, narrative sequence):

- **Dial 0–3 (Airy / Minimalist)**: Clean CSS hover transitions (`duration-200 ease-out`), subtle press scale (`0.98`), zero heavy JS scroll hooks.
- **Dial 4–6 (Kinetic / Interactive)**: Motion/React reveal animations, GSAP ScrollTrigger sticky-card stacks, horizontal scroll tracks, magnetic button cursors.
- **Dial 7–10 (Immersive / 3D Canvas)**: Three.js / React Three Fiber interactive 3D stages, custom GLSL liquid/aurora shaders, audio-reactive visualizers, particle physics.

---

## 2. AUTOMATIC MANDATORY PURE SKILLS INGESTION STEP

When `MOTION_INTENSITY > 3`, you MUST NOT rely on memory alone. Execute `view_file` automatically on the target pure skill instructions BEFORE writing code:

- **GSAP & ScrollTrigger Animation**: Read `d:\AI-OS\brain-aios\wiki\research\skills-library\gsap-skills\SKILL.md` (or `C:\Users\HP\.gemini\config\skills\gsap-animation\SKILL.md`) for pin spacing, scrub math, text split reveals, and Lenis smooth scroll setup.
- **Three.js & GLSL Canvas Shaders**: Read `d:\AI-OS\brain-aios\wiki\research\skills-library\threejs-skills\SKILL.md` (or `C:\Users\HP\.gemini\config\skills\threejs-webgl\SKILL.md`) for vertex/fragment shader programs, camera lighting, and frame-rate throttling.

---

## 3. GSAP ScrollTrigger Canonical Skeletons

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

## 4. Motion Performance Rules & WebGL Canvas Fallbacks

- **NEVER use `useState` for Scroll/Pointer Physics**: Always use Motion's `useMotionValue` and `useTransform`. React state re-renders cause severe jank on mobile devices.
- **Hardware Acceleration**: Animate ONLY `transform` (`translate`, `scale`, `rotate`) and `opacity`. Never animate `top`, `left`, `width`, `height`, or `margin`.
- **Forbidden Scroll Listener**: Raw `window.addEventListener("scroll")` state updates are BANNED. Use Motion `useScroll()` or GSAP `ScrollTrigger`.
- **Mandatory WebGL Canvas Fallback Guard**:
  ```tsx
  // WebGL Container Guard Pattern
  export function SafeCanvas({ children, fallback }: { children: React.ReactNode; fallback: React.ReactNode }) {
    const [webGlAvailable, setWebGlAvailable] = useState(true);
    useEffect(() => {
      try {
        const canvas = document.createElement("canvas");
        const hasGl = !!(window.WebGLRenderingContext && (canvas.getContext("webgl") || canvas.getContext("experimental-webgl")));
        setWebGlAvailable(hasGl);
      } catch (e) {
        setWebGlAvailable(false);
      }
    }, []);

    return webGlAvailable ? <>{children}</> : <div className="canvas-fallback-container">{fallback}</div>;
  }
  ```
- **Pause Render Loops**: Pause WebGL render loops (`requestAnimationFrame`) when canvas is not intersecting the active viewport (`IntersectionObserver`).
- **Reduced Motion Safety**: All animations MUST degrade gracefully to static layout when `@media (prefers-reduced-motion: reduce)` is active.
