import asyncio
import os
from playwright.async_api import async_playwright

async def verify():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(viewport={"width": 1920, "height": 1080})
        page = await context.new_page()
        
        slide_url = r"file:///d:/AI-OS/clients/001-vashishthya-research-edu/04-visual-assets-and-previews/notion_google_sync_presentation.html"
        await page.goto(slide_url)
        await page.wait_for_timeout(1000)
        
        out_dir = r"d:\AI-OS\clients\001-vashishthya-research-edu\04-visual-assets-and-previews\slides_preview"
        os.makedirs(out_dir, exist_ok=True)
        
        for i in range(1, 8):
            out_shot = os.path.join(out_dir, f"slide_{i}.png")
            await page.screenshot(path=out_shot)
            print(f"Captured Slide {i} -> {out_shot}")
            await page.keyboard.press("ArrowRight")
            await page.wait_for_timeout(400)
            
        await browser.close()

if __name__ == "__main__":
    asyncio.run(verify())
