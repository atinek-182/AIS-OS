---
title: F2 Sticky Scroll Stack
domain: skill
summary: Sticky left pane, scrolling right pane that cycles through related screenshots. *Use when:* feature has multiple
  sub-states worth showing in sequence.
critical_directives:
- Follow document guidance without bypassing established safeguards.
section_outline:
- F2 · Sticky-scroll stack
read_triggers:
- When working on skill in .agents/skills/hallmark/references/components/f2-sticky-scroll-stack.md
- When reading context for F2 Sticky Scroll Stack
tags:
- skill
- f2-sticky-scroll-stack
updated: '2026-08-08'
---

### F2 · Sticky-scroll stack
Sticky left pane, scrolling right pane that cycles through related screenshots.
*Use when:* feature has multiple sub-states worth showing in sequence.
*Don't confuse with:* F4 Step sequence (which is linearly numbered, not synced).

```html
<section class="sticky-stack">
  <div class="pane-sticky"><h3>…</h3><p>…</p></div>
  <div class="pane-scroll">
    <figure>1</figure><figure>2</figure><figure>3</figure>
  </div>
</section>
```
```css
.sticky-stack { display: grid; grid-template-columns: 1fr 1fr; gap: var(--space-2xl); }
/* `calc(--banner-height + --space-xl)` so the sticky pane docks below the
   nav with breathing room. Falls back to --space-xl alone when no sticky
   nav is on the page (slop-test gate 56). */
.pane-sticky { position: sticky; top: calc(var(--banner-height, 0px) + var(--space-xl)); align-self: start; z-index: var(--z-sticky); }
```
