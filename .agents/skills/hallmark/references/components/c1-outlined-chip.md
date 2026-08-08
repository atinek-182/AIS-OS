---
title: C1 Outlined Chip
domain: skill
summary: A bordered, transparent button with a typographic verb ("Save changes"). *Use when:* the page has one primary action;
  you want it visible but quiet.
critical_directives:
- Follow document guidance without bypassing established safeguards.
section_outline:
- C1 · Outlined chip
read_triggers:
- When working on skill in .agents/skills/hallmark/references/components/c1-outlined-chip.md
- When reading context for C1 Outlined Chip
tags:
- skill
- c1-outlined-chip
updated: '2026-08-08'
---

### C1 · Outlined chip
A bordered, transparent button with a typographic verb ("Save changes").
*Use when:* the page has one primary action; you want it visible but quiet.
*Don't confuse with:* C2 Oversized solid (which is statement-loud).

```html
<a class="cta-outline">Open your studio →</a>
```
```css
.cta-outline { display: inline-flex; align-items: center; gap: 0.4em; padding: 0.7rem 1.2rem; border: 1px solid var(--color-ink); min-height: 44px; }
```
