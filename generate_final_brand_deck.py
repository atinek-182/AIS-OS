import base64
import os

# 1. Load Font Base64 CSS
font_sources = [
    # Official ZORIXEL Brand Fonts
    ('Nuqun-Regular', 'd:/AI-OS/projects/font-showcase/fonts/Nuqun-Regular.otf'),
    ('Havock', 'd:/AI-OS/projects/font-showcase/fonts/Havock.otf'),
    ('AICON-Bold', 'C:/Users/HP/Downloads/New Fonts/extracted/aicon/AICON-Bold.otf'),
    ('AICON-ExtraBold', 'C:/Users/HP/Downloads/New Fonts/extracted/aicon/AICON-ExtraBold.otf'),
    ('Rosehot', 'd:/AI-OS/projects/font-showcase/fonts/Rosehot.ttf'),

    # Vault Fonts (Client / Non-Zorixel)
    ('Chorus-Black', 'C:/Users/HP/Downloads/New Fonts/extracted/chorus/CHORUS/CHORUS-BLACK.otf'),
    ('Pavot-Bold', 'C:/Users/HP/Downloads/New Fonts/extracted/pavot/OTF/Pavot-Bold.otf'),
    ('Queensides', 'C:/Users/HP/Downloads/New Fonts/extracted/queensides-font/Queensides-3z7Ey.ttf'),
    ('Rozina-Bold', 'C:/Users/HP/Downloads/New Fonts/extracted/rozina/Rozina V07-Bold.otf'),
    ('ST-Kosmolet-Futurism', 'C:/Users/HP/Downloads/New Fonts/extracted/st_kosmolet/ST-Kosmolet-Futurism.otf'),
    ('BiggerDisplay', 'C:/Users/HP/Downloads/New Fonts/extracted/bigger_display/BiggerDisplay.otf'),
    ('Martius', 'C:/Users/HP/Downloads/New Fonts/extracted/martius/Martius.ttf'),
    ('Ortland', 'C:/Users/HP/Downloads/New Fonts/extracted/ortland/Ortland.otf')
]

css_faces = ""
for name, p in font_sources:
    if os.path.exists(p):
        with open(p, 'rb') as f:
            b64 = base64.b64encode(f.read()).decode('utf-8')
            fmt = 'opentype' if p.endswith('.otf') else 'truetype'
            css_faces += f"@font-face {{\n  font-family: '{name}';\n  src: url('data:font/{fmt};base64,{b64}');\n}}\n"

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>ZORIXEL — Official Brand Typography & Color Identity Specification</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Outfit:wght@400;600;800;900&display=swap" rel="stylesheet">
  <style>
    {css_faces}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      font-family: 'Inter', sans-serif;
      background-color: #060709;
      color: #f3f4f6;
      padding: 2.5rem;
      line-height: 1.5;
    }}

    .container {{
      max-width: 1600px;
      margin: 0 auto;
    }}

    .header-banner {{
      margin-bottom: 3.5rem;
      border-bottom: 1px solid #262832;
      padding-bottom: 2.5rem;
    }}

    .brand-tag {{
      display: inline-block;
      padding: 0.4rem 1rem;
      background: #D61C2C;
      color: #ffffff;
      border-radius: 9999px;
      font-size: 0.85rem;
      font-weight: 800;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      margin-bottom: 1rem;
    }}

    h1 {{
      font-family: 'Outfit', sans-serif;
      font-size: 3.2rem;
      font-weight: 900;
      letter-spacing: -0.02em;
      margin-bottom: 0.75rem;
      background: linear-gradient(135deg, #ffffff 0%, #a1a1aa 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }}

    p.subtitle {{
      color: #9ca3af;
      font-size: 1.2rem;
      max-width: 950px;
    }}

    .palette-strip {{
      display: flex;
      gap: 1rem;
      margin-top: 1.75rem;
      flex-wrap: wrap;
    }}

    .swatch {{
      padding: 0.6rem 1.2rem;
      border-radius: 8px;
      font-weight: 700;
      font-size: 0.85rem;
      font-family: monospace;
    }}

    /* SLIDE STYLES */
    .deck-section {{
      margin-bottom: 5rem;
    }}

    .section-label {{
      font-family: 'Outfit', sans-serif;
      font-size: 2.2rem;
      font-weight: 800;
      color: #ffffff;
      margin-bottom: 2rem;
      display: flex;
      align-items: center;
      gap: 1rem;
    }}

    .section-label::after {{
      content: '';
      flex: 1;
      height: 1px;
      background: #262832;
    }}

    .slide {{
      width: 100%;
      min-height: 80vh;
      border-radius: 24px;
      padding: 4rem;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      box-shadow: 0 25px 60px rgba(0, 0, 0, 0.7);
      border: 1px solid rgba(255, 255, 255, 0.12);
      position: relative;
      overflow: hidden;
      margin-bottom: 3.5rem;
    }}

    .slide-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      z-index: 5;
    }}

    .badge-pill {{
      padding: 0.35rem 1rem;
      border: 1px solid;
      border-radius: 9999px;
      font-size: 0.85rem;
      font-weight: 700;
      font-family: monospace;
      letter-spacing: 0.08em;
    }}

    .font-tag-badge {{
      padding: 0.4rem 1.2rem;
      border-radius: 8px;
      font-weight: 800;
      font-size: 1rem;
      font-family: monospace;
    }}

    .slide-body {{
      margin: auto 0;
      z-index: 5;
      padding: 2rem 0;
    }}

    .subheading-text {{
      font-family: 'Rosehot', serif;
      font-size: clamp(1.8rem, 3.5vw, 3rem);
      margin-bottom: 0.5rem;
      letter-spacing: 0.04em;
    }}

    .main-headline-solid, .main-headline-stroke {{
      font-size: clamp(3.8rem, 9vw, 11rem);
      line-height: 0.95;
      font-weight: 900;
      text-transform: uppercase;
      letter-spacing: 0.04em;
      word-break: break-word;
    }}

    .main-headline-stroke {{
      -webkit-text-stroke: 2.5px;
      color: transparent;
      margin-top: -0.15em;
    }}

    .body-copy-box {{
      margin-top: 2rem;
      border-top: 1px solid;
      padding-top: 1.5rem;
      max-width: 850px;
    }}

    .body-copy-box p {{
      font-size: 1.15rem;
      line-height: 1.6;
      opacity: 0.9;
    }}

    .slide-footer {{
      display: flex;
      justify-content: space-between;
      align-items: flex-end;
      z-index: 5;
    }}

    .logo-mark {{
      font-family: 'Nuqun-Regular', sans-serif;
      font-size: 1.6rem;
      letter-spacing: 0.05em;
    }}

    .rule-meta {{
      font-family: monospace;
      font-size: 0.85rem;
    }}

    /* LIVE HERO PREVIEW COMPONENT */
    .hero-container {{
      display: flex;
      flex-direction: column;
      gap: 1.5rem;
    }}

    .nav-bar {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid rgba(255,255,255,0.15);
      padding-bottom: 1rem;
    }}

    .nav-links {{
      display: flex;
      gap: 2rem;
      font-size: 0.9rem;
      font-weight: 600;
    }}

    .cta-btn {{
      padding: 0.8rem 1.8rem;
      background: #D61C2C;
      color: #ffffff;
      border: none;
      border-radius: 8px;
      font-weight: 800;
      font-size: 0.95rem;
      cursor: pointer;
      align-self: flex-start;
      margin-top: 1.5rem;
    }}
  </style>
</head>
<body>
  <div class="container">
    <div class="main-header">
      <div class="brand-tag">ZORIXEL OFFICIAL BRAND IDENTITY SPECIFICATION</div>
      <h1>ZORIXEL Final Approved Brand Typography & Color Identity</h1>
      <p class="subtitle">
        Finalized brand identity architecture based on your explicit font selection. Features Option 1 Upgraded 5-Color Palette, official Logotype (<code>Nuqun-Regular</code>), Primary Headlines (<code>Havock</code> & <code>AICON</code>), Editorial Subheadings (<code>Rosehot</code>), and UI Body Text (<code>Inter</code>).
      </p>

      <div class="palette-strip">
        <div class="swatch" style="background: #0D0E12; color: #FAF8F5;">Obsidian #0D0E12 (Primary Dark)</div>
        <div class="swatch" style="background: #6D001A; color: #ffffff;">Burgundy #6D001A (Deep Accent)</div>
        <div class="swatch" style="background: #D61C2C; color: #ffffff;">Crimson #D61C2C (Primary Pop)</div>
        <div class="swatch" style="background: #C5A059; color: #0D0E12;">Vintage Ochre Gold #C5A059 (Accent Only)</div>
        <div class="swatch" style="background: #FAF8F5; color: #0D0E12;">Linen Cream #FAF8F5 (Primary Light)</div>
      </div>
    </div>

    <!-- SECTION 1: OFFICIAL ZORIXEL BRAND FONTS -->
    <div class="deck-section">
      <div class="section-label">Section 1: Official ZORIXEL Brand Fonts</div>

      <!-- SLIDE 1: LOGO MARK ONLY -->
      <div class="slide" style="background-color: #0D0E12; color: #FAF8F5; border-color: #6D001A;">
        <div class="slide-header">
          <div class="badge-pill" style="border-color: #C5A059; color: #C5A059;">OFFICIAL BRAND LOGOTYPE</div>
          <div class="font-tag-badge" style="background-color: #D61C2C; color: #ffffff;">Nuqun-Regular</div>
        </div>

        <div class="slide-body">
          <div style="font-family: 'Nuqun-Regular', sans-serif; font-size: clamp(5rem, 13vw, 14rem); color: #FAF8F5; letter-spacing: 0.05em; line-height: 0.9;">
            ZORIXEL
          </div>
        </div>

        <div class="body-copy-box" style="border-color: #C5A059;">
          <div style="font-family: monospace; color: #C5A059; font-weight: 700; margin-bottom: 0.5rem;">STRICT BRAND RULE:</div>
          <p>
            <strong>Nuqun-Regular</strong> is reserved EXCLUSIVELY for the official ZORIXEL logo and brand name marks. It is NEVER used for main headlines, subheadings, or body text.
          </p>
        </div>

        <div class="slide-footer">
          <div class="logo-mark">ZORIXEL</div>
          <div class="rule-meta" style="color: #C5A059;">RULE: LOGO MARK ONLY</div>
        </div>
      </div>

      <!-- SLIDE 2: HAVOCK (FAVORITE PRIMARY HEADLINE FONT) -->
      <div class="slide" style="background-color: #0D0E12; color: #FAF8F5; border-color: #D61C2C;">
        <div class="slide-header">
          <div class="badge-pill" style="border-color: #C5A059; color: #C5A059;">PRIMARY BRAND HEADLINE #1 (FAVORITE)</div>
          <div class="font-tag-badge" style="background-color: #D61C2C; color: #ffffff;">Havock</div>
        </div>

        <div class="slide-body">
          <div class="subheading-text" style="color: #C5A059;">
            ZORIXEL ACADEMY // EDITORIAL VISION 2026
          </div>
          <div class="main-headline-solid" style="font-family: 'Havock', sans-serif; color: #FAF8F5;">
            BUILD
          </div>
          <div class="main-headline-stroke" style="font-family: 'Havock', sans-serif; -webkit-text-stroke-color: #D61C2C;">
            AI APPS
          </div>
        </div>

        <div class="body-copy-box" style="border-color: #C5A059;">
          <div style="font-family: monospace; color: #C5A059; font-weight: 700; margin-bottom: 0.5rem;">PRIMARY FONT SPECIFICATION:</div>
          <p>
            <strong>Havock</strong> is your #1 favorite brand font for ZORIXEL. It is the primary choice for big high-impact headlines, hero titles, and major brand posters. Supports solid fill + hollow crimson text stroke overlays.
          </p>
        </div>

        <div class="slide-footer">
          <div class="logo-mark">ZORIXEL</div>
          <div class="rule-meta" style="color: #D61C2C;">PRIMARY HEADLINE FONT (FAVORITE)</div>
        </div>
      </div>

      <!-- SLIDE 3: AICON EXTRA-BOLD & BOLD (PRIMARY BRAND & POSTER FONT #2) -->
      <div class="slide" style="background-color: #FAF8F5; color: #0D0E12; border-color: #0D0E12;">
        <div class="slide-header">
          <div class="badge-pill" style="border-color: #D61C2C; color: #D61C2C;">PRIMARY BRAND & POSTER HEADLINE #2</div>
          <div class="font-tag-badge" style="background-color: #0D0E12; color: #FAF8F5;">AICON ExtraBold / Bold</div>
        </div>

        <div class="slide-body">
          <div class="subheading-text" style="color: #6D001A;">
            HIGH-PERFORMANCE FRONTEND ARCHITECTURE
          </div>
          <div class="main-headline-solid" style="font-family: 'AICON-ExtraBold', sans-serif; color: #0D0E12;">
            AUTONOMOUS
          </div>
          <div class="main-headline-stroke" style="font-family: 'AICON-Bold', sans-serif; -webkit-text-stroke-color: #D61C2C;">
            ENGINE
          </div>
        </div>

        <div class="body-copy-box" style="border-color: #0D0E12;">
          <div style="font-family: monospace; color: #6D001A; font-weight: 700; margin-bottom: 0.5rem;">PRIMARY FONT SPECIFICATION:</div>
          <p>
            <strong>AICON (Bold & ExtraBold)</strong> is finalized as a primary brand headline font alongside Havock. Excellent for clean technical website headers, feature sections, and high-octane social posters.
          </p>
        </div>

        <div class="slide-footer">
          <div class="logo-mark" style="color: #0D0E12;">ZORIXEL</div>
          <div class="rule-meta" style="color: #D61C2C;">PRIMARY HEADLINE & POSTER FONT</div>
        </div>
      </div>

      <!-- SLIDE 4: ROSEHOT (SUBHEADINGS ONLY) -->
      <div class="slide" style="background-color: #6D001A; color: #FAF8F5; border-color: #D61C2C;">
        <div class="slide-header">
          <div class="badge-pill" style="border-color: #C5A059; color: #C5A059;">OFFICIAL SUBHEADLINE & EDITORIAL TAG FONT</div>
          <div class="font-tag-badge" style="background-color: #C5A059; color: #0D0E12;">Rosehot</div>
        </div>

        <div class="slide-body">
          <div style="font-family: 'Rosehot', serif; font-size: clamp(2.5rem, 5vw, 4.5rem); color: #C5A059; margin-bottom: 1.5rem; line-height: 1.1;">
            Subheading: Master Modern Web Design, Vibe Coding & Agentic Systems
          </div>
          
          <div style="font-family: 'Havock', sans-serif; font-size: clamp(3.5rem, 8vw, 9rem); color: #FAF8F5; text-transform: uppercase;">
            VIBE CODING
          </div>
        </div>

        <div class="body-copy-box" style="border-color: #C5A059;">
          <div style="font-family: monospace; color: #C5A059; font-weight: 700; margin-bottom: 0.5rem;">SUBHEADING RULE:</div>
          <p>
            <strong>Rosehot</strong> is used strictly for subheadings, lead-in editorial tags, and category labels. It is NEVER scaled up to be the giant main headline.
          </p>
        </div>

        <div class="slide-footer">
          <div class="logo-mark">ZORIXEL</div>
          <div class="rule-meta" style="color: #C5A059;">RULE: SUBHEADINGS ONLY</div>
        </div>
      </div>

      <!-- SLIDE 5: LIVE COMPONENT HERO PREVIEW -->
      <div class="slide" style="background-color: #0D0E12; color: #FAF8F5; border-color: #6D001A;">
        <div class="slide-header">
          <div class="badge-pill" style="border-color: #C5A059; color: #C5A059;">COMPLETE ZORIXEL UI HERO COMPONENT PREVIEW</div>
          <div class="font-tag-badge" style="background-color: #D61C2C; color: #ffffff;">Integrated Hierarchy</div>
        </div>

        <div class="slide-body">
          <div class="hero-container">
            <div class="nav-bar">
              <div class="logo-mark" style="color: #FAF8F5;">ZORIXEL</div>
              <div class="nav-links" style="color: #a1a1aa;">
                <span>Workflows</span>
                <span>Academy</span>
                <span>Vibe Coding</span>
                <span style="color: #C5A059;">Option 1 System</span>
              </div>
            </div>

            <div style="margin-top: 1rem;">
              <div class="subheading-text" style="color: #C5A059;">
                // THE 3Ms FRAMEWORK: MINDSET · METHOD · MACHINE
              </div>
              <div class="main-headline-solid" style="font-family: 'Havock', sans-serif; color: #FAF8F5;">
                BUILD UNSTOPPABLE
              </div>
              <div class="main-headline-stroke" style="font-family: 'AICON-ExtraBold', sans-serif; -webkit-text-stroke-color: #D61C2C;">
                AI AUTOMATION
              </div>
            </div>

            <p style="font-size: 1.15rem; max-width: 750px; color: #a1a1aa; line-height: 1.6;">
              Learn fullstack web design, agentic code compilation, and autonomous multi-agent pipelines with Zorixel's high-octane engineering suite.
            </p>

            <button class="cta-btn">Start Learning →</button>
          </div>
        </div>

        <div class="slide-footer">
          <div class="logo-mark">ZORIXEL</div>
          <div class="rule-meta" style="color: #C5A059;">ZORIXEL BRAND SYSTEM v3.0</div>
        </div>
      </div>
    </div>

    <!-- SECTION 2: NON-ZORIXEL CLIENT & POSTER VAULT -->
    <div class="deck-section">
      <div class="section-label">Section 2: Non-ZORIXEL Client & Social Poster Vault</div>

      <!-- SLIDE 6: CHORUS BLACK (ZORIXEL POSTERS & CLIENT VAULT) -->
      <div class="slide" style="background-color: #FAF8F5; color: #0D0E12; border-color: #0D0E12;">
        <div class="slide-header">
          <div class="badge-pill" style="border-color: #D61C2C; color: #D61C2C;">ZORIXEL SOCIAL POSTER & CLIENT VAULT</div>
          <div class="font-tag-badge" style="background-color: #6D001A; color: #ffffff;">Chorus-Black</div>
        </div>

        <div class="slide-body">
          <div class="main-headline-solid" style="font-family: 'Chorus-Black', sans-serif; color: #0D0E12;">
            ZERO SLOP
          </div>
          <div class="main-headline-stroke" style="font-family: 'Chorus-Black', sans-serif; -webkit-text-stroke-color: #D61C2C;">
            UI/UX CAROUSEL
          </div>
        </div>

        <div class="body-copy-box" style="border-color: #0D0E12;">
          <div style="font-family: monospace; color: #6D001A; font-weight: 700; margin-bottom: 0.5rem;">VAULT CLASSIFICATION:</div>
          <p>
            <strong>Chorus-Black</strong> is approved for Zorixel Instagram posters/carousels and client websites. Not used on main Zorixel website.
          </p>
        </div>

        <div class="slide-footer">
          <div class="logo-mark" style="color: #0D0E12;">ZORIXEL POSTERS</div>
          <div class="rule-meta" style="color: #D61C2C;">CAROUSEL & CLIENT VAULT</div>
        </div>
      </div>

      <!-- SLIDE 7: ARCHIVED CLIENT FONTS OVERVIEW -->
      <div class="slide" style="background-color: #0D0E12; color: #FAF8F5; border-color: #262832;">
        <div class="slide-header">
          <div class="badge-pill" style="border-color: #C5A059; color: #C5A059;">ARCHIVED CLIENT & OTHER WEBSITES VAULT</div>
          <div class="font-tag-badge" style="background-color: #262832; color: #FAF8F5;">8 Vault Fonts</div>
        </div>

        <div class="slide-body">
          <div style="font-size: 1.8rem; font-weight: 800; color: #C5A059; margin-bottom: 1.5rem;">
            PRESERVED FOR OTHER CLIENT PROJECTS & WEBSITES
          </div>

          <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 1.5rem;">
            <div style="background: rgba(255,255,255,0.05); padding: 1.25rem; border-radius: 12px; border: 1px solid #262832;">
              <div style="font-family: 'Pavot-Bold'; font-size: 2rem; color: #FAF8F5;">Pavot-Bold</div>
              <div style="font-size: 0.85rem; color: #9ca3af; margin-top: 0.25rem;">Client luxury serif websites</div>
            </div>
            <div style="background: rgba(255,255,255,0.05); padding: 1.25rem; border-radius: 12px; border: 1px solid #262832;">
              <div style="font-family: 'Queensides'; font-size: 2rem; color: #FAF8F5;">Queensides</div>
              <div style="font-size: 0.85rem; color: #9ca3af; margin-top: 0.25rem;">Minimal client portfolios</div>
            </div>
            <div style="background: rgba(255,255,255,0.05); padding: 1.25rem; border-radius: 12px; border: 1px solid #262832;">
              <div style="font-family: 'Rozina-Bold'; font-size: 2rem; color: #FAF8F5;">Rozina-Bold</div>
              <div style="font-size: 0.85rem; color: #9ca3af; margin-top: 0.25rem;">Futuristic tech client projects</div>
            </div>
            <div style="background: rgba(255,255,255,0.05); padding: 1.25rem; border-radius: 12px; border: 1px solid #262832;">
              <div style="font-family: 'ST-Kosmolet-Futurism'; font-size: 2rem; color: #FAF8F5;">ST-Kosmolet</div>
              <div style="font-size: 0.85rem; color: #9ca3af; margin-top: 0.25rem;">Constructivist client banners</div>
            </div>
            <div style="background: rgba(255,255,255,0.05); padding: 1.25rem; border-radius: 12px; border: 1px solid #262832;">
              <div style="font-family: 'BiggerDisplay'; font-size: 2rem; color: #FAF8F5;">BiggerDisplay</div>
              <div style="font-size: 0.85rem; color: #9ca3af; margin-top: 0.25rem;">Ultra-bold client headlines</div>
            </div>
            <div style="background: rgba(255,255,255,0.05); padding: 1.25rem; border-radius: 12px; border: 1px solid #262832;">
              <div style="font-family: 'Martius'; font-size: 2rem; color: #FAF8F5;">Martius & Ortland</div>
              <div style="font-size: 0.85rem; color: #9ca3af; margin-top: 0.25rem;">Client editorial & graphic design</div>
            </div>
          </div>
        </div>

        <div class="slide-footer">
          <div class="logo-mark">CLIENT VAULT</div>
          <div class="rule-meta" style="color: #a1a1aa;">ARCHIVED FOR NON-ZORIXEL PROJECTS</div>
        </div>
      </div>
    </div>
  </div>
</body>
</html>
"""

output_path = 'd:/AI-OS/projects/font-showcase/zorixel_final_brand_deck.html'
with open(output_path, 'w', encoding='utf-8') as out:
    out.write(html_content)

print(f"ZORIXEL Final Brand Deck generated successfully at {output_path}!")
