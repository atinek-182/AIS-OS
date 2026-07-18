# -*- coding: utf-8 -*-
import os

fpath = "projects/font-showcase/presentation.html"

# Read original file to keep the font-face imports and header styling
with open(fpath, "r", encoding="utf-8") as f:
    html = f.read()

# Locate the end of style sheet and start of body
style_end = html.find('</style>')
body_start = html.find('<body>')

if style_end == -1 or body_start == -1:
    print("Error: Could not locate stylesheet ending or body start!")
    exit(1)

# Extract styles and fonts declarations
head_html = html[:style_end]

# Define new styles for Dashboard layout elements and forms
custom_styles = """
        /* ===========================================
           HIGH-FIDELITY INTERACTIVE LAYOUT MODULES
           =========================================== */
        .grid-dashboard {
            display: grid;
            grid-template-columns: 240px 1fr;
            width: 100%;
            height: 100%;
            background: rgba(255,255,255,0.02);
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: 24px;
            overflow: hidden;
            box-shadow: 0 40px 100px rgba(0,0,0,0.5);
            text-align: left;
        }

        .db-sidebar {
            background: rgba(0,0,0,0.2);
            border-right: 1px solid rgba(255,255,255,0.06);
            padding: 32px 24px;
            display: flex;
            flex-direction: column;
            gap: 32px;
        }

        .db-menu-item {
            display: flex;
            align-items: center;
            gap: 12px;
            font-family: 'Outfit';
            font-size: 15px;
            color: rgba(255,255,255,0.6);
            cursor: pointer;
            padding: 10px 14px;
            border-radius: 8px;
            transition: all 0.2s;
        }

        .db-menu-item.active-item {
            color: #ffffff;
            background: rgba(255,255,255,0.06);
        }

        .db-content {
            padding: 40px;
            display: flex;
            flex-direction: column;
            gap: 32px;
            overflow: hidden;
        }

        .db-stats-row {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 24px;
        }

        .db-card {
            background: rgba(255,255,255,0.02);
            border: 1px solid rgba(255,255,255,0.06);
            border-radius: 16px;
            padding: 24px;
            display: flex;
            flex-direction: column;
            gap: 12px;
        }

        .db-card-label {
            font-family: 'Space Mono', monospace;
            font-size: 11px;
            text-transform: uppercase;
            color: rgba(255,255,255,0.4);
            letter-spacing: 0.1em;
        }

        .db-card-value {
            font-family: 'Space Mono', monospace;
            font-size: 38px;
            font-weight: 700;
            color: #ffffff;
            letter-spacing: -0.02em;
        }

        .form-field {
            display: flex;
            flex-direction: column;
            gap: 8px;
            width: 100%;
        }

        .form-field label {
            font-family: 'Space Mono', monospace;
            font-size: 11px;
            text-transform: uppercase;
            color: rgba(255,255,255,0.5);
            letter-spacing: 0.1em;
        }

        .form-field input, .form-field textarea {
            background: rgba(255,255,255,0.03);
            border: 1px solid rgba(255,255,255,0.12);
            border-radius: 8px;
            padding: 14px 18px;
            font-family: 'Outfit';
            font-size: 15px;
            color: #ffffff;
            outline: none;
            transition: border-color 0.2s;
        }

        .form-field input:focus, .form-field textarea:focus {
            border-color: var(--accent);
        }
"""

new_deck_html = """<body>

    <div class="deck-viewport">
        <main class="deck-stage" id="deckStage">

            <!-- ===========================================
               OPTION A: ROSEHOT (DARK EDITORIAL)
               =========================================== -->

            <!-- Slide 1: Option A - Hero Section -->
            <section class="slide theme-b active" style="--bg-primary: #0f0f12; --text-primary: #f5f5f7; --accent: #df5d4b; padding: 80px 100px; justify-content: space-between;">
                <!-- Header nav -->
                <div style="display: flex; justify-content: space-between; align-items: center; width: 100%; z-index: 2;">
                    <span style="font-family: 'Nuqun'; font-size: 32px; font-weight: bold; text-transform: lowercase; letter-spacing: 0.05em; color: #ffffff;">zorixel</span>
                    <div style="display: flex; gap: 32px; font-family: 'Outfit'; font-size: 14px; color: rgba(255,255,255,0.6);">
                        <span>Products</span>
                        <span>Solutions</span>
                        <span>Showcase</span>
                        <span>Contact</span>
                    </div>
                </div>

                <!-- Hero Content -->
                <div style="z-index: 2; text-align: left; max-width: 1200px; margin-top: 40px;">
                    <h1 contenteditable="true" style="font-family: 'Rosehot'; font-size: 95px; font-weight: normal; line-height: 0.95; margin: 0 0 24px 0; letter-spacing: 0.01em; color: #ffffff;">
                        Web Design Showcase
                    </h1>
                    <p contenteditable="true" style="font-family: 'Outfit'; font-size: 19px; color: rgba(245,245,247,0.7); margin-bottom: 40px; max-width: 800px; line-height: 1.6; letter-spacing: 0.03em;">
                        A classic serif typeface paired with geometric layouts. Designed for storytelling, premium publications, and high-end agency portfolios.
                    </p>
                    <div style="display: flex; gap: 16px;">
                        <button style="background: var(--accent); color: #ffffff; border: none; padding: 14px 32px; border-radius: 50px; font-family: 'Space Mono', monospace; font-weight: 700; font-size: 13px; cursor: pointer; transition: transform 0.2s;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">View Gallery</button>
                        <button style="background: transparent; color: #ffffff; border: 1px solid rgba(255,255,255,0.2); padding: 14px 32px; border-radius: 50px; font-family: 'Space Mono', monospace; font-weight: 700; font-size: 13px; cursor: pointer; transition: transform 0.2s;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">Learn More</button>
                    </div>
                </div>

                <div class="slide-footer" style="z-index: 2; width: 100%;">
                    <span>Option A (Rosehot Dark) — Hero Section</span>
                    <span>Slide 1 of 20</span>
                </div>
            </section>

            <!-- Slide 2: Option A - About & Contact -->
            <section class="slide theme-b" style="--bg-primary: #0f0f12; --text-primary: #f5f5f7; --accent: #df5d4b; padding: 80px 100px; justify-content: flex-start;">
                <!-- Header nav -->
                <div style="display: flex; justify-content: space-between; align-items: center; width: 100%; border-bottom: 1px solid rgba(255,255,255,0.08); padding-bottom: 16px; margin-bottom: 40px;">
                    <span style="font-family: 'Nuqun'; font-size: 24px; font-weight: bold; text-transform: lowercase; letter-spacing: 0.05em; color: #ffffff;">zorixel</span>
                    <span style="font-family: 'Space Mono', monospace; font-size: 12px; color: rgba(255,255,255,0.4);">Brand Showcase</span>
                </div>

                <div class="split-grid">
                    <!-- Left: About text -->
                    <div style="display: flex; flex-direction: column; gap: 24px; text-align: left;">
                        <h2 contenteditable="true" style="font-family: 'Rosehot'; font-size: 54px; font-weight: normal; margin: 0; line-height: 1.0; color: #ffffff; letter-spacing: 0.01em;">
                            The Character of Form
                        </h2>
                        <p contenteditable="true" style="font-family: 'Outfit'; font-size: 18px; color: rgba(245,245,247,0.75); margin: 0; line-height: 1.7; letter-spacing: 0.03em;">
                            We believe typography is the core behavior of a user interface. Every letter shape should balance high-impact presentation and seamless utility. Pairing this styling with modern geometric text systems ensures maximum readability across screens of all sizes.
                        </p>
                    </div>

                    <!-- Right: Contact form -->
                    <div style="background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.08); border-radius: 20px; padding: 40px; display: flex; flex-direction: column; gap: 20px; text-align: left;">
                        <h3 contenteditable="true" style="font-family: 'Rosehot'; font-size: 32px; font-weight: normal; margin: 0; color: #ffffff;">
                            Get in Touch
                        </h3>
                        <div class="form-field">
                            <label>Your Name</label>
                            <input type="text" placeholder="e.g. Atinek Maurya" readonly>
                        </div>
                        <div class="form-field">
                            <label>Email Address</label>
                            <input type="email" placeholder="e.g. hello@zorixel.design" readonly>
                        </div>
                        <button style="background: var(--accent); color: #ffffff; border: none; padding: 14px; border-radius: 8px; font-family: 'Space Mono', monospace; font-weight: 700; font-size: 13px; cursor: pointer; text-transform: uppercase; margin-top: 10px;">Send Message</button>
                    </div>
                </div>

                <div class="slide-footer" style="border-top: 1px solid rgba(255,255,255,0.08); padding-top: 16px; margin-top: auto; width: 100%;">
                    <span>Option A (Rosehot Dark) — About &amp; Contact</span>
                    <span>Slide 2 of 20</span>
                </div>
            </section>

            <!-- Slide 3: Option A - Dashboard Page -->
            <section class="slide theme-b" style="--bg-primary: #0f0f12; --text-primary: #f5f5f7; --accent: #df5d4b; padding: 60px 80px; justify-content: space-between;">
                <!-- Grid Dashboard wrapper -->
                <div class="grid-dashboard" style="background: rgba(255,255,255,0.01); border-color: rgba(255,255,255,0.06);">
                    <!-- Sidebar -->
                    <div class="db-sidebar" style="border-color: rgba(255,255,255,0.04);">
                        <span style="font-family: 'Nuqun'; font-size: 24px; font-weight: bold; text-transform: lowercase; letter-spacing: 0.05em; color: #ffffff;">zorixel</span>
                        <div style="display: flex; flex-direction: column; gap: 8px; margin-top: 20px;">
                            <div class="db-menu-item active-item">Overview</div>
                            <div class="db-menu-item">Subscribers</div>
                            <div class="db-menu-item">Campaigns</div>
                            <div class="db-menu-item">Settings</div>
                        </div>
                    </div>

                    <!-- Content -->
                    <div class="db-content">
                        <!-- Stats Row -->
                        <div class="db-stats-row">
                            <div class="db-card">
                                <span class="db-card-label">monthly readers</span>
                                <span class="db-card-value" contenteditable="true">384,120</span>
                            </div>
                            <div class="db-card">
                                <span class="db-card-label">session duration</span>
                                <span class="db-card-value" contenteditable="true">4m 12s</span>
                            </div>
                            <div class="db-card">
                                <span class="db-card-label">conversion rate</span>
                                <span class="db-card-value" contenteditable="true">8.45%</span>
                            </div>
                        </div>

                        <!-- Panel with chart SVG -->
                        <div style="flex-grow: 1; border: 1px solid rgba(255,255,255,0.06); border-radius: 16px; padding: 24px; display: flex; flex-direction: column; justify-content: space-between; position: relative; background: rgba(0,0,0,0.15);">
                            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
                                <span style="font-family: 'Space Mono', monospace; font-size: 12px; color: rgba(255,255,255,0.4); text-transform: uppercase;">Story Engagement Chart</span>
                                <span style="font-family: 'Space Mono', monospace; font-size: 12px; color: var(--accent);">Editorial Stats</span>
                            </div>
                            
                            <!-- SVG Chart -->
                            <div style="width: 100%; height: 260px;">
                                <svg viewBox="0 0 1400 260" style="width: 100%; height: 100%; overflow: visible;">
                                    <defs>
                                        <linearGradient id="gradient-rosehot-dark" x1="0" y1="0" x2="0" y2="1">
                                            <stop offset="0%" stop-color="var(--accent)" stop-opacity="0.25"/>
                                            <stop offset="100%" stop-color="var(--accent)" stop-opacity="0.00"/>
                                        </linearGradient>
                                    </defs>
                                    <path d="M 0,260 L 0,210 Q 300,100 600,190 T 1000,90 T 1400,60 L 1400,260 Z" fill="url(#gradient-rosehot-dark)"/>
                                    <line x1="0" y1="65" x2="1400" y2="65" stroke="rgba(255,255,255,0.05)" stroke-dasharray="4"/>
                                    <line x1="0" y1="130" x2="1400" y2="130" stroke="rgba(255,255,255,0.05)" stroke-dasharray="4"/>
                                    <line x1="0" y1="195" x2="1400" y2="195" stroke="rgba(255,255,255,0.05)" stroke-dasharray="4"/>
                                    <path d="M 0,210 Q 300,100 600,190 T 1000,90 T 1400,60" fill="none" stroke="var(--accent)" stroke-width="4"/>
                                    <circle cx="600" cy="190" r="6" fill="#ffffff" stroke="var(--accent)" stroke-width="3"/>
                                    <circle cx="1000" cy="90" r="6" fill="#ffffff" stroke="var(--accent)" stroke-width="3"/>
                                </svg>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="slide-footer" style="width: 100%;">
                    <span>Option A (Rosehot Dark) — Live Dashboard Interface</span>
                    <span>Slide 3 of 20</span>
                </div>
            </section>

            <!-- Slide 4: Option A - Poster Section -->
            <section class="slide theme-b" style="--bg-primary: #0f0f12; --text-primary: #f5f5f7; --accent: #df5d4b; padding: 80px 100px; justify-content: center; align-items: center;">
                <div class="bg-photo" style="background-image: url('https://images.unsplash.com/photo-1600585154340-be6161a56a0c?q=80&w=1920'); opacity: 0.15;"></div>
                <div class="bg-overlay"></div>
                
                <div style="background: rgba(15, 15, 18, 0.75); backdrop-filter: blur(24px); border: 1px solid rgba(223,93,75,0.15); border-radius: 32px; padding: 60px 80px; max-width: 900px; text-align: center; z-index: 2; box-shadow: 0 40px 100px rgba(0,0,0,0.6);">
                    <h2 contenteditable="true" style="font-family: 'Rosehot'; font-size: 72px; font-weight: normal; margin: 0 0 24px 0; line-height: 0.95; color: #ffffff; letter-spacing: 0.01em;">
                        System Architecture
                    </h2>
                    <p contenteditable="true" style="font-family: 'Outfit'; font-size: 18px; color: rgba(245,245,247,0.7); margin-bottom: 32px; line-height: 1.6; letter-spacing: 0.03em;">
                        Download the case studies and visual layouts, designed for storytellers who seek to balance elegance and technical structure.
                    </p>
                    
                    <div style="display: flex; background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.1); border-radius: 8px; overflow: hidden; width: 100%; max-width: 500px; padding: 4px; margin: 0 auto;">
                        <input type="email" placeholder="Your email" style="flex: 1; border: none; outline: none; background: transparent; padding: 14px 20px; font-family: 'Outfit'; font-size: 16px; color: #ffffff;" readonly>
                        <button style="background: var(--accent); color: #ffffff; border: none; outline: none; padding: 12px 30px; font-family: 'Space Mono', monospace; font-weight: 700; font-size: 13px; border-radius: 6px; cursor: pointer; text-transform: uppercase;">Submit</button>
                    </div>
                </div>

                <div class="slide-footer" style="z-index: 2; width: 100%;">
                    <span>Option A (Rosehot Dark) — Creative Poster Layout</span>
                    <span>Slide 4 of 20</span>
                </div>
            </section>

            <!-- Slide 5: Option A - Footer Layout -->
            <section class="slide theme-b" style="--bg-primary: #000000; --text-primary: #ffffff; --accent: #df5d4b; padding: 60px 80px; justify-content: space-between;">
                <!-- Header navigation -->
                <div style="display: flex; justify-content: space-between; align-items: center; width: 100%; z-index: 2;">
                    <span style="font-family: 'Nuqun'; font-size: 24px; font-weight: bold; text-transform: lowercase; letter-spacing: 0.05em;">zorixel</span>
                    <div style="display: flex; gap: 32px; font-family: 'Outfit'; font-size: 14px; color: rgba(255,255,255,0.7);">
                        <span>Products</span>
                        <span>Projects</span>
                        <span>Stores</span>
                        <span>Contact</span>
                        <span style="color: #ffffff; font-weight: bold;">ENG ∨</span>
                    </div>
                </div>

                <!-- Central Massive Logo (Rosehot) -->
                <div style="text-align: center; width: 100%; z-index: 2; margin: 40px 0;">
                    <h1 contenteditable="true" style="font-family: 'Rosehot'; font-size: 260px; font-weight: normal; letter-spacing: -0.01em; margin: 0; line-height: 0.85;">
                        Zorixel
                    </h1>
                    <!-- Dot emblem -->
                    <div style="width: 28px; height: 28px; background: #ffffff; border-radius: 50%; margin: 30px auto 0 auto; box-shadow: 0 0 20px rgba(255,255,255,0.5);"></div>
                </div>

                <!-- Footer details grid -->
                <div style="display: grid; grid-template-columns: 1.5fr 1fr 1.5fr; gap: 40px; width: 100%; z-index: 2; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 30px; text-align: left;">
                    <div style="display: flex; flex-direction: column; justify-content: space-between; height: 120px;">
                        <a href="mailto:hello@zorixel.design" style="color: #ffffff; text-decoration: none; font-family: 'Outfit'; font-size: 16px; border-bottom: 1px solid rgba(255,255,255,0.2); width: fit-content; padding-bottom: 2px;">hello@zorixel.design</a>
                        <div style="display: flex; gap: 12px; margin-top: 12px;">
                            <span style="width: 36px; height: 36px; border-radius: 50%; border: 1px solid rgba(255,255,255,0.2); display: flex; align-items: center; justify-content: center; font-size: 14px;">IG</span>
                            <span style="width: 36px; height: 36px; border-radius: 50%; border: 1px solid rgba(255,255,255,0.2); display: flex; align-items: center; justify-content: center; font-size: 14px;">GH</span>
                        </div>
                        <div style="font-family: 'Outfit'; font-size: 12px; color: rgba(255,255,255,0.4); margin-top: 16px;">
                            2026 zorixel All rights reserved.<br>
                            Terms of Service | Privacy Policy
                        </div>
                    </div>

                    <div style="display: flex; flex-direction: column; gap: 8px; font-family: 'Outfit'; font-size: 15px; color: rgba(255,255,255,0.8);">
                        <span>Home</span>
                        <span>Products</span>
                        <span>Projects</span>
                        <span>Store</span>
                        <span>Contact</span>
                    </div>

                    <div style="font-family: 'Outfit'; font-size: 14px; color: rgba(255,255,255,0.5); line-height: 1.6; display: flex; flex-direction: column; justify-content: flex-start;">
                        <span style="font-weight: 600; color: #ffffff; margin-bottom: 4px;">zorixel office</span>
                        <span>40, Changdeokgung 1-gil,</span>
                        <span>Seoul, Korea</span>
                    </div>
                </div>

                <div class="slide-footer" style="z-index: 2; width: 100%;">
                    <span>Option A (Rosehot Dark) — Brand Footer Layout</span>
                    <span>Slide 5 of 20</span>
                </div>
            </section>


            <!-- ===========================================
               OPTION B: ROSEHOT (LIGHT EDITORIAL)
               =========================================== -->

            <!-- Slide 6: Option B - Hero Section -->
            <section class="slide theme-b" style="--bg-primary: #faf8f5; --text-primary: #111111; --accent: #df5d4b; padding: 80px 100px; justify-content: space-between;">
                <!-- Header nav -->
                <div style="display: flex; justify-content: space-between; align-items: center; width: 100%; z-index: 2;">
                    <span style="font-family: 'Nuqun'; font-size: 32px; font-weight: bold; text-transform: lowercase; letter-spacing: 0.05em; color: #111111;">zorixel</span>
                    <div style="display: flex; gap: 32px; font-family: 'Outfit'; font-size: 14px; color: rgba(17,17,17,0.6);">
                        <span>Products</span>
                        <span>Solutions</span>
                        <span>Showcase</span>
                        <span>Contact</span>
                    </div>
                </div>

                <!-- Hero Content -->
                <div style="z-index: 2; text-align: left; max-width: 1200px; margin-top: 40px;">
                    <h1 contenteditable="true" style="font-family: 'Rosehot'; font-size: 95px; font-weight: normal; line-height: 0.95; margin: 0 0 24px 0; letter-spacing: 0.01em; color: #111111;">
                        Crafting Editorial Digital Design
                    </h1>
                    <p contenteditable="true" style="font-family: 'Outfit'; font-size: 19px; color: rgba(17,17,17,0.7); margin-bottom: 40px; max-width: 800px; line-height: 1.6; letter-spacing: 0.03em;">
                        A classic serif typeface paired with geometric layouts. Designed for storytelling, premium publications, and high-end agency portfolios.
                    </p>
                    <div style="display: flex; gap: 16px;">
                        <button style="background: #111111; color: #faf8f5; border: none; padding: 14px 32px; border-radius: 50px; font-family: 'Space Mono', monospace; font-weight: 700; font-size: 13px; cursor: pointer; transition: transform 0.2s;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">View Gallery</button>
                        <button style="background: transparent; color: #111111; border: 1px solid rgba(17,17,17,0.2); padding: 14px 32px; border-radius: 50px; font-family: 'Space Mono', monospace; font-weight: 700; font-size: 13px; cursor: pointer; transition: transform 0.2s;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">Learn More</button>
                    </div>
                </div>

                <div class="slide-footer" style="z-index: 2; width: 100%;">
                    <span>Option B (Rosehot Light) — Hero Section</span>
                    <span>Slide 6 of 20</span>
                </div>
            </section>

            <!-- Slide 7: Option B - About & Contact -->
            <section class="slide theme-b" style="--bg-primary: #faf8f5; --text-primary: #111111; --accent: #df5d4b; padding: 80px 100px; justify-content: flex-start;">
                <!-- Header nav -->
                <div style="display: flex; justify-content: space-between; align-items: center; width: 100%; border-bottom: 1px solid rgba(17,17,17,0.08); padding-bottom: 16px; margin-bottom: 40px;">
                    <span style="font-family: 'Nuqun'; font-size: 24px; font-weight: bold; text-transform: lowercase; letter-spacing: 0.05em; color: #111111;">zorixel</span>
                    <span style="font-family: 'Space Mono', monospace; font-size: 12px; color: rgba(17,17,17,0.4);">Brand Showcase</span>
                </div>

                <div class="split-grid">
                    <!-- Left: About text -->
                    <div style="display: flex; flex-direction: column; gap: 24px; text-align: left;">
                        <h2 contenteditable="true" style="font-family: 'Rosehot'; font-size: 54px; font-weight: normal; margin: 0; line-height: 1.0; color: #111111; letter-spacing: 0.01em;">
                            Elegant Proportions
                        </h2>
                        <p contenteditable="true" style="font-family: 'Outfit'; font-size: 18px; color: rgba(17,17,17,0.75); margin: 0; line-height: 1.7; letter-spacing: 0.03em;">
                            Editorial serif curves offer organic contrast to rigid digital viewports, bringing human touch and narrative flow back to technical interfaces. Pairing this styling with modern geometric text systems ensures maximum readability across screens of all sizes.
                        </p>
                    </div>

                    <!-- Right: Contact form -->
                    <div style="background: rgba(0,0,0,0.02); border: 1px solid rgba(17,17,17,0.08); border-radius: 20px; padding: 40px; display: flex; flex-direction: column; gap: 20px; text-align: left;">
                        <h3 contenteditable="true" style="font-family: 'Rosehot'; font-size: 32px; font-weight: normal; margin: 0; color: #111111;">
                            Write to Us
                        </h3>
                        <div class="form-field" style="--accent: #111111;">
                            <label style="color: rgba(17,17,17,0.5);">Your Name</label>
                            <input type="text" placeholder="e.g. Atinek Maurya" style="background: transparent; border-color: rgba(17,17,17,0.15); color: #111111;" readonly>
                        </div>
                        <div class="form-field" style="--accent: #111111;">
                            <label style="color: rgba(17,17,17,0.5);">Email Address</label>
                            <input type="email" placeholder="e.g. hello@zorixel.design" style="background: transparent; border-color: rgba(17,17,17,0.15); color: #111111;" readonly>
                        </div>
                        <button style="background: #111111; color: #faf8f5; border: none; padding: 14px; border-radius: 8px; font-family: 'Space Mono', monospace; font-weight: 700; font-size: 13px; cursor: pointer; text-transform: uppercase; margin-top: 10px;">Send Message</button>
                    </div>
                </div>

                <div class="slide-footer" style="border-top: 1px solid rgba(17,17,17,0.08); padding-top: 16px; margin-top: auto; width: 100%;">
                    <span>Option B (Rosehot Light) — About &amp; Contact</span>
                    <span>Slide 7 of 20</span>
                </div>
            </section>

            <!-- Slide 8: Option B - Dashboard Page -->
            <section class="slide theme-b" style="--bg-primary: #111111; --text-primary: #f5f5f7; --accent: #df5d4b; padding: 60px 80px; justify-content: space-between;">
                <!-- Grid Dashboard wrapper -->
                <div class="grid-dashboard" style="background: rgba(255,255,255,0.01); border-color: rgba(255,255,255,0.06);">
                    <!-- Sidebar -->
                    <div class="db-sidebar" style="border-color: rgba(255,255,255,0.04);">
                        <span style="font-family: 'Nuqun'; font-size: 24px; font-weight: bold; text-transform: lowercase; letter-spacing: 0.05em; color: #ffffff;">zorixel</span>
                        <div style="display: flex; flex-direction: column; gap: 8px; margin-top: 20px;">
                            <div class="db-menu-item active-item">Overview</div>
                            <div class="db-menu-item">Subscribers</div>
                            <div class="db-menu-item">Campaigns</div>
                            <div class="db-menu-item">Settings</div>
                        </div>
                    </div>

                    <!-- Content -->
                    <div class="db-content">
                        <!-- Stats Row -->
                        <div class="db-stats-row">
                            <div class="db-card">
                                <span class="db-card-label">monthly readers</span>
                                <span class="db-card-value" contenteditable="true">384,120</span>
                            </div>
                            <div class="db-card">
                                <span class="db-card-label">session duration</span>
                                <span class="db-card-value" contenteditable="true">4m 12s</span>
                            </div>
                            <div class="db-card">
                                <span class="db-card-label">conversion rate</span>
                                <span class="db-card-value" contenteditable="true">8.45%</span>
                            </div>
                        </div>

                        <!-- Panel with chart SVG -->
                        <div style="flex-grow: 1; border: 1px solid rgba(255,255,255,0.06); border-radius: 16px; padding: 24px; display: flex; flex-direction: column; justify-content: space-between; position: relative; background: rgba(0,0,0,0.15);">
                            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
                                <span style="font-family: 'Space Mono', monospace; font-size: 12px; color: rgba(255,255,255,0.4); text-transform: uppercase;">Story Engagement Chart</span>
                                <span style="font-family: 'Space Mono', monospace; font-size: 12px; color: var(--accent);">Editorial Stats</span>
                            </div>
                            
                            <!-- SVG Chart -->
                            <div style="width: 100%; height: 260px;">
                                <svg viewBox="0 0 1400 260" style="width: 100%; height: 100%; overflow: visible;">
                                    <defs>
                                        <linearGradient id="gradient-rosehot-light" x1="0" y1="0" x2="0" y2="1">
                                            <stop offset="0%" stop-color="var(--accent)" stop-opacity="0.25"/>
                                            <stop offset="100%" stop-color="var(--accent)" stop-opacity="0.00"/>
                                        </linearGradient>
                                    </defs>
                                    <path d="M 0,260 L 0,210 Q 300,100 600,190 T 1000,90 T 1400,60 L 1400,260 Z" fill="url(#gradient-rosehot-light)"/>
                                    <line x1="0" y1="65" x2="1400" y2="65" stroke="rgba(255,255,255,0.05)" stroke-dasharray="4"/>
                                    <line x1="0" y1="130" x2="1400" y2="130" stroke="rgba(255,255,255,0.05)" stroke-dasharray="4"/>
                                    <line x1="0" y1="195" x2="1400" y2="195" stroke="rgba(255,255,255,0.05)" stroke-dasharray="4"/>
                                    <path d="M 0,210 Q 300,100 600,190 T 1000,90 T 1400,60" fill="none" stroke="var(--accent)" stroke-width="4"/>
                                    <circle cx="600" cy="190" r="6" fill="#ffffff" stroke="var(--accent)" stroke-width="3"/>
                                    <circle cx="1000" cy="90" r="6" fill="#ffffff" stroke="var(--accent)" stroke-width="3"/>
                                </svg>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="slide-footer" style="width: 100%;">
                    <span>Option B (Rosehot Light) — Live Dashboard Interface</span>
                    <span>Slide 8 of 20</span>
                </div>
            </section>

            <!-- Slide 9: Option B - Poster Section -->
            <section class="slide theme-b" style="--bg-primary: #111111; --text-primary: #f5f5f7; --accent: #df5d4b; padding: 80px 100px; justify-content: center; align-items: center;">
                <div class="bg-photo" style="background-image: url('https://images.unsplash.com/photo-1600585154340-be6161a56a0c?q=80&w=1920'); opacity: 0.15;"></div>
                <div class="bg-overlay"></div>
                
                <div style="background: rgba(17, 17, 17, 0.75); backdrop-filter: blur(24px); border: 1px solid rgba(223,93,75,0.15); border-radius: 32px; padding: 60px 80px; max-width: 900px; text-align: center; z-index: 2; box-shadow: 0 40px 100px rgba(0,0,0,0.6);">
                    <h2 contenteditable="true" style="font-family: 'Rosehot'; font-size: 72px; font-weight: normal; margin: 0 0 24px 0; line-height: 0.95; color: #ffffff; letter-spacing: 0.01em;">
                        Pure Narrative
                    </h2>
                    <p contenteditable="true" style="font-family: 'Outfit'; font-size: 18px; color: rgba(245,245,247,0.7); margin-bottom: 32px; line-height: 1.6; letter-spacing: 0.03em;">
                        Download the case studies and visual layouts, designed for storytellers who seek to balance elegance and technical structure.
                    </p>
                    
                    <div style="display: flex; background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.1); border-radius: 8px; overflow: hidden; width: 100%; max-width: 500px; padding: 4px; margin: 0 auto;">
                        <input type="email" placeholder="Your email" style="flex: 1; border: none; outline: none; background: transparent; padding: 14px 20px; font-family: 'Outfit'; font-size: 16px; color: #ffffff;" readonly>
                        <button style="background: var(--accent); color: #ffffff; border: none; outline: none; padding: 12px 30px; font-family: 'Space Mono', monospace; font-weight: 700; font-size: 13px; border-radius: 6px; cursor: pointer; text-transform: uppercase;">Submit</button>
                    </div>
                </div>

                <div class="slide-footer" style="z-index: 2; width: 100%;">
                    <span>Option B (Rosehot Light) — Creative Poster Layout</span>
                    <span>Slide 9 of 20</span>
                </div>
            </section>

            <!-- Slide 10: Option B - Footer Layout -->
            <section class="slide theme-b" style="--bg-primary: #000000; --text-primary: #ffffff; --accent: #df5d4b; padding: 60px 80px; justify-content: space-between;">
                <!-- Header navigation -->
                <div style="display: flex; justify-content: space-between; align-items: center; width: 100%; z-index: 2;">
                    <span style="font-family: 'Nuqun'; font-size: 24px; font-weight: bold; text-transform: lowercase; letter-spacing: 0.05em;">zorixel</span>
                    <div style="display: flex; gap: 32px; font-family: 'Outfit'; font-size: 14px; color: rgba(255,255,255,0.7);">
                        <span>Products</span>
                        <span>Projects</span>
                        <span>Stores</span>
                        <span>Contact</span>
                        <span style="color: #ffffff; font-weight: bold;">ENG ∨</span>
                    </div>
                </div>

                <!-- Central Massive Logo (Rosehot) -->
                <div style="text-align: center; width: 100%; z-index: 2; margin: 40px 0;">
                    <h1 contenteditable="true" style="font-family: 'Rosehot'; font-size: 260px; font-weight: normal; letter-spacing: -0.01em; margin: 0; line-height: 0.85;">
                        Zorixel
                    </h1>
                    <!-- Dot emblem -->
                    <div style="width: 28px; height: 28px; background: #ffffff; border-radius: 50%; margin: 30px auto 0 auto; box-shadow: 0 0 20px rgba(255,255,255,0.5);"></div>
                </div>

                <!-- Footer details grid -->
                <div style="display: grid; grid-template-columns: 1.5fr 1fr 1.5fr; gap: 40px; width: 100%; z-index: 2; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 30px; text-align: left;">
                    <div style="display: flex; flex-direction: column; justify-content: space-between; height: 120px;">
                        <a href="mailto:hello@zorixel.design" style="color: #ffffff; text-decoration: none; font-family: 'Outfit'; font-size: 16px; border-bottom: 1px solid rgba(255,255,255,0.2); width: fit-content; padding-bottom: 2px;">hello@zorixel.design</a>
                        <div style="display: flex; gap: 12px; margin-top: 12px;">
                            <span style="width: 36px; height: 36px; border-radius: 50%; border: 1px solid rgba(255,255,255,0.2); display: flex; align-items: center; justify-content: center; font-size: 14px;">IG</span>
                            <span style="width: 36px; height: 36px; border-radius: 50%; border: 1px solid rgba(255,255,255,0.2); display: flex; align-items: center; justify-content: center; font-size: 14px;">GH</span>
                        </div>
                        <div style="font-family: 'Outfit'; font-size: 12px; color: rgba(255,255,255,0.4); margin-top: 16px;">
                            2026 zorixel All rights reserved.<br>
                            Terms of Service | Privacy Policy
                        </div>
                    </div>

                    <div style="display: flex; flex-direction: column; gap: 8px; font-family: 'Outfit'; font-size: 15px; color: rgba(255,255,255,0.8);">
                        <span>Home</span>
                        <span>Products</span>
                        <span>Projects</span>
                        <span>Store</span>
                        <span>Contact</span>
                    </div>

                    <div style="font-family: 'Outfit'; font-size: 14px; color: rgba(255,255,255,0.5); line-height: 1.6; display: flex; flex-direction: column; justify-content: flex-start;">
                        <span style="font-weight: 600; color: #ffffff; margin-bottom: 4px;">zorixel office</span>
                        <span>40, Changdeokgung 1-gil,</span>
                        <span>Seoul, Korea</span>
                    </div>
                </div>

                <div class="slide-footer" style="z-index: 2; width: 100%;">
                    <span>Option B (Rosehot Light) — Brand Footer Layout</span>
                    <span>Slide 10 of 20</span>
                </div>
            </section>


            <!-- ===========================================
               OPTION C: VIXA (ORGANIC CREATIVE)
               =========================================== -->

            <!-- Slide 11: Option C - Hero Section -->
            <section class="slide theme-d" style="--bg-primary: #06120e; --text-primary: #ecf4f0; --accent: #7df9be; padding: 80px 100px; justify-content: space-between;">
                <!-- Header nav -->
                <div style="display: flex; justify-content: space-between; align-items: center; width: 100%; z-index: 2;">
                    <span style="font-family: 'Nuqun'; font-size: 32px; font-weight: bold; text-transform: lowercase; letter-spacing: 0.05em; color: #ffffff;">zorixel</span>
                    <div style="display: flex; gap: 32px; font-family: 'Outfit'; font-size: 14px; color: rgba(255,255,255,0.6);">
                        <span>Products</span>
                        <span>Solutions</span>
                        <span>Showcase</span>
                        <span>Contact</span>
                    </div>
                </div>

                <!-- Hero Content -->
                <div style="z-index: 2; text-align: left; max-width: 1200px; margin-top: 40px;">
                    <h1 contenteditable="true" style="font-family: 'Vixa'; font-size: 90px; font-weight: normal; line-height: 0.95; margin: 0 0 24px 0; color: #ffffff; letter-spacing: -0.01em;">
                        Human Creative Systems
                    </h1>
                    <p contenteditable="true" style="font-family: 'Outfit'; font-size: 19px; color: rgba(236,244,240,0.7); margin-bottom: 40px; max-width: 800px; line-height: 1.6; letter-spacing: 0.03em;">
                        A quirky, organic display typeface inspired by Art Nouveau shapes. Designed for indie creators, vibe coders, and organic brands.
                    </p>
                    <div style="display: flex; gap: 16px;">
                        <button style="background: var(--accent); color: #06120e; border: none; padding: 14px 32px; border-radius: 50px; font-family: 'Space Mono', monospace; font-weight: 700; font-size: 13px; cursor: pointer; transition: transform 0.2s;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">Open Library</button>
                        <button style="background: transparent; color: #ffffff; border: 1px solid rgba(255,255,255,0.2); padding: 14px 32px; border-radius: 50px; font-family: 'Space Mono', monospace; font-weight: 700; font-size: 13px; cursor: pointer; transition: transform 0.2s;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">Read Story</button>
                    </div>
                </div>

                <div class="slide-footer" style="z-index: 2; width: 100%;">
                    <span>Option C (Vixa Organic) — Hero Section</span>
                    <span>Slide 11 of 20</span>
                </div>
            </section>

            <!-- Slide 12: Option C - About & Contact -->
            <section class="slide theme-d" style="--bg-primary: #06120e; --text-primary: #ecf4f0; --accent: #7df9be; padding: 80px 100px; justify-content: flex-start;">
                <!-- Header nav -->
                <div style="display: flex; justify-content: space-between; align-items: center; width: 100%; border-bottom: 1px solid rgba(255,255,255,0.08); padding-bottom: 16px; margin-bottom: 40px;">
                    <span style="font-family: 'Nuqun'; font-size: 24px; font-weight: bold; text-transform: lowercase; letter-spacing: 0.05em; color: #ffffff;">zorixel</span>
                    <span style="font-family: 'Space Mono', monospace; font-size: 12px; color: rgba(255,255,255,0.4);">Brand Showcase</span>
                </div>

                <div class="split-grid">
                    <!-- Left: About text -->
                    <div style="display: flex; flex-direction: column; gap: 24px; text-align: left;">
                        <h2 contenteditable="true" style="font-family: 'Vixa'; font-size: 54px; font-weight: normal; margin: 0; line-height: 1.0; color: #ffffff;">
                            Creative Intuition
                        </h2>
                        <p contenteditable="true" style="font-family: 'Outfit'; font-size: 18px; color: rgba(236,244,240,0.75); margin: 0; line-height: 1.7; letter-spacing: 0.03em;">
                            Unusual terminal shapes and organic character strokes express design intuition, avoiding standard corporate layouts. Pairing these Display forms with extremely clean body copy lets details shine while keeping copy readable.
                        </p>
                    </div>

                    <!-- Right: Contact form -->
                    <div style="background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.06); border-radius: 20px; padding: 40px; display: flex; flex-direction: column; gap: 20px; text-align: left;">
                        <h3 contenteditable="true" style="font-family: 'Vixa'; font-size: 32px; font-weight: normal; margin: 0; color: #ffffff;">
                            Say Hello
                        </h3>
                        <div class="form-field">
                            <label>Your Name</label>
                            <input type="text" placeholder="e.g. Atinek Maurya" readonly>
                        </div>
                        <div class="form-field">
                            <label>Email Address</label>
                            <input type="email" placeholder="e.g. hello@zorixel.design" readonly>
                        </div>
                        <button style="background: var(--accent); color: #06120e; border: none; padding: 14px; border-radius: 8px; font-family: 'Space Mono', monospace; font-weight: 700; font-size: 13px; cursor: pointer; text-transform: uppercase; margin-top: 10px;">Send Message</button>
                    </div>
                </div>

                <div class="slide-footer" style="border-top: 1px solid rgba(255,255,255,0.08); padding-top: 16px; margin-top: auto; width: 100%;">
                    <span>Option C (Vixa Organic) — About &amp; Contact</span>
                    <span>Slide 12 of 20</span>
                </div>
            </section>

            <!-- Slide 13: Option C - Dashboard Page -->
            <section class="slide theme-d" style="--bg-primary: #06120e; --text-primary: #ecf4f0; --accent: #7df9be; padding: 60px 80px; justify-content: space-between;">
                <!-- Grid Dashboard wrapper -->
                <div class="grid-dashboard" style="background: rgba(255,255,255,0.01); border-color: rgba(255,255,255,0.06);">
                    <!-- Sidebar -->
                    <div class="db-sidebar" style="border-color: rgba(255,255,255,0.04);">
                        <span style="font-family: 'Nuqun'; font-size: 24px; font-weight: bold; text-transform: lowercase; letter-spacing: 0.05em; color: #ffffff;">zorixel</span>
                        <div style="display: flex; flex-direction: column; gap: 8px; margin-top: 20px;">
                            <div class="db-menu-item active-item">Library</div>
                            <div class="db-menu-item">Analytics</div>
                            <div class="db-menu-item">Submissions</div>
                            <div class="db-menu-item">Settings</div>
                        </div>
                    </div>

                    <!-- Content -->
                    <div class="db-content">
                        <!-- Stats Row -->
                        <div class="db-stats-row">
                            <div class="db-card">
                                <span class="db-card-label">active creators</span>
                                <span class="db-card-value" contenteditable="true">45,902</span>
                            </div>
                            <div class="db-card">
                                <span class="db-card-label">curated items</span>
                                <span class="db-card-value" contenteditable="true">1,284</span>
                            </div>
                            <div class="db-card">
                                <span class="db-card-label">brand score</span>
                                <span class="db-card-value" contenteditable="true">9.8 / 10</span>
                            </div>
                        </div>

                        <!-- Panel with chart SVG -->
                        <div style="flex-grow: 1; border: 1px solid rgba(255,255,255,0.06); border-radius: 16px; padding: 24px; display: flex; flex-direction: column; justify-content: space-between; position: relative; background: rgba(0,0,0,0.15);">
                            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
                                <span style="font-family: 'Space Mono', monospace; font-size: 12px; color: rgba(255,255,255,0.4); text-transform: uppercase;">Creator Volume Growth</span>
                                <span style="font-family: 'Space Mono', monospace; font-size: 12px; color: var(--accent);">Creative Analytics</span>
                            </div>
                            
                            <!-- SVG Chart -->
                            <div style="width: 100%; height: 260px;">
                                <svg viewBox="0 0 1400 260" style="width: 100%; height: 100%; overflow: visible;">
                                    <defs>
                                        <linearGradient id="gradient-vixa-organic" x1="0" y1="0" x2="0" y2="1">
                                            <stop offset="0%" stop-color="var(--accent)" stop-opacity="0.25"/>
                                            <stop offset="100%" stop-color="var(--accent)" stop-opacity="0.00"/>
                                        </linearGradient>
                                    </defs>
                                    <path d="M 0,260 L 0,200 Q 300,220 600,140 T 1000,70 T 1400,40 L 1400,260 Z" fill="url(#gradient-vixa-organic)"/>
                                    <line x1="0" y1="65" x2="1400" y2="65" stroke="rgba(255,255,255,0.05)" stroke-dasharray="4"/>
                                    <line x1="0" y1="130" x2="1400" y2="130" stroke="rgba(255,255,255,0.05)" stroke-dasharray="4"/>
                                    <line x1="0" y1="195" x2="1400" y2="195" stroke="rgba(255,255,255,0.05)" stroke-dasharray="4"/>
                                    <path d="M 0,200 Q 300,220 600,140 T 1000,70 T 1400,40" fill="none" stroke="var(--accent)" stroke-width="4"/>
                                    <circle cx="600" cy="140" r="6" fill="#ffffff" stroke="var(--accent)" stroke-width="3"/>
                                    <circle cx="1000" cy="70" r="6" fill="#ffffff" stroke="var(--accent)" stroke-width="3"/>
                                </svg>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="slide-footer" style="width: 100%;">
                    <span>Option C (Vixa Organic) — Live Dashboard Interface</span>
                    <span>Slide 13 of 20</span>
                </div>
            </section>

            <!-- Slide 14: Option C - Poster Section -->
            <section class="slide theme-d" style="--bg-primary: #06120e; --text-primary: #ecf4f0; --accent: #7df9be; padding: 80px 100px; justify-content: center; align-items: center;">
                <div class="bg-photo" style="background-image: url('https://images.unsplash.com/photo-1542273917363-3b1817f69a2d?q=80&w=1920'); opacity: 0.22;"></div>
                <div class="bg-overlay"></div>
                
                <div style="background: rgba(6, 18, 14, 0.75); backdrop-filter: blur(24px); border: 1px solid rgba(125,249,190,0.15); border-radius: 32px; padding: 60px 80px; max-width: 900px; text-align: center; z-index: 2; box-shadow: 0 40px 100px rgba(0,0,0,0.6);">
                    <h2 contenteditable="true" style="font-family: 'Vixa'; font-size: 72px; font-weight: normal; margin: 0 0 24px 0; line-height: 0.95; color: #ffffff;">
                        Organic Flow
                    </h2>
                    <p contenteditable="true" style="font-family: 'Outfit'; font-size: 18px; color: rgba(236,244,240,0.7); margin-bottom: 32px; line-height: 1.6; letter-spacing: 0.03em;">
                        Download the case studies and visual layouts, designed for storytellers who seek to balance elegance and technical structure.
                    </p>
                    
                    <div style="display: flex; background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.1); border-radius: 8px; overflow: hidden; width: 100%; max-width: 500px; padding: 4px; margin: 0 auto;">
                        <input type="email" placeholder="Your email" style="flex: 1; border: none; outline: none; background: transparent; padding: 14px 20px; font-family: 'Outfit'; font-size: 16px; color: #ffffff;" readonly>
                        <button style="background: var(--accent); color: #06120e; border: none; outline: none; padding: 12px 30px; font-family: 'Space Mono', monospace; font-weight: 700; font-size: 13px; border-radius: 6px; cursor: pointer; text-transform: uppercase;">Submit</button>
                    </div>
                </div>

                <div class="slide-footer" style="z-index: 2; width: 100%;">
                    <span>Option C (Vixa Organic) — Creative Poster Layout</span>
                    <span>Slide 14 of 20</span>
                </div>
            </section>

            <!-- Slide 15: Option C - Footer Layout -->
            <section class="slide theme-d" style="--bg-primary: #000000; --text-primary: #ffffff; --accent: #7df9be; padding: 60px 80px; justify-content: space-between;">
                <!-- Header navigation -->
                <div style="display: flex; justify-content: space-between; align-items: center; width: 100%; z-index: 2;">
                    <span style="font-family: 'Nuqun'; font-size: 24px; font-weight: bold; text-transform: lowercase; letter-spacing: 0.05em;">zorixel</span>
                    <div style="display: flex; gap: 32px; font-family: 'Outfit'; font-size: 14px; color: rgba(255,255,255,0.7);">
                        <span>Products</span>
                        <span>Projects</span>
                        <span>Stores</span>
                        <span>Contact</span>
                        <span style="color: #ffffff; font-weight: bold;">ENG ∨</span>
                    </div>
                </div>

                <!-- Central Massive Logo (Vixa) -->
                <div style="text-align: center; width: 100%; z-index: 2; margin: 40px 0;">
                    <h1 contenteditable="true" style="font-family: 'Vixa'; font-size: 240px; font-weight: normal; letter-spacing: -0.01em; margin: 0; line-height: 0.85;">
                        Zorixel
                    </h1>
                    <!-- Dot emblem -->
                    <div style="width: 28px; height: 28px; background: #ffffff; border-radius: 50%; margin: 30px auto 0 auto; box-shadow: 0 0 20px rgba(255,255,255,0.5);"></div>
                </div>

                <!-- Footer details grid -->
                <div style="display: grid; grid-template-columns: 1.5fr 1fr 1.5fr; gap: 40px; width: 100%; z-index: 2; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 30px; text-align: left;">
                    <div style="display: flex; flex-direction: column; justify-content: space-between; height: 120px;">
                        <a href="mailto:hello@zorixel.design" style="color: #ffffff; text-decoration: none; font-family: 'Outfit'; font-size: 16px; border-bottom: 1px solid rgba(255,255,255,0.2); width: fit-content; padding-bottom: 2px;">hello@zorixel.design</a>
                        <div style="display: flex; gap: 12px; margin-top: 12px;">
                            <span style="width: 36px; height: 36px; border-radius: 50%; border: 1px solid rgba(255,255,255,0.2); display: flex; align-items: center; justify-content: center; font-size: 14px;">IG</span>
                            <span style="width: 36px; height: 36px; border-radius: 50%; border: 1px solid rgba(255,255,255,0.2); display: flex; align-items: center; justify-content: center; font-size: 14px;">GH</span>
                        </div>
                        <div style="font-family: 'Outfit'; font-size: 12px; color: rgba(255,255,255,0.4); margin-top: 16px;">
                            2026 zorixel All rights reserved.<br>
                            Terms of Service | Privacy Policy
                        </div>
                    </div>

                    <div style="display: flex; flex-direction: column; gap: 8px; font-family: 'Outfit'; font-size: 15px; color: rgba(255,255,255,0.8);">
                        <span>Home</span>
                        <span>Products</span>
                        <span>Projects</span>
                        <span>Store</span>
                        <span>Contact</span>
                    </div>

                    <div style="font-family: 'Outfit'; font-size: 14px; color: rgba(255,255,255,0.5); line-height: 1.6; display: flex; flex-direction: column; justify-content: flex-start;">
                        <span style="font-weight: 600; color: #ffffff; margin-bottom: 4px;">zorixel office</span>
                        <span>40, Changdeokgung 1-gil,</span>
                        <span>Seoul, Korea</span>
                    </div>
                </div>

                <div class="slide-footer" style="z-index: 2; width: 100%;">
                    <span>Option C (Vixa Organic) — Brand Footer Layout</span>
                    <span>Slide 15 of 20</span>
                </div>
            </section>


            <!-- ===========================================
               OPTION D: VIXA (MIDNIGHT CREATIVE)
               =========================================== -->

            <!-- Slide 16: Option D - Hero Section -->
            <section class="slide theme-d" style="--bg-primary: #000000; --text-primary: #ffffff; --accent: #ff5500; padding: 80px 100px; justify-content: space-between;">
                <!-- Header nav -->
                <div style="display: flex; justify-content: space-between; align-items: center; width: 100%; z-index: 2;">
                    <span style="font-family: 'Nuqun'; font-size: 32px; font-weight: bold; text-transform: lowercase; letter-spacing: 0.05em; color: #ffffff;">zorixel</span>
                    <div style="display: flex; gap: 32px; font-family: 'Outfit'; font-size: 14px; color: rgba(255,255,255,0.6);">
                        <span>Products</span>
                        <span>Solutions</span>
                        <span>Showcase</span>
                        <span>Contact</span>
                    </div>
                </div>

                <!-- Hero Content -->
                <div style="z-index: 2; text-align: left; max-width: 1200px; margin-top: 40px;">
                    <h1 contenteditable="true" style="font-family: 'Vixa'; font-size: 90px; font-weight: normal; line-height: 0.95; margin: 0 0 24px 0; color: #ffffff; letter-spacing: -0.01em;">
                        Organic Flow Systems
                    </h1>
                    <p contenteditable="true" style="font-family: 'Outfit'; font-size: 19px; color: rgba(255,255,255,0.7); margin-bottom: 40px; max-width: 800px; line-height: 1.6; letter-spacing: 0.03em;">
                        Unusual terminal shapes and organic character strokes express design intuition, avoiding standard corporate layouts to stand out.
                    </p>
                    <div style="display: flex; gap: 16px;">
                        <button style="background: var(--accent); color: #ffffff; border: none; padding: 14px 32px; border-radius: 50px; font-family: 'Space Mono', monospace; font-weight: 700; font-size: 13px; cursor: pointer; transition: transform 0.2s;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">Open Library</button>
                        <button style="background: transparent; color: #ffffff; border: 1px solid rgba(255,255,255,0.2); padding: 14px 32px; border-radius: 50px; font-family: 'Space Mono', monospace; font-weight: 700; font-size: 13px; cursor: pointer; transition: transform 0.2s;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">Read Story</button>
                    </div>
                </div>

                <div class="slide-footer" style="z-index: 2; width: 100%;">
                    <span>Option D (Vixa Midnight) — Hero Section</span>
                    <span>Slide 16 of 20</span>
                </div>
            </section>

            <!-- Slide 17: Option D - About & Contact -->
            <section class="slide theme-d" style="--bg-primary: #000000; --text-primary: #ffffff; --accent: #ff5500; padding: 80px 100px; justify-content: flex-start;">
                <!-- Header nav -->
                <div style="display: flex; justify-content: space-between; align-items: center; width: 100%; border-bottom: 1px solid rgba(255,255,255,0.08); padding-bottom: 16px; margin-bottom: 40px;">
                    <span style="font-family: 'Nuqun'; font-size: 24px; font-weight: bold; text-transform: lowercase; letter-spacing: 0.05em; color: #ffffff;">zorixel</span>
                    <span style="font-family: 'Space Mono', monospace; font-size: 12px; color: rgba(255,255,255,0.4);">Brand Showcase</span>
                </div>

                <div class="split-grid">
                    <!-- Left: About text -->
                    <div style="display: flex; flex-direction: column; gap: 24px; text-align: left;">
                        <h2 contenteditable="true" style="font-family: 'Vixa'; font-size: 54px; font-weight: normal; margin: 0; line-height: 1.0; color: #ffffff;">
                            Design Experience
                        </h2>
                        <p contenteditable="true" style="font-family: 'Outfit'; font-size: 18px; color: rgba(255,255,255,0.75); margin: 0; line-height: 1.7; letter-spacing: 0.03em;">
                            Unusual terminal shapes and organic character strokes express design intuition, avoiding standard corporate layouts. Pairing these Display forms with extremely clean body copy lets details shine while keeping copy readable.
                        </p>
                    </div>

                    <!-- Right: Contact form -->
                    <div style="background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.06); border-radius: 20px; padding: 40px; display: flex; flex-direction: column; gap: 20px; text-align: left;">
                        <h3 contenteditable="true" style="font-family: 'Vixa'; font-size: 32px; font-weight: normal; margin: 0; color: #ffffff;">
                            Join the Network
                        </h3>
                        <div class="form-field">
                            <label>Your Name</label>
                            <input type="text" placeholder="e.g. Atinek Maurya" readonly>
                        </div>
                        <div class="form-field">
                            <label>Email Address</label>
                            <input type="email" placeholder="e.g. hello@zorixel.design" readonly>
                        </div>
                        <button style="background: var(--accent); color: #ffffff; border: none; padding: 14px; border-radius: 8px; font-family: 'Space Mono', monospace; font-weight: 700; font-size: 13px; cursor: pointer; text-transform: uppercase; margin-top: 10px;">Send Message</button>
                    </div>
                </div>

                <div class="slide-footer" style="border-top: 1px solid rgba(255,255,255,0.08); padding-top: 16px; margin-top: auto; width: 100%;">
                    <span>Option D (Vixa Midnight) — About &amp; Contact</span>
                    <span>Slide 17 of 20</span>
                </div>
            </section>

            <!-- Slide 18: Option D - Dashboard Page -->
            <section class="slide theme-d" style="--bg-primary: #000000; --text-primary: #ffffff; --accent: #ff5500; padding: 60px 80px; justify-content: space-between;">
                <!-- Grid Dashboard wrapper -->
                <div class="grid-dashboard" style="background: rgba(255,255,255,0.01); border-color: rgba(255,255,255,0.06);">
                    <!-- Sidebar -->
                    <div class="db-sidebar" style="border-color: rgba(255,255,255,0.04);">
                        <span style="font-family: 'Nuqun'; font-size: 24px; font-weight: bold; text-transform: lowercase; letter-spacing: 0.05em; color: #ffffff;">zorixel</span>
                        <div style="display: flex; flex-direction: column; gap: 8px; margin-top: 20px;">
                            <div class="db-menu-item active-item">Library</div>
                            <div class="db-menu-item">Analytics</div>
                            <div class="db-menu-item">Submissions</div>
                            <div class="db-menu-item">Settings</div>
                        </div>
                    </div>

                    <!-- Content -->
                    <div class="db-content">
                        <!-- Stats Row -->
                        <div class="db-stats-row">
                            <div class="db-card">
                                <span class="db-card-label">active creators</span>
                                <span class="db-card-value" contenteditable="true">45,902</span>
                            </div>
                            <div class="db-card">
                                <span class="db-card-label">curated items</span>
                                <span class="db-card-value" contenteditable="true">1,284</span>
                            </div>
                            <div class="db-card">
                                <span class="db-card-label">brand score</span>
                                <span class="db-card-value" contenteditable="true">9.8 / 10</span>
                            </div>
                        </div>

                        <!-- Panel with chart SVG -->
                        <div style="flex-grow: 1; border: 1px solid rgba(255,255,255,0.06); border-radius: 16px; padding: 24px; display: flex; flex-direction: column; justify-content: space-between; position: relative; background: rgba(0,0,0,0.15);">
                            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
                                <span style="font-family: 'Space Mono', monospace; font-size: 12px; color: rgba(255,255,255,0.4); text-transform: uppercase;">Creator Volume Growth</span>
                                <span style="font-family: 'Space Mono', monospace; font-size: 12px; color: var(--accent);">Creative Analytics</span>
                            </div>
                            
                            <!-- SVG Chart -->
                            <div style="width: 100%; height: 260px;">
                                <svg viewBox="0 0 1400 260" style="width: 100%; height: 100%; overflow: visible;">
                                    <defs>
                                        <linearGradient id="gradient-vixa-midnight" x1="0" y1="0" x2="0" y2="1">
                                            <stop offset="0%" stop-color="var(--accent)" stop-opacity="0.25"/>
                                            <stop offset="100%" stop-color="var(--accent)" stop-opacity="0.00"/>
                                        </linearGradient>
                                    </defs>
                                    <path d="M 0,260 L 0,200 Q 300,220 600,140 T 1000,70 T 1400,40 L 1400,260 Z" fill="url(#gradient-vixa-midnight)"/>
                                    <line x1="0" y1="65" x2="1400" y2="65" stroke="rgba(255,255,255,0.05)" stroke-dasharray="4"/>
                                    <line x1="0" y1="130" x2="1400" y2="130" stroke="rgba(255,255,255,0.05)" stroke-dasharray="4"/>
                                    <line x1="0" y1="195" x2="1400" y2="195" stroke="rgba(255,255,255,0.05)" stroke-dasharray="4"/>
                                    <path d="M 0,200 Q 300,220 600,140 T 1000,70 T 1400,40" fill="none" stroke="var(--accent)" stroke-width="4"/>
                                    <circle cx="600" cy="140" r="6" fill="#ffffff" stroke="var(--accent)" stroke-width="3"/>
                                    <circle cx="1000" cy="70" r="6" fill="#ffffff" stroke="var(--accent)" stroke-width="3"/>
                                </svg>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="slide-footer" style="width: 100%;">
                    <span>Option D (Vixa Midnight) — Live Dashboard Interface</span>
                    <span>Slide 18 of 20</span>
                </div>
            </section>

            <!-- Slide 19: Option D - Poster Section -->
            <section class="slide theme-d" style="--bg-primary: #000000; --text-primary: #ffffff; --accent: #ff5500; padding: 80px 100px; justify-content: center; align-items: center;">
                <div class="bg-photo" style="background-image: url('https://images.unsplash.com/photo-1549490349-8643362247b5?q=80&w=1920'); opacity: 0.15;"></div>
                <div class="bg-overlay"></div>
                
                <div style="background: rgba(0, 0, 0, 0.8); backdrop-filter: blur(24px); border: 1px solid rgba(255,85,0,0.15); border-radius: 32px; padding: 60px 80px; max-width: 900px; text-align: center; z-index: 2; box-shadow: 0 40px 100px rgba(0,0,0,0.6);">
                    <h2 contenteditable="true" style="font-family: 'Vixa'; font-size: 72px; font-weight: normal; margin: 0 0 24px 0; line-height: 0.95; color: #ffffff;">
                        Break Rules
                    </h2>
                    <p contenteditable="true" style="font-family: 'Outfit'; font-size: 18px; color: rgba(255,255,255,0.7); margin-bottom: 32px; line-height: 1.6; letter-spacing: 0.03em;">
                        Unlock the viral carousels pack and Figma content blocks, optimized to maximize feed engagement.
                    </p>
                    
                    <div style="display: flex; background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.1); border-radius: 8px; overflow: hidden; width: 100%; max-width: 500px; padding: 4px; margin: 0 auto;">
                        <input type="email" placeholder="Your email" style="flex: 1; border: none; outline: none; background: transparent; padding: 14px 20px; font-family: 'Outfit'; font-size: 16px; color: #ffffff;" readonly>
                        <button style="background: var(--accent); color: #ffffff; border: none; outline: none; padding: 12px 30px; font-family: 'Space Mono', monospace; font-weight: 700; font-size: 13px; border-radius: 6px; cursor: pointer; text-transform: uppercase;">Submit</button>
                    </div>
                </div>

                <div class="slide-footer" style="z-index: 2; width: 100%;">
                    <span>Option D (Vixa Midnight) — Creative Poster Layout</span>
                    <span>Slide 19 of 20</span>
                </div>
            </section>

            <!-- Slide 20: Option D - Footer Layout -->
            <section class="slide theme-d" style="--bg-primary: #000000; --text-primary: #ffffff; --accent: #ff5500; padding: 60px 80px; justify-content: space-between;">
                <!-- Header navigation -->
                <div style="display: flex; justify-content: space-between; align-items: center; width: 100%; z-index: 2;">
                    <span style="font-family: 'Nuqun'; font-size: 24px; font-weight: bold; text-transform: lowercase; letter-spacing: 0.05em;">zorixel</span>
                    <div style="display: flex; gap: 32px; font-family: 'Outfit'; font-size: 14px; color: rgba(255,255,255,0.7);">
                        <span>Products</span>
                        <span>Projects</span>
                        <span>Stores</span>
                        <span>Contact</span>
                        <span style="color: #ffffff; font-weight: bold;">ENG ∨</span>
                    </div>
                </div>

                <!-- Central Massive Logo (Vixa) -->
                <div style="text-align: center; width: 100%; z-index: 2; margin: 40px 0;">
                    <h1 contenteditable="true" style="font-family: 'Vixa'; font-size: 240px; font-weight: normal; letter-spacing: -0.01em; margin: 0; line-height: 0.85;">
                        Zorixel
                    </h1>
                    <!-- Dot emblem -->
                    <div style="width: 28px; height: 28px; background: #ffffff; border-radius: 50%; margin: 30px auto 0 auto; box-shadow: 0 0 20px rgba(255,255,255,0.5);"></div>
                </div>

                <!-- Footer details grid -->
                <div style="display: grid; grid-template-columns: 1.5fr 1fr 1.5fr; gap: 40px; width: 100%; z-index: 2; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 30px; text-align: left;">
                    <div style="display: flex; flex-direction: column; justify-content: space-between; height: 120px;">
                        <a href="mailto:hello@zorixel.design" style="color: #ffffff; text-decoration: none; font-family: 'Outfit'; font-size: 16px; border-bottom: 1px solid rgba(255,255,255,0.2); width: fit-content; padding-bottom: 2px;">hello@zorixel.design</a>
                        <div style="display: flex; gap: 12px; margin-top: 12px;">
                            <span style="width: 36px; height: 36px; border-radius: 50%; border: 1px solid rgba(255,255,255,0.2); display: flex; align-items: center; justify-content: center; font-size: 14px;">IG</span>
                            <span style="width: 36px; height: 36px; border-radius: 50%; border: 1px solid rgba(255,255,255,0.2); display: flex; align-items: center; justify-content: center; font-size: 14px;">GH</span>
                        </div>
                        <div style="font-family: 'Outfit'; font-size: 12px; color: rgba(255,255,255,0.4); margin-top: 16px;">
                            2026 zorixel All rights reserved.<br>
                            Terms of Service | Privacy Policy
                        </div>
                    </div>

                    <div style="display: flex; flex-direction: column; gap: 8px; font-family: 'Outfit'; font-size: 15px; color: rgba(255,255,255,0.8);">
                        <span>Home</span>
                        <span>Products</span>
                        <span>Projects</span>
                        <span>Store</span>
                        <span>Contact</span>
                    </div>

                    <div style="font-family: 'Outfit'; font-size: 14px; color: rgba(255,255,255,0.5); line-height: 1.6; display: flex; flex-direction: column; justify-content: flex-start;">
                        <span style="font-weight: 600; color: #ffffff; margin-bottom: 4px;">zorixel office</span>
                        <span>40, Changdeokgung 1-gil,</span>
                        <span>Seoul, Korea</span>
                    </div>
                </div>

                <div class="slide-footer" style="z-index: 2; width: 100%;">
                    <span>Option D (Vixa Midnight) — Brand Footer Layout</span>
                    <span>Slide 20 of 20</span>
                </div>
            </section>

        </main>
    </div>

    <!-- PRESENTATION CHROME DOCK CONTROLS -->
    <div class="deck-controls" style="display: flex; flex-direction: column; gap: 12px; bottom: 30px; right: 40px; background: rgba(15, 15, 25, 0.85); padding: 16px 24px; border-radius: 20px; border: 1px solid rgba(255,255,255,0.1);">
        <div style="display: flex; align-items: center; justify-content: space-between; gap: 20px; width: 100%;">
            <div style="display: flex; gap: 10px;">
                <button class="btn-nav" onclick="presentation.prevSlide()">← Prev</button>
                <button class="btn-nav" onclick="presentation.nextSlide()">Next →</button>
            </div>
            <span class="slide-counter" id="slideCounter">1 / 20</span>
        </div>
    </div>

    <!-- QUICK ROUTE JUMP LINKS -->
    <div class="route-jumps" style="display: flex; flex-direction: column; gap: 10px; bottom: 30px; left: 40px; background: rgba(15, 15, 25, 0.85); padding: 16px 24px; border-radius: 20px; border: 1px solid rgba(255,255,255,0.1); width: 620px;">
        <!-- Row 1: Font Options -->
        <div style="display: flex; gap: 8px; width: 100%; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 10px;">
            <span style="font-family: 'Space Mono', monospace; font-size: 11px; color: rgba(255,255,255,0.4); text-transform: uppercase; letter-spacing: 0.1em; line-height: 28px; width: 80px;">FONTS:</span>
            <button class="btn-jump active-route" id="jump-opt-0" onclick="presentation.setOption(0)" style="font-size: 11px;">A: Rosehot (Dark)</button>
            <button class="btn-jump" id="jump-opt-1" onclick="presentation.setOption(1)" style="font-size: 11px;">B: Rosehot (Light)</button>
            <button class="btn-jump" id="jump-opt-2" onclick="presentation.setOption(2)" style="font-size: 11px;">C: Vixa (Organic)</button>
            <button class="btn-jump" id="jump-opt-3" onclick="presentation.setOption(3)" style="font-size: 11px;">D: Vixa (Midnight)</button>
        </div>
        <!-- Row 2: Page Sections -->
        <div style="display: flex; gap: 8px; width: 100%;">
            <span style="font-family: 'Space Mono', monospace; font-size: 11px; color: rgba(255,255,255,0.4); text-transform: uppercase; letter-spacing: 0.1em; line-height: 28px; width: 80px;">PAGES:</span>
            <button class="btn-jump active-route" id="jump-page-0" onclick="presentation.setPage(0)" style="font-size: 11px;">1. Hero</button>
            <button class="btn-jump" id="jump-page-1" onclick="presentation.setPage(1)" style="font-size: 11px;">2. About</button>
            <button class="btn-jump" id="jump-page-2" onclick="presentation.setPage(2)" style="font-size: 11px;">3. Dash</button>
            <button class="btn-jump" id="jump-page-3" onclick="presentation.setPage(3)" style="font-size: 11px;">4. Poster</button>
            <button class="btn-jump" id="jump-page-4" onclick="presentation.setPage(4)" style="font-size: 11px;">5. Footer</button>
        </div>
    </div>

    <!-- INLINE EDITOR HOVER REGIONS -->
    <div class="edit-hotzone"></div>
    <button class="edit-toggle" id="editToggle" title="Toggle edit mode (E)">✏️</button>
"""

# Rebuild JavaScript Presentation controller code
new_js_code = """
    <!-- ===========================================
       PRESENTATION & EDITOR CONTROLLER SCRIPTS
       =========================================== -->
    <script>
        class SlidePresentation {
            constructor() {
                this.slides = document.querySelectorAll('.slide');
                this.currentSlide = 0;
                this.currentOption = 0;
                this.currentPage = 0;
                this.stage = document.getElementById('deckStage');
                this.counterEl = document.getElementById('slideCounter');
                
                this.setupStageScale();
                this.setupKeyboardNav();
                this.setupTouchNav();
                this.updateRouteNavHighlight();
            }

            setOption(optIndex) {
                this.currentOption = optIndex;
                this.showSlide(this.currentOption * 5 + this.currentPage);
            }

            setPage(pageIndex) {
                this.currentPage = pageIndex;
                this.showSlide(this.currentOption * 5 + this.currentPage);
            }

            setupStageScale() {
                const scale = () => {
                    const factor = Math.min(window.innerWidth / 1920, window.innerHeight / 1080);
                    const x = (window.innerWidth - 1920 * factor) / 2;
                    const y = (window.innerHeight - 1080 * factor) / 2;
                    this.stage.style.transform = `translate(${x}px, ${y}px) scale(${factor})`;
                };
                scale();
                window.addEventListener('resize', scale);
            }

            setupKeyboardNav() {
                document.addEventListener('keydown', (e) => {
                    if (e.target.getAttribute('contenteditable') === 'true') return;

                    if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'PageDown') {
                        this.nextSlide();
                    } else if (e.key === 'ArrowLeft' || e.key === 'PageUp') {
                        this.prevSlide();
                    }
                });
            }

            setupTouchNav() {
                let startX = 0;
                document.addEventListener('touchstart', (e) => {
                    startX = e.touches[0].clientX;
                }, {passive: true});

                document.addEventListener('touchend', (e) => {
                    let endX = e.changedTouches[0].clientX;
                    let diffX = startX - endX;
                    if (Math.abs(diffX) > 80) {
                        if (diffX > 0) {
                            this.nextSlide();
                        } else {
                            this.prevSlide();
                        }
                    }
                }, {passive: true});
            }

            showSlide(index) {
                this.currentSlide = Math.max(0, Math.min(index, this.slides.length - 1));
                
                this.currentOption = Math.floor(this.currentSlide / 5);
                this.currentPage = this.currentSlide % 5;

                this.slides.forEach((slide, i) => {
                    slide.classList.toggle('active', i === this.currentSlide);
                });
                
                this.counterEl.innerText = `${this.currentSlide + 1} / ${this.slides.length}`;
                this.updateRouteNavHighlight();
            }

            nextSlide() {
                if (this.currentSlide < this.slides.length - 1) {
                    this.showSlide(this.currentSlide + 1);
                }
            }

            prevSlide() {
                if (this.currentSlide > 0) {
                    this.showSlide(this.currentSlide - 1);
                }
            }

            updateRouteNavHighlight() {
                document.querySelectorAll('.btn-jump').forEach(btn => btn.classList.remove('active-route'));
                
                const optBtn = document.getElementById(`jump-opt-${this.currentOption}`);
                if (optBtn) optBtn.classList.add('active-route');

                const pageBtn = document.getElementById(`jump-page-${this.currentPage}`);
                if (pageBtn) pageBtn.classList.add('active-route');
            }
        }

        const presentation = new SlidePresentation();

        /* ===========================================
           INLINE EDITING SYSTEM
           =========================================== */
        class InlineEditor {
            constructor() {
                this.isActive = false;
                this.toggleBtn = document.getElementById('editToggle');
                this.hotzone = document.querySelector('.edit-hotzone');
                
                this.setupHotzoneHover();
                this.setupToggleClick();
                this.setupKeyboardShortcut();
                this.loadSavedContent();
            }

            toggleEditMode() {
                this.isActive = !this.isActive;
                this.toggleBtn.classList.toggle('active', this.isActive);
                
                const editables = document.querySelectorAll('[contenteditable]');
                editables.forEach(el => {
                    el.setAttribute('contenteditable', this.isActive ? 'true' : 'false');
                });

                if (!this.isActive) {
                    this.saveContent();
                }
            }

            setupHotzoneHover() {
                let hideTimeout = null;
                this.hotzone.addEventListener('mouseenter', () => {
                    clearTimeout(hideTimeout);
                    this.toggleBtn.classList.add('show');
                });
                this.hotzone.addEventListener('mouseleave', () => {
                    hideTimeout = setTimeout(() => {
                        if (!this.isActive) this.toggleBtn.classList.remove('show');
                    }, 400);
                });
                this.toggleBtn.addEventListener('mouseenter', () => {
                    clearTimeout(hideTimeout);
                });
                this.toggleBtn.addEventListener('mouseleave', () => {
                    hideTimeout = setTimeout(() => {
                        if (!this.isActive) this.toggleBtn.classList.remove('show');
                    }, 400);
                });
                this.hotzone.addEventListener('click', () => {
                    this.toggleEditMode();
                });
            }

            setupToggleClick() {
                this.toggleBtn.addEventListener('click', () => {
                    this.toggleEditMode();
                });
            }

            setupKeyboardShortcut() {
                document.addEventListener('keydown', (e) => {
                    if ((e.key === 'e' || e.key === 'E') && e.target.getAttribute('contenteditable') !== 'true') {
                        e.preventDefault();
                        this.toggleEditMode();
                    }
                });
            }

            saveContent() {
                const editables = document.querySelectorAll('[contenteditable]');
                const data = {};
                editables.forEach((el, index) => {
                    data[index] = el.innerHTML;
                });
                localStorage.setItem('zorixel_slide_content', JSON.stringify(data));
            }

            loadSavedContent() {
                const raw = localStorage.getItem('zorixel_slide_content');
                if (raw) {
                    try {
                        const data = JSON.parse(raw);
                        const editables = document.querySelectorAll('[contenteditable]');
                        editables.forEach((el, index) => {
                            if (data[index] !== undefined) {
                                el.innerHTML = data[index];
                            }
                        });
                    } catch(e) {
                        console.error('Error loading local slide content', e);
                    }
                }
            }
        }

        const editor = new InlineEditor();
    </script>
</body>
</html>
"""

# Assemble new presentation contents
full_html = head_html + custom_styles + "</style>\\n</head>\\n" + new_deck_html + new_js_code

with open(fpath, "w", encoding="utf-8") as f:
    f.write(full_html)

print("Rebuilt presentation.html with 20 slides featuring Rosehot and Vixa in multiple themes!")
