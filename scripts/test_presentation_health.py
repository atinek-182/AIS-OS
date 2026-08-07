import os
import sys

TARGET_HTML_1 = r"d:\AI-OS\clients\001-vashishthya-research-edu\01-pre-outreach-audit\04-visual-assets-and-previews\vashishthya_loom_presentation.html"
TARGET_HTML_2 = r"d:\AI-OS\clients\001-vashishthya-research-edu\04-visual-assets-and-previews\notion_google_sync_presentation.html"

REQUIRED_STRINGS = [
    "data:font/otf;base64,",
    "data:font/ttf;base64,",
    "line-height: 1.28",
    "notion_user_screenshot.png",
    "gsheet_user_screenshot.png",
    "https://app.notion.com/p/Vashishthya-Master-Client-Desk",
    "https://docs.google.com/spreadsheets/d/1HK6B26dVJuaNCM9vkfbe781iZttJr16O7gCPJBEuCh0",
    "lightbox-modal",
    "openModal",
    "Slide 1 / 9",
    "Instant Plagiarism Estimator"
]

def check_file(filepath):
    if not os.path.exists(filepath):
        print(f"[ERROR] File not found: {filepath}")
        return False
    
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
        
    missing = []
    for req in REQUIRED_STRINGS:
        if req not in content:
            missing.append(req)
            
    if missing:
        print(f"[ERROR] {filepath} is missing required elements: {missing}")
        return False
    else:
        print(f"[SUCCESS] {os.path.basename(filepath)} passed all health checks.")
        return True

def main():
    print("Running ZORIXEL AIOS Presentation Health Sweep...")
    res1 = check_file(TARGET_HTML_1)
    res2 = check_file(TARGET_HTML_2)
    
    if res1 and res2:
        print("ALL PRESENTATION HEALTH CHECKS PASSED CLEANLY!")
        sys.exit(0)
    else:
        print("HEALTH CHECK FAILED!")
        sys.exit(1)

if __name__ == "__main__":
    main()
