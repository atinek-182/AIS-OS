---
title: S1 Left Margin Numbered
domain: skill
summary: A narrow left column holds `01 — LABEL.`; the wide right column holds the heading and content. *Use when:* the page
  is editorial / specimen.
critical_directives:
- Follow document guidance without bypassing established safeguards.
section_outline:
- S1 · Left-margin numbered
read_triggers:
- When working on skill in .agents/skills/hallmark/references/components/s1-left-margin-numbered.md
- When reading context for S1 Left Margin Numbered
tags:
- skill
- s1-left-margin-numbered
updated: '2026-08-08'
---

### S1 · Left-margin numbered
A narrow left column holds `01 — LABEL.`; the wide right column holds the heading and content.
*Use when:* the page is editorial / specimen.
*Don't confuse with:* S5 Bottom-anchored (which puts the label *under* the section).

```html
<header class="head-margin">
  <p class="num-label">01 — Foundations</p>
  <h2>…</h2>
</header>
```
```css
.head-margin { display: grid; grid-template-columns: 10rem 1fr; gap: var(--space-xl); align-items: baseline; }
```
