# -*- coding: utf-8 -*-
import re

fpath = "projects/font-showcase/presentation.html"
with open(fpath, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Replace the entire <main class="deck-stage" id="deckStage"> ... </main> block and jumps
start_idx = html.find('<main class="deck-stage" id="deckStage">')
end_idx = html.find('<!-- INLINE EDITOR HOVER REGIONS -->')

if start_idx == -1 or end_idx == -1:
    print("Error: Could not find target markers in HTML!")
    exit(1)

new_deck = """<main class="deck-stage" id="deckStage">

            <!-- Slide 1: Deck Title (Screenshot 3 Cover Style) -->
            <section class="slide theme-c active" style="--bg-primary: #000000; --text-primary: #ffffff; padding: 80px 100px; justify-content: space-between; align-items: stretch;">
                <div style="display: flex; justify-content: space-between; align-items: center; width: 100%; z-index: 2;">
                    <span style="font-family: 'Nuqun'; font-size: 24px; font-weight: bold; text-transform: lowercase; letter-spacing: 0.05em; color: #ffffff;">zorixel</span>
                    <span style="font-family: 'Space Mono', monospace; font-size: 13px; color: rgba(255,255,255,0.4); letter-spacing: 0.1em;">SHOWCASE VOL. 01</span>
                </div>

                <div style="z-index: 2; text-align: left; margin: 40px 0; width: 100%;">
                    <h1 contenteditable="true" style="font-family: 'Bezmiar'; font-size: 180px; font-weight: normal; margin: 0; line-height: 0.85; letter-spacing: -0.02em; text-transform: uppercase;">
                        ZORIXEL<br>BRANDING
                    </h1>
                </div>

                <div style="display: flex; justify-content: space-between; align-items: flex-end; width: 100%; z-index: 2;">
                    <div style="font-family: 'Outfit'; font-size: 15px; color: rgba(255,255,255,0.6); line-height: 1.7; text-align: left;">
                        <span style="font-family: 'Space Mono', monospace; font-size: 11px; text-transform: uppercase; color: rgba(255,255,255,0.4); display: block; margin-bottom: 8px;">AUDIT SCORE</span>
                        <span>Premium Frontend Experience System Compliance</span><br>
                        <span>Zero-Dependency Dynamic Local Font Rendering</span>
                    </div>
                    <div style="font-family: 'Space Mono', monospace; font-size: 140px; font-weight: bold; line-height: 0.8; color: #ffffff; letter-spacing: -0.04em;">
                        2026
                    </div>
                </div>
                <div class="slide-footer" style="z-index: 2; width: 100%;">
                    <span>Zorixel Typography Cover Experiment</span>
                    <span>Slide 1 of 12</span>
                </div>
            </section>

            <!-- Slide 2: Clean Font Directory -->
            <section class="slide theme-a" style="--bg-primary: #121214; --text-primary: #ffffff; padding: 80px 100px; justify-content: flex-start; align-items: stretch;">
                <div class="slide-header" style="border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 16px; margin-bottom: 40px; width: 100%;">
                    <span style="font-family: 'Space Mono', monospace; font-size: 12px; text-transform: uppercase; color: rgba(255,255,255,0.4); letter-spacing: 0.15em;">Active Font Directory</span>
                    <span style="font-family: 'Space Mono', monospace; font-size: 12px; color: rgba(255,255,255,0.4);">6 Selected Candidates</span>
                </div>

                <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 40px 60px; width: 100%; text-align: left; z-index: 2;">
                    <!-- Bezmiar -->
                    <div style="border-bottom: 1px solid rgba(255,255,255,0.06); padding-bottom: 24px;">
                        <span style="font-family: 'Space Mono', monospace; font-size: 11px; color: rgba(255,255,255,0.4); text-transform: uppercase; display: block; margin-bottom: 8px;">01. Bezmiar (Futuristic Display)</span>
                        <h2 style="font-family: 'Bezmiar'; font-size: 48px; font-weight: normal; margin: 0; color: #ffffff; letter-spacing: -0.01em;">zorixel design</h2>
                    </div>

                    <!-- Rosehot -->
                    <div style="border-bottom: 1px solid rgba(255,255,255,0.06); padding-bottom: 24px;">
                        <span style="font-family: 'Space Mono', monospace; font-size: 11px; color: rgba(255,255,255,0.4); text-transform: uppercase; display: block; margin-bottom: 8px;">02. Rosehot (Editorial Serif)</span>
                        <h2 style="font-family: 'Rosehot'; font-size: 48px; font-weight: normal; margin: 0; color: #ffffff;">Zorixel Editorial</h2>
                    </div>

                    <!-- Grith -->
                    <div style="border-bottom: 1px solid rgba(255,255,255,0.06); padding-bottom: 24px;">
                        <span style="font-family: 'Space Mono', monospace; font-size: 11px; color: rgba(255,255,255,0.4); text-transform: uppercase; display: block; margin-bottom: 8px;">03. Grith (Bold Condensed Sans)</span>
                        <h2 style="font-family: 'Grith'; font-size: 48px; font-weight: normal; margin: 0; color: #ffffff; text-transform: uppercase; letter-spacing: 0.05em;">ZORIXEL CREATIVE</h2>
                    </div>

                    <!-- Vixa -->
                    <div style="border-bottom: 1px solid rgba(255,255,255,0.06); padding-bottom: 24px;">
                        <span style="font-family: 'Space Mono', monospace; font-size: 11px; color: rgba(255,255,255,0.4); text-transform: uppercase; display: block; margin-bottom: 8px;">04. Vixa (Organic Creative)</span>
                        <h2 style="font-family: 'Vixa'; font-size: 44px; font-weight: normal; margin: 0; color: #ffffff;">Zorixel Flow</h2>
                    </div>

                    <!-- Nuqun -->
                    <div>
                        <span style="font-family: 'Space Mono', monospace; font-size: 11px; color: rgba(255,255,255,0.4); text-transform: uppercase; display: block; margin-bottom: 8px;">05. Nuqun (Geometric Sans / Logo Primary)</span>
                        <h2 style="font-family: 'Nuqun'; font-size: 44px; font-weight: normal; margin: 0; color: #ffffff; text-transform: lowercase;">zorixel identity</h2>
                    </div>

                    <!-- Kalamayka -->
                    <div>
                        <span style="font-family: 'Space Mono', monospace; font-size: 11px; color: rgba(255,255,255,0.4); text-transform: uppercase; display: block; margin-bottom: 8px;">06. Kalamayka (Quirky Sans / Brand Accent)</span>
                        <h2 style="font-family: 'Kalamayka'; font-size: 44px; font-weight: normal; margin: 0; color: #ffffff;">Zorixel Modern</h2>
                    </div>
                </div>

                <div class="slide-footer" style="border-top: 1px solid rgba(255,255,255,0.1); padding-top: 16px; margin-top: auto; width: 100%;">
                    <span>Font Directory (Filtered Selection)</span>
                    <span>Slide 2 of 12</span>
                </div>
            </section>

            <!-- Slide 3: Primary Logo Identity Focus (Nuqun Lowercase) -->
            <section class="slide theme-c" style="--bg-primary: #000000; --text-primary: #ffffff; justify-content: center; align-items: center; text-align: center; padding: 100px;">
                <div style="z-index: 2;">
                    <!-- Massive Center Logo -->
                    <h1 contenteditable="true" style="font-family: 'Nuqun'; font-size: 280px; font-weight: normal; text-transform: lowercase; letter-spacing: 0.02em; margin: 0; line-height: 0.9; color: #ffffff;">
                        zorixel
                    </h1>
                    <!-- Tiny Dot badge -->
                    <div style="width: 24px; height: 24px; background: #ffffff; border-radius: 50%; margin: 40px auto 0 auto; box-shadow: 0 0 30px rgba(255,255,255,0.8);"></div>
                    
                    <p style="font-family: 'Space Mono', monospace; font-size: 16px; color: rgba(255,255,255,0.4); margin-top: 60px; text-transform: uppercase; letter-spacing: 0.2em;">
                        Primary Brand Wordmark Identity (Nuqun)
                    </p>
                </div>

                <div class="slide-footer" style="width: 100%;">
                    <span>Primary Logo Identity (Nuqun Lowercase Focus)</span>
                    <span>Slide 3 of 12</span>
                </div>
            </section>

            <!-- Slide 4: Brand Footer Layout (Bezmiar Style) -->
            <section class="slide theme-c" style="--bg-primary: #000000; --text-primary: #ffffff; padding: 60px 80px; justify-content: space-between;">
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

                <!-- Central Massive Logo (Bezmiar) -->
                <div style="text-align: center; width: 100%; z-index: 2; margin: 40px 0;">
                    <h1 contenteditable="true" style="font-family: 'Bezmiar'; font-size: 240px; font-weight: normal; text-transform: lowercase; letter-spacing: -0.03em; margin: 0; line-height: 0.85;">
                        zorixel
                    </h1>
                    <!-- dot emblem -->
                    <div style="width: 28px; height: 28px; background: #ffffff; border-radius: 50%; margin: 30px auto 0 auto; box-shadow: 0 0 20px rgba(255,255,255,0.5);"></div>
                </div>

                <!-- Footer details grid -->
                <div style="display: grid; grid-template-columns: 1.5fr 1fr 1.5fr; gap: 40px; width: 100%; z-index: 2; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 30px; text-align: left;">
                    <!-- Column 1: Contact & Socials -->
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

                    <!-- Column 2: Sitemap Links -->
                    <div style="display: flex; flex-direction: column; gap: 8px; font-family: 'Outfit'; font-size: 15px; color: rgba(255,255,255,0.8);">
                        <span>Home</span>
                        <span>Products</span>
                        <span>Projects</span>
                        <span>Store</span>
                        <span>Contact</span>
                    </div>

                    <!-- Column 3: Address / Office Details -->
                    <div style="font-family: 'Outfit'; font-size: 14px; color: rgba(255,255,255,0.5); line-height: 1.6; display: flex; flex-direction: column; justify-content: flex-start;">
                        <span style="font-weight: 600; color: #ffffff; margin-bottom: 4px;">zorixel office</span>
                        <span>40, Changdeokgung 1-gil,</span>
                        <span>Seoul, Korea</span>
                    </div>
                </div>

                <div class="slide-footer" style="z-index: 2; width: 100%;">
                    <span>Zorixel Footer Layout (Bezmiar Logo Focus)</span>
                    <span>Slide 4 of 12</span>
                </div>
            </section>

            <!-- Slide 5: Brand Footer Layout (Rosehot Style) -->
            <section class="slide theme-c" style="--bg-primary: #000000; --text-primary: #ffffff; padding: 60px 80px; justify-content: space-between;">
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
                    <h1 contenteditable="true" style="font-family: 'Rosehot'; font-size: 240px; font-weight: normal; letter-spacing: -0.02em; margin: 0; line-height: 0.85;">
                        Zorixel
                    </h1>
                    <!-- dot emblem -->
                    <div style="width: 28px; height: 28px; background: #ffffff; border-radius: 50%; margin: 30px auto 0 auto; box-shadow: 0 0 20px rgba(255,255,255,0.5);"></div>
                </div>

                <!-- Footer details grid -->
                <div style="display: grid; grid-template-columns: 1.5fr 1fr 1.5fr; gap: 40px; width: 100%; z-index: 2; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 30px; text-align: left;">
                    <!-- Column 1: Contact & Socials -->
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

                    <!-- Column 2: Sitemap Links -->
                    <div style="display: flex; flex-direction: column; gap: 8px; font-family: 'Outfit'; font-size: 15px; color: rgba(255,255,255,0.8);">
                        <span>Home</span>
                        <span>Products</span>
                        <span>Projects</span>
                        <span>Store</span>
                        <span>Contact</span>
                    </div>

                    <!-- Column 3: Address / Office Details -->
                    <div style="font-family: 'Outfit'; font-size: 14px; color: rgba(255,255,255,0.5); line-height: 1.6; display: flex; flex-direction: column; justify-content: flex-start;">
                        <span style="font-weight: 600; color: #ffffff; margin-bottom: 4px;">zorixel office</span>
                        <span>40, Changdeokgung 1-gil,</span>
                        <span>Seoul, Korea</span>
                    </div>
                </div>

                <div class="slide-footer" style="z-index: 2; width: 100%;">
                    <span>Zorixel Footer Layout (Rosehot Logo Focus)</span>
                    <span>Slide 5 of 12</span>
                </div>
            </section>

            <!-- Slide 6: Brand Footer Layout (Grith Style) -->
            <section class="slide theme-c" style="--bg-primary: #000000; --text-primary: #ffffff; padding: 60px 80px; justify-content: space-between;">
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

                <!-- Central Massive Logo (Grith) -->
                <div style="text-align: center; width: 100%; z-index: 2; margin: 40px 0;">
                    <h1 contenteditable="true" style="font-family: 'Grith'; font-size: 260px; font-weight: normal; text-transform: uppercase; letter-spacing: 0.03em; margin: 0; line-height: 0.85;">
                        ZORIXEL
                    </h1>
                    <!-- dot emblem -->
                    <div style="width: 28px; height: 28px; background: #ffffff; border-radius: 50%; margin: 30px auto 0 auto; box-shadow: 0 0 20px rgba(255,255,255,0.5);"></div>
                </div>

                <!-- Footer details grid -->
                <div style="display: grid; grid-template-columns: 1.5fr 1fr 1.5fr; gap: 40px; width: 100%; z-index: 2; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 30px; text-align: left;">
                    <!-- Column 1: Contact & Socials -->
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

                    <!-- Column 2: Sitemap Links -->
                    <div style="display: flex; flex-direction: column; gap: 8px; font-family: 'Outfit'; font-size: 15px; color: rgba(255,255,255,0.8);">
                        <span>Home</span>
                        <span>Products</span>
                        <span>Projects</span>
                        <span>Store</span>
                        <span>Contact</span>
                    </div>

                    <!-- Column 3: Address / Office Details -->
                    <div style="font-family: 'Outfit'; font-size: 14px; color: rgba(255,255,255,0.5); line-height: 1.6; display: flex; flex-direction: column; justify-content: flex-start;">
                        <span style="font-weight: 600; color: #ffffff; margin-bottom: 4px;">zorixel office</span>
                        <span>40, Changdeokgung 1-gil,</span>
                        <span>Seoul, Korea</span>
                    </div>
                </div>

                <div class="slide-footer" style="z-index: 2; width: 100%;">
                    <span>Zorixel Footer Layout (Grith Logo Focus)</span>
                    <span>Slide 6 of 12</span>
                </div>
            </section>

            <!-- Slide 7: Brand Footer Layout (Vixa Style) -->
            <section class="slide theme-c" style="--bg-primary: #000000; --text-primary: #ffffff; padding: 60px 80px; justify-content: space-between;">
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
                    <h1 contenteditable="true" style="font-family: 'Vixa'; font-size: 220px; font-weight: normal; letter-spacing: -0.01em; margin: 0; line-height: 0.85;">
                        Zorixel
                    </h1>
                    <!-- dot emblem -->
                    <div style="width: 28px; height: 28px; background: #ffffff; border-radius: 50%; margin: 30px auto 0 auto; box-shadow: 0 0 20px rgba(255,255,255,0.5);"></div>
                </div>

                <!-- Footer details grid -->
                <div style="display: grid; grid-template-columns: 1.5fr 1fr 1.5fr; gap: 40px; width: 100%; z-index: 2; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 30px; text-align: left;">
                    <!-- Column 1: Contact & Socials -->
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

                    <!-- Column 2: Sitemap Links -->
                    <div style="display: flex; flex-direction: column; gap: 8px; font-family: 'Outfit'; font-size: 15px; color: rgba(255,255,255,0.8);">
                        <span>Home</span>
                        <span>Products</span>
                        <span>Projects</span>
                        <span>Store</span>
                        <span>Contact</span>
                    </div>

                    <!-- Column 3: Address / Office Details -->
                    <div style="font-family: 'Outfit'; font-size: 14px; color: rgba(255,255,255,0.5); line-height: 1.6; display: flex; flex-direction: column; justify-content: flex-start;">
                        <span style="font-weight: 600; color: #ffffff; margin-bottom: 4px;">zorixel office</span>
                        <span>40, Changdeokgung 1-gil,</span>
                        <span>Seoul, Korea</span>
                    </div>
                </div>

                <div class="slide-footer" style="z-index: 2; width: 100%;">
                    <span>Zorixel Footer Layout (Vixa Logo Focus)</span>
                    <span>Slide 7 of 12</span>
                </div>
            </section>

            <!-- Slide 8: Editorial Report Typography Layout (Rosehot) -->
            <section class="slide theme-a" style="--bg-primary: #ffffff; --text-primary: #111111; padding: 80px 120px; justify-content: flex-start;">
                <div class="slide-header" style="border-bottom: 1px solid rgba(0,0,0,0.08); padding-bottom: 16px; margin-bottom: 40px; width: 100%;">
                    <span style="font-family: 'Space Mono', monospace; font-size: 12px; text-transform: uppercase; color: rgba(0,0,0,0.4); letter-spacing: 0.15em;">REPORT ANALYSIS</span>
                    <span style="font-family: 'Space Mono', monospace; font-size: 12px; color: rgba(0,0,0,0.4);">[ SEC_01 ]</span>
                </div>
                
                <div style="max-width: 960px; text-align: left; width: 100%;">
                    <h2 contenteditable="true" style="font-family: 'Rosehot'; font-size: 54px; line-height: 1.25; color: #111111; letter-spacing: 0.02em; margin: 0 0 32px 0; font-weight: normal;">
                        Zorixel System aims to capture how custom typography transforms digital design across creators' screens and within their teams.
                    </h2>
                    
                    <p contenteditable="true" style="font-family: 'Outfit'; font-size: 18px; line-height: 1.7; color: #333336; margin-bottom: 24px; letter-spacing: 0.03em;">
                        We initiated our typographic sandbox in early 2026 because we consistently heard vibe coders and brand creators ask, "How do we pair these display fonts, and what layout formulas actually look premium?" A few cycles later, we're publishing these live render playgrounds to demonstrate the principles.
                    </p>
                    
                    <p contenteditable="true" style="font-family: 'Outfit'; font-size: 18px; line-height: 1.7; color: #333336; margin-bottom: 24px; letter-spacing: 0.03em;">
                        The results come from over 900 design audits at creative startups and boutique development agencies who work across disciplines like product engineering, interactive brand direction, and visual prototyping.
                    </p>
                    
                    <p contenteditable="true" style="font-family: 'Outfit'; font-size: 18px; line-height: 1.7; color: #333336; margin: 0; letter-spacing: 0.03em;">
                        Given how quickly visual conventions are shifting, we'll continue to release new typographic pairings and design patterns throughout the year. <a href="#" style="color: #111111; font-weight: 600; text-decoration: underline;">Sign up for new releases.</a>
                    </p>
                </div>

                <div class="slide-footer" style="border-top: 1px solid rgba(0,0,0,0.08); padding-top: 16px; margin-top: auto; width: 100%;">
                    <span>Clean Editorial Page (Rosehot Serif Focus)</span>
                    <span>Slide 8 of 12</span>
                </div>
            </section>

            <!-- Slide 9: Editorial Report Typography Layout (Vixa) -->
            <section class="slide theme-a" style="--bg-primary: #ffffff; --text-primary: #111111; padding: 80px 120px; justify-content: flex-start;">
                <div class="slide-header" style="border-bottom: 1px solid rgba(0,0,0,0.08); padding-bottom: 16px; margin-bottom: 40px; width: 100%;">
                    <span style="font-family: 'Space Mono', monospace; font-size: 12px; text-transform: uppercase; color: rgba(0,0,0,0.4); letter-spacing: 0.15em;">REPORT ANALYSIS</span>
                    <span style="font-family: 'Space Mono', monospace; font-size: 12px; color: rgba(0,0,0,0.4);">[ SEC_02 ]</span>
                </div>
                
                <div style="max-width: 960px; text-align: left; width: 100%;">
                    <h2 contenteditable="true" style="font-family: 'Vixa'; font-size: 50px; line-height: 1.25; color: #111111; margin: 0 0 32px 0; font-weight: normal;">
                        Zorixel System aims to capture how custom typography transforms digital design across creators' screens and within their teams.
                    </h2>
                    
                    <p contenteditable="true" style="font-family: 'Outfit'; font-size: 18px; line-height: 1.7; color: #333336; margin-bottom: 24px; letter-spacing: 0.03em;">
                        We initiated our typographic sandbox in early 2026 because we consistently heard vibe coders and brand creators ask, "How do we pair these display fonts, and what layout formulas actually look premium?" A few cycles later, we're publishing these live render playgrounds to demonstrate the principles.
                    </p>
                    
                    <p contenteditable="true" style="font-family: 'Outfit'; font-size: 18px; line-height: 1.7; color: #333336; margin-bottom: 24px; letter-spacing: 0.03em;">
                        The results come from over 900 design audits at creative startups and boutique development agencies who work across disciplines like product engineering, interactive brand direction, and visual prototyping.
                    </p>
                    
                    <p contenteditable="true" style="font-family: 'Outfit'; font-size: 18px; line-height: 1.7; color: #333336; margin: 0; letter-spacing: 0.03em;">
                        Given how quickly visual conventions are shifting, we'll continue to release new typographic pairings and design patterns throughout the year. <a href="#" style="color: #111111; font-weight: 600; text-decoration: underline;">Sign up for new releases.</a>
                    </p>
                </div>

                <div class="slide-footer" style="border-top: 1px solid rgba(0,0,0,0.08); padding-top: 16px; margin-top: auto; width: 100%;">
                    <span>Clean Editorial Page (Vixa Organic Focus)</span>
                    <span>Slide 9 of 12</span>
                </div>
            </section>

            <!-- Slide 10: Editorial Report Cover (Grith Style) -->
            <section class="slide theme-c" style="--bg-primary: #000000; --text-primary: #ffffff; padding: 80px 100px; justify-content: space-between; align-items: stretch;">
                <div style="z-index: 2; text-align: left; margin-top: 40px; width: 100%;">
                    <h1 contenteditable="true" style="font-family: 'Grith'; font-size: 180px; font-weight: normal; margin: 0; line-height: 0.85; letter-spacing: 0.05em; text-transform: uppercase;">
                        ZORIXEL<br>SYSTEM
                    </h1>
                </div>

                <div style="display: flex; justify-content: space-between; align-items: flex-end; width: 100%; z-index: 2; margin-bottom: 20px;">
                    <div style="display: flex; gap: 80px; text-align: left;">
                        <div>
                            <span style="font-family: 'Space Mono', monospace; font-size: 11px; text-transform: uppercase; color: rgba(255,255,255,0.4); letter-spacing: 0.1em; display: block; margin-bottom: 12px;">SYSTEM PAIRINGS</span>
                            <div style="font-family: 'Outfit'; font-size: 14px; color: rgba(255,255,255,0.8); line-height: 1.6; display: grid; grid-template-columns: 1fr 1fr; gap: 8px 24px;">
                                <span>Bezmiar</span><span>Rosehot</span>
                                <span>Vixa</span><span>Grith</span>
                                <span>Nuqun</span><span>Kalamayka</span>
                            </div>
                        </div>
                        <div>
                            <span style="font-family: 'Space Mono', monospace; font-size: 11px; text-transform: uppercase; color: rgba(255,255,255,0.4); letter-spacing: 0.1em; display: block; margin-bottom: 12px;">DOCUMENTS</span>
                            <div style="font-family: 'Outfit'; font-size: 14px; color: rgba(255,255,255,0.8); line-height: 1.6; display: flex; flex-direction: column; gap: 4px;">
                                <span>Read the Spec</span>
                                <span>Design Log</span>
                                <span>Vibe Sheets</span>
                            </div>
                        </div>
                    </div>

                    <!-- Year (Space Mono for clean numbers) -->
                    <div style="font-family: 'Space Mono', monospace; font-size: 150px; font-weight: bold; line-height: 0.8; letter-spacing: -0.04em; color: #ffffff;">
                        2026
                    </div>
                </div>

                <div class="slide-footer" style="border-top: 1px solid rgba(255,255,255,0.1); padding-top: 16px; width: 100%;">
                    <span>Zorixel System Identity Cover (Grith &amp; Space Mono Focus)</span>
                    <span>Slide 10 of 12</span>
                </div>
            </section>

            <!-- Slide 11: Stats & Newsletter Signup Layout (Nuqun & Space Mono) -->
            <section class="slide theme-c" style="--bg-primary: #050508; --text-primary: #ffffff; padding: 80px 100px; justify-content: space-between; align-items: stretch;">
                <div style="z-index: 2; text-align: center; max-width: 650px; margin: 40px auto 0 auto; display: flex; flex-direction: column; align-items: center; gap: 20px;">
                    <h2 contenteditable="true" style="font-family: 'Nuqun'; font-size: 40px; font-weight: normal; margin: 0; line-height: 1.2; letter-spacing: 0.08em; text-transform: uppercase;">
                        Get new case studies &amp; report markdown
                    </h2>
                    <p contenteditable="true" style="font-family: 'Outfit'; font-size: 16px; color: rgba(255,255,255,0.6); margin: 0 0 10px 0; line-height: 1.5;">
                        Download the markdown version of the report, ready to drop into any tool. Get notified as new case studies go live.
                    </p>
                    
                    <!-- Signup Box Form -->
                    <div style="display: flex; background: #ffffff; border-radius: 8px; overflow: hidden; width: 100%; max-width: 500px; padding: 4px; box-shadow: 0 10px 30px rgba(0,0,0,0.3);">
                        <input type="email" placeholder="Your email" style="flex: 1; border: none; outline: none; background: transparent; padding: 14px 20px; font-family: 'Outfit'; font-size: 16px; color: #111111;" readonly>
                        <button style="background: #ff5500; color: #ffffff; border: none; outline: none; padding: 12px 30px; font-family: 'Outfit'; font-weight: 700; font-size: 16px; border-radius: 6px; cursor: pointer;">Submit</button>
                    </div>
                    <span style="font-family: 'Outfit'; font-size: 11px; color: rgba(255,255,255,0.4);">
                        By subscribing, you agree to receive communications in accordance with our privacy policy.
                    </span>
                </div>

                <!-- Bottom Methodology Grid -->
                <div style="display: grid; grid-template-columns: 1.5fr 1fr 1fr 1fr; gap: 30px; width: 100%; z-index: 2; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 24px; text-align: left;">
                    <div style="display: flex; flex-direction: column; justify-content: flex-start; gap: 8px;">
                        <span style="font-family: 'Space Mono', monospace; font-size: 11px; text-transform: uppercase; color: rgba(255,255,255,0.4); letter-spacing: 0.1em;">METHODOLOGY</span>
                        <h3 contenteditable="true" style="font-family: 'Outfit'; font-size: 24px; font-weight: 700; margin: 0; color: #ffffff; line-height: 1.2;">This report draws from</h3>
                    </div>
                    
                    <!-- Numbers in beautifully spaced Space Mono -->
                    <div style="border-left: 1px solid rgba(255,255,255,0.1); padding-left: 20px;">
                        <span style="font-family: 'Space Mono', monospace; font-size: 64px; font-weight: bold; color: #ffffff; line-height: 1.0; display: block; margin-bottom: 8px; letter-spacing: 0.05em;">13+</span>
                        <span style="font-family: 'Outfit'; font-size: 14px; color: rgba(255,255,255,0.5);">Local Brand Fonts</span>
                    </div>

                    <div style="border-left: 1px solid rgba(255,255,255,0.1); padding-left: 20px;">
                        <span style="font-family: 'Space Mono', monospace; font-size: 64px; font-weight: bold; color: #ffffff; line-height: 1.0; display: block; margin-bottom: 8px; letter-spacing: 0.05em;">4</span>
                        <span style="font-family: 'Outfit'; font-size: 14px; color: rgba(255,255,255,0.5);">Concept Routes</span>
                    </div>

                    <div style="border-left: 1px solid rgba(255,255,255,0.1); padding-left: 20px;">
                        <span style="font-family: 'Space Mono', monospace; font-size: 64px; font-weight: bold; color: #ffffff; line-height: 1.0; display: block; margin-bottom: 8px; letter-spacing: 0.05em;">12</span>
                        <span style="font-family: 'Outfit'; font-size: 14px; color: rgba(255,255,255,0.5);">Showcase Slides</span>
                    </div>
                </div>

                <div class="slide-footer" style="z-index: 2; width: 100%;">
                    <span>Zorixel Methodology &amp; Audience Connect</span>
                    <span>Slide 11 of 12</span>
                </div>
            </section>

            <!-- Slide 12: Voting Dashboard -->
            <section class="slide theme-a" style="--bg-primary: #0b0b0e; --text-primary: #ffffff; padding: 80px 100px; justify-content: flex-start; align-items: stretch;">
                <div class="slide-header" style="border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 16px; margin-bottom: 40px; width: 100%;">
                    <span style="font-family: 'Space Mono', monospace; font-size: 12px; text-transform: uppercase; color: rgba(255,255,255,0.4); letter-spacing: 0.15em;">Decision Dashboard</span>
                    <span style="font-family: 'Space Mono', monospace; font-size: 12px; color: rgba(255,255,255,0.4);">Select Branding Font</span>
                </div>

                <div style="text-align: center; margin-bottom: 40px; z-index: 2;">
                    <h2 style="font-family: 'Outfit'; font-weight: 700; font-size: 36px; margin: 0 0 12px 0;">Select your Zorixel Branding direction</h2>
                    <p style="font-family: 'Outfit'; font-size: 16px; color: rgba(255,255,255,0.5); margin: 0;">Click to register your votes. The results save locally.</p>
                </div>

                <!-- Voting Cards Grid -->
                <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 24px; width: 100%; z-index: 2; margin-bottom: 40px;">
                    <!-- Bezmiar -->
                    <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.1); border-radius: 16px; padding: 24px; text-align: center; display: flex; flex-direction: column; gap: 16px;">
                        <span style="font-family: 'Space Mono', monospace; font-size: 11px; color: rgba(255,255,255,0.4);">ROUTE A</span>
                        <h3 style="font-family: 'Bezmiar'; font-size: 28px; font-weight: normal; margin: 0; text-transform: lowercase;">zorixel</h3>
                        <div style="font-size: 24px; font-weight: bold; font-family: 'Space Mono', monospace; color: #ffffff;" id="percent-a">0%</div>
                        <div style="font-size: 12px; color: rgba(255,255,255,0.4); font-family: 'Space Mono', monospace;"><span id="votes-a">0</span> votes</div>
                        <button onclick="castVote('a')" style="background: #ffffff; color: #000000; border: none; padding: 10px; border-radius: 8px; font-family: 'Outfit'; font-weight: 700; cursor: pointer; transition: transform 0.2s;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">Vote Bezmiar</button>
                    </div>

                    <!-- Rosehot -->
                    <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.1); border-radius: 16px; padding: 24px; text-align: center; display: flex; flex-direction: column; gap: 16px;">
                        <span style="font-family: 'Space Mono', monospace; font-size: 11px; color: rgba(255,255,255,0.4);">ROUTE B</span>
                        <h3 style="font-family: 'Rosehot'; font-size: 28px; font-weight: normal; margin: 0;">Zorixel</h3>
                        <div style="font-size: 24px; font-weight: bold; font-family: 'Space Mono', monospace; color: #ffffff;" id="percent-b">0%</div>
                        <div style="font-size: 12px; color: rgba(255,255,255,0.4); font-family: 'Space Mono', monospace;"><span id="votes-b">0</span> votes</div>
                        <button onclick="castVote('b')" style="background: #ffffff; color: #000000; border: none; padding: 10px; border-radius: 8px; font-family: 'Outfit'; font-weight: 700; cursor: pointer; transition: transform 0.2s;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">Vote Rosehot</button>
                    </div>

                    <!-- Grith -->
                    <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.1); border-radius: 16px; padding: 24px; text-align: center; display: flex; flex-direction: column; gap: 16px;">
                        <span style="font-family: 'Space Mono', monospace; font-size: 11px; color: rgba(255,255,255,0.4);">ROUTE C</span>
                        <h3 style="font-family: 'Grith'; font-size: 28px; font-weight: normal; margin: 0; text-transform: uppercase; letter-spacing: 0.05em;">ZORIXEL</h3>
                        <div style="font-size: 24px; font-weight: bold; font-family: 'Space Mono', monospace; color: #ffffff;" id="percent-c">0%</div>
                        <div style="font-size: 12px; color: rgba(255,255,255,0.4); font-family: 'Space Mono', monospace;"><span id="votes-c">0</span> votes</div>
                        <button onclick="castVote('c')" style="background: #ffffff; color: #000000; border: none; padding: 10px; border-radius: 8px; font-family: 'Outfit'; font-weight: 700; cursor: pointer; transition: transform 0.2s;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">Vote Grith</button>
                    </div>

                    <!-- Vixa -->
                    <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.1); border-radius: 16px; padding: 24px; text-align: center; display: flex; flex-direction: column; gap: 16px;">
                        <span style="font-family: 'Space Mono', monospace; font-size: 11px; color: rgba(255,255,255,0.4);">ROUTE D</span>
                        <h3 style="font-family: 'Vixa'; font-size: 28px; font-weight: normal; margin: 0;">Zorixel</h3>
                        <div style="font-size: 24px; font-weight: bold; font-family: 'Space Mono', monospace; color: #ffffff;" id="percent-d">0%</div>
                        <div style="font-size: 12px; color: rgba(255,255,255,0.4); font-family: 'Space Mono', monospace;"><span id="votes-d">0</span> votes</div>
                        <button onclick="castVote('d')" style="background: #ffffff; color: #000000; border: none; padding: 10px; border-radius: 8px; font-family: 'Outfit'; font-weight: 700; cursor: pointer; transition: transform 0.2s;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">Vote Vixa</button>
                    </div>
                </div>

                <div class="slide-footer" style="border-top: 1px solid rgba(255,255,255,0.1); padding-top: 16px; margin-top: auto; width: 100%;">
                    <span>Interactive Decision Matrix</span>
                    <span>Slide 12 of 12</span>
                </div>
            </section>

        </main>
    </div>

    <!-- PRESENTATION CHROME DOCK CONTROLS -->
    <div class="deck-controls">
        <button class="btn-nav" onclick="presentation.prevSlide()">← Prev</button>
        <button class="btn-nav" onclick="presentation.nextSlide()">Next →</button>
        <span class="slide-counter" id="slideCounter">1 / 12</span>
    </div>

    <!-- QUICK ROUTE JUMP LINKS -->
    <div class="route-jumps">
        <button class="btn-jump active-route" id="jump-intro" onclick="presentation.showSlide(0)">Cover</button>
        <button class="btn-jump" id="jump-fonts" onclick="presentation.showSlide(1)">Fonts</button>
        <button class="btn-jump" id="jump-logo" onclick="presentation.showSlide(2)">Logo</button>
        <button class="btn-jump" id="jump-footers" onclick="presentation.showSlide(3)">Footers</button>
        <button class="btn-jump" id="jump-reports" onclick="presentation.showSlide(7)">Reports</button>
        <button class="btn-jump" id="jump-cover" onclick="presentation.showSlide(9)">Report Cover</button>
        <button class="btn-jump" id="jump-stats" onclick="presentation.showSlide(10)">Stats</button>
        <button class="btn-jump" id="jump-compare" onclick="presentation.showSlide(11)">Compare</button>
    </div>"""

# 2. Also replace updateRouteNavHighlight function
old_js_func = """            updateRouteNavHighlight() {
                // Remove active classes
                document.querySelectorAll('.btn-jump').forEach(btn => btn.classList.remove('active-route'));

                if (this.currentSlide === 0 || this.currentSlide === 1) {
                    document.getElementById('jump-intro').classList.add('active-route');
                } else if (this.currentSlide >= 2 && this.currentSlide <= 5) {
                    document.getElementById('jump-a').classList.add('active-route');
                } else if (this.currentSlide >= 6 && this.currentSlide <= 9) {
                    document.getElementById('jump-b').classList.add('active-route');
                } else if (this.currentSlide >= 10 && this.currentSlide <= 13) {
                    document.getElementById('jump-c').classList.add('active-route');
                } else if (this.currentSlide >= 14 && this.currentSlide <= 17) {
                    document.getElementById('jump-d').classList.add('active-route');
                } else if (this.currentSlide === 18) {
                    document.getElementById('jump-compare').classList.add('active-route');
                } else if (this.currentSlide >= 19 && this.currentSlide <= 24) {
                    document.getElementById('jump-mega').classList.add('active-route');
                } else if (this.currentSlide >= 25 && this.currentSlide <= 29) {
                    document.getElementById('jump-refined').classList.add('active-route');
                } else if (this.currentSlide >= 30 && this.currentSlide <= 33) {
                    document.getElementById('jump-layouts').classList.add('active-route');
                }
            }"""

new_js_func = """            updateRouteNavHighlight() {
                // Remove active classes
                document.querySelectorAll('.btn-jump').forEach(btn => btn.classList.remove('active-route'));

                if (this.currentSlide === 0) {
                    document.getElementById('jump-intro').classList.add('active-route');
                } else if (this.currentSlide === 1) {
                    document.getElementById('jump-fonts').classList.add('active-route');
                } else if (this.currentSlide === 2) {
                    document.getElementById('jump-logo').classList.add('active-route');
                } else if (this.currentSlide >= 3 && this.currentSlide <= 6) {
                    document.getElementById('jump-footers').classList.add('active-route');
                } else if (this.currentSlide >= 7 && this.currentSlide <= 8) {
                    document.getElementById('jump-reports').classList.add('active-route');
                } else if (this.currentSlide === 9) {
                    document.getElementById('jump-cover').classList.add('active-route');
                } else if (this.currentSlide === 10) {
                    document.getElementById('jump-stats').classList.add('active-route');
                } else if (this.currentSlide === 11) {
                    document.getElementById('jump-compare').classList.add('active-route');
                }
            }"""

html_new = html[:start_idx] + new_deck + "\\n\\n    " + html[end_idx:]
html_new = html_new.replace(old_js_func, new_js_func)

with open(fpath, "w", encoding="utf-8") as f:
    f.write(html_new)

print("Rebuilt presentation.html cleanly with 12 targeted slides!")
