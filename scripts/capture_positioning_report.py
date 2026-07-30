# -*- coding: utf-8 -*-
import os
from playwright.sync_api import sync_playwright

html_file = r"D:\ZORIXEL-BRAND-OS\deliverables\positioning-report.html"
png_file = r"D:\ZORIXEL-BRAND-OS\deliverables\positioning-report.png"

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1280, "height": 1400})
    page.goto(f"file:///{html_file.replace('\\', '/')}")
    page.wait_for_timeout(1000)
    page.screenshot(path=png_file, full_page=True)
    browser.close()

print(f"Captured screenshot: {png_file}")
