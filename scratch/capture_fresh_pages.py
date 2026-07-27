import asyncio
import os
from playwright.async_api import async_playwright

timestamps = [
    ("01_intro_app", 60),
    ("02_context_structure", 1380),
    ("03_canvas_editor", 7500),
    ("04_ai_trigger_dev", 11200)
]

os.makedirs('scratch/fresh_frames', exist_ok=True)

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        
        for name, t in timestamps:
            print(f"Loading {name} at {t}s...")
            context = await browser.new_context(
                viewport={'width': 1920, 'height': 1080},
                user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
            )
            page = await context.new_page()
            try:
                await page.goto(f"https://www.youtube.com/watch?v=14RP8liACqo&t={t}s", wait_until="networkidle", timeout=30000)
                await page.wait_for_timeout(3000)
                
                # Press play / pause
                await page.keyboard.press("k")
                await page.wait_for_timeout(1000)
                
                path = f"scratch/fresh_frames/{name}.png"
                await page.screenshot(path=path)
                print(f"Saved {path}")
            except Exception as e:
                print(f"Error on {name}: {e}")
            finally:
                await context.close()

        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
