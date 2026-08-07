import base64
import os

havock_path = r"d:\AI-OS\projects\font-showcase\fonts\Havock.otf"
rosehot_path = r"d:\AI-OS\projects\font-showcase\fonts\Rosehot.ttf"

with open(havock_path, "rb") as f:
    havock_b64 = base64.b64encode(f.read()).decode("utf-8")

with open(rosehot_path, "rb") as f:
    rosehot_b64 = base64.b64encode(f.read()).decode("utf-8")

print(f"Havock b64 len: {len(havock_b64)}")
print(f"Rosehot b64 len: {len(rosehot_b64)}")

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Client Onboarding Guide: Notion to Google Sheets Auto-Sync</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600&family=Outfit:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    /* =========================================================
       ZORIXEL BRAND FONTS (BASE64 INLINED) & COLOR PALETTE
       ========================================================= */
    @font-face {{
      font-family: 'Havock';
      src: url('data:font/opentype;base64,{havock_b64}') format('opentype');
      font-weight: normal;
      font-style: normal;
      font-display: swap;
    }}

    @font-face {{
      font-family: 'Rosehot';
      src: url('data:font/truetype;base64,{rosehot_b64}') format('truetype');
      font-weight: normal;
      font-style: normal;
      font-display: swap;
    }}

    :root {{
      --bg-dark: #0D0E12;
      --bg-card: #15171E;
      --border-card: #252833;
      --text-main: #FAF8F5;
      --text-muted: #9E9EA6;
      --brand-burgundy: #6D001A;
      --brand-crimson: #D61C2C;
      --brand-ochre: #C5A059;
      --font-hero: 'Havock', sans-serif;
      --font-heading: 'Rosehot', serif;
      --font-body: 'Outfit', sans-serif;
      --font-mono: 'JetBrains Mono', monospace;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    html, body {{
      width: 100%;
      height: 100%;
      background-color: #050507;
      color: var(--text-main);
      font-family: var(--font-body);
      overflow: hidden;
      display: flex;
      justify-content: center;
      align-items: center;
      -webkit-font-smoothing: antialiased;
    }}

    /* Fixed 16:9 Stage (1920x1080) */
    .stage-wrapper {{
      width: 100vw;
      height: 100vh;
      display: flex;
      justify-content: center;
      align-items: center;
      position: relative;
    }}

    .stage {{
      width: 1920px;
      height: 1080px;
      background-color: var(--bg-dark);
      position: absolute;
      transform-origin: center center;
      box-shadow: 0 30px 100px rgba(0,0,0,0.8);
      overflow: hidden;
      display: flex;
      flex-direction: column;
    }}

    /* Slide Navigation System */
    .slide {{
      width: 100%;
      height: 100%;
      position: absolute;
      top: 0;
      left: 0;
      opacity: 0;
      visibility: hidden;
      transition: opacity 0.4s cubic-bezier(0.16, 1, 0.3, 1), transform 0.4s cubic-bezier(0.16, 1, 0.3, 1);
      transform: scale(0.98);
      padding: 80px 100px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }}

    .slide.active {{
      opacity: 1;
      visibility: visible;
      transform: scale(1);
      z-index: 2;
    }}

    /* Header & Badges */
    .slide-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 30px;
    }}

    .badge {{
      display: inline-flex;
      align-items: center;
      gap: 10px;
      padding: 8px 20px;
      background-color: rgba(214, 28, 44, 0.1);
      border: 1px solid rgba(214, 28, 44, 0.3);
      color: var(--brand-crimson);
      font-family: var(--font-heading);
      font-size: 18px;
      letter-spacing: 1px;
    }}

    .badge-ochre {{
      background-color: rgba(197, 160, 89, 0.1);
      border-color: rgba(197, 160, 89, 0.3);
      color: var(--brand-ochre);
    }}

    .brand-mark {{
      font-family: var(--font-heading);
      font-size: 24px;
      letter-spacing: 2px;
      color: var(--text-main);
    }}

    /* Typography Utilities */
    .hero-title {{
      font-family: var(--font-hero);
      font-size: 96px;
      font-weight: normal;
      line-height: 1.1;
      letter-spacing: 1px;
      color: var(--text-main);
      margin-bottom: 24px;
      text-transform: uppercase;
    }}

    .section-title {{
      font-family: var(--font-hero);
      font-size: 72px;
      font-weight: normal;
      line-height: 1.15;
      letter-spacing: 1px;
      color: var(--text-main);
      margin-bottom: 20px;
      text-transform: uppercase;
    }}

    .sub-title {{
      font-family: var(--font-heading);
      font-size: 32px;
      color: var(--brand-ochre);
      margin-bottom: 16px;
    }}

    .lead-text {{
      font-size: 24px;
      line-height: 1.6;
      color: var(--text-muted);
      max-width: 1200px;
    }}

    .text-crimson {{ color: var(--brand-crimson); }}
    .text-ochre {{ color: var(--brand-ochre); }}

    /* Grid Layouts */
    .grid-2 {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 60px;
      align-items: center;
      flex: 1;
    }}

    .grid-3 {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 40px;
      align-items: stretch;
      flex: 1;
    }}

    .grid-4 {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 30px;
      align-items: stretch;
      flex: 1;
    }}

    /* Cards & Containers */
    .card {{
      background-color: var(--bg-card);
      border: 1px solid var(--border-card);
      padding: 40px;
      display: flex;
      flex-direction: column;
      justify-content: flex-start;
      position: relative;
    }}

    .card-highlight {{
      border-color: var(--brand-crimson);
      background-color: #1A1115;
    }}

    .card-number {{
      font-family: var(--font-hero);
      font-size: 48px;
      color: var(--brand-ochre);
      margin-bottom: 16px;
    }}

    .card-title {{
      font-family: var(--font-heading);
      font-size: 28px;
      margin-bottom: 14px;
      color: var(--text-main);
    }}

    .card-desc {{
      font-size: 18px;
      line-height: 1.6;
      color: var(--text-muted);
    }}

    /* Mockup Screens (UI Screenshots) */
    .mockup-window {{
      background-color: #111319;
      border: 1px solid #2B2F3D;
      border-radius: 8px;
      overflow: hidden;
      box-shadow: 0 20px 50px rgba(0,0,0,0.6);
      display: flex;
      flex-direction: column;
      width: 100%;
    }}

    .mockup-header {{
      background-color: #1A1D27;
      padding: 12px 20px;
      display: flex;
      align-items: center;
      gap: 12px;
      border-bottom: 1px solid #2B2F3D;
    }}

    .dots {{
      display: flex;
      gap: 6px;
    }}

    .dot {{
      width: 10px;
      height: 10px;
      border-radius: 50%;
      background-color: #383D4F;
    }}
    .dot.red {{ background-color: #FF5F56; }}
    .dot.yellow {{ background-color: #FFBD2E; }}
    .dot.green {{ background-color: #27C93F; }}

    .mockup-title {{
      font-family: var(--font-mono);
      font-size: 13px;
      color: var(--text-muted);
      margin-left: 10px;
    }}

    .mockup-body {{
      padding: 30px;
      font-family: var(--font-mono);
      font-size: 15px;
      line-height: 1.7;
      color: #D4D4D8;
      overflow-x: auto;
    }}

    .code-keyword {{ color: #F472B6; }}
    .code-string {{ color: #A7F3D0; }}
    .code-var {{ color: #93C5FD; }}
    .code-comment {{ color: #6B7280; }}

    /* UI Table Mockup */
    .mockup-table {{
      width: 100%;
      border-collapse: collapse;
      font-family: var(--font-body);
      font-size: 15px;
      text-align: left;
    }}

    .mockup-table th {{
      background-color: #1F2330;
      color: var(--brand-ochre);
      padding: 14px 18px;
      font-family: var(--font-mono);
      font-size: 13px;
      text-transform: uppercase;
      border-bottom: 1px solid #2B2F3D;
    }}

    .mockup-table td {{
      padding: 14px 18px;
      border-bottom: 1px solid #1F2330;
      color: #E4E4E7;
    }}

    .tag-status {{
      display: inline-block;
      padding: 4px 10px;
      border-radius: 4px;
      font-size: 12px;
      font-weight: 600;
      font-family: var(--font-mono);
    }}
    .tag-green {{ background: rgba(39, 201, 63, 0.15); color: #4ADE80; }}
    .tag-yellow {{ background: rgba(255, 189, 46, 0.15); color: #FACC15; }}

    /* Controls Bar */
    .controls {{
      position: absolute;
      bottom: 30px;
      right: 40px;
      z-index: 100;
      display: flex;
      align-items: center;
      gap: 20px;
      background: rgba(13, 14, 18, 0.85);
      padding: 12px 24px;
      border: 1px solid var(--border-card);
      backdrop-filter: blur(10px);
    }}

    .btn-ctrl {{
      background: none;
      border: 1px solid var(--border-card);
      color: var(--text-main);
      padding: 8px 16px;
      font-family: var(--font-mono);
      font-size: 14px;
      cursor: pointer;
      transition: all 0.2s ease;
    }}

    .btn-ctrl:hover {{
      background-color: var(--brand-crimson);
      border-color: var(--brand-crimson);
    }}

    .slide-counter {{
      font-family: var(--font-mono);
      font-size: 14px;
      color: var(--text-muted);
    }}

    /* Progress Bar */
    .progress-container {{
      position: absolute;
      bottom: 0;
      left: 0;
      width: 100%;
      height: 4px;
      background-color: rgba(255,255,255,0.05);
      z-index: 100;
    }}

    .progress-bar {{
      height: 100%;
      width: 14.28%;
      background-color: var(--brand-crimson);
      transition: width 0.3s ease;
    }}
  </style>
</head>
<body>

  <div class="stage-wrapper">
    <div class="stage" id="stage">

      <!-- SLIDE 1: Title & Hero Stage -->
      <div class="slide active" id="slide-1">
        <div class="slide-header">
          <div class="badge">CLIENT ONBOARDING GUIDE</div>
          <div class="brand-mark">YOUR SETUP MANUAL</div>
        </div>
        <div style="flex: 1; display: flex; flex-direction: column; justify-content: center;">
          <h1 class="hero-title">NOTION DATABASE<br><span class="text-crimson">TO GOOGLE SHEETS AUTO-SYNC</span></h1>
          <div class="sub-title">Simple 4-Step Setup Guide for Your Team</div>
          <p class="lead-text">Follow this quick visual guide to connect your Notion database to a live Google Sheet ledger. Once connected, your records update automatically 24/7 with zero monthly software costs.</p>
        </div>
        <div style="display: flex; gap: 40px; border-top: 1px solid var(--border-card); padding-top: 30px;">
          <div>
            <div style="font-family: var(--font-mono); font-size: 13px; color: var(--text-muted);">SETUP TIME</div>
            <div style="font-size: 18px; font-weight: 700;">Under 5 Minutes</div>
          </div>
          <div>
            <div style="font-family: var(--font-mono); font-size: 13px; color: var(--text-muted);">MONTHLY FEE</div>
            <div style="font-size: 18px; font-weight: 700;" class="text-ochre">$0.00 / Free Forever</div>
          </div>
          <div>
            <div style="font-family: var(--font-mono); font-size: 13px; color: var(--text-muted);">TECHNICAL SKILL NEEDED</div>
            <div style="font-size: 18px; font-weight: 700;">None (Copy & Paste Only)</div>
          </div>
        </div>
      </div>

      <!-- SLIDE 2: What You Need Before Starting -->
      <div class="slide" id="slide-2">
        <div class="slide-header">
          <div class="badge badge-ochre">PRE-FLIGHT CHECKLIST</div>
          <div class="brand-mark">WHAT YOU NEED</div>
        </div>
        <div>
          <h2 class="section-title">BEFORE YOU <span class="text-ochre">BEGIN SETUP</span></h2>
          <p class="lead-text" style="font-size: 22px; margin-bottom: 40px;">Make sure you have these 3 simple things ready in your web browser:</p>
        </div>
        <div class="grid-3">
          <div class="card">
            <div class="card-number">01</div>
            <div class="card-title">Notion Account</div>
            <div class="card-desc">Access to your company's Notion workspace where your database lives.</div>
          </div>
          <div class="card card-highlight">
            <div class="card-number" style="color: var(--brand-crimson);">02</div>
            <div class="card-title">Google Account</div>
            <div class="card-desc">A free Google or Google Workspace account to host your Google Sheet ledger.</div>
          </div>
          <div class="card">
            <div class="card-number">03</div>
            <div class="card-title">The Template Script</div>
            <div class="card-desc">The copyable Google Apps Script file (`GoogleAppsScript_NotionSync.gs`) provided in your onboarding folder.</div>
          </div>
        </div>
      </div>

      <!-- SLIDE 3: Step 1 — Notion Integration Setup -->
      <div class="slide" id="slide-3">
        <div class="slide-header">
          <div class="badge">STEP 1 OF 4</div>
          <div class="brand-mark">NOTION ACCESS</div>
        </div>
        <div class="grid-2">
          <div>
            <h2 class="section-title">CREATE YOUR <span class="text-crimson">NOTION ACCESS KEY</span></h2>
            <div class="sub-title">Connecting Your Notion Workspace Safely</div>
            <ol style="padding-left: 24px; font-size: 20px; line-height: 1.8; color: var(--text-muted);">
              <li>Open <strong style="color: #fff;">notion.so/my-integrations</strong> in your browser.</li>
              <li>Click <strong>New integration</strong>, name it <strong style="color: #fff;">My Company Sync</strong>, and click Save.</li>
              <li>Copy your secret key (<code style="color: var(--brand-ochre); font-family: var(--font-mono);">ntn_...</code>).</li>
              <li>Open your Notion database, click <strong style="color: #fff;">... (Top Right)</strong> &rarr; <strong style="color: #fff;">Add connections</strong> &rarr; Select <strong style="color: #fff;">My Company Sync</strong>.</li>
            </ol>
          </div>
          <div class="mockup-window">
            <div class="mockup-header">
              <div class="dots"><div class="dot red"></div><div class="dot yellow"></div><div class="dot green"></div></div>
              <div class="mockup-title">Notion Settings & Connections</div>
            </div>
            <div class="mockup-body">
              <div style="background-color: #191B24; border: 1px dashed #3F4457; padding: 20px; text-align: center; margin-bottom: 20px;">
                <div style="color: var(--brand-ochre); font-weight: 700; font-size: 16px; margin-bottom: 8px;">Your Secret Integration Token:</div>
                <div style="font-family: var(--font-mono); color: #fff;">[YOUR_NOTION_SECRET_TOKEN]</div>
              </div>
              <div style="border: 1px solid #2B2F3D; padding: 16px; background: #0E1017;">
                <div style="font-size: 13px; color: #888; margin-bottom: 8px;">CONNECTED INTEGRATIONS:</div>
                <div style="display: flex; justify-content: space-between; align-items: center; background: #191B24; padding: 10px 14px;">
                  <span style="color: #fff; font-weight: 600;">My Company Sync</span>
                  <span style="color: #4ADE80; font-size: 12px; font-family: var(--font-mono);">[CONNECTED]</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- SLIDE 4: Step 2 — Apps Script Setup -->
      <div class="slide" id="slide-4">
        <div class="slide-header">
          <div class="badge badge-ochre">STEP 2 OF 4</div>
          <div class="brand-mark">GOOGLE SHEETS</div>
        </div>
        <div class="grid-2">
          <div>
            <h2 class="section-title">PASTE CODE INTO <span class="text-ochre">GOOGLE SHEETS</span></h2>
            <div class="sub-title">Placing the Automation Engine</div>
            <ol style="padding-left: 24px; font-size: 20px; line-height: 1.8; color: var(--text-muted);">
              <li>Open your Google Sheet (or create a new blank sheet).</li>
              <li>Click the top menu: <strong style="color: #fff;">Extensions</strong> &rarr; <strong style="color: #fff;">Apps Script</strong>.</li>
              <li>Delete all existing text in `Code.gs` and paste the template code.</li>
              <li>Paste your <code style="color: var(--brand-ochre); font-family: var(--font-mono);">[YOUR_NOTION_SECRET_TOKEN]</code> and <code style="color: var(--brand-ochre); font-family: var(--font-mono);">[YOUR_NOTION_DATABASE_ID]</code> into lines 21-22.</li>
              <li>Click <strong style="color: #fff;">Save (Ctrl + S)</strong>.</li>
            </ol>
          </div>
          <div class="mockup-window">
            <div class="mockup-header">
              <div class="dots"><div class="dot red"></div><div class="dot yellow"></div><div class="dot green"></div></div>
              <div class="mockup-title">Google Apps Script Editor · Code.gs</div>
            </div>
            <div class="mockup-body">
              <span class="code-comment">// REPLACE WITH YOUR OWN KEYS BELOW</span><br>
              <span class="code-keyword">var</span> <span class="code-var">CONFIG</span> = {{<br>
              &nbsp;&nbsp;<span class="code-var">NOTION_API_KEY</span>: <span class="code-string">'[YOUR_NOTION_SECRET_TOKEN]'</span>,<br>
              &nbsp;&nbsp;<span class="code-var">NOTION_DATABASE_ID</span>: <span class="code-string">'[YOUR_NOTION_DATABASE_ID]'</span>,<br>
              &nbsp;&nbsp;<span class="code-var">TAB_CLIENTS</span>: <span class="code-string">'Client Roster'</span>,<br>
              &nbsp;&nbsp;<span class="code-var">TAB_FINANCIALS</span>: <span class="code-string">'Financial Ledger'</span><br>
              }};
            </div>
          </div>
        </div>
      </div>

      <!-- SLIDE 5: Step 3 — Automated Trigger Setup -->
      <div class="slide" id="slide-5">
        <div class="slide-header">
          <div class="badge">STEP 3 OF 4</div>
          <div class="brand-mark">AUTO-TRIGGER</div>
        </div>
        <div class="grid-2">
          <div>
            <h2 class="section-title">TURN ON THE <span class="text-crimson">AUTOMATIC CLOCK</span></h2>
            <div class="sub-title">Making it Run 24/7 in the Background</div>
            <ol style="padding-left: 24px; font-size: 20px; line-height: 1.8; color: var(--text-muted);">
              <li>On the Apps Script left menu, click the <strong style="color: #fff;">Triggers (Clock Icon)</strong>.</li>
              <li>Click <strong style="color: #fff;">+ Add Trigger</strong> in the bottom right corner.</li>
              <li>Set Function to: <code style="color: var(--brand-ochre); font-family: var(--font-mono);">runMasterSync</code>.</li>
              <li>Set Event Source to: <strong style="color: #fff;">Time-driven</strong> &rarr; <strong style="color: #fff;">Every 15 minutes</strong>.</li>
              <li>Click <strong style="color: #fff;">Save</strong> and grant permissions when prompted.</li>
            </ol>
          </div>
          <div class="mockup-window">
            <div class="mockup-header">
              <div class="dots"><div class="dot red"></div><div class="dot yellow"></div><div class="dot green"></div></div>
              <div class="mockup-title">Add Trigger Settings Modal</div>
            </div>
            <div class="mockup-body" style="padding: 24px;">
              <div style="background: #191B24; border: 1px solid #2B2F3D; padding: 14px; margin-bottom: 12px; display: flex; justify-content: space-between;">
                <span style="color: #888;">Choose function to run:</span>
                <span style="color: var(--brand-ochre); font-weight: 600;">runMasterSync</span>
              </div>
              <div style="background: #191B24; border: 1px solid #2B2F3D; padding: 14px; margin-bottom: 12px; display: flex; justify-content: space-between;">
                <span style="color: #888;">Select event source:</span>
                <span style="color: #fff; font-weight: 600;">Time-driven</span>
              </div>
              <div style="background: #191B24; border: 1px solid #2B2F3D; padding: 14px; display: flex; justify-content: space-between;">
                <span style="color: #888;">Select minute interval:</span>
                <span style="color: #4ADE80; font-weight: 600;">Every 15 minutes</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- SLIDE 6: Step 4 — Live Ledger & WhatsApp Actions -->
      <div class="slide" id="slide-6">
        <div class="slide-header">
          <div class="badge badge-ochre">STEP 4 OF 4</div>
          <div class="brand-mark">LIVE RESULT</div>
        </div>
        <div>
          <h2 class="section-title">YOUR LIVE <span class="text-ochre">CLIENT LEDGER IS READY</span></h2>
          <p class="lead-text" style="font-size: 20px; margin-bottom: 30px;">Whenever your team adds or updates a record in Notion, Google Sheets updates automatically with zero manual entry.</p>
        </div>
        <div class="mockup-window" style="flex: 1;">
          <div class="mockup-header">
            <div class="dots"><div class="dot red"></div><div class="dot yellow"></div><div class="dot green"></div></div>
            <div class="mockup-title">Google Sheets · Tab: Client Roster (Sample Output)</div>
          </div>
          <div class="mockup-body" style="padding: 0;">
            <table class="mockup-table">
              <thead>
                <tr>
                  <th>Client ID</th>
                  <th>Client Name</th>
                  <th>Contact Number</th>
                  <th>Contract Value</th>
                  <th>Advance Paid</th>
                  <th>Balance Due</th>
                  <th>Status</th>
                  <th>1-Click WhatsApp Link</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td style="font-family: var(--font-mono);">CL-101</td>
                  <td>Client Alpha</td>
                  <td>+1 (555) 019-2834</td>
                  <td>$5,000</td>
                  <td>$2,500</td>
                  <td style="color: #F87171;">$2,500</td>
                  <td><span class="tag-status tag-yellow">In Progress</span></td>
                  <td><a href="#" style="color: #60A5FA; text-decoration: none;">Click to Chat on WhatsApp</a></td>
                </tr>
                <tr>
                  <td style="font-family: var(--font-mono);">CL-102</td>
                  <td>Client Beta</td>
                  <td>+1 (555) 019-5829</td>
                  <td>$2,000</td>
                  <td>$2,000</td>
                  <td style="color: #4ADE80;">$0</td>
                  <td><span class="tag-status tag-green">Completed</span></td>
                  <td><a href="#" style="color: #60A5FA; text-decoration: none;">Click to Chat on WhatsApp</a></td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>

      <!-- SLIDE 7: Conclusion & Execution Checkpoint -->
      <div class="slide" id="slide-7">
        <div class="slide-header">
          <div class="badge">CONGRATULATIONS</div>
          <div class="brand-mark">SYSTEM LIVE</div>
        </div>
        <div style="flex: 1; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center;">
          <h2 class="hero-title" style="font-size: 80px;">YOUR SYSTEM IS <span class="text-crimson">FULLY AUTOMATED</span></h2>
          <p class="lead-text" style="max-width: 900px; margin: 0 auto 40px auto;">You now have a zero-maintenance sync engine linking your Notion workspace to Google Sheets, operating 24/7 on your own Google account with zero subscription costs.</p>
          <div style="display: flex; gap: 20px;">
            <div class="card" style="padding: 24px 40px; text-align: center;">
              <div style="font-size: 24px; font-weight: 700; color: var(--brand-ochre);">100%</div>
              <div style="font-size: 14px; color: var(--text-muted);">Self-Hosted & Private</div>
            </div>
            <div class="card" style="padding: 24px 40px; text-align: center;">
              <div style="font-size: 24px; font-weight: 700; color: var(--brand-crimson);">$0.00</div>
              <div style="font-size: 14px; color: var(--text-muted);">Monthly Software Cost</div>
            </div>
            <div class="card" style="padding: 24px 40px; text-align: center;">
              <div style="font-size: 24px; font-weight: 700; color: #4ADE80;">24/7</div>
              <div style="font-size: 14px; color: var(--text-muted);">Automated Cloud Sync</div>
            </div>
          </div>
        </div>
      </div>

      <!-- Progress Bar -->
      <div class="progress-container">
        <div class="progress-bar" id="progress-bar"></div>
      </div>

      <!-- Controls Overlay -->
      <div class="controls">
        <button class="btn-ctrl" id="btn-prev">&larr; PREV</button>
        <span class="slide-counter" id="slide-counter">SLIDE 1 / 7</span>
        <button class="btn-ctrl" id="btn-next">NEXT &rarr;</button>
      </div>

    </div>
  </div>

  <script>
    // Fixed 16:9 Viewport Stage Scaler
    function scaleStage() {{
      const stage = document.getElementById('stage');
      const windowWidth = window.innerWidth;
      const windowHeight = window.innerHeight;
      const scaleX = windowWidth / 1920;
      const scaleY = windowHeight / 1080;
      const scale = Math.min(scaleX, scaleY);
      stage.style.transform = `scale(${{scale}})`;
    }}

    window.addEventListener('resize', scaleStage);
    scaleStage();

    // Slide Navigation Controller
    let currentSlide = 1;
    const totalSlides = 7;

    function showSlide(index) {{
      if (index < 1) index = 1;
      if (index > totalSlides) index = totalSlides;
      
      currentSlide = index;
      
      document.querySelectorAll('.slide').forEach((slide, idx) => {{
        if (idx + 1 === currentSlide) {{
          slide.classList.add('active');
        }} else {{
          slide.classList.remove('active');
        }}
      }});

      document.getElementById('slide-counter').innerText = `SLIDE ${{currentSlide}} / ${{totalSlides}}`;
      document.getElementById('progress-bar').style.width = `${{(currentSlide / totalSlides) * 100}}%`;
    }}

    document.getElementById('btn-prev').addEventListener('click', () => showSlide(currentSlide - 1));
    document.getElementById('btn-next').addEventListener('click', () => showSlide(currentSlide + 1));

    window.addEventListener('keydown', (e) => {{
      if (e.key === 'ArrowRight' || e.key === 'Space' || e.key === 'PageDown') {{
        showSlide(currentSlide + 1);
      }} else if (e.key === 'ArrowLeft' || e.key === 'PageUp') {{
        showSlide(currentSlide - 1);
      }} else if (e.key === 'f' || e.key === 'F') {{
        if (!document.fullscreenElement) {{
          document.documentElement.requestFullscreen();
        }} else {{
          document.exitFullscreen();
        }}
      }}
    }});
  </script>
</body>
</html>"""

target_path_1 = r"d:\AI-OS\clients\001-vashishthya-research-edu\04-visual-assets-and-previews\notion_google_sync_presentation.html"
target_path_2 = r"d:\AI-OS\projects\notion-google-sync-presentation\index.html"

with open(target_path_1, "w", encoding="utf-8") as f:
    f.write(html_content)

with open(target_path_2, "w", encoding="utf-8") as f:
    f.write(html_content)

print("Successfully compiled client presentation deck with Havock & Rosehot base64 fonts!")
