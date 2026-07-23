---
category: template
tags: [template, slide-components, html, css-keyframes, animations]
created: 2026-07-17
updated: 2026-07-17
sources:
  - "[[raw/web-clips/2026-07-17-claude-html-slides-=-the-new-powerpoint-killer-(full-tutorial).md]]"
---

# Slide Components Design Guide & Blueprints

This guide provides CSS, HTML, and JS structural blueprints for creating high-impact slide components (inspired by Vengeance UI). All templates use zero-dependency vanilla HTML/CSS/JS.

---

## 1. Token Stream / Processing Pipeline

Visualizes linear data flows, log streams, or LLM token generations using CSS keyframe animations.

```html
<div class="comp-token-stream">
    <div class="token-lane">
        <span class="token node-start">Input</span>
        <div class="stream-line">
            <span class="pulse-dot"></span>
        </div>
        <span class="token node-end">Output</span>
    </div>
</div>

<style>
.comp-token-stream {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 100%;
    height: 150px;
    background: var(--surface-dark, #0d1117);
    border-radius: 12px;
    padding: 24px;
}
.token-lane {
    display: flex;
    align-items: center;
    gap: 16px;
    width: 80%;
}
.token {
    padding: 8px 16px;
    background: var(--bg-primary, #ffffff);
    color: var(--text-primary, #000000);
    border-radius: 8px;
    font-family: var(--font-mono, monospace);
    font-weight: bold;
    border: 2px solid var(--accent, #ff6b4a);
}
.stream-line {
    position: relative;
    flex-grow: 1;
    height: 4px;
    background: rgba(255, 107, 74, 0.2);
    border-radius: 2px;
    overflow: hidden;
}
.pulse-dot {
    position: absolute;
    top: 0;
    left: -50px;
    width: 50px;
    height: 100%;
    background: linear-gradient(90deg, transparent, var(--accent, #ff6b4a), transparent);
    animation: flow-stream 2s infinite linear;
}
@keyframes flow-stream {
    0% { left: -50px; }
    100% { left: 100%; }
}
</style>
```

---

## 2. Animated Progress Bento Grid

A grid-based dashboard component with soft shadows and scale transitions on layout cards.

```html
<div class="comp-bento">
    <div class="bento-card bento-hero">
        <h3>Feature Hero</h3>
        <p>Main product callout text.</p>
    </div>
    <div class="bento-card bento-stat">
        <div class="stat-number">98%</div>
        <div class="stat-label">Accuracy Rate</div>
    </div>
    <div class="bento-card bento-detail">
        <h3>Status</h3>
        <div class="status-indicator">
            <span class="ping-circle"></span> Active
        </div>
    </div>
</div>

<style>
.comp-bento {
    display: grid;
    grid-template-columns: 2fr 1fr;
    grid-template-rows: repeat(2, 180px);
    gap: 16px;
    width: 100%;
}
.bento-card {
    background: var(--card-bg, #ffffff);
    color: var(--text-primary, #141413);
    border-radius: var(--card-border-radius, 12px);
    box-shadow: var(--card-shadow, 0 20px 48px rgba(20, 20, 19, 0.04));
    padding: 24px;
    transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1);
}
.bento-card:hover {
    transform: translateY(-4px) scale(1.02);
}
.bento-hero {
    grid-row: span 2;
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
    border-left: 6px solid var(--accent, #ff6b4a);
}
.stat-number {
    font-size: 48px;
    font-weight: 800;
    color: var(--accent, #ff6b4a);
}
.status-indicator {
    display: flex;
    align-items: center;
    gap: 8px;
    margin-top: 12px;
}
.ping-circle {
    width: 10px;
    height: 10px;
    background-color: var(--accent, #ff6b4a);
    border-radius: 50%;
    animation: pulse-ring 1.5s infinite ease-in-out;
}
@keyframes pulse-ring {
    0% { transform: scale(0.95); opacity: 0.5; }
    50% { transform: scale(1.2); opacity: 1; }
    100% { transform: scale(0.95); opacity: 0.5; }
}
</style>
```

---

## 3. Interactive Code Terminal Showcase

Simulates a modern command prompt or IDE terminal window inside presentation slides.

```html
<div class="comp-terminal">
    <div class="terminal-header">
        <span class="dot red"></span>
        <span class="dot yellow"></span>
        <span class="dot green"></span>
        <span class="terminal-title">bash -- setup.sh</span>
    </div>
    <div class="terminal-body">
        <div class="cmd-line"><span class="prompt">$</span> npm run build</div>
        <div class="output-line">Compiling resources...</div>
        <div class="output-line success">✓ Assets compiled successfully.</div>
        <div class="cmd-line cursor-line"><span class="prompt">$</span> <span class="typing-text"></span><span class="blink-cursor">_</span></div>
    </div>
</div>

<style>
.comp-terminal {
    background: #0f141c;
    border-radius: 12px;
    border: 1px solid rgba(255, 255, 255, 0.1);
    box-shadow: 0 16px 40px rgba(0,0,0,0.4);
    font-family: var(--font-mono, monospace);
    overflow: hidden;
    width: 100%;
}
.terminal-header {
    background: #181f29;
    padding: 12px;
    display: flex;
    align-items: center;
    gap: 6px;
    border-bottom: 1px solid rgba(255,255,255,0.05);
}
.dot {
    width: 12px;
    height: 12px;
    border-radius: 50%;
}
.dot.red { background-color: #ff5f56; }
.dot.yellow { background-color: #ffbd2e; }
.dot.green { background-color: #27c93f; }
.terminal-title {
    color: #8c95a5;
    font-size: 13px;
    margin-left: 12px;
}
.terminal-body {
    padding: 20px;
    font-size: 16px;
    line-height: 1.6;
    color: #e5e9f0;
}
.prompt { color: var(--accent, #ff6b4a); font-weight: bold; }
.output-line.success { color: #a3be8c; }
.blink-cursor {
    animation: blink-anim 1s infinite step-end;
    color: var(--accent, #ff6b4a);
}
@keyframes blink-anim {
    from, to { opacity: 0 }
    50% { opacity: 1 }
}
</style>
```

---

## 4. Perspective wireframe Grid background

Creates a moving tech grid backdrop that provides layout depth.

```html
<div class="comp-perspective-grid">
    <div class="grid-canvas"></div>
</div>

<style>
.comp-perspective-grid {
    position: absolute;
    inset: 0;
    z-index: -1;
    overflow: hidden;
    background-color: var(--bg-primary, #000000);
}
.grid-canvas {
    width: 200%;
    height: 200%;
    position: absolute;
    top: -50%;
    left: -50%;
    background-image: 
        linear-gradient(rgba(255,255,255,0.03) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255,255,255,0.03) 1px, transparent 1px);
    background-size: 40px 40px;
    transform: perspective(500px) rotateX(60deg);
    animation: grid-slide 20s infinite linear;
}
@keyframes grid-slide {
    0% { transform: perspective(500px) rotateX(60deg) translateY(0); }
    100% { transform: perspective(500px) rotateX(60deg) translateY(40px); }
}
</style>
```
