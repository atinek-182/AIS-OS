---
title: T2 Logo Wall Hairline
domain: skill
summary: A row of customer logos, monochromatic, separated by hairline rules. No card boxes, no shadows. *Use when:* you have
  recognisable customers and want to surface them quietly.
critical_directives:
- Follow document guidance without bypassing established safeguards.
section_outline:
- T2 · Logo wall (hairline)
read_triggers:
- When working on skill in .agents/skills/hallmark/references/components/t2-logo-wall-hairline.md
- When reading context for T2 Logo Wall Hairline
tags:
- skill
- t2-logo-wall-hairline
updated: '2026-08-08'
---

### T2 · Logo wall (hairline)
A row of customer logos, monochromatic, separated by hairline rules. No card boxes, no shadows.
*Use when:* you have recognisable customers and want to surface them quietly.
*Don't confuse with:* the AI-default 6-logo box grid; this version refuses card boxes.

```html
<section class="logo-wall">
  <ul>
    <li><img src="" /></li>
    <li><img src="" /></li>
    <li><img src="" /></li>
  </ul>
</section>
```
```css
.logo-wall ul { display: grid; grid-template-columns: repeat(auto-fit, minmax(8rem, 1fr)); gap: 0; }
.logo-wall li { padding: var(--space-md); border-right: 1px solid var(--color-rule); display: grid; place-items: center; }
.logo-wall img { filter: grayscale(1); opacity: 0.7; }
```
