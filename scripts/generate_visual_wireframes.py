import os
import asyncio
from playwright.async_api import async_playwright

# ULTRA-DETAILED WIREFRAME TEMPLATES WITH ACTUAL SITE COPY, FULL COMPONENT STRUCTURE, AND TECHNICAL ANNOTATIONS

SONDAVEN_ULTRA_WIREFRAME = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Sondaven Resort — Hyper-Detailed Architectural Wireframe Blueprint</title>
<style>
  :root {
    --wf-bg: #eef0f4;
    --wf-surface: #ffffff;
    --wf-border: #717680;
    --wf-dark: #18191c;
    --wf-accent: #2b5c8f;
    --wf-orange: #d97706;
    --wf-grid: rgba(43, 92, 143, 0.08);
    --wf-note: #475569;
  }
  * { box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, monospace; }
  body { background-color: var(--wf-bg); color: var(--wf-dark); padding: 40px 20px; line-height: 1.4; }
  .blueprint-wrapper { max-width: 1400px; margin: 0 auto; background: var(--wf-surface); border: 2px solid var(--wf-border); border-radius: 12px; box-shadow: 0 20px 40px rgba(0,0,0,0.1); overflow: hidden; position: relative; }
  
  /* Grid Background Overlay */
  .grid-overlay { position: absolute; inset: 0; background-size: 20px 20px; background-image: linear-gradient(to right, var(--wf-grid) 1px, transparent 1px), linear-gradient(to bottom, var(--wf-grid) 1px, transparent 1px); pointer-events: none; z-index: 0; }
  .content { relative; z-index: 1; }

  /* Wireframe Top Header Bar */
  .wf-header { background: var(--wf-dark); color: #fff; padding: 18px 32px; display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid var(--wf-border); }
  .wf-title { font-size: 16px; font-weight: 800; letter-spacing: 1.5px; text-transform: uppercase; }
  .wf-meta { font-size: 11px; background: var(--wf-accent); color: #fff; padding: 4px 12px; border-radius: 4px; font-weight: 600; }

  /* Navigation Header Component */
  .wf-section { padding: 40px 32px; border-bottom: 2px dashed var(--wf-border); position: relative; }
  .spec-tag { position: absolute; top: 12px; right: 16px; font-size: 10px; font-weight: 700; background: #e2e8f0; color: #334155; padding: 3px 8px; border-radius: 3px; border: 1px solid #cbd5e1; }
  
  .wf-nav-bar { display: flex; justify-content: space-between; align-items: center; padding: 16px 24px; border: 2px solid var(--wf-border); background: #f8fafc; border-radius: 8px; }
  .wf-logo { font-size: 20px; font-weight: 900; letter-spacing: 3px; font-family: serif; border-bottom: 2px solid var(--wf-dark); }
  .wf-menu-list { display: flex; gap: 24px; font-size: 12px; font-weight: 700; text-transform: uppercase; }
  .wf-menu-item { position: relative; padding: 4px 0; }
  .wf-menu-item.active::after { content: ""; position: absolute; bottom: 0; left: 0; right: 0; height: 2px; background: var(--wf-accent); }

  /* Hero Section Wireframe */
  .wf-hero-container { border: 2px solid var(--wf-border); border-radius: 8px; background: #fff; padding: 32px; margin-top: 16px; }
  .wf-hero-headline { font-size: 42px; font-weight: 300; font-family: serif; line-height: 1.1; margin-bottom: 16px; color: #0f172a; }
  .wf-hero-sub { font-size: 15px; color: var(--wf-note); max-width: 650px; margin-bottom: 24px; }
  .wf-3d-stage { height: 320px; border: 2px dashed var(--wf-accent); background: rgba(43, 92, 143, 0.04); border-radius: 8px; display: flex; flex-direction: column; align-items: center; justify-content: center; font-weight: 700; color: var(--wf-accent); text-align: center; }

  /* 2-Column Content Grid */
  .grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 32px; margin-top: 16px; }
  .grid-3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; margin-top: 16px; }

  .wf-card { border: 2px solid var(--wf-border); border-radius: 8px; padding: 24px; background: #fff; position: relative; }
  .wf-card-header { font-size: 18px; font-weight: 700; margin-bottom: 12px; color: var(--wf-dark); border-bottom: 1px solid #e2e8f0; pb: 8px; }
  .wf-img-box { height: 200px; border: 2px dashed #94a3b8; background: #f1f5f9; border-radius: 6px; display: flex; flex-direction: column; align-items: center; justify-content: center; font-size: 13px; font-weight: 600; color: #475569; margin-bottom: 16px; }
  
  .wf-btn { display: inline-flex; align-items: center; justify-content: center; padding: 10px 24px; border: 2px solid var(--wf-dark); font-size: 12px; font-weight: 700; text-transform: uppercase; border-radius: 20px; background: #fff; cursor: pointer; }
  .wf-btn-primary { background: var(--wf-dark); color: #fff; }

  /* Technical Annotation Note Box */
  .tech-note { background: #fffbeb; border: 1.5px solid #f59e0b; padding: 12px 16px; border-radius: 6px; font-size: 11px; color: #92400e; margin-top: 16px; font-family: monospace; }
</style>
</head>
<body>
<div class="blueprint-wrapper">
  <div class="grid-overlay"></div>
  <div class="content">

    <div class="wf-header">
      <div class="wf-title">SONDAVEN LUXURY RESORT — HYPER-DETAILED WIREFRAME BLUEPRINT</div>
      <div class="wf-meta">VIEWPORT: 1920x1080 | ARCHETYPE: EDITORIAL LUXURY RESORT</div>
    </div>

    <!-- 1. HEADER & NAVBAR MECHANICS -->
    <div class="wf-section">
      <div class="spec-tag">COMPONENT: HEADER / NAV SYSTEM</div>
      <div class="wf-nav-bar">
        <div class="wf-logo">SONDAVEN</div>
        <div class="wf-menu-list">
          <div class="wf-menu-item active">OVERVIEW</div>
          <div class="wf-menu-item">VILLAS & SUITES</div>
          <div class="wf-menu-item">THERMAL SPA</div>
          <div class="wf-menu-item">GASTRONOMY</div>
          <div class="wf-menu-item">LOCATION</div>
        </div>
        <div style="display:flex; gap:12px; align-items:center;">
          <span style="font-size:11px; font-weight:bold; color:var(--wf-accent);">EN | RO</span>
          <div class="wf-btn">BOOK YOUR STAY</div>
        </div>
      </div>
      <div class="tech-note">
        <strong>TECHNICAL ANNOTATION:</strong> Fixed header with backdrop-filter: blur(12px). Automatically hides on scroll down (threshold &gt; 40px) and reveals on scroll up. Link hover triggersclip-path underline expansion.
      </div>
    </div>

    <!-- 2. HERO & 3D CANVAS STAGE -->
    <div class="wf-section">
      <div class="spec-tag">COMPONENT: HERO SECTION & 3D WEBGL STAGE</div>
      <div class="wf-hero-container">
        <div style="font-size: 12px; font-weight: bold; color: var(--wf-accent); letter-spacing: 2px;">CARPATHIAN MOUNTAINS, ROMANIA</div>
        <h1 class="wf-hero-headline">Architectural Sanctuary Embedded in Mountain Mist</h1>
        <p class="wf-hero-sub">Experience organic luxury, thermal Carpathian springs, and private heliport access in Europe's most pristine alpine valley.</p>

        <div class="wf-3d-stage">
          🌐 THREE.JS 3D CLOUD TERRAIN CANVAS STAGE (canvas#canvas)
          <div style="font-size: 11px; font-weight: normal; color: #64748b; margin-top: 8px;">
            • GLSL Volumetric Cloud Shader Fragment<br>
            • Lenis Scroll Inertia Scrubber driving Camera Target Z-Position (0 -> 100)<br>
            • Ambient Soundscape Visualizer Stream (Carpathian Stream Audio API)
          </div>
        </div>

        <div style="display:flex; justify-content:space-between; align-items:center; margin-top: 20px;">
          <div style="font-size: 12px; font-weight: bold; color: var(--wf-note);">SCROLL TO DISCOVER VILLA COLLECTION ↓</div>
          <div class="wf-btn wf-btn-primary">EXPLORE RESORT EXPERIENCE</div>
        </div>
      </div>
    </div>

    <!-- 3. SCROLLESTELLING & ACCORDION GRID -->
    <div class="wf-section">
      <div class="spec-tag">COMPONENT: 2-COLUMN SCROLLESTELLING & ACCORDION</div>
      <div class="grid-2">
        <div class="wf-card">
          <div class="wf-card-header">01. ORGANIC ARCHITECTURE</div>
          <div class="wf-img-box">
            🖼️ PARALLAX IMAGE STAGE
            <span style="font-size: 10px; color: #64748b;">yPercent: -20 -> 20 | GSAP ScrollTrigger Pin</span>
          </div>
          <p style="font-size: 13px; color: #334155;">Villas sculpted from local stone, glass, and sustainable cedar wood to minimize environmental impact while maximizing panoramic valley views.</p>
        </div>

        <div class="wf-card">
          <div class="wf-card-header">RESORT AMENITIES & SERVICES</div>
          <div style="display:flex; flex-direction:column; gap:12px; margin-top:16px;">
            <div style="border: 1px solid var(--wf-border); padding: 14px; border-radius: 6px; display:flex; justify-content:space-between; font-weight:bold; font-size:13px; background:#f8fafc;">
              <span>01. Carpathian Thermal Springs Spa</span>
              <span>+</span>
            </div>
            <div style="border: 1px solid var(--wf-border); padding: 14px; border-radius: 6px; display:flex; justify-content:space-between; font-weight:bold; font-size:13px; background:#f8fafc;">
              <span>02. Private Heliport & Concierge Transfers</span>
              <span>+</span>
            </div>
            <div style="border: 1px solid var(--wf-border); padding: 14px; border-radius: 6px; display:flex; justify-content:space-between; font-weight:bold; font-size:13px; background:#f8fafc;">
              <span>03. Michelin Star Organic Farm-to-Table</span>
              <span>+</span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- 4. SVG PATH SEASON SLIDER -->
    <div class="wf-section">
      <div class="spec-tag">COMPONENT: DRAG-ALONG-PATH SVG SEASON SLIDER</div>
      <div class="wf-card">
        <div class="wf-card-header">02. SEASONAL EXPERIENCE PATHWAYS</div>
        <div class="wf-img-box" style="height: 180px; background: #fafafa;">
          ⚡ SVG CURVE INTERACTIVE SLIDER (getPointAtLength Drag Physics)
          <span style="font-size: 11px; color: #64748b; margin-top: 6px;">Spring Inertia Easing: ease: "elastic.out(1, 0.3)" • Spring Velocity Drag</span>
        </div>
      </div>
    </div>

    <!-- 5. FOOTER & RESERVATION FLIP FORM -->
    <div class="wf-section" style="background: #0f172a; color: #fff;">
      <div class="spec-tag" style="background:#334155; color:#fff; border-color:#475569;">COMPONENT: FOOTER & 180° CARD FLIP FORM</div>
      <div class="grid-3" style="margin-top: 24px;">
        <div>
          <div style="font-size: 20px; font-weight: 900; letter-spacing: 2px;">SONDAVEN</div>
          <p style="font-size: 12px; color: #94a3b8; margin-top: 8px;">Carpathian Alpine Valley<br>Romania • Europe</p>
        </div>
        <div>
          <div style="font-size: 12px; font-weight: bold; color: var(--wf-accent);">RESERVATIONS</div>
          <p style="font-size: 12px; color: #94a3b8; margin-top: 4px;">stay@sondaven.com<br>+40 (0) 700 123 456</p>
        </div>
        <div>
          <div class="wf-btn" style="background: var(--wf-accent); border-color: var(--wf-accent); color: #fff;">RESERVE VILLA →</div>
        </div>
      </div>
    </div>

  </div>
</div>
</body>
</html>
"""

ORYZO_ULTRA_WIREFRAME = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Oryzo AI — Hyper-Detailed 3D & Satirical UI Wireframe Blueprint</title>
<style>
  :root {
    --wf-bg: #09090b;
    --wf-surface: #18181b;
    --wf-border: #3f3f46;
    --wf-text: #ffedd6;
    --wf-orange: #f97316;
    --wf-muted: #a1a1aa;
  }
  * { box-sizing: border-box; margin: 0; padding: 0; font-family: "Space Mono", monospace, sans-serif; }
  body { background-color: var(--wf-bg); color: var(--wf-text); padding: 40px 20px; line-height: 1.5; }
  .blueprint-wrapper { max-width: 1400px; margin: 0 auto; background: var(--wf-surface); border: 2px solid var(--wf-border); border-radius: 12px; overflow: hidden; }

  .wf-header { background: #000; color: var(--wf-orange); padding: 18px 32px; display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid var(--wf-border); }
  .wf-title { font-size: 16px; font-weight: 800; letter-spacing: 1px; }

  .wf-section { padding: 40px 32px; border-bottom: 2px dashed var(--wf-border); position: relative; }
  .spec-tag { position: absolute; top: 12px; right: 16px; font-size: 10px; font-weight: 700; background: #27272a; color: var(--wf-orange); padding: 3px 8px; border-radius: 3px; border: 1px solid var(--wf-border); }

  .wf-nav-bar { display: flex; justify-content: space-between; align-items: center; padding: 16px 24px; border: 1.5px solid var(--wf-border); background: #09090b; border-radius: 8px; }
  .wf-logo { font-size: 20px; font-weight: 900; letter-spacing: 3px; }

  .wf-hero-card { border: 2px solid var(--wf-border); border-radius: 8px; background: #000; padding: 32px; margin-top: 16px; }
  .wf-3d-stage { height: 340px; border: 2px dashed var(--wf-orange); background: rgba(249, 115, 22, 0.05); border-radius: 8px; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; color: var(--wf-orange); font-weight: 700; margin: 20px 0; }

  .grid-3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; margin-top: 16px; }
  .wf-card { border: 1.5px solid var(--wf-border); border-radius: 8px; padding: 24px; background: #09090b; }
  .wf-card-title { font-size: 14px; font-weight: 700; color: var(--wf-orange); margin-bottom: 12px; }

  .wf-prompt-container { border: 2px solid var(--wf-orange); border-radius: 8px; padding: 24px; background: #000; margin-top: 24px; }
  .wf-input { width: 100%; background: #18181b; border: 1px solid var(--wf-border); padding: 12px 16px; border-radius: 6px; color: var(--wf-text); font-size: 13px; margin-top: 8px; }

  .tech-note { background: #1c1917; border: 1.5px solid var(--wf-orange); padding: 12px 16px; border-radius: 6px; font-size: 11px; color: var(--wf-orange); margin-top: 16px; }
</style>
</head>
<body>
<div class="blueprint-wrapper">
  <div class="wf-header">
    <div class="wf-title">ORYZO AI — HYPER-DETAILED 3D & SATIRICAL WIREFRAME BLUEPRINT</div>
    <div style="font-size: 11px; background: var(--wf-orange); color: #000; padding: 4px 10px; font-weight: bold; border-radius: 3px;">GAUSSIAN SPLAT WORKER & 60,000px SCROLL</div>
  </div>

  <!-- NAV BAR -->
  <div class="wf-section">
    <div class="spec-tag">COMPONENT: HEADER & SLOGAN</div>
    <div class="wf-nav-bar">
      <div class="wf-logo">ORYZO AI</div>
      <div style="font-size: 12px; color: var(--wf-muted);">MADE FOR MUGS. BUILT FOR TABLES.</div>
      <div style="background: var(--wf-orange); color: #000; font-size: 11px; font-weight: bold; padding: 6px 14px; border-radius: 4px;">LUSION STUDIO ARCHITECTURE</div>
    </div>
  </div>

  <!-- HERO & 3D STAGE -->
  <div class="wf-section">
    <div class="spec-tag">COMPONENT: 3D GAUSSIAN SPLAT STAGE & HERO NARRATIVE</div>
    <div class="wf-hero-card">
      <div style="font-size: 32px; font-weight: 900; letter-spacing: -1px;">ORYZO-1 OPEN WEIGHT PHYSICAL MODEL</div>
      <p style="font-size: 13px; color: var(--wf-muted); margin-top: 8px;">Designed to lift, insulate, and grip in all the right ways. Oryzo makes the simplest moment feel considered.</p>

      <div class="wf-3d-stage">
        🎲 THREE.JS WEBGL GAUSSIAN SPLATTING CANVAS (canvas#canvas)
        <div style="font-size: 11px; font-weight: normal; color: var(--wf-muted); margin-top: 8px;">
          • Off-thread SplatsWorker-DSMxtdkh.js decoding real-world cork 3D point cloud scan<br>
          • 60,582.1px DOM height driving continuous camera keyframes<br>
          • Custom Three.js r178 shader with dynamic roughness (0.85) & specular highlight maps
        </div>
      </div>

      <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 16px;">
        <div style="font-size: 12px; color: var(--wf-muted);">Designed by Lusion • The world's most unnecessarily sophisticated cork coaster</div>
        <div style="background: var(--wf-orange); color: #000; font-size: 12px; font-weight: bold; padding: 10px 20px; border-radius: 20px;">PLAY REVEAL FILM ▶</div>
      </div>
    </div>

    <div class="tech-note">
      <strong>TECHNICAL ANNOTATION:</strong> Text Splitter wraps characters in &lt;div aria-hidden="true"&gt; nodes for kinetic stagger while root element carries aria-label for accessibility.
    </div>
  </div>

  <!-- SATIRICAL MAGAZINE & WIDGETS -->
  <div class="wf-section">
    <div class="spec-tag">COMPONENT: SATIRICAL MAGAZINE & PROMPT WIDGET</div>
    <div class="grid-3">
      <div class="wf-card">
        <div class="wf-card-title">ISSUE NO. 00124</div>
        <div style="font-size: 22px; font-weight: 900;">WE ARE SO COOKED!</div>
        <p style="font-size: 12px; color: var(--wf-muted); margin-top: 8px;">Oryzo is taking everyone's jobs... and replacing them with AI!</p>
      </div>

      <div class="wf-card">
        <div class="wf-card-title">ELEVATE EXPERIENCE</div>
        <div style="font-size: 13px;">Precision-engineered lift (exactly one coaster thick). Elevates your mug above mediocre surfaces.</div>
      </div>

      <div class="wf-card">
        <div class="wf-card-title">WARNING MODAL</div>
        <div style="font-size: 11px; color: #ef4444;">⚠️ This stunt was performed by professionals. Do not attempt this at home.</div>
      </div>
    </div>

    <div class="wf-prompt-container">
      <div style="font-size: 12px; font-weight: bold; color: var(--wf-orange);">ASK @ORYZO AI PROMPT GENERATOR</div>
      <input class="wf-input" value="Hey @oryzo, can you put on a bikini?" readonly>
      <div style="display:flex; justify-content:flex-end; margin-top: 12px;">
        <div style="background: var(--wf-orange); color: #000; font-size: 12px; font-weight: bold; padding: 8px 20px; border-radius: 6px;">SEND PROMPT</div>
      </div>
    </div>
  </div>

</div>
</body>
</html>
"""

LINE_STUDIO_ULTRA_WIREFRAME = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>The Line Studio — Hyper-Detailed Kinetic Wireframe Blueprint</title>
<style>
  :root {
    --wf-bg: #dddee2;
    --wf-surface: #f8f8f8;
    --wf-border: #9498a1;
    --wf-dark: #0b0b0b;
    --wf-red: #ff391e;
  }
  * { box-sizing: border-box; margin: 0; padding: 0; font-family: "DenimWeb", -apple-system, BlinkMacSystemFont, sans-serif; }
  body { background-color: var(--wf-bg); color: var(--wf-dark); padding: 40px 20px; line-height: 1.4; }
  .blueprint-wrapper { max-width: 1400px; margin: 0 auto; background: var(--wf-surface); border: 2px solid var(--wf-border); border-radius: 12px; overflow: hidden; }

  .wf-header { background: var(--wf-red); color: #fff; padding: 18px 32px; display: flex; justify-content: space-between; align-items: center; }
  .wf-section { padding: 40px 32px; border-bottom: 2px dashed var(--wf-border); position: relative; }
  .spec-tag { position: absolute; top: 12px; right: 16px; font-size: 10px; font-weight: 700; background: var(--wf-dark); color: #fff; padding: 3px 8px; border-radius: 3px; }

  .wf-nav-bar { display: flex; justify-content: space-between; align-items: center; padding: 16px 24px; border: 2px solid var(--wf-dark); background: #fff; border-radius: 8px; }
  .wf-logo { font-size: 24px; font-weight: 900; letter-spacing: -1px; }

  .wf-[#ffedd6]-ticker { display: flex; flex-direction: column; gap: 16px; margin-top: 16px; }
  .wf-[#ffedd6]-card { border: 2px solid var(--wf-dark); padding: 24px; border-radius: 8px; background: #fff; display: flex; justify-content: space-between; align-items: center; relative; overflow: hidden; }

  .tech-note { background: #fef2f2; border: 1.5px solid var(--wf-red); padding: 12px 16px; border-radius: 6px; font-size: 11px; color: var(--wf-red); margin-top: 16px; font-family: monospace; }
</style>
</head>
<body>
<div class="blueprint-wrapper">
  <div class="wf-header">
    <div style="font-size: 16px; font-weight: 800; letter-spacing: 1px;">THE LINE STUDIO LONDON — HYPER-DETAILED KINETIC WIREFRAME</div>
    <div style="font-size: 11px; background: #000; color: #fff; padding: 4px 10px; font-weight: bold; border-radius: 3px;">NUXT.JS SSR & LENIS INERTIA SCROLL</div>
  </div>

  <!-- HEADER -->
  <div class="wf-section">
    <div class="spec-tag">COMPONENT: KINETIC NAV & STATUS</div>
    <div class="wf-nav-bar">
      <div class="wf-logo">THE LINE <span style="color: var(--wf-red);">●</span></div>
      <div style="font-size: 12px; font-weight: bold; color: var(--wf-dark);">LONDON <span style="color: var(--wf-red);">●</span> hello@thelinestudio.com</div>
      <div style="display: flex; gap: 20px; font-size: 12px; font-weight: bold;">
        <span style="color: var(--wf-red);">WORK ●</span>
        <span>ABOUT</span>
        <span>ENTERTAINMENT</span>
        <span>PODCAST</span>
        <span>CONTACT</span>
      </div>
    </div>
  </div>

  <!-- SHOWCASE TICKER -->
  <div class="wf-section">
    <div class="spec-tag">COMPONENT: FEATURED SHOWCASE TICKER</div>
    <div style="font-size: 18px; font-weight: 800; margin-bottom: 12px;">FEATURED ANIMATION SHOWCASE (ELECTRIC RED ACETATE MULTIPLY)</div>

    <div class="wf-[#ffedd6]-ticker">
      <div class="wf-[#ffedd6]-card">
        <div>
          <span style="font-size: 11px; font-weight: bold; color: var(--wf-red);">[01]</span>
          <h2 style="font-size: 32px; font-weight: 900;">GORILLAZ — CRACKERS ISLAND</h2>
          <p style="font-size: 12px; opacity: 0.7; margin-top: 4px;">PARLOPHONE RECORDS • MUSIC VIDEO / 2D ANIMATION</p>
        </div>
        <div style="font-size: 12px; font-weight: bold;">VIEW CASE STUDY →</div>
      </div>

      <div class="wf-[#ffedd6]-card">
        <div>
          <span style="font-size: 11px; font-weight: bold; color: var(--wf-red);">[02]</span>
          <h2 style="font-size: 32px; font-weight: 900;">RIOT GAMES — LEAGUE OF LEGENDS CINEMATIC</h2>
          <p style="font-size: 12px; opacity: 0.7; margin-top: 4px;">RIOT GAMES • GAME TRAILER / 3D ANIME</p>
        </div>
        <div style="font-size: 12px; font-weight: bold;">VIEW CASE STUDY →</div>
      </div>
    </div>

    <div class="tech-note">
      <strong>TECHNICAL ANNOTATION:</strong> Hovering project cards activates .acetate background with mix-blend-mode: multiply (#FF391E). Page navigation triggers 3D card tilt animation (transform: translateY(-25lvh) rotate(4deg)).
    </div>
  </div>

</div>
</body>
</html>
"""

GEHRY_GETTY_ULTRA_WIREFRAME = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Gehry Getty — Hyper-Detailed Architectural 3D Wireframe Blueprint</title>
<style>
  :root {
    --wf-bg: #f2f0eb;
    --wf-surface: #ffffff;
    --wf-border: #c8c5bc;
    --wf-dark: #1c1b18;
    --wf-rust: #d94f30;
  }
  * { box-sizing: border-box; margin: 0; padding: 0; font-family: "Playfair Display", Georgia, serif; }
  body { background-color: var(--wf-bg); color: var(--wf-dark); padding: 40px 20px; line-height: 1.5; }
  .blueprint-wrapper { max-width: 1400px; margin: 0 auto; background: var(--wf-surface); border: 2px solid var(--wf-border); border-radius: 12px; overflow: hidden; }

  .wf-header { padding: 24px 32px; border-bottom: 2px dashed var(--wf-border); display: flex; justify-content: space-between; align-items: center; }
  .wf-section { padding: 40px 32px; border-bottom: 2px dashed var(--wf-border); position: relative; }
  .spec-tag { position: absolute; top: 12px; right: 16px; font-size: 10px; font-weight: 700; background: var(--wf-dark); color: #fff; padding: 3px 8px; border-radius: 3px; font-family: monospace; }

  .wf-3d-stage { height: 380px; border: 2px dashed var(--wf-rust); background: rgba(217, 79, 48, 0.04); margin-top: 16px; border-radius: 8px; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; color: var(--wf-rust); font-weight: bold; position: relative; }
  .wf-audio-container { background: var(--wf-dark); color: #f2f0eb; padding: 24px; border-radius: 12px; margin-top: 16px; display: flex; justify-content: space-between; align-items: center; }
</style>
</head>
<body>
<div class="blueprint-wrapper">
  <div class="wf-header">
    <div>
      <div style="font-size: 10px; font-family: monospace; letter-spacing: 2px; color: var(--wf-rust);">GETTY RESEARCH INSTITUTE ARCHIVE</div>
      <h1 style="font-size: 26px; font-weight: normal; margin-top: 4px;">FRANK GEHRY ARCHITECTURAL FORM STUDIES</h1>
    </div>
    <div style="background: var(--wf-dark); color: #fff; padding: 6px 16px; font-size: 11px; font-family: monospace; border-radius: 20px;">3D ARCHIVE MODEL EXPLORER</div>
  </div>

  <div class="wf-section">
    <div class="spec-tag">COMPONENT: THREE.JS 3D GLTF STAGE & HOTSPOTS</div>
    <div class="wf-3d-stage">
      🏛️ THREE.JS 3D GLTF ARCHITECTURAL MODEL STAGE (getty_formStudy_hotspot_desktop.glb)
      <div style="font-size: 11px; font-family: monospace; color: #666; margin-top: 8px;">
        • Basis Universal Transcoder WASM (basis_transcoder.wasm)<br>
        • Vector Spring Camera Orbit Damping (three-vector-spring.js)<br>
        • Screen-space vector hotspot pin projection (Hotspot.032182a1.js)
      </div>
      <div style="position: absolute; top: 30%; left: 35%; background: var(--wf-rust); color: #fff; width: 28px; height: 28px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 14px; font-family: monospace;">📍</div>
      <div style="position: absolute; top: 55%; right: 40%; background: var(--wf-rust); color: #fff; width: 28px; height: 28px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 14px; font-family: monospace;">📍</div>
    </div>
  </div>

  <div class="wf-section">
    <div class="spec-tag">COMPONENT: MULTI-CHAPTER AUDIO STREAM PLAYER</div>
    <div class="wf-audio-container">
      <div>
        <div style="font-size: 10px; font-family: monospace; color: var(--wf-rust);">GUIDED ARCHITECTURAL AUDIO NARRATIVE</div>
        <div style="font-size: 18px; font-weight: bold; margin-top: 4px;">Chapter 1: The Model as Thought (04:12)</div>
        <div style="font-size: 11px; color: #a1a1aa; margin-top: 4px;">Synchronized with timecoded transcript JSON (getty_CH1_en.json)</div>
      </div>
      <div style="background: var(--wf-rust); color: #fff; width: 48px; height: 48px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 20px; cursor: pointer;">▶</div>
    </div>
  </div>
</div>
</body>
</html>
"""

async def generate_all_visual_wireframes():
    sites = [
        ("sondaven", SONDAVEN_ULTRA_WIREFRAME),
        ("oryzo-ai", ORYZO_ULTRA_WIREFRAME),
        ("the-line-studio", LINE_STUDIO_ULTRA_WIREFRAME),
        ("gehry-getty", GEHRY_GETTY_ULTRA_WIREFRAME),
    ]

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={"width": 1440, "height": 1100})

        for slug, html_content in sites:
            base_dir = os.path.join(r"d:\AI-OS\premium-frontend-experience-system\reference-inputs\sites", slug, "assets")
            os.makedirs(base_dir, exist_ok=True)
            
            # Save HTML wireframe
            html_path = os.path.join(base_dir, "wireframe.html")
            with open(html_path, "w", encoding="utf-8") as f:
                f.write(html_content)
            print(f"[ULTRA WIREFRAME] Saved {html_path}")

            # Capture PNG visual wireframe image
            await page.set_content(html_content)
            png_path = os.path.join(base_dir, "wireframe.png")
            await page.screenshot(path=png_path, full_page=True)
            print(f"[ULTRA WIREFRAME] Captured PNG: {png_path}")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(generate_all_visual_wireframes())
