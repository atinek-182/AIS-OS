---
title: H6 Photographic Fold
domain: skill
summary: Single full-bleed image fills the viewport. Caption sits in a corner. *Use when:* you have real photography that
  earns full-bleed.
critical_directives:
- Follow document guidance without bypassing established safeguards.
section_outline:
- H6 · Photographic Fold
read_triggers:
- When working on skill in .agents/skills/hallmark/references/components/h6-photographic-fold.md
- When reading context for H6 Photographic Fold
tags:
- skill
- h6-photographic-fold
updated: '2026-08-08'
---

### H6 · Photographic Fold
Single full-bleed image fills the viewport. Caption sits in a corner.
*Use when:* you have real photography that earns full-bleed.
*Don't confuse with:* H2 Split (which pairs image with text in a grid).

```html
<section class="hero-photo">
  <img class="bleed" src="" alt="" />
  <p class="caption">Spring, 2026.</p>
</section>
```
```css
.hero-photo { position: relative; height: 80dvh; }
.hero-photo .bleed { width: 100%; height: 100%; object-fit: cover; }
.hero-photo .caption { position: absolute; bottom: var(--space-md); right: var(--space-md); }
```
