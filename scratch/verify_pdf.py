import os

pdf_path = r"d:\AI-OS\clients\001-vashishthya-research-edu\01-pre-outreach-audit\03-pitch-and-loom-guides\LOOM_VIDEO_DEMO_SCRIPT_GUIDE.pdf"
if os.path.exists(pdf_path):
    size = os.path.getsize(pdf_path)
    print(f"PDF exists: {pdf_path} ({size / 1024:.2f} KB)")
else:
    print("PDF does not exist!")
