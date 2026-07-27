import asyncio
import os
from playwright.async_api import async_playwright

timestamps = [
    ("01_intro_app_demo", 60),
    ("02_crash_course_principles", 220),
    ("03_crash_course_architecture_diagram", 450),
    ("04_crash_course_ai_workflow", 750),
    ("05_project_setup", 900),
    ("06_preparing_context_rules", 1350),
    ("07_context_specs_prompts", 1800),
    ("08_ui_primitive_components", 2450),
    ("09_layout_setup", 2950),
    ("10_authentication_clerk", 3600),
    ("11_project_dialogues", 4900),
    ("12_prisma_schema_setup", 5500),
    ("13_project_crud_apis", 6000),
    ("14_editor_access_sharing", 6800),
    ("15_editor_liveblocks_canvas", 7500),
    ("16_editor_canvas_features", 8700),
    ("17_chat_sidebar_auto_save", 10000),
    ("18_trigger_dev_background_jobs", 11200),
    ("19_ai_architecture_generation", 11800),
    ("20_ai_spec_generation", 13200),
    ("21_deployment_cloud", 13900)
]

os.makedirs('scratch/screenshots', exist_ok=True)

async def main():
    async with async_playwright() as p:
        # Launch browser with user agent and bypass cookie dialogs if needed
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            viewport={'width': 1920, 'height': 1080},
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        )
        page = await context.new_page()

        for name, t in timestamps:
            url = f"https://www.youtube.com/watch?v=14RP8liACqo&t={t}s"
            print(f"Navigating to {name} at {t}s ({url})...")
            try:
                await page.goto(url, wait_until="domcontentloaded", timeout=25000)
                await page.wait_for_timeout(4000)
                
                # Click play button if needed or pause video to grab exact frame
                await page.evaluate("""() => {
                    // Try to dismiss overlays/cookies if present
                    const dismissBtns = document.querySelectorAll('button[aria-label*="Reject"], button[aria-label*="Accept"], .ytp-ad-skip-button');
                    dismissBtns.forEach(b => b.click());
                    
                    const video = document.querySelector('video');
                    if (video) {
                        video.pause();
                    }
                }""")
                await page.wait_for_timeout(1000)
                path = f"scratch/screenshots/{name}.png"
                await page.screenshot(path=path)
                print(f"Saved {path}")
            except Exception as e:
                print(f"Error capturing {name}: {e}")

        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
