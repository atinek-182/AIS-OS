---
title: H1 Marquee
domain: skill
summary: A single statement fills the fold. No subhead, no CTA in view. *Use when:* the brand or person *is* the message.
critical_directives:
- Follow document guidance without bypassing established safeguards.
section_outline:
- H1 · Marquee
read_triggers:
- When working on skill in .agents/skills/hallmark/references/components/h1-marquee.md
- When reading context for H1 Marquee
tags:
- skill
- h1-marquee
updated: '2026-08-08'
---

### H1 · Marquee
A single statement fills the fold. No subhead, no CTA in view.
*Use when:* the brand or person *is* the message.
*Don't confuse with:* H4 Stat-Led (which is a number, not a statement).

```html
<section class="hero-marquee">
  <h1 class="display-xxl">A statement.</h1>
</section>
```
```css
.hero-marquee { min-height: 80dvh; display: grid; align-content: end; padding: 0 var(--page-gutter) var(--space-2xl); }
.display-xxl { font-size: clamp(4rem, 12vw, 12rem); line-height: 0.92; }
```
