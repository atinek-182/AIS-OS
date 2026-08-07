import asyncio
import os
from playwright.async_api import async_playwright

OUTPUT_DIR = r"d:\AI-OS\clients\001-vashishthya-research-edu\01-pre-outreach-audit\04-visual-assets-and-previews"

async def capture():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(viewport={"width": 1920, "height": 1080})
        page = await context.new_page()

        # 1. Capture Notion Operator Setup Dashboard (Local high-res fallback)
        dashboard_url = r"file:///d:/AI-OS/clients/001-vashishthya-research-edu/01-pre-outreach-audit/04-visual-assets-and-previews/operator_setup_dashboard.html"
        print(f"Navigating to {dashboard_url}...")
        await page.goto(dashboard_url)
        await page.wait_for_timeout(1000)
        notion_shot = os.path.join(OUTPUT_DIR, "notion_dashboard_preview.png")
        await page.screenshot(path=notion_shot, full_page=False)
        print(f"Saved {notion_shot}")

        # 2. Try capturing live public Notion Page if accessible
        try:
            notion_public_url = "https://app.notion.com/p/Vashishthya-Master-Client-Desk-3b2b0c7463df80a3b4f4c7a78b835f7e?source=copy_link"
            print(f"Navigating to public Notion page {notion_public_url}...")
            await page.goto(notion_public_url, timeout=20000)
            await page.wait_for_timeout(4000)
            notion_live_shot = os.path.join(OUTPUT_DIR, "notion_live_desk_preview.png")
            await page.screenshot(path=notion_live_shot, full_page=False)
            print(f"Saved {notion_live_shot}")
        except Exception as e:
            print(f"Notice (Public Notion capture): {e}")

        # 3. Capture IJORAR Journal Website Homepage (Mobile viewport issue)
        try:
            print("Navigating to http://ijorarjournal.com...")
            await page.goto("http://ijorarjournal.com", timeout=15000)
            await page.wait_for_timeout(2000)
            ijorar_shot = os.path.join(OUTPUT_DIR, "ijorar_homepage_preview.png")
            await page.screenshot(path=ijorar_shot, full_page=False)
            print(f"Saved {ijorar_shot}")
        except Exception as e:
            print(f"Error loading IJORAR homepage: {e}")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(capture())
