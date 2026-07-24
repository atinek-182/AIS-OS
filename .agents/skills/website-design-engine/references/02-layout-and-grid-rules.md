# 📐 Phase 2 Reference: Layout, Grid Canons & Architecture Rules

## 1. Obys 4 Grid Canons & Vertical Rhythm Math

1. **Canon 1: Strict Column Alignment**: Every section must anchor to the same 12-column or asymmetric grid system. No rogue margin offsets (`ml-[17px]`).
2. **Canon 2: Vertical Rhythm Baseline**: Spacing between elements must follow an 8px/16px/24px/32px/48px/64px/96px step scale.
3. **Canon 3: Line-Length Cap**: Body paragraphs must cap at `max-w-[65ch]` to preserve reading comfort.
4. **Canon 4: Section Transition Rhythm**: Alternate padding and background shade (`bg-zinc-950` vs `bg-zinc-900`) between adjacent sections to define clear boundaries.

---

## 2. Hard Layout Rules & Anti-Pattern Bans

### Hero Section Discipline
- **Viewport Fit**: Hero MUST fit within initial viewport height (`min-h-[100dvh]`). Never use `h-screen` (causes mobile browser bar jumps).
- **Hero Top Padding Cap**: Top padding max `pt-24` (6rem) on desktop.
- **Hero Stack Cap (Max 4 Text Elements)**:
  1. Eyebrow OR brand strip (zero or one)
  2. Headline (max 2 lines)
  3. Subtext (max 20 words, max 4 lines)
  4. CTAs (1 primary + max 1 secondary)
- **Banned in Hero**: "Used by" logo walls inside the hero flex stack, pricing teasers, 10-line feature descriptions, or secondary taglines below CTAs.

### Eyebrow Restraint Rule (Critical Anti-Slop)
- An eyebrow is a small uppercase mono label above a headline (`text-xs uppercase tracking-widest`).
- **MAX 1 eyebrow per 3 sections**. Hero counts as 1. A page with 9 sections gets max 3 eyebrows total.
- If section A has an eyebrow, sections B and C CANNOT have an eyebrow.

### Section Layout Diversity
- **Layout Repetition Ban**: Once a section layout family (e.g. 3-column card grid, 50/50 text-image split) is used, it cannot be repeated on the page.
- **Zigzag Alternation Cap**: Alternating "left-image + right-text" then "left-text + right-image" is capped at max 2 consecutive sections. The 3rd consecutive split is a failure.
- **Split-Header Ban**: The pattern "left big headline + right small paragraph" is banned as default. Use focused stacked headers unless the right column carries an interactive element.

### Bento Grid Cell Rules
- **Cell Count Match**: A bento grid must have EXACTLY as many cells as there are items (3 items = 3 cells in asymmetric 1+2 split; 5 items = 5 cells in 2+3 split). Never leave blank placeholder tiles.
- **Bento Background Diversity**: A bento section cannot have 6 white-on-white text cards. At least 2 tiles MUST feature real visual elements (image, WebGL shader canvas, gradient, or interactive preview).

### Navigation & Header Rules
- **Desktop Single Line**: Navigation items MUST render on a single line on desktop (`lg:` breakpoint).
- **Navigation Height Cap**: Max `80px` on desktop (default `64px`–`72px`).
- **Logo Wall Placement**: "Trusted by / Used by" logo walls belong in a dedicated section directly below the hero.

---

## 3. CTA & Form Rules

- **Button Text Single Line**: CTA labels must never wrap to 2 lines on desktop. Shorten label (max 3 words) or widen button.
- **Single Intent CTA Lock**: Do not duplicate CTA intents on one page (e.g. don't mix "Get Started", "Start Free", "Sign Up" — pick ONE primary label and use it consistently).
- **Form Label Requirement**: Labels sit ABOVE inputs. Never use placeholders as labels.
