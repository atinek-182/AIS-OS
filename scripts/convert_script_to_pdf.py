import base64
import os

FONTS_DIR = r"d:\AI-OS\projects\font-showcase\fonts"
SCRIPT_MD = r"d:\AI-OS\clients\001-vashishthya-research-edu\01-pre-outreach-audit\03-pitch-and-loom-guides\LOOM_VIDEO_DEMO_SCRIPT_GUIDE.md"
TARGET_HTML = r"d:\AI-OS\clients\001-vashishthya-research-edu\01-pre-outreach-audit\03-pitch-and-loom-guides\LOOM_VIDEO_DEMO_SCRIPT_GUIDE.html"

def get_base64_font(font_filename):
    path = os.path.join(FONTS_DIR, font_filename)
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

def build_pdf_html():
    havock_b64 = get_base64_font("Havock.otf")
    rosehot_b64 = get_base64_font("Rosehot.ttf")
    nuqun_b64 = get_base64_font("Nuqun-Regular.otf")

    # Native Nuqun Logotype Element
    logo_html = """<span class="brand-logo-nuqun">zorixel</span>"""

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Vashishthya Research - Interactive Loom Demo Script Guide</title>
  <style>
    @font-face {{
      font-family: 'Havock';
      src: url('data:font/otf;base64,{havock_b64}') format('opentype');
      font-weight: bold;
    }}

    @font-face {{
      font-family: 'Rosehot';
      src: url('data:font/ttf;base64,{rosehot_b64}') format('truetype');
      font-weight: normal;
    }}

    @font-face {{
      font-family: 'Nuqun';
      src: url('data:font/otf;base64,{nuqun_b64}') format('opentype');
      font-weight: normal;
      font-style: normal;
    }}

    @page {{
      size: A4 portrait;
      margin: 12mm 12mm 12mm 12mm;
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

    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      background-color: var(--canvas);
      color: var(--text-main);
      line-height: 1.5;
      padding: 24px;
    }}

    .header-bar {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 2px solid var(--burgundy);
      padding-bottom: 16px;
      margin-bottom: 24px;
    }}

    .brand-logo-nuqun {{
      font-family: 'Nuqun', sans-serif;
      font-size: 36px;
      color: var(--text-main);
      text-transform: lowercase;
      letter-spacing: 0.04em;
      line-height: 1;
      display: inline-block;
      filter: drop-shadow(0 2px 6px rgba(0,0,0,0.5));
    }}

    .doc-title {{
      font-family: 'Havock', serif;
      font-size: 26px;
      color: var(--text-main);
      text-transform: uppercase;
      letter-spacing: 1px;
    }}

    .doc-meta {{
      font-family: 'Rosehot', sans-serif;
      font-size: 15px;
      color: var(--ochre);
    }}

    .meta-box {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-left: 4px solid var(--crimson);
      border-radius: 8px;
      padding: 18px 22px;
      margin-bottom: 24px;
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 12px;
    }}

    .meta-item {{
      font-size: 14.5px;
      color: var(--text-muted);
    }}

    .meta-label {{
      font-weight: bold;
      color: var(--text-main);
      margin-right: 6px;
    }}

    .section-title {{
      font-family: 'Rosehot', sans-serif;
      font-size: 20px;
      font-weight: 700;
      color: var(--crimson);
      text-transform: uppercase;
      letter-spacing: 2px;
      margin-top: 26px;
      margin-bottom: 16px;
      border-bottom: 1px solid var(--card-border);
      padding-bottom: 8px;
    }}

    .setup-list {{
      display: flex;
      flex-direction: column;
      gap: 12px;
      margin-bottom: 24px;
    }}

    .setup-item {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 8px;
      padding: 14px 18px;
      font-size: 14.5px;
      color: var(--text-muted);
    }}

    .setup-item strong {{
      color: var(--text-main);
    }}

    .setup-badge {{
      background: var(--burgundy);
      color: var(--text-main);
      font-family: 'Rosehot', sans-serif;
      font-weight: bold;
      font-size: 12px;
      padding: 4px 10px;
      border-radius: 4px;
      margin-right: 10px;
      letter-spacing: 1px;
    }}

    /* Stage Presentation Cards (Dark Theme) */
    .stage-card {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 12px;
      padding: 22px 26px;
      margin-bottom: 20px;
      box-shadow: 0 10px 25px rgba(0,0,0,0.5);
      page-break-inside: avoid;
    }}

    .stage-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 14px;
    }}

    .stage-time {{
      font-family: 'Rosehot', sans-serif;
      font-size: 14px;
      font-weight: bold;
      color: var(--ochre);
      background: rgba(197, 160, 89, 0.15);
      border: 1px solid var(--ochre);
      padding: 4px 14px;
      border-radius: 20px;
    }}

    .stage-name {{
      font-family: 'Havock', serif;
      font-size: 20px;
      color: var(--text-main);
    }}

    .visual-tag {{
      font-size: 13.5px;
      color: var(--text-muted);
      margin-bottom: 14px;
      padding: 8px 14px;
      background: #0D0E12;
      border-radius: 6px;
      border-left: 3px solid var(--ochre);
    }}

    .action-box {{
      background: #101C33;
      border: 1px solid #1E3A8A;
      border-radius: 8px;
      padding: 14px 18px;
      margin-bottom: 14px;
      font-size: 14px;
      color: #93C5FD;
      line-height: 1.6;
    }}

    .action-title {{
      font-weight: bold;
      color: #60A5FA;
      margin-bottom: 6px;
      font-family: 'Rosehot', sans-serif;
      font-size: 15px;
    }}

    .voice-box {{
      background: #121319;
      border-left: 4px solid var(--crimson);
      padding: 14px 18px;
      font-size: 15px;
      color: var(--text-main);
      border-radius: 0 8px 8px 0;
      line-height: 1.65;
    }}

    .voice-label {{
      font-family: 'Rosehot', sans-serif;
      font-size: 13px;
      font-weight: bold;
      color: var(--crimson);
      text-transform: uppercase;
      letter-spacing: 1px;
      margin-bottom: 6px;
    }}

    .pro-tips {{
      background: #1C1913;
      border: 1px solid var(--ochre);
      border-radius: 10px;
      padding: 20px 24px;
      margin-top: 28px;
      page-break-inside: avoid;
    }}

    .pro-tips-title {{
      font-family: 'Rosehot', sans-serif;
      font-weight: bold;
      color: var(--ochre);
      font-size: 18px;
      margin-bottom: 10px;
    }}

    .pro-tips-list {{
      font-size: 14px;
      color: var(--text-muted);
      padding-left: 20px;
      line-height: 1.6;
    }}
  </style>
</head>
<body>

  <div class="header-bar">
    <div>{logo_html}</div>
    <div>
      <div class="doc-title">VASHISTHYA LOOM VIDEO SCRIPT</div>
      <div class="doc-meta">Client Demo Blueprint · Dr. Prashant Singh & Dr. Pooja Singh</div>
    </div>
  </div>

  <div class="meta-box">
    <div class="meta-item"><span class="meta-label">Target Duration:</span> 4 to 5 Minutes</div>
    <div class="meta-item"><span class="meta-label">Recording Mode:</span> Dual-View Interactive Demo</div>
    <div class="meta-item"><span class="meta-label">Tone & Style:</span> Simple, Warm, Human, Non-Technical</div>
    <div class="meta-item"><span class="meta-label">Client Brand:</span> Vashishthya Research Foundation</div>
  </div>

  <div class="section-title">Part 1: Pre-Recording Tab Setup</div>
  <div class="setup-list">
    <div class="setup-item"><span class="setup-badge">TAB 1</span> <strong>Presentation Deck:</strong> Open <code>vashishthya_loom_presentation.html</code> in Chrome full screen mode (<code>F11</code>).</div>
    <div class="setup-item"><span class="setup-badge">TAB 2</span> <strong>Live Notion Workspace:</strong> Open <code>Vashishthya Master Client Desk</code>.</div>
    <div class="setup-item"><span class="setup-badge">TAB 3</span> <strong>Live Synced Google Sheet:</strong> Open <code>Vashishthya-01Master-OS</code>.</div>
  </div>

  <div class="section-title">Part 2: Interactive Line-by-Line Script & Demo Blueprint</div>

  <!-- Stage 1 -->
  <div class="stage-card">
    <div class="stage-header">
      <div class="stage-name">Stage 1: Intro & Respectful Hook</div>
      <div class="stage-time">0:00 - 0:45</div>
    </div>
    <div class="visual-tag">Visual: Tab 1 (Slide 1: VASHISTHYA MASTER CLIENT DESK)</div>
    <div class="voice-box">
      <div class="voice-label">Voice Line (Warm & Respectful):</div>
      "Namaste Prashant Sir & Pooja Mam! I got your reference through [Sister's Name] and saw how dedicatedly you both run Vashishthya Research and your academic journals.<br><br>
      I am not here to sell anything or charge any monthly fee — I just built a simple, easy-to-use tool for your team to save time every single day."
    </div>
  </div>

  <!-- Stage 2 -->
  <div class="stage-card">
    <div class="stage-header">
      <div class="stage-name">Stage 2: Daily Friction & Wasted Hours</div>
      <div class="stage-time">0:45 - 1:30</div>
    </div>
    <div class="visual-tag">Visual: Tab 1 (Slide 2: RECOVER 50-100 STAFF HOURS & 60 LOST LEADS)</div>
    <div class="voice-box">
      <div class="voice-label">Voice Line (Empathetic & Simple):</div>
      "I noticed a lot of your time goes into talking to scholars on calls. Writing details on paper notes, remembering fee updates, and calling staff again and again to check work progress takes a lot of energy and wastes nearly 50 to 100 staff hours every month."
    </div>
  </div>

  <!-- Stage 3 -->
  <div class="stage-card">
    <div class="stage-header">
      <div class="stage-name">Stage 3: Slide 3 & Live Notion Call Intake Demo</div>
      <div class="stage-time">1:30 - 2:30</div>
    </div>
    <div class="visual-tag">Visual Switch: Tab 1 (Slide 3) &rarr; Switch to Tab 2 (Live Notion Workspace)</div>
    <div class="action-box">
      <div class="action-title">Live Action on Notion (Tab 2):</div>
      1. Click <strong>+ New Intake Call</strong>.<br>
      2. Type Candidate Name: <code>Dr. Rajesh Kumar</code> & Phone: <code>9876543210</code>.<br>
      3. Tick services: <code>Ph.D. Writing Assistance (₹20,000)</code> & <code>Patent Service (₹15,000)</code>.<br>
      4. Enter Total Fee (<code>35000</code>) & Advance (<code>10000</code>) &rarr; Point out auto-calculated Balance Due (<code>₹25,000</code>).<br>
      5. Tick a sub-task box to show live visual progress bar updating (<code>0%</code> &rarr; <code>40%</code> &rarr; <code>100%</code>).
    </div>
    <div class="voice-box">
      <div class="voice-label">Voice Line during Live Demo:</div>
      "To fix this, I made a simple <strong>Call Intake Form</strong> that opens on your phone in 1 tap. During any call, just fill in these 3 fields. As soon as you click Submit, your staff gets the task automatically, and you can see this live progress bar on your phone without calling anyone!"
    </div>
  </div>

  <!-- Stage 4 -->
  <div class="stage-card">
    <div class="stage-header">
      <div class="stage-name">Stage 4: Slide 4 & Live Google Sheets Sync Demo</div>
      <div class="stage-time">2:30 - 3:15</div>
    </div>
    <div class="visual-tag">Visual Switch: Switch back to Tab 1 (Slide 4) &rarr; Switch to Tab 3 (Live Google Sheet)</div>
    <div class="action-box">
      <div class="action-title">Live Action on Google Sheets (Tab 3):</div>
      Show the <code>Vashishthya-01Master-OS</code> Google Sheet tab and highlight the newly created row for <code>Dr. Rajesh Kumar</code>.
    </div>
    <div class="voice-box">
      <div class="voice-label">Voice Line during Live Demo:</div>
      "You don't have to worry about losing any data or learning complex systems. Every 15 minutes, our background system automatically syncs every new Notion entry into this shared Google Sheet. So your data is 100% safe, backed up, and accessible anytime!"
    </div>
  </div>

  <!-- Stage 5 -->
  <div class="stage-card">
    <div class="stage-header">
      <div class="stage-name">Stage 5: Slide 5 & Live 1-Click WhatsApp Trigger Demo</div>
      <div class="stage-time">3:15 - 4:00</div>
    </div>
    <div class="visual-tag">Visual Switch: Switch back to Tab 1 (Slide 5) &rarr; Switch to Tab 2 (Live Notion Workspace)</div>
    <div class="action-box">
      <div class="action-title">Live Action on Notion (Tab 2):</div>
      Click the <strong>WhatsApp Action Link</strong> in the Notion row and show WhatsApp Web opening with the auto-generated receipt message pre-filled.
    </div>
    <div class="voice-box">
      <div class="voice-label">Voice Line during Live Demo:</div>
      "Look at this — with just 1 click on Notion, WhatsApp opens with the receipt and balance alert pre-filled for the scholar. You don't have to type long messages manually!"
    </div>
  </div>

  <!-- Stage 6 -->
  <div class="stage-card">
    <div class="stage-header">
      <div class="stage-name">Stage 6: Slides 6 & 7 (Website Audit Findings)</div>
      <div class="stage-time">4:00 - 4:30</div>
    </div>
    <div class="visual-tag">Visual Switch: Switch back to Tab 1 (Slides 6 & 7)</div>
    <div class="voice-box">
      <div class="voice-label">Voice Line (Simple Website Fixes):</div>
      "We also checked your journal website and found two simple things we can fix for you:<br>
      1. Fixing the website layout so scholars can easily read it on smartphones without scrolling sideways.<br>
      2. Helping your published research papers show up directly on Google Scholar so authors get full citation credit."
    </div>
  </div>

  <!-- Stage 7 -->
  <div class="stage-card">
    <div class="stage-header">
      <div class="stage-name">Stage 7: Slide 8 (5 Helpful Future Features)</div>
      <div class="stage-time">4:30 - 5:00</div>
    </div>
    <div class="visual-tag">Visual: Tab 1 (Slide 8: 5 POWERFUL AUTOMATIONS FOR VASHISTHYA)</div>
    <div class="voice-box">
      <div class="voice-label">Voice Line (Curiosity Hook):</div>
      "This simple workspace is just step one. In the future, we can also add 5 more helpful features for your team:<br>
      1. Word Document Layout Checker (checks paper formatting in 10 seconds)<br>
      2. 24/7 WhatsApp Inquiry Assistant<br>
      3. Gentle Reminder Bot for paper reviewers<br>
      4. 1-Click Payment Receipts and Invoices<br>
      5. Instant Originality and Plagiarism Checker."
    </div>
  </div>

  <!-- Stage 8 -->
  <div class="stage-card">
    <div class="stage-header">
      <div class="stage-name">Stage 8: Slide 9 (Free Pilot Offer & Zoom CTA)</div>
      <div class="stage-time">5:00 - 5:30</div>
    </div>
    <div class="visual-tag">Visual: Tab 1 (Slide 9: FREE INSTALLATION & 30-MINUTE ZOOM SETUP)</div>
    <div class="voice-box">
      <div class="voice-label">Voice Line (Warm Closing & CTA):</div>
      "I will set up this entire simple workspace and fix your website issues for FREE as a special pilot project. If you like this idea, just reply 'YES' on WhatsApp, and we can spend 30 minutes on a Zoom call to hand it over to you. Thank you so much Sir & Mam!"
    </div>
  </div>

  <div class="pro-tips">
    <div class="pro-tips-title">Recording Pro-Tips</div>
    <ol class="pro-tips-list">
      <li>Keep Tab 1 (Deck), Tab 2 (Notion), and Tab 3 (Google Sheet) open side-by-side.</li>
      <li>Use <code>Ctrl + Tab</code> or mouse clicks to switch browser tabs smoothly during the live demo.</li>
      <li>Keep your voice tone warm, friendly, calm, and natural throughout the recording.</li>
    </ol>
  </div>

</body>
</html>
"""

    with open(TARGET_HTML, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Successfully generated Dark Theme HTML preview with Nuqun font logo: {TARGET_HTML}")

if __name__ == "__main__":
    build_pdf_html()
