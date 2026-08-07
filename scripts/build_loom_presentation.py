import base64
import os

FONTS_DIR = r"d:\AI-OS\projects\font-showcase\fonts"
TARGET_HTML_1 = r"d:\AI-OS\clients\001-vashishthya-research-edu\01-pre-outreach-audit\04-visual-assets-and-previews\vashishthya_loom_presentation.html"
TARGET_HTML_2 = r"d:\AI-OS\clients\001-vashishthya-research-edu\04-visual-assets-and-previews\notion_google_sync_presentation.html"

def get_base64_font(font_filename):
    path = os.path.join(FONTS_DIR, font_filename)
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

def build_presentation():
    havock_b64 = get_base64_font("Havock.otf")
    rosehot_b64 = get_base64_font("Rosehot.ttf")
    nuqun_b64 = get_base64_font("Nuqun-Regular.otf")

    # Native Nuqun Logotype Element
    logo_html = """<span class="brand-logo-nuqun">zorixel</span>"""

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Vashishthya Research - Loom Video Presentation Deck</title>
  <style>
    @font-face {{
      font-family: 'Havock';
      src: url('data:font/otf;base64,{havock_b64}') format('opentype');
      font-weight: bold;
      font-style: normal;
    }}

    @font-face {{
      font-family: 'Rosehot';
      src: url('data:font/ttf;base64,{rosehot_b64}') format('truetype');
      font-weight: normal;
      font-style: normal;
    }}

    @font-face {{
      font-family: 'Nuqun';
      src: url('data:font/otf;base64,{nuqun_b64}') format('opentype');
      font-weight: normal;
      font-style: normal;
    }}

    :root {{
      --canvas: #0D0E12;
      --card-bg: #16181F;
      --card-border: #2A2D3A;
      --text-main: #FAF8F5;
      --text-muted: #A0A5B5;
      --burgundy: #6D001A;
      --crimson: #D61C2C;
      --ochre: #C5A059;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    html, body {{
      width: 100%;
      height: 100%;
      overflow: hidden;
      background-color: #000;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      color: var(--text-main);
    }}

    /* Fixed 16:9 Stage (1920x1080) */
    .stage-container {{
      position: absolute;
      top: 50%;
      left: 50%;
      width: 1920px;
      height: 1080px;
      transform: translate(-50%, -50%) scale(1);
      transform-origin: center center;
      background-color: var(--canvas);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      padding: 60px 90px;
      overflow: hidden;
    }}

    /* Navigation Header */
    .deck-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 2px solid var(--burgundy);
      padding-bottom: 18px;
    }}

    .brand-badge {{
      display: flex;
      align-items: center;
      gap: 20px;
    }}

    .brand-logo-nuqun {{
      font-family: 'Nuqun', sans-serif;
      font-size: 34px;
      color: var(--text-main);
      text-transform: lowercase;
      letter-spacing: 0.04em;
      line-height: 1;
      display: inline-block;
      filter: drop-shadow(0 2px 8px rgba(0,0,0,0.6));
    }}

    .brand-title {{
      font-family: 'Rosehot', sans-serif;
      font-size: 20px;
      color: var(--text-muted);
    }}

    .slide-counter {{
      font-family: 'Rosehot', sans-serif;
      font-size: 18px;
      color: var(--ochre);
      font-weight: 600;
      letter-spacing: 1px;
    }}

    /* Slide Content Frames */
    .slide {{
      display: none;
      height: 800px;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      text-align: center;
      padding: 20px 40px;
      animation: fadeIn 0.4s ease-in-out forwards;
    }}

    .slide.active {{
      display: flex;
    }}

    @keyframes fadeIn {{
      from {{ opacity: 0; transform: translateY(12px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}

    /* Zorixel Brand Typography with Generous Spacing & Fixed Line Height */
    .slide-eyebrow {{
      font-family: 'Rosehot', sans-serif;
      font-size: 22px;
      font-weight: 700;
      color: var(--crimson);
      text-transform: uppercase;
      letter-spacing: 3px;
      margin-bottom: 20px;
    }}

    .slide-headline {{
      font-family: 'Havock', serif, sans-serif;
      font-size: 72px;
      font-weight: 900;
      line-height: 1.28;
      color: var(--text-main);
      max-width: 1550px;
      margin-top: 10px;
      margin-bottom: 28px;
      text-transform: uppercase;
      letter-spacing: 1px;
    }}

    .slide-subtext {{
      font-size: 24px;
      color: var(--text-muted);
      max-width: 1250px;
      line-height: 1.55;
      margin-top: 12px;
      margin-bottom: 30px;
    }}

    /* Grid Panel Components for Value Metrics */
    .metrics-grid {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 28px;
      width: 100%;
      max-width: 1450px;
      margin-top: 24px;
    }}

    .metric-card {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 12px;
      padding: 32px 24px;
      text-align: center;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
    }}

    .metric-value {{
      font-family: 'Havock', sans-serif;
      font-size: 44px;
      color: var(--crimson);
      margin-bottom: 12px;
    }}

    .metric-label {{
      font-family: 'Rosehot', sans-serif;
      font-size: 20px;
      color: var(--text-main);
      margin-bottom: 10px;
    }}

    .metric-desc {{
      font-size: 16px;
      color: var(--text-muted);
      line-height: 1.45;
    }}

    /* High-Legibility 5-Automation Layout System (3 + 2 Grid) */
    .automations-container {{
      display: flex;
      flex-direction: column;
      gap: 24px;
      width: 100%;
      max-width: 1550px;
      margin-top: 20px;
    }}

    .automations-row-3 {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 26px;
      width: 100%;
    }}

    .automations-row-2 {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 26px;
      width: 72%;
      margin: 0 auto;
    }}

    .feature-card-large {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 14px;
      padding: 32px 28px;
      text-align: left;
      box-shadow: 0 12px 30px rgba(0, 0, 0, 0.5);
      border-left: 4px solid var(--crimson);
      transition: transform 0.2s ease, border-color 0.2s ease;
    }}

    .feature-card-large:hover {{
      transform: translateY(-4px);
      border-left-color: var(--ochre);
    }}

    .feature-header-row {{
      display: flex;
      align-items: center;
      gap: 16px;
      margin-bottom: 14px;
    }}

    .feature-num-badge {{
      font-family: 'Havock', sans-serif;
      font-size: 36px;
      color: var(--ochre);
      line-height: 1;
    }}

    .feature-title-large {{
      font-family: 'Rosehot', sans-serif;
      font-size: 24px;
      font-weight: 700;
      color: var(--text-main);
      line-height: 1.3;
    }}

    .feature-desc-large {{
      font-size: 18px;
      color: var(--text-muted);
      line-height: 1.55;
    }}

    /* Clickable Screenshot Frame */
    .screenshot-container {{
      position: relative;
      width: 100%;
      max-width: 1350px;
      height: 440px;
      background: var(--card-bg);
      border: 2px solid var(--crimson);
      border-radius: 16px;
      margin-top: 18px;
      overflow: hidden;
      cursor: pointer;
      box-shadow: 0 20px 50px rgba(0, 0, 0, 0.6);
      transition: transform 0.2s ease, border-color 0.2s ease;
    }}

    .screenshot-container:hover {{
      transform: scale(1.01);
      border-color: #FF3B4E;
    }}

    .screenshot-container img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: top left;
    }}

    .zoom-hint {{
      position: absolute;
      bottom: 16px;
      right: 20px;
      background: rgba(13, 14, 18, 0.92);
      color: var(--text-main);
      font-family: 'Rosehot', sans-serif;
      font-size: 15px;
      padding: 8px 18px;
      border-radius: 6px;
      border: 1px solid var(--ochre);
      pointer-events: none;
    }}

    /* Action Buttons & Links */
    .button-group {{
      display: flex;
      gap: 24px;
      margin-top: 24px;
    }}

    .cta-button {{
      display: inline-block;
      background: var(--crimson);
      color: #FFFFFF;
      font-family: 'Rosehot', sans-serif;
      font-size: 20px;
      font-weight: 700;
      padding: 16px 36px;
      border-radius: 8px;
      text-decoration: none;
      transition: background 0.2s ease;
    }}

    .cta-button:hover {{
      background: #B51423;
    }}

    .cta-secondary {{
      background: transparent;
      border: 2px solid var(--ochre);
      color: var(--ochre);
    }}

    .cta-secondary:hover {{
      background: var(--ochre);
      color: var(--canvas);
    }}

    /* Full-Screen Pop-up Modal Lightbox */
    .lightbox-modal {{
      display: none;
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      background: rgba(0, 0, 0, 0.95);
      z-index: 9999;
      justify-content: center;
      align-items: center;
      flex-direction: column;
      padding: 40px;
    }}

    .lightbox-modal.active {{
      display: flex;
    }}

    .lightbox-modal img {{
      max-width: 95%;
      max-height: 85vh;
      border-radius: 12px;
      border: 2px solid var(--ochre);
      box-shadow: 0 25px 60px rgba(0, 0, 0, 0.95);
    }}

    .close-modal {{
      position: absolute;
      top: 24px;
      right: 36px;
      background: var(--crimson);
      color: #FFF;
      font-family: 'Rosehot', sans-serif;
      font-size: 18px;
      padding: 10px 22px;
      border-radius: 8px;
      cursor: pointer;
      border: none;
    }}

    /* Code Preview Container */
    .code-preview {{
      width: 100%;
      height: 100%;
      background: #0B0C10;
      padding: 30px;
      text-align: left;
      font-family: "Courier New", Courier, monospace;
      font-size: 20px;
      color: #E2E8F0;
      overflow: auto;
    }}

    .code-highlight {{
      color: var(--crimson);
      font-weight: bold;
    }}

    .code-success {{
      color: #4ADE80;
      font-weight: bold;
    }}

    /* Footer Controls */
    .deck-footer {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-top: 1px solid var(--card-border);
      padding-top: 18px;
    }}

    .footer-note {{
      font-size: 15px;
      color: var(--text-muted);
    }}

    .controls-hint {{
      font-family: 'Rosehot', sans-serif;
      font-size: 15px;
      color: var(--ochre);
      font-weight: 500;
    }}
  </style>
</head>
<body>

  <div class="stage-container" id="stage">

    <!-- Header with Official Native Nuqun Logo Font -->
    <div class="deck-header">
      <div class="brand-badge">
        <div class="brand-logo-container">
          {logo_html}
        </div>
        <span class="brand-title">Vashishthya Research & Educational Academy</span>
      </div>
      <div class="slide-counter" id="counter">Slide 1 / 9</div>
    </div>

    <!-- Slide 1: Title Hook -->
    <div class="slide active">
      <div class="slide-eyebrow">Zero-Cost Operational Infrastructure</div>
      <h1 class="slide-headline">VASHISTHYA MASTER CLIENT DESK</h1>
      <p class="slide-subtext">Custom Notion OS & Automated Google Sheets Engine for Dr. Prashant Singh & Dr. Pooja Singh</p>
    </div>

    <!-- Slide 2: Wasted Time & Revenue Leakage -->
    <div class="slide">
      <div class="slide-eyebrow">Quantified Operational Bottlenecks</div>
      <h1 class="slide-headline">RECOVER 50-100 STAFF HOURS & 60 LOST LEADS</h1>
      <p class="slide-subtext">Eliminate paper notes, verbal handoffs, and repetitive WhatsApp phone nagging.</p>
      
      <div class="metrics-grid">
        <div class="metric-card">
          <div class="metric-value">50-100 HR</div>
          <div class="metric-label">Staff Hours Saved / Month</div>
          <div class="metric-desc">Automates manual manuscript routing, formatting checks, and reviewer nudging.</div>
        </div>
        <div class="metric-card">
          <div class="metric-value">60 LEADS</div>
          <div class="metric-label">PhD Candidates Saved / Month</div>
          <div class="metric-desc">Eliminates candidate drop-off caused by delayed manual WhatsApp responses.</div>
        </div>
        <div class="metric-card">
          <div class="metric-value">₹0 COST</div>
          <div class="metric-label">100% Free Pilot Sprint</div>
          <div class="metric-desc">Delivered free in exchange for a case study, video testimonial, and referral.</div>
        </div>
      </div>
    </div>

    <!-- Slide 3: Notion Master Client Desk (User's Actual Screenshot + Lightbox Modal) -->
    <div class="slide">
      <div class="slide-eyebrow">Single Source of Truth</div>
      <h1 class="slide-headline">NOTION CALL INTAKE DESK & LIVE DISPATCHER</h1>
      <p class="slide-subtext">Single-tap intake form with real-time employee completion progress bars (0% to 100%).</p>
      
      <div class="screenshot-container" onclick="openModal('notion_user_screenshot.png')">
        <img src="notion_user_screenshot.png" alt="Vashishthya Master Client Desk Workspace" onerror="this.src='notion_live_desk_preview.png';">
        <div class="zoom-hint">Click Image to Open Interactive Full-Screen View</div>
      </div>

      <div class="button-group">
        <a href="https://app.notion.com/p/Vashishthya-Master-Client-Desk-3b2b0c7463df80a3b4f4c7a78b835f7e?source=copy_link" target="_blank" class="cta-button">Open Live Notion Master Client Desk</a>
        <button onclick="openModal('notion_user_screenshot.png')" class="cta-button cta-secondary">Expand Screenshot Lightbox</button>
      </div>
    </div>

    <!-- Slide 4: Google Sheets Integration & Live Synced Sheet Screenshot -->
    <div class="slide">
      <div class="slide-eyebrow">Zero Downtime Failsafe Engine</div>
      <h1 class="slide-headline">AUTOMATED GOOGLE SHEETS LIVE SYNC</h1>
      <p class="slide-subtext">Google Apps Script syncs every Notion row into Google Sheets with zero maintenance.</p>
      
      <div class="screenshot-container" onclick="openModal('gsheet_user_screenshot.png')">
        <img src="gsheet_user_screenshot.png" alt="Vashishthya Synced Google Sheet Workspace">
        <div class="zoom-hint">Click Image to View Synced Google Sheet Full-Screen</div>
      </div>

      <div class="button-group">
        <a href="https://docs.google.com/spreadsheets/d/1HK6B26dVJuaNCM9vkfbe781iZttJr16O7gCPJBEuCh0/edit?gid=0#gid=0" target="_blank" class="cta-button">Open Synced Live Google Sheet</a>
        <button onclick="openModal('gsheet_user_screenshot.png')" class="cta-button cta-secondary">Expand Sheet Screenshot Lightbox</button>
      </div>
    </div>

    <!-- Slide 5: Direct 1-Click WhatsApp Client Actions -->
    <div class="slide">
      <div class="slide-eyebrow">Instant Scholar Communication</div>
      <h1 class="slide-headline">1-CLICK WHATSAPP DIRECT CLIENT ACTIONS</h1>
      <p class="slide-subtext">Pre-encoded WhatsApp click-to-chat links for instant receipts, balance alerts, and status updates.</p>
      
      <div class="metrics-grid">
        <div class="metric-card">
          <div class="metric-value">AUTO-SANITY</div>
          <div class="metric-label">Regex Phone Sanitizer</div>
          <div class="metric-desc">Clean regex formula strips spaces and symbols: replaceAll(prop("Phone"), "[^0-9]", "").</div>
        </div>
        <div class="metric-card">
          <div class="metric-value">%20 ENCODED</div>
          <div class="metric-label">Pre-Formatted WhatsApp Text</div>
          <div class="metric-desc">Sends candidate name, total fee, advance received, and balance due in 1 click.</div>
        </div>
        <div class="metric-card">
          <div class="metric-value">NULL-GUARDS</div>
          <div class="metric-label">Defensive Property Wrappers</div>
          <div class="metric-desc">Prevents Notion formula crashes on blank rows using empty() guards.</div>
        </div>
      </div>
    </div>

    <!-- Slide 6: Mobile Deficiencies & Fixed 768px Breakages -->
    <div class="slide">
      <div class="slide-eyebrow">Website Audit Finding #1</div>
      <h1 class="slide-headline">ZERO MOBILE VIEWPORTS & FIXED 768px BREAKAGES</h1>
      <p class="slide-subtext">Missing viewport meta tags and unadapted fixed graphics break layout on mobile viewports.</p>
      
      <div class="metrics-grid">
        <div class="metric-card">
          <div class="metric-value">30-50%</div>
          <div class="metric-label">Mobile Candidate Loss</div>
          <div class="metric-desc">Scholars leaving due to horizontal scroll breaks on smartphones.</div>
        </div>
        <div class="metric-card">
          <div class="metric-value">7 SERVICES</div>
          <div class="metric-label">Automated Service Pricing</div>
          <div class="metric-desc">PhD (₹20k), PG (₹5k), Books (₹3-5k), Papers (₹2k), Patents (₹15k), Plagiarism (₹100-200).</div>
        </div>
        <div class="metric-card">
          <div class="metric-value">1-TAP</div>
          <div class="metric-label">Mobile Intake Shortcut</div>
          <div class="metric-desc">Pinned directly to founder smartphone home screen for instant call intake.</div>
        </div>
      </div>
    </div>

    <!-- Slide 7: Google Scholar & Indexing Audit -->
    <div class="slide">
      <div class="slide-eyebrow">Website Audit Finding #2</div>
      <h1 class="slide-headline">MISSING GOOGLE SCHOLAR CITATION META-TAGS</h1>
      <p class="slide-subtext">Articles hidden 4 layers deep behind form dropdowns without Dublin Core tags or HTML landing pages.</p>
      
      <div class="screenshot-container" style="cursor:default;">
        <div class="code-preview">
          <div style="color:#94A3B8; margin-bottom:12px;">// Current Codebase Defect: Zero Citation Meta Tags</div>
          <div class="code-highlight">&lt;!-- MISSING: &lt;meta name="citation_title" content="..."&gt; --&gt;</div>
          <div class="code-highlight">&lt;!-- MISSING: &lt;meta name="citation_author" content="..."&gt; --&gt;</div>
          <div class="code-highlight">&lt;!-- MISSING: &lt;meta name="citation_journal_title" content="IJORAR / MJAP"&gt; --&gt;</div>
          
          <div style="color:#94A3B8; margin-top:24px; margin-bottom:12px;">// Proposed Ingestion Fix: Automated Google Scholar Metadata</div>
          <div class="code-success">&lt;meta name="citation_title" content="Academic Research Paper Title"&gt;</div>
          <div class="code-success">&lt;meta name="citation_author" content="Author Full Name"&gt;</div>
          <div class="code-success">&lt;meta name="citation_journal_title" content="International Journal of Original Recent Advanced Research"&gt;</div>
        </div>
      </div>
    </div>

    <!-- Slide 8: 5 Future Expansion AI Automations (NEW 5th AUTOMATION: PLAGIARISM ESTIMATOR) -->
    <div class="slide">
      <div class="slide-eyebrow">Future Growth Expansion</div>
      <h1 class="slide-headline">5 POWERFUL AUTOMATIONS FOR VASHISTHYA</h1>
      <p class="slide-subtext">Next-stage AI capabilities to eliminate manual editorial work and boost author conversions.</p>
      
      <div class="automations-container">
        <!-- Row 1: 3 High-Legibility Cards -->
        <div class="automations-row-3">
          <div class="feature-card-large">
            <div class="feature-header-row">
              <span class="feature-num-badge">01</span>
              <span class="feature-title-large">Manuscript Format Scanner</span>
            </div>
            <div class="feature-desc-large">Auto-checks uploaded Word files for margins, fonts, and layout errors in 10 seconds.</div>
          </div>
          <div class="feature-card-large">
            <div class="feature-header-row">
              <span class="feature-num-badge">02</span>
              <span class="feature-title-large">WhatsApp Intake Assistant</span>
            </div>
            <div class="feature-desc-large">Greets candidates 24/7 on WhatsApp, screens eligibility, and captures thesis scope.</div>
          </div>
          <div class="feature-card-large">
            <div class="feature-header-row">
              <span class="feature-num-badge">03</span>
              <span class="feature-title-large">Reviewer Reminder Bot</span>
            </div>
            <div class="feature-desc-large">Sends automated gentle reminders to peer reviewers before deadlines without staff calls.</div>
          </div>
        </div>
        <!-- Row 2: 2 High-Legibility Cards Centered -->
        <div class="automations-row-2">
          <div class="feature-card-large">
            <div class="feature-header-row">
              <span class="feature-num-badge">04</span>
              <span class="feature-title-large">1-Click APC Invoicing</span>
            </div>
            <div class="feature-desc-large">Auto-generates PDF invoices and publication receipts the moment a paper is accepted.</div>
          </div>
          <div class="feature-card-large">
            <div class="feature-header-row">
              <span class="feature-num-badge">05</span>
              <span class="feature-title-large">Instant Plagiarism Estimator</span>
            </div>
            <div class="feature-desc-large">Runs instant preliminary similarity & plagiarism checks on uploaded drafts before peer review.</div>
          </div>
        </div>
      </div>
    </div>

    <!-- Slide 9: Zero-Cost Flagship Agreement CTA (LAST SLIDE) -->
    <div class="slide">
      <div class="slide-eyebrow">Flagship Case Study Agreement</div>
      <h1 class="slide-headline">FREE INSTALLATION & 30-MINUTE ZOOM SETUP</h1>
      <p class="slide-subtext">Zero upfront cost in exchange for a written case study and recorded video testimonial.</p>
      
      <div class="button-group">
        <a href="https://wa.me/918319353139" target="_blank" class="cta-button">Reply YES on WhatsApp to Schedule Call</a>
      </div>
    </div>

    <!-- Footer Controls -->
    <div class="deck-footer">
      <div class="footer-note">ZORIXEL AI Systems & Business Automation</div>
      <div class="controls-hint">Use Left / Right Arrow Keys or Spacebar to Navigate</div>
    </div>

  </div>

  <!-- Full-Screen Screenshot Lightbox Modal -->
  <div class="lightbox-modal" id="lightboxModal">
    <button class="close-modal" onclick="closeModal()">Close Preview [X]</button>
    <img src="notion_user_screenshot.png" alt="Full Screen Screenshot Preview" id="modalImage">
  </div>

  <script>
    // 16:9 Viewport Auto-Scaler
    function scaleStage() {{
      const stage = document.getElementById('stage');
      const targetWidth = 1920;
      const targetHeight = 1080;
      const windowWidth = window.innerWidth;
      const windowHeight = window.innerHeight;

      const scaleX = windowWidth / targetWidth;
      const scaleY = windowHeight / targetHeight;
      const scale = Math.min(scaleX, scaleY) * 0.96;

      stage.style.transform = `translate(-50%, -50%) scale(${{scale}})`;
    }}

    window.addEventListener('resize', scaleStage);
    window.addEventListener('load', scaleStage);

    // Slide Presentation Controller
    const slides = document.querySelectorAll('.slide');
    const counter = document.getElementById('counter');
    let currentIndex = 0;

    function showSlide(index) {{
      if (index < 0) index = 0;
      if (index >= slides.length) index = slides.length - 1;
      currentIndex = index;

      slides.forEach((slide, idx) => {{
        if (idx === currentIndex) {{
          slide.classList.add('active');
        }} else {{
          slide.classList.remove('active');
        }}
      }});

      counter.textContent = `Slide ${{currentIndex + 1}} / ${{slides.length}}`;
    }}

    document.addEventListener('keydown', (e) => {{
      if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;
      if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'PageDown') {{
        showSlide(currentIndex + 1);
      }} else if (e.key === 'ArrowLeft' || e.key === 'PageUp') {{
        showSlide(currentIndex - 1);
      }} else if (e.key === 'Escape') {{
        closeModal();
      }}
    }});

    // Lightbox Modal Handlers
    function openModal(imageSrc) {{
      const img = document.getElementById('modalImage');
      if (imageSrc) {{
        img.src = imageSrc;
      }}
      document.getElementById('lightboxModal').classList.add('active');
    }}

    function closeModal() {{
      document.getElementById('lightboxModal').classList.remove('active');
    }}
  </script>

</body>
</html>
"""

    for target in [TARGET_HTML_1, TARGET_HTML_2]:
        with open(target, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"Successfully recompiled {target} with native base64 Nuqun font logo!")

if __name__ == "__main__":
    build_presentation()
