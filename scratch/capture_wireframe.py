import asyncio
import os
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1920, "height": 1200})
        wireframe_path = os.path.abspath(r"premium-frontend-experience-system\reference-inputs\sites\grids-obys-agency\assets\wireframe.html")
        await page.goto(f"file:///{wireframe_path.replace('\\', '/')}")
        out_path = r"premium-frontend-experience-system\reference-inputs\sites\grids-obys-agency\assets\wireframe.png"
        await page.screenshot(path=out_path, full_page=True)
        print("Wireframe screenshot saved successfully!")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
