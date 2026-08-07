import asyncio
import os
from playwright.async_api import async_playwright

async def verify():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(viewport={"width": 1920, "height": 1080})
        page = await context.new_page()
        
        slide_url = r"file:///d:/AI-OS/clients/001-vashishthya-research-edu/01-pre-outreach-audit/04-visual-assets-and-previews/vashishthya_loom_presentation.html"
        await page.goto(slide_url)
        await page.wait_for_timeout(1000)
        
        out_shot = r"d:\AI-OS\clients\001-vashishthya-research-edu\01-pre-outreach-audit\04-visual-assets-and-previews\presentation_verification.png"
        await page.screenshot(path=out_shot)
        print(f"Verified and saved slide screenshot to {out_shot}")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(verify())
