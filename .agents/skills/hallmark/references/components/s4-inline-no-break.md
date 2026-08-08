---
title: S4 Inline No Break
domain: skill
summary: The heading is a small caps phrase that emerges *inside* the body flow; no spatial break. *Use when:* the page is
  prose-led; reading should be continuous.
critical_directives:
- Follow document guidance without bypassing established safeguards.
section_outline:
- S4 · Inline (no break)
read_triggers:
- When working on skill in .agents/skills/hallmark/references/components/s4-inline-no-break.md
- When reading context for S4 Inline No Break
tags:
- skill
- s4-inline-no-break
updated: '2026-08-08'
---

### S4 · Inline (no break)
The heading is a small caps phrase that emerges *inside* the body flow; no spatial break.
*Use when:* the page is prose-led; reading should be continuous.
*Don't confuse with:* S2 Hanging (which separates with negative space).

```html
<p>… <span class="head-inline">A small heading.</span> …</p>
```
```css
.head-inline { font-variant-caps: all-small-caps; letter-spacing: 0.06em; font-weight: 500; }
```
