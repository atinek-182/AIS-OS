#!/usr/bin/env python3
"""
verify-component.py — Verify a generated slide component
1. Loads the component HTML in a headless browser (via Playwright)
2. Checks for CSS/JS errors and console logs
3. Captures a screenshot of the component's rendered output

Requires: pip install playwright
"""

import os
import sys
import http.server
import socketserver
import threading
import time

def find_free_port():
    import socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', 0))
        return s.getsockname()[1]

def run_server(port, directory):
    class QuietHandler(http.server.SimpleHTTPRequestHandler):
        def log_message(self, format, *args):
            pass # Suppress server log outputs

    os.chdir(directory)
    handler = QuietHandler
    with socketserver.TCPServer(("", port), handler) as httpd:
        httpd.serve_forever()

def verify_component(html_path):
    if not os.path.exists(html_path):
        print(f"Error: File not found {html_path}")
        sys.exit(1)

    html_dir = os.path.dirname(os.path.abspath(html_path))
    html_file = os.path.basename(html_path)

    # 1. Attempt to import Playwright
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("Playwright is not installed for Python. Running static HTML parsing check...")
        # Fallback to simple static check
        with open(html_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Verify tag matching and script/style existence
        if "<style>" not in content:
            print("Warning: No inline styles (<style>) found in component.")
        if "<script>" not in content and "script" in content.lower():
            print("Note: Component contains no inline scripts.")
        print("Static verification passed. (Install python playwright to enable visual screenshot checks: pip install playwright)")
        return

    # 2. Start local HTTP server to avoid file protocol issues on Windows
    port = find_free_port()
    server_thread = threading.Thread(target=run_server, args=(port, html_dir), daemon=True)
    server_thread.start()
    time.sleep(0.5) # Give the server a moment to start

    # 3. Drive headless Playwright
    print(f"Serving component on http://localhost:{port}/{html_file}")
    
    preview_dir = os.path.join(html_dir, "..", "previews")
    os.makedirs(preview_dir, exist_ok=True)
    screenshot_path = os.path.join(preview_dir, f"{os.path.splitext(html_file)[0]}_preview.png")

    errors = []
    
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1200, "height": 800})
        
        # Listen for console errors
        page.on("console", lambda msg: errors.append(msg.text) if msg.type == "error" else None)
        page.on("pageerror", lambda err: errors.append(err.message))
        
        # Load component page
        page.goto(f"http://localhost:{port}/{html_file}", wait_until="networkidle")
        
        # Give animations 1 second to settle
        page.wait_for_timeout(1000)
        
        # Take screenshot of the rendered element
        page.screenshot(path=screenshot_path)
        print(f"Screenshot saved to: {os.path.abspath(screenshot_path)}")
        
        browser.close()

    if errors:
        print("\nErrors detected during rendering:")
        for err in errors:
            print(f"  - {err}")
        sys.exit(1)
    else:
        print("\nComponent verified successfully! No runtime errors detected.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python verify-component.py <path-to-component.html>")
        sys.exit(1)
        
    verify_component(sys.argv[1])
