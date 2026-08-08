import os
import re
import glob

# Comprehensive emoji mapping to clean text headers / labels
EMOJI_REPLACEMENTS = {
    "⚡": "",
    "🎯": "",
    "👥": "",
    "⚖️": "",
    "🔗": "",
    "🔄": "",
    "📌": "",
    "📝": "",
    "🛡️": "",
    "🧠": "",
    "🗣️": "",
    "🛠️": "",
    "💡": "",
    "🚀": "",
    "⚠️": "",
    "✅": "",
    "❌": "",
    "🔥": "",
    "✨": "",
    "⭐": "",
    "🎉": "",
    "📦": "",
    "🎨": "",
    "🔍": "",
    "📊": "",
    "📁": "",
    "📄": "",
    "💻": "",
    "🔧": "",
    "🤖": "",
    "💬": "",
    "📢": "",
    "🚨": "",
    "🛑": "",
    "🔒": "",
    "🔑": "",
    "🏆": "",
    "💎": "",
    "▶️": "",
    "⏹️": "",
    "🔼": "",
    "🔽": "",
    "🚩": "",
    "🏷️": "",
}

def clean_file_content(content):
    modified = content
    # Replace individual emojis
    for emoji, replacement in EMOJI_REPLACEMENTS.items():
        modified = modified.replace(emoji, replacement)
    
    # Clean up double spaces created by emoji removal at start of headings
    modified = re.sub(r'^(#+\s+)\s+', r'\1', modified, flags=re.MULTILINE)
    modified = re.sub(r'\|\s+([A-Z])', r'| \1', modified)
    
    return modified

def process_skills(skills_dir):
    skills_files = glob.glob(os.path.join(skills_dir, "**", "*.md"), recursive=True)
    modified_count = 0
    total_files = len(skills_files)

    print(f"[SKILL UPGRADE] Scanning {total_files} markdown files in {skills_dir}...")

    for file_path in skills_files:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            cleaned = clean_file_content(content)

            if cleaned != content:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(cleaned)
                modified_count += 1
                rel_path = os.path.relpath(file_path, skills_dir)
                print(f"  [CLEANED] {rel_path}")
        except Exception as e:
            print(f"  [ERROR] Could not process {file_path}: {e}")

    print(f"\n[SUCCESS] Upgraded {modified_count} out of {total_files} files across all skills!")

if __name__ == "__main__":
    skills_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".agents", "skills"))
    process_skills(skills_path)
