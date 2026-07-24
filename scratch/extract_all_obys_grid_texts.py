import json
import os

widgets_file = r"premium-frontend-experience-system\reference-inputs\sites\grids-obys-agency\mirror\api_viewer_project_3031437_widgets.html"
out_file = r"premium-frontend-experience-system\reference-inputs\sites\grids-obys-agency\research\complete_obys_text_corpus.md"

def extract_texts():
    with open(widgets_file, "r", encoding="utf-8") as f:
        widgets = json.load(f)

    extracted_blocks = []
    
    for w in widgets:
        if w.get("type") == "text":
            blocks = w.get("blocks", [])
            for b in blocks:
                txt = b.get("text", "").strip()
                if txt and len(txt) > 1:
                    extracted_blocks.append(txt)

    # De-duplicate while preserving order
    unique_texts = []
    for t in extracted_blocks:
        if t not in unique_texts:
            unique_texts.append(t)

    with open(out_file, "w", encoding="utf-8") as f:
        f.write("# 📖 Complete Extracted Text Corpus: Grids by Obys Agency\n\n")
        f.write(f"Total Text Blocks Extracted: {len(unique_texts)}\n\n")
        f.write("---\n\n")
        for idx, text in enumerate(unique_texts, 1):
            f.write(f"### Block {idx}\n{text}\n\n")

    print(f"Extracted {len(unique_texts)} text blocks into {out_file}")

if __name__ == "__main__":
    extract_texts()
