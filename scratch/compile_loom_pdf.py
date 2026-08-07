import os
import re
from playwright.sync_api import sync_playwright

md_path = r"d:\AI-OS\clients\001-vashishthya-research-edu\01-pre-outreach-audit\03-pitch-and-loom-guides\LOOM_VIDEO_DEMO_SCRIPT_GUIDE.md"
html_path = r"d:\AI-OS\clients\001-vashishthya-research-edu\01-pre-outreach-audit\03-pitch-and-loom-guides\LOOM_VIDEO_DEMO_SCRIPT_GUIDE.html"
pdf_path = r"d:\AI-OS\clients\001-vashishthya-research-edu\01-pre-outreach-audit\03-pitch-and-loom-guides\LOOM_VIDEO_DEMO_SCRIPT_GUIDE.pdf"

with open(md_path, "r", encoding="utf-8") as f:
    md_content = f.read()

# Build HTML template with Zorixel Premium Styling
html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Vashishthya Client Demo & Loom Video Presentation Guide</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Outfit:wght@500;600;700&display=swap');

  @page {{
    size: A4;
    margin: 18mm 15mm 18mm 15mm;
  }}

  * {{
    box-sizing: border-box;
    -webkit-print-color-adjust: exact !important;
    print-color-adjust: exact !important;
  }}

  body {{
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    background-color: #0D0E12;
    color: #FAF8F5;
    margin: 0;
    padding: 0;
    font-size: 13.5px;
    line-height: 1.6;
  }}

  .container {{
    max-width: 100%;
    margin: 0 auto;
  }}

  .header {{
    border-bottom: 2px solid #6D001A;
    padding-bottom: 20px;
    margin-bottom: 25px;
  }}

  .brand-badge {{
    display: inline-block;
    background-color: #6D001A;
    color: #FAF8F5;
    font-family: 'Outfit', sans-serif;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    padding: 4px 12px;
    border-radius: 4px;
    margin-bottom: 12px;
  }}

  h1 {{
    font-family: 'Outfit', sans-serif;
    font-size: 26px;
    font-weight: 700;
    color: #FFFFFF;
    margin: 0 0 10px 0;
    letter-spacing: -0.5px;
  }}

  .meta-grid {{
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 10px 20px;
    background: #161821;
    border: 1px solid #272A38;
    border-radius: 8px;
    padding: 14px 18px;
    margin-top: 15px;
  }}

  .meta-item {{
    font-size: 12px;
  }}

  .meta-item strong {{
    color: #C5A059;
    font-weight: 600;
  }}

  h2 {{
    font-family: 'Outfit', sans-serif;
    font-size: 18px;
    font-weight: 700;
    color: #FFFFFF;
    border-left: 4px solid #D61C2C;
    padding-left: 12px;
    margin: 30px 0 15px 0;
    letter-spacing: -0.3px;
    page-break-after: avoid;
  }}

  h3 {{
    font-family: 'Outfit', sans-serif;
    font-size: 15px;
    font-weight: 600;
    color: #FAF8F5;
    background: #1C1F2D;
    padding: 8px 14px;
    border-radius: 6px;
    margin: 22px 0 12px 0;
    border: 1px solid #2B2F44;
    page-break-after: avoid;
  }}

  p {{
    margin: 0 0 12px 0;
    color: #D1D5DB;
  }}

  ul, ol {{
    margin: 0 0 15px 0;
    padding-left: 22px;
    color: #D1D5DB;
  }}

  li {{
    margin-bottom: 6px;
  }}

  li strong {{
    color: #FFFFFF;
  }}

  .script-box {{
    background-color: #12141C;
    border-left: 4px solid #6D001A;
    border-right: 1px solid #232736;
    border-top: 1px solid #232736;
    border-bottom: 1px solid #232736;
    border-radius: 0 8px 8px 0;
    padding: 16px 20px;
    margin: 12px 0 20px 0;
    font-size: 13px;
    color: #E2E8F0;
    font-style: normal;
    page-break-inside: avoid;
  }}

  .script-label {{
    font-family: 'Outfit', sans-serif;
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1px;
    color: #D61C2C;
    margin-bottom: 8px;
    display: block;
  }}

  .action-box {{
    background-color: #181C2B;
    border: 1px solid #2E344D;
    border-radius: 8px;
    padding: 14px 18px;
    margin: 12px 0 16px 0;
    font-size: 12.5px;
    page-break-inside: avoid;
  }}

  .action-label {{
    font-family: 'Outfit', sans-serif;
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1px;
    color: #C5A059;
    margin-bottom: 6px;
    display: block;
  }}

  .visual-tag {{
    display: inline-block;
    background: #252A3E;
    color: #93C5FD;
    font-family: monospace;
    font-size: 11px;
    padding: 3px 8px;
    border-radius: 4px;
    margin-bottom: 8px;
  }}

  hr {{
    border: none;
    border-top: 1px solid #232736;
    margin: 25px 0;
  }}

  .footer {{
    margin-top: 40px;
    padding-top: 15px;
    border-top: 1px solid #232736;
    text-align: center;
    font-size: 11px;
    color: #64748B;
  }}

  .pro-tips {{
    background: #171A26;
    border: 1px dashed #3B425B;
    border-radius: 8px;
    padding: 18px 22px;
    margin-top: 20px;
  }}
</style>
</head>
<body>
<div class="container">
  <div class="header">
    <div class="brand-badge">ZORIXEL AIOS · CLIENT DEMO GUIDE</div>
    <h1>Vashishthya Client Demo & Loom Video Script</h1>
    <div class="meta-grid">
      <div class="meta-item"><strong>Target Client:</strong> Dr. Prashant Singh & Dr. Pooja Singh</div>
      <div class="meta-item"><strong>Organization:</strong> Vashishthya Research Academy</div>
      <div class="meta-item"><strong>Recording Mode:</strong> Dual-View Interactive Pitch (Deck / Notion / Sheets)</div>
      <div class="meta-item"><strong>Target Loom Duration:</strong> 4 to 5 Minutes</div>
      <div class="meta-item"><strong>Sister Reference:</strong> Hrishita Maurya</div>
      <div class="meta-item"><strong>Tone & Style:</strong> Professional, Warm, Authoritative, Reassuring</div>
    </div>
  </div>
"""

# Process Markdown to HTML sections
lines = md_content.splitlines()
in_script_block = False
script_lines = []

for line in lines:
    if line.startswith("# Vashishthya Client Demo") or line.startswith("**Target Client:**") or line.startswith("**Goal:**") or line.startswith("**Recording Mode:**") or line.startswith("**Tone & Style:**") or line.startswith("**Target Loom Duration:**"):
        continue # handled in header
    
    if line.startswith("## PART "):
        if in_script_block:
            html_content += '<div class="script-box"><span class="script-label">Full Word-for-Word Spoken Script</span>' + '<br>'.join(script_lines) + '</div>'
            in_script_block = False
            script_lines = []
        html_content += f"<h2>{line.replace('## ', '')}</h2>"
    elif line.startswith("### STAGE") or line.startswith("### Pre-Record") or line.startswith("### PART"):
        if in_script_block:
            html_content += '<div class="script-box"><span class="script-label">Full Word-for-Word Spoken Script</span>' + '<br>'.join(script_lines) + '</div>'
            in_script_block = False
            script_lines = []
        html_content += f"<h3>{line.replace('### ', '')}</h3>"
    elif line.startswith("**Visual**:") or line.startswith("**Visual Switch**:"):
        tag_text = line.replace("**Visual**:", "").replace("**Visual Switch**:", "").strip()
        html_content += f'<div class="visual-tag">VISUAL: {tag_text}</div>'
    elif line.startswith("**Screen Action**:") or line.startswith("1.") or line.startswith("2.") or line.startswith("3.") or line.startswith("4.") or line.startswith("5.") or line.startswith("6.") or line.startswith("7.") or line.startswith("8."):
        if not line.startswith(">"):
            if in_script_block:
                html_content += '<div class="script-box"><span class="script-label">Full Word-for-Word Spoken Script</span>' + '<br>'.join(script_lines) + '</div>'
                in_script_block = False
                script_lines = []
            
            # format action line
            formatted_line = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', line)
            if line.startswith("**Screen Action**"):
                html_content += f'<div class="action-box"><span class="action-label">Screen Choreography</span>{formatted_line}</div>'
            else:
                html_content += f'<p>{formatted_line}</p>'
    elif line.startswith(">"):
        in_script_block = True
        clean_line = line.lstrip("> ").replace('"', '&quot;')
        clean_line = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', clean_line)
        script_lines.append(clean_line)
    elif line.startswith("---"):
        if in_script_block:
            html_content += '<div class="script-box"><span class="script-label">Full Word-for-Word Spoken Script</span>' + '<br>'.join(script_lines) + '</div>'
            in_script_block = False
            script_lines = []
        html_content += "<hr>"
    else:
        if line.strip():
            if in_script_block:
                html_content += '<div class="script-box"><span class="script-label">Full Word-for-Word Spoken Script</span>' + '<br>'.join(script_lines) + '</div>'
                in_script_block = False
                script_lines = []
            formatted_line = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', line)
            html_content += f"<p>{formatted_line}</p>"

if in_script_block:
    html_content += '<div class="script-box"><span class="script-label">Full Word-for-Word Spoken Script</span>' + '<br>'.join(script_lines) + '</div>'

html_content += """
  <div class="footer">
    ZORIXEL AIOS · Operational System Pitch & Presentation Guide · Client Confidential
  </div>
</div>
</body>
</html>
"""

# Save HTML file
with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Generated HTML: {html_path}")

# Render PDF using Playwright
print("Rendering PDF via Playwright...")
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto(f"file:///{html_path.replace('\\', '/')}", wait_until="networkidle")
    
    page.pdf(
        path=pdf_path,
        format="A4",
        print_background=True,
        margin={
            "top": "15mm",
            "bottom": "15mm",
            "left": "15mm",
            "right": "15mm"
        }
    )
    browser.close()

print(f"SUCCESS: Compiled PDF to {pdf_path}")
