import asyncio
import os
from playwright.async_api import async_playwright

timestamps = [
    ("01_intro_app_demo", 60),
    ("03_crash_course_architecture_diagram", 450),
    ("04_crash_course_ai_workflow", 750),
    ("06_preparing_context_rules", 1350),
    ("07_context_specs_prompts", 1800),
    ("08_ui_primitive_components", 2450),
    ("11_project_dialogues", 4900),
    ("12_prisma_schema_setup", 5500),
    ("15_editor_liveblocks_canvas", 7500),
    ("16_editor_canvas_features", 8700),
    ("18_trigger_dev_background_jobs", 11200),
    ("19_ai_architecture_generation", 11800),
    ("20_ai_spec_generation", 13200)
]

os.makedirs('scratch/clean_screenshots', exist_ok=True)

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            viewport={'width': 1920, 'height': 1080},
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        )
        page = await context.new_page()

        # Open YouTube watch page once
        print("Opening video page...")
        await page.goto("https://www.youtube.com/watch?v=14RP8liACqo", wait_until="domcontentloaded")
        await page.wait_for_timeout(5000)

        # Handle cookie consent or ads initially
        await page.evaluate("""() => {
            const btns = Array.from(document.querySelectorAll('button'));
            const accept = btns.find(b => b.textContent.includes('Accept') || b.textContent.includes('Agree'));
            if (accept) accept.click();
        }""")

        for name, t in timestamps:
            print(f"Seeking to {name} at {t}s...")
            try:
                # Seek video to timestamp using JS
                await page.evaluate(f"""() => {{
                    // Skip ads if present
                    const skipBtn = document.querySelector('.ytp-ad-skip-button, .ytp-skip-ad-button');
                    if (skipBtn) skipBtn.click();

                    const video = document.querySelector('video');
                    if (video) {{
                        video.currentTime = {t};
                        video.pause();
                    }}
                }}""")
                await page.wait_for_timeout(2500)

                # Capture element screenshot of the video player element specifically!
                player_elem = await page.query_selector('#player-container, #ytd-player, .html5-video-player, video')
                path = f"scratch/clean_screenshots/{name}.png"
                if player_elem:
                    await player_elem.screenshot(path=path)
                else:
                    await page.screenshot(path=path)
                print(f"Saved frame {path}")
            except Exception as e:
                print(f"Error capturing {name}: {e}")

        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
