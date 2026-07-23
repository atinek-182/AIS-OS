#!/usr/bin/env python3
"""
Scrapling Runner - Adaptive & Stealthy Web Scraping Engine for AIOS
Powered by Scrapling (d4vinci/Scrapling)

Features:
- Fast HTTP parsing (Fetcher)
- Headless Browser execution (DynamicFetcher)
- Anti-bot stealth header emulation (StealthyFetcher)
- CSS / XPath extraction
"""

import sys
import json
import argparse
from typing import Dict, Any, Optional

Fetcher = None
DynamicFetcher = None
StealthyFetcher = None

try:
    from scrapling import Fetcher
except Exception:
    Fetcher = None

try:
    from scrapling import DynamicFetcher
except Exception:
    DynamicFetcher = None

try:
    from scrapling import StealthyFetcher
except Exception:
    StealthyFetcher = None


def run_scrape(
    url: str,
    mode: str = "fast",
    css: Optional[str] = None,
    xpath: Optional[str] = None,
    text_only: bool = False,
    timeout: int = 30
) -> Dict[str, Any]:
    try:
        page = None
        if mode == "fast":
            if Fetcher is None:
                return {"status": "error", "message": "Fetcher unavailable. Ensure scrapling, curl_cffi, and browserforge are installed."}
            fetcher = Fetcher()
            page = fetcher.get(url)
        elif mode == "dynamic":
            if DynamicFetcher is None:
                return {"status": "error", "message": "DynamicFetcher unavailable. Ensure Playwright dependencies are installed."}
            fetcher = DynamicFetcher()
            page = fetcher.get(url)
        elif mode == "stealth":
            if StealthyFetcher is None:
                return {"status": "error", "message": "StealthyFetcher unavailable. Ensure Camoufox/Playwright dependencies are installed."}
            fetcher = StealthyFetcher()
            page = fetcher.get(url)
        else:
            return {"status": "error", "message": f"Unknown mode: {mode}"}

        if page is None:
            return {"status": "error", "message": "Scrape operation returned empty result"}

        status_code = getattr(page, "status", getattr(page, "status_code", 200))
        results = {
            "status": "success",
            "url": url,
            "mode": mode,
            "status_code": status_code,
            "title": "",
            "matched_elements": [],
            "content": ""
        }

        # Extract title if present
        title_nodes = page.css("title")
        if title_nodes:
            results["title"] = title_nodes[0].text.strip() if hasattr(title_nodes[0], 'text') else str(title_nodes[0])

        # Custom element selection
        if css:
            elements = page.css(css)
            results["matched_elements"] = [
                el.text.strip() if hasattr(el, 'text') and el.text else str(el)
                for el in elements
            ]
        elif xpath:
            elements = page.xpath(xpath)
            results["matched_elements"] = [
                el.text.strip() if hasattr(el, 'text') and el.text else str(el)
                for el in elements
            ]

        # General content text extraction
        if hasattr(page, 'text') and isinstance(page.text, str):
            results["content"] = page.text if text_only else page.text[:10000]
        else:
            body_nodes = page.css("body")
            if body_nodes:
                results["content"] = body_nodes[0].text.strip() if hasattr(body_nodes[0], 'text') else str(body_nodes[0])

        return results

    except Exception as e:
        return {
            "status": "error",
            "url": url,
            "mode": mode,
            "error_type": type(e).__name__,
            "message": str(e)
        }


def main():
    parser = argparse.ArgumentParser(description="AIOS Scrapling Web Scraping Engine")
    parser.add_argument("--url", required=True, help="Target URL to scrape")
    parser.add_argument("--mode", choices=["fast", "dynamic", "stealth"], default="fast", help="Fetcher engine mode")
    parser.add_argument("--css", help="CSS selector to extract")
    parser.add_argument("--xpath", help="XPath selector to extract")
    parser.add_argument("--output", help="Path to save JSON results")
    parser.add_argument("--text-only", action="store_true", help="Extract plain text")
    parser.add_argument("--timeout", type=int, default=30, help="Timeout in seconds")

    args = parser.parse_args()

    result = run_scrape(
        url=args.url,
        mode=args.mode,
        css=args.css,
        xpath=args.xpath,
        text_only=args.text_only,
        timeout=args.timeout
    )

    output_json = json.dumps(result, indent=2)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(output_json)
        print(f"Scrape results saved to: {args.output}")
    else:
        print(output_json)


if __name__ == "__main__":
    main()
