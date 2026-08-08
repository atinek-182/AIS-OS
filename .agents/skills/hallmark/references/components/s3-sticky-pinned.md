---
title: S3 Sticky Pinned
domain: skill
summary: Heading remains in viewport while content scrolls beneath. Orientation aid. *Use when:* the section is dense and
  the user benefits from always seeing where they are.
critical_directives:
- Use when:* the section is dense and the user benefits from always seeing where they are.
- 'Sticky pairing rule:** if the page emits a sticky `<header>` / `<nav>` / `.banner` (anything with `position: sticky; top'
section_outline:
- S3 · Sticky pinned
read_triggers:
- When working on skill in .agents/skills/hallmark/references/components/s3-sticky-pinned.md
- When reading context for S3 Sticky Pinned
tags:
- skill
- s3-sticky-pinned
updated: '2026-08-08'
---

### S3 · Sticky pinned
Heading remains in viewport while content scrolls beneath. Orientation aid.
*Use when:* the section is dense and the user benefits from always seeing where they are.
*Don't confuse with:* S1 Left-margin (which doesn't move).

```html
<header class="head-sticky">
  <p class="num-label">02</p>
  <h2>…</h2>
</header>
```
```css
/* If the page has a sticky top nav, offset by its height so the sticky
   head docks BENEATH it instead of bleeding over (slop-test gate 56).
   Use --z-sticky (in-page) so the nav's --z-sticky-nav out-paints it. */
.head-sticky { position: sticky; top: var(--banner-height, 0px); background: var(--color-paper); padding-block: var(--space-sm); border-bottom: 1px solid var(--color-ink); z-index: var(--z-sticky); }
```

**Sticky pairing rule:** if the page emits a sticky `<header>` / `<nav>` / `.banner` (anything with `position: sticky; top: 0`), you MUST also declare `--banner-height` (a px value matching the nav's height) and `--z-sticky-nav` (≥ 1 above `--z-sticky`) in `tokens.css`. The S3 recipe above pulls both. Without those tokens the section head paints over the nav during scroll — see slop-test gate 56.
