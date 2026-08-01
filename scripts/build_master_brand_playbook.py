# -*- coding: utf-8 -*-
import os
from playwright.sync_api import sync_playwright

out_dir = r"D:\ZORIXEL-BRAND-OS\deliverables"
os.makedirs(out_dir, exist_ok=True)

html_file = os.path.join(out_dir, "zorixel-master-brand-playbook.html")
png_file = os.path.join(out_dir, "zorixel-master-brand-playbook.png")

print("Generating ZORIXEL Master Brand Playbook & Execution Blueprint HTML Report...")

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ZORIXEL — Master Brand Operating Playbook & Roadmap</title>
<style>
  :root {
    --bg-page: #050508;
    --bg-surface: #0e0e14;
    --bg-card: #14141d;
    --bg-card-hover: #1c1c28;
    --border-subtle: rgba(255, 255, 255, 0.08);
    --border-strong: rgba(255, 255, 255, 0.18);
    --text-primary: #f8fafc;
    --text-secondary: #94a3b8;
    --text-muted: #64748b;
    --accent-blue: #3b82f6;
    --accent-cyan: #06b6d4;
    --accent-emerald: #10b981;
    --accent-purple: #8b5cf6;
    --accent-amber: #f59e0b;
    --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    --font-mono: 'JetBrains Mono', monospace;
  }

  * { box-sizing: border-box; margin: 0; padding: 0; }

  body {
    background-color: var(--bg-page);
    color: var(--text-primary);
    font-family: var(--font-sans);
    line-height: 1.6;
    padding: 40px 20px;
    -webkit-font-smoothing: antialiased;
  }

  .container {
    max-width: 1100px;
    margin: 0 auto;
  }

  /* Header Section */
  .header {
    text-align: center;
    padding: 60px 24px 50px;
    background: radial-gradient(circle at top, rgba(59, 130, 246, 0.12) 0%, transparent 70%);
    border-bottom: 1px solid var(--border-subtle);
    border-radius: 24px 24px 0 0;
  }

  .badge-tag {
    display: inline-block;
    padding: 6px 14px;
    border-radius: 30px;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    background: rgba(6, 182, 212, 0.1);
    color: var(--accent-cyan);
    border: 1px solid rgba(6, 182, 212, 0.3);
    margin-bottom: 16px;
  }

  .main-title {
    font-size: 52px;
    font-weight: 800;
    letter-spacing: -0.04em;
    line-height: 1.1;
    background: linear-gradient(135deg, #ffffff 0%, #cbd5e1 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 16px;
  }

  .subtitle {
    font-size: 18px;
    color: var(--text-secondary);
    max-width: 780px;
    margin: 0 auto 30px;
  }

  /* Hero Banner Card */
  .hero-banner {
    background: linear-gradient(135deg, rgba(30, 41, 59, 0.6) 0%, rgba(15, 23, 42, 0.8) 100%);
    border: 1px solid var(--border-strong);
    border-radius: 20px;
    padding: 32px;
    margin: 30px 0 50px;
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4);
  }

  .hero-banner-title {
    font-size: 13px;
    font-weight: 700;
    color: var(--accent-amber);
    text-transform: uppercase;
    letter-spacing: 0.1em;
    margin-bottom: 12px;
  }

  .hero-banner-hook {
    font-size: 26px;
    font-weight: 700;
    color: #fff;
    line-height: 1.35;
  }

  /* Key Metrics Grid */
  .metrics-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
    gap: 20px;
    margin-bottom: 50px;
  }

  .metric-card {
    background: var(--bg-card);
    border: 1px solid var(--border-subtle);
    border-radius: 16px;
    padding: 24px;
    transition: transform 0.2s ease, border-color 0.2s ease;
  }

  .metric-card:hover {
    transform: translateY(-2px);
    border-color: var(--border-strong);
    background: var(--bg-card-hover);
  }

  .metric-label {
    font-size: 12px;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-bottom: 8px;
  }

  .metric-value {
    font-size: 32px;
    font-weight: 800;
    color: var(--accent-emerald);
    font-family: var(--font-mono);
  }

  .metric-subtext {
    font-size: 13px;
    color: var(--text-secondary);
    margin-top: 6px;
  }

  /* Section Styling */
  .section-block {
    margin-bottom: 60px;
  }

  .section-header {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 24px;
    padding-bottom: 12px;
    border-bottom: 1px solid var(--border-subtle);
  }

  .section-num {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 36px;
    height: 36px;
    border-radius: 10px;
    background: rgba(59, 130, 246, 0.15);
    color: var(--accent-blue);
    font-weight: 800;
    font-family: var(--font-mono);
    font-size: 16px;
    border: 1px solid rgba(59, 130, 246, 0.3);
  }

  .section-title {
    font-size: 24px;
    font-weight: 700;
    letter-spacing: -0.02em;
    color: #fff;
  }

  /* Step Cards Grid */
  .step-cards-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
    gap: 24px;
  }

  .step-card {
    background: var(--bg-card);
    border: 1px solid var(--border-subtle);
    border-radius: 18px;
    padding: 28px;
    position: relative;
  }

  .step-tag {
    position: absolute;
    top: 24px;
    right: 24px;
    font-size: 11px;
    font-weight: 700;
    padding: 4px 10px;
    border-radius: 20px;
    background: rgba(16, 185, 129, 0.15);
    color: var(--accent-emerald);
    border: 1px solid rgba(16, 185, 129, 0.3);
    font-family: var(--font-mono);
  }

  .step-card-title {
    font-size: 18px;
    font-weight: 700;
    color: #fff;
    margin-bottom: 12px;
    padding-right: 80px;
  }

  .step-card-body {
    font-size: 14px;
    color: var(--text-secondary);
    line-height: 1.6;
  }

  .step-card-list {
    margin-top: 16px;
    padding-left: 20px;
  }

  .step-card-list li {
    margin-bottom: 8px;
    font-size: 14px;
    color: var(--text-primary);
  }

  /* Data Table */
  .data-table {
    width: 100%;
    border-collapse: collapse;
    background: var(--bg-card);
    border-radius: 16px;
    overflow: hidden;
    border: 1px solid var(--border-subtle);
    margin-top: 16px;
  }

  .data-table th, .data-table td {
    padding: 16px 20px;
    text-align: left;
    border-bottom: 1px solid var(--border-subtle);
  }

  .data-table th {
    background: rgba(255, 255, 255, 0.03);
    font-size: 12px;
    font-weight: 700;
    color: var(--text-secondary);
    text-transform: uppercase;
    letter-spacing: 0.06em;
  }

  .data-table td {
    font-size: 14px;
    color: var(--text-primary);
  }

  .pill {
    display: inline-block;
    padding: 4px 10px;
    border-radius: 12px;
    font-size: 12px;
    font-weight: 600;
    font-family: var(--font-mono);
  }

  .pill-blue { background: rgba(59, 130, 246, 0.15); color: var(--accent-blue); }
  .pill-green { background: rgba(16, 185, 129, 0.15); color: var(--accent-emerald); }
  .pill-amber { background: rgba(245, 158, 11, 0.15); color: var(--accent-amber); }

  /* Callout Box */
  .callout-box {
    background: rgba(139, 92, 246, 0.08);
    border: 1px solid rgba(139, 92, 246, 0.25);
    border-radius: 16px;
    padding: 24px;
    margin: 24px 0;
  }

  .callout-title {
    font-size: 15px;
    font-weight: 700;
    color: var(--accent-purple);
    margin-bottom: 8px;
  }

  .callout-desc {
    font-size: 14px;
    color: var(--text-secondary);
  }

  .footer {
    text-align: center;
    padding: 40px 0;
    color: var(--text-muted);
    font-size: 13px;
    border-top: 1px solid var(--border-subtle);
    margin-top: 80px;
  }
</style>
</head>
<body>
<div class="container">

  <!-- Header -->
  <div class="header">
    <div class="badge-tag">ZORIXEL Master Operating Playbook</div>
    <h1 class="main-title">The Complete Brand Architecture & Execution Roadmap</h1>
    <p class="subtitle">AI Workflows & Business Automation Agency — Delivering High-ROI Agent Infrastructure & Custom Web Dashboards</p>

    <!-- Hero Banner -->
    <div class="hero-banner">
      <div class="hero-banner-title">The Master Hook & Positioning Statement</div>
      <div class="hero-banner-hook">
        "ZORIXEL is an AI Workflows & Business Automation Agency delivering high-ROI AI agent infrastructure, sales automations, and custom full-stack web UI dashboards for companies globally — eliminating operational bottlenecks and driving client revenue."
      </div>
    </div>
  </div>

  <!-- Key Metrics -->
  <div class="metrics-grid">
    <div class="metric-card">
      <div class="metric-label">Flagship Offer</div>
      <div class="metric-value">$1,500 - $5,000+</div>
      <div class="metric-subtext">DFY AI Engineering Sprint</div>
    </div>
    <div class="metric-card">
      <div class="metric-label">Dual-Market Strategy</div>
      <div class="metric-value">India + Global</div>
      <div class="metric-subtext">INR Launchpad / USD Revenue</div>
    </div>
    <div class="metric-card">
      <div class="metric-label">Target Clients</div>
      <div class="metric-value">3 / Mo</div>
      <div class="metric-subtext">50% Deposit ($1,500) Upfront</div>
    </div>
    <div class="metric-card">
      <div class="metric-label">Sales Channel</div>
      <div class="metric-value">100% Async</div>
      <div class="metric-subtext">DMs + Loom Audits + Notion</div>
    </div>
  </div>

  <!-- Section 1: What to Create for Yourself FIRST -->
  <div class="section-block">
    <div class="section-header">
      <div class="section-num">01</div>
      <h2 class="section-title">What to Create for Yourself FIRST (Before Outreach)</h2>
    </div>

    <div class="callout-box">
      <div class="callout-title">💡 The Core Principle: Build Proof First</div>
      <div class="callout-desc">
        Do not send cold DMs without proof. Build these 3 exact assets for yourself over the next 3–5 days using your local Antigravity AIOS stack. This gives you instant credibility when sending 2-minute Loom screen video audits.
      </div>
    </div>

    <div class="step-cards-grid">
      <div class="step-card">
        <div class="step-tag">PRIORITY #1</div>
        <h3 class="step-card-title">1. ZORIXEL Showcase App (`zorixel.me`)</h3>
        <div class="step-card-body">
          Build a 1-page ultra-sleek showcase website on your domain `zorixel.me` using <code>website-design-engine</code>.
          <ul class="step-card-list">
            <li>OKLCH Dark-mode design system & custom typography.</li>
            <li>GSAP ScrollTrigger micro-interactions & smooth Lenis scroll.</li>
            <li>Live interactive component preview grid.</li>
          </ul>
        </div>
      </div>

      <div class="step-card">
        <div class="step-tag">PRIORITY #2</div>
        <h3 class="step-card-title">2. Three Flagship Showcase Components</h3>
        <div class="step-card-body">
          Extract and compile 3 high-craft interactive components into your local showcase folder:
          <ul class="step-card-list">
            <li><strong>Hero Section:</strong> Non-generic micro-interactive hero with live stats.</li>
            <li><strong>OKLCH Swatch Swapper:</strong> Interactive color token system.</li>
            <li><strong>Speed-to-Lead Intake Demo:</strong> Instant &lt;5-minute AI response form.</li>
          </ul>
        </div>
      </div>

      <div class="step-card">
        <div class="step-tag">PRIORITY #3</div>
        <h3 class="step-card-title">3. 1-Page Interactive Notion Proposal</h3>
        <div class="step-card-body">
          Create a standardized Notion proposal template containing:
          <ul class="step-card-list">
            <li>Scope & 14-Day Delivery Timeline.</li>
            <li>1-Page Scope Checklist & Playwright Visual QA guarantee.</li>
            <li>Stripe/PayPal/Wise 50% Deposit ($1,500) checkout link.</li>
          </ul>
        </div>
      </div>
    </div>
  </div>

  <!-- Section 2: The Global Async Arbitrage Engine -->
  <div class="section-block">
    <div class="section-header">
      <div class="section-num">02</div>
      <h2 class="section-title">The India Global Async Arbitrage Engine</h2>
    </div>

    <table class="data-table">
      <thead>
        <tr>
          <th>Execution Phase</th>
          <th>Strategy & Workflow</th>
          <th>Tool Stack</th>
          <th>Output & Impact</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>1. Prospecting</strong></td>
          <td>Identify 20 target AI SaaS founders / agency owners per day on LinkedIn & X</td>
          <td><span class="pill pill-blue">Agent Reach / LinkedIn</span></td>
          <td>100 Target Western Prospects / Week</td>
        </tr>
        <tr>
          <td><strong>2. Audit Teardown</strong></td>
          <td>Create a 2-minute Loom screen video audit pointing out 1 generic site element & showing your interactive component prototype</td>
          <td><span class="pill pill-amber">Loom + Screen Share</span></td>
          <td>15 Loom Audits / Week</td>
        </tr>
        <tr>
          <td><strong>3. Async Closing</strong></td>
          <td>Send Loom link in DM $\rightarrow$ Send 1-page Notion proposal $\rightarrow$ Collect $1,500 deposit</td>
          <td><span class="pill pill-green">Notion + Stripe/Wise</span></td>
          <td>1–2 Signed Clients / Month ($3,000–$6,000)</td>
        </tr>
        <tr>
          <td><strong>4. AIOS Delivery</strong></td>
          <td>Build 14-Day Web Experience using local AIOS stack & run Playwright visual QA</td>
          <td><span class="pill pill-blue">Antigravity + Playwright</span></td>
          <td>100% Client Satisfaction & Case Study</td>
        </tr>
      </tbody>
    </table>
  </div>

  <!-- Section 3: 30-Day Execution Roadmap -->
  <div class="section-block">
    <div class="section-header">
      <div class="section-num">03</div>
      <h2 class="section-title">30-Day Day-by-Day Execution Roadmap</h2>
    </div>

    <div class="step-cards-grid">
      <div class="step-card">
        <div class="step-tag">DAYS 1 - 5</div>
        <h3 class="step-card-title">Phase 1: Build Your Own Showcase Assets</h3>
        <div class="step-card-body">
          Focus 100% on self-creation before outreach:
          <ul class="step-card-list">
            <li>Compile Brand Assets (logos, OKLCH swatches, brand posters).</li>
            <li>Deploy <code>zorixel.me</code> showcase landing page.</li>
            <li>Build Notion proposal template with $1,500 deposit link.</li>
          </ul>
        </div>
      </div>

      <div class="step-card">
        <div class="step-tag">DAYS 6 - 15</div>
        <h3 class="step-card-title">Phase 2: Launch Async Lead Generation</h3>
        <div class="step-card-body">
          Start daily outreach rhythm (28–49 hrs/week available):
          <ul class="step-card-list">
            <li>Send 20 LinkedIn/X DMs daily to AI SaaS founders.</li>
            <li>Send 3 personalized Loom teardown videos daily.</li>
            <li>Publish 2 YouTube / X build breakdowns weekly.</li>
          </ul>
        </div>
      </div>

      <div class="step-card">
        <div class="step-tag">DAYS 16 - 30</div>
        <h3 class="step-card-title">Phase 3: Close Client #1 & Scale to $10K MRR</h3>
        <div class="step-card-body">
          Close first client and execute 14-Day Sprint:
          <ul class="step-card-list">
            <li>Collect 50% deposit ($1,500) upon proposal signature.</li>
            <li>Deliver 14-Day Sprint using local AIOS stack.</li>
            <li>Collect remaining 50% ($1,500) & scale to 3 clients/mo ($10,500 MRR).</li>
          </ul>
        </div>
      </div>
    </div>
  </div>

  <!-- Section 4: Next Immediate Step -->
  <div class="section-block">
    <div class="section-header">
      <div class="section-num">04</div>
      <h2 class="section-title">Next Immediate Step: Brand Asset Creation</h2>
    </div>

    <div class="callout-box" style="background: rgba(16, 185, 129, 0.08); border-color: rgba(16, 185, 129, 0.3);">
      <div class="callout-title" style="color: var(--accent-emerald);">🎯 Ready for Brand Asset Generation!</div>
      <div class="callout-desc">
        Now that your strategy, positioning, business model, and execution roadmap are 100% locked, we move directly to <strong>finding and generating your ZORIXEL brand assets</strong> (color tokens, logos, brand guidelines, posters, and 16:9 presentation slides).
      </div>
    </div>
  </div>

  <div class="footer">
    ZORIXEL Brand OS · Master Playbook & Execution Roadmap · 2026-07-30
  </div>

</div>
</body>
</html>
"""

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Generated master playbook HTML: {html_file}")

# Capture PNG Screenshot via Playwright
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1280, "height": 2000})
    page.goto(f"file:///{html_file.replace('\\', '/')}")
    page.wait_for_timeout(1000)
    page.screenshot(path=png_file, full_page=True)
    browser.close()

print(f"Captured Playwright screenshot: {png_file}")
