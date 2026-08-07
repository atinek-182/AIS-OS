import base64
import os
import sys

FONTS_DIR = r"d:\AI-OS\projects\font-showcase\fonts"
SCRIPT_HTML = r"d:\AI-OS\clients\001-vashishthya-research-edu\01-pre-outreach-audit\03-pitch-and-loom-guides\LOOM_VIDEO_DEMO_SCRIPT_GUIDE.html"
SCRIPT_PDF = r"d:\AI-OS\clients\001-vashishthya-research-edu\01-pre-outreach-audit\03-pitch-and-loom-guides\LOOM_VIDEO_DEMO_SCRIPT_GUIDE.pdf"

def run_pdf_health_check():
    print("Running ZORIXEL AIOS PDF & Font Health Verification Sweep...")
    errors = []

    # Check 1: Required Font Files Exist
    required_fonts = ["Havock.otf", "Rosehot.ttf", "Nuqun-Regular.otf"]
    for font in required_fonts:
        font_path = os.path.join(FONTS_DIR, font)
        if not os.path.exists(font_path):
            errors.append(f"Missing required brand font: {font_path}")
        else:
            print(f"[OK] Found brand font: {font}")

    # Check 2: HTML Source File Exists and Contains Base64 Fonts
    if not os.path.exists(SCRIPT_HTML):
        errors.append(f"Missing HTML source template: {SCRIPT_HTML}")
    else:
        with open(SCRIPT_HTML, "r", encoding="utf-8") as f:
            html_content = f.read()
        if "data:font/otf;base64," not in html_content and "data:font/ttf;base64," not in html_content:
            errors.append("HTML source template lacks base64 embedded fonts.")
        else:
            print("[OK] HTML source template contains verified base64 embedded fonts.")

        if 'class="brand-logo-nuqun"' not in html_content:
            errors.append("HTML template missing native Nuqun font logo element.")
        else:
            print("[OK] HTML template contains verified native Nuqun font logo element.")

    # Check 3: PDF File Exists and is non-zero
    if not os.path.exists(SCRIPT_PDF):
        errors.append(f"Missing generated PDF file: {SCRIPT_PDF}")
    else:
        pdf_size = os.path.getsize(SCRIPT_PDF)
        if pdf_size < 10000:
            errors.append(f"Generated PDF file is abnormally small ({pdf_size} bytes).")
        else:
            print(f"[OK] Verified PDF output file size: {pdf_size} bytes.")

    if errors:
        print("\n[ERROR] PDF Health Verification Failed:")
        for err in errors:
            print(f"  - {err}")
        sys.exit(1)
    else:
        print("\n[SUCCESS] ALL PDF & FONT HEALTH CHECKS PASSED CLEANLY!")

if __name__ == "__main__":
    run_pdf_health_check()
