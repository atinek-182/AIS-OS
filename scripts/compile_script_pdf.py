import asyncio
import os
from playwright.async_api import async_playwright

HTML_PATH = r"d:\AI-OS\clients\001-vashishthya-research-edu\01-pre-outreach-audit\03-pitch-and-loom-guides\LOOM_VIDEO_DEMO_SCRIPT_GUIDE.html"
PDF_PATH = r"d:\AI-OS\clients\001-vashishthya-research-edu\01-pre-outreach-audit\03-pitch-and-loom-guides\LOOM_VIDEO_DEMO_SCRIPT_GUIDE.pdf"

async def generate_pdf():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        file_url = f"file:///{HTML_PATH.replace('\\', '/')}"
        await page.goto(file_url, wait_until="networkidle")
        await page.pdf(
            path=PDF_PATH,
            format="A4",
            print_background=True,
            margin={"top": "15mm", "bottom": "15mm", "left": "15mm", "right": "15mm"}
        )
        await browser.close()
        print(f"Successfully generated formatted PDF: {PDF_PATH}")

if __name__ == "__main__":
    asyncio.run(generate_pdf())
