import asyncio
from playwright.async_api import async_playwright
import os

VIEWPORTS = [
    {"name": "desktop_1920", "width": 1920, "height": 1080},
    {"name": "laptop_1440", "width": 1440, "height": 900},
    {"name": "tablet_1024", "width": 1024, "height": 768},
    {"name": "tablet_768", "width": 768, "height": 1024},
    {"name": "mobile_375", "width": 375, "height": 812},
]

OUTPUT_DIR = r"d:\AI-OS\premium-frontend-experience-system\reference-inputs\sites\sondaven\assets"

async def capture():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        for vp in VIEWPORTS:
            context = await browser.new_context(
                viewport={"width": vp["width"], "height": vp["height"]},
                device_scale_factor=2 if vp["width"] <= 768 else 1
            )
            page = await context.new_page()
            try:
                print(f"Capturing {vp['name']} ({vp['width']}x{vp['height']})...")
                await page.goto("https://sondaven.com/en", wait_until="domcontentloaded", timeout=30000)
                await asyncio.sleep(2)
                # Click cookie button if present
                cookie_btn = page.locator("text=Ok")
                if await cookie_btn.count() > 0:
                    try:
                        await cookie_btn.first.click(timeout=2000)
                    except:
                        pass
                await asyncio.sleep(1)
                out_path = os.path.join(OUTPUT_DIR, f"{vp['name']}.png")
                await page.screenshot(path=out_path)
                print(f"Saved: {out_path}")
            except Exception as e:
                print(f"Error capturing {vp['name']}: {e}")
            finally:
                await context.close()
        await browser.close()

if __name__ == "__main__":
    asyncio.run(capture())
