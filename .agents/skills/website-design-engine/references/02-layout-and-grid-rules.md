---
title: 'Phase 2 Reference: Layout, Grid Canons & UX Psychology Rules (v4.0)'
domain: skill
summary: '1. **Canon 1: Strict Column Alignment**: Every section must anchor to the same 12-column or asymmetric grid system.
  No rogue margin offsets (`ml-[17px]`). 2. **Canon 2: Obys Spatial Rhythm Ratios**:'
critical_directives:
- Initial viewport load MUST remain focused on 1 headline, 1 value prop, and 1 primary CTA stack.
- 'Viewport Fit**: Hero MUST fit within initial viewport height (`min-h-[100dvh]`). Never use `h-screen` (causes mobile bro'
- 'Cell Count Match**: A bento grid must have EXACTLY as many cells as there are items (3 items = 3 cells in asymmetric 1+2'
- 'Bento Background Diversity**: A bento section cannot have 6 white-on-white text cards. At least 2 tiles MUST feature rea'
section_outline:
- 'Phase 2 Reference: Layout, Grid Canons & UX Psychology Rules (v4.0)'
- Obys Grid Canons & Obys Spatial Rhythm Ratios
- UX Design Psychology & Lead Conversion Mechanics
- Hard Layout Rules & Anti-Pattern Bans
- Hero Section Discipline
read_triggers:
- When working on skill in .agents/skills/website-design-engine/references/02-layout-and-grid-rules.md
- 'When reading context for Phase 2 Reference: Layout, Grid Canons & UX Psychology Rules (v4.0)'
tags:
- skill
- 02-layout-and-grid-rules
updated: '2026-08-08'
---

# Phase 2 Reference: Layout, Grid Canons & UX Psychology Rules (v4.0)

## Obys Grid Canons & Obys Spatial Rhythm Ratios

1. **Canon 1: Strict Column Alignment**: Every section must anchor to the same 12-column or asymmetric grid system. No rogue margin offsets (`ml-[17px]`).
2. **Canon 2: Obys Spatial Rhythm Ratios**:
   - Macro Section Vertical Padding: `120px` to `160px` on desktop, `64px` to `80px` on mobile.
   - Card Internal Spacing: `24px` to `32px`.
   - Grid Element Gaps: `16px` to `24px`.
3. **Canon 3: Line-Length Cap**: Body paragraphs must cap at `max-w-[65ch]` to preserve reading comfort.
4. **Canon 4: Section Transition Rhythm**: Alternate padding and background shade (`bg-zinc-950` vs `bg-zinc-900`) between adjacent sections to define clear boundaries.

---

## UX Design Psychology & Lead Conversion Mechanics

1. **Progressive Disclosure & Cognitive Chunking**:
   - Initial viewport load MUST remain focused on 1 headline, 1 value prop, and 1 primary CTA stack.
   - Secondary technical features belong in expandable accordions, tabbed drawers, or asymmetric bento cards.

2. **Micro-Copy Friction Reducers**:
   - Place subtle micro-copy directly adjacent to primary CTA buttons (*"No credit card required"*, *"Takes 2 minutes"*, *"Client-Owned 0 SaaS Fees"*).

3. **Nate Herk Lead Conversion Mechanics**:
   - **Custom Bottleneck Freedom**: Provide an open-ended custom text input field giving prospects total freedom to type their specific business bottleneck.
   - **Value-First Price Lock / Delay**: Show positive financial savings & hours saved on initial screens before showing price tags.
   - **Google Sheets Lead CRM Sync**: Automatically sync lead inputs into a client-owned Google Sheet CRM tracker via Apps Script.

4. **Tension & Release Scroll Flow**:
   - Alternate visual weight across sequential sections:
     - *Dense / Dark*: 3D Canvas / WebGL Hero Stage (High Tension).
     - *Clean / Light*: Typography Manifesto Statement (Release).
     - *Grid / Structured*: Asymmetric Bento Feature Grid (Tension).
     - *Minimal / Clean*: Accordion FAQ & Testimonial Slider (Release).

---

## Hard Layout Rules & Anti-Pattern Bans

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

## CTA & Form Rules

- **Button Text Single Line**: CTA labels must never wrap to 2 lines on desktop. Shorten label (max 3 words) or widen button.
- **Single Intent CTA Lock**: Do not duplicate CTA intents on one page (e.g. don't mix "Get Started", "Start Free", "Sign Up" — pick ONE primary label and use it consistently).
- **Form Label Requirement**: Labels sit ABOVE inputs. Never use placeholders as labels.
