import asyncio
import json
import os
from playwright.async_api import async_playwright

PAGES = [
    {"name": "01_main", "url": "https://grids.obys.agency/"},
    {"name": "02_columns_vandegraaf", "url": "https://grids.obys.agency/columns_vandegraaf"},
    {"name": "03_rectangular_others", "url": "https://grids.obys.agency/rectangular_others"},
    {"name": "04_booksandcredits", "url": "https://grids.obys.agency/booksandcredits"},
]

OUTPUT_DIR = r"premium-frontend-experience-system\reference-inputs\sites\grids-obys-agency\research"

async def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    results = {}

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            viewport={"width": 1920, "height": 1080},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = await context.new_page()

        for pg in PAGES:
            print(f"[SCRAPE] Navigating to {pg['name']} -> {pg['url']}")
            try:
                await page.goto(pg["url"], wait_until="domcontentloaded", timeout=25000)
                await asyncio.sleep(2)

                # Extract text content directly from DOM
                text_content = await page.evaluate("""() => {
                    const texts = [];
                    document.querySelectorAll('h1, h2, h3, h4, h5, p, span, div, a, li').forEach(el => {
                        const txt = el.innerText ? el.innerText.trim() : '';
                        if (txt && txt.length > 2 && !texts.includes(txt) && !txt.includes('\\n')) {
                            texts.push(txt);
                        }
                    });
                    return texts;
                }""")

                # Take full page screenshot
                screenshot_path = os.path.join(OUTPUT_DIR, f"{pg['name']}_fullpage.png")
                await page.screenshot(path=screenshot_path, full_page=True)
                print(f"Saved full page screenshot: {screenshot_path}")

                results[pg["name"]] = {
                    "url": pg["url"],
                    "text_snippets": text_content
                }

            except Exception as e:
                print(f"Error scraping {pg['name']}: {e}")

        await browser.close()

    json_path = os.path.join(OUTPUT_DIR, "scraped_text_analysis.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"[SUCCESS] Fast research scraping complete! Saved to {json_path}")

if __name__ == "__main__":
    asyncio.run(main())
