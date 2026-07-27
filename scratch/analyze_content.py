import json

with open('scratch/structured_transcript.json', 'r', encoding='utf-8') as f:
    transcript = json.load(f)

print("--- TRANSCRIPT ANALYSIS ---")
for chapter, text in transcript.items():
    print(f"\n### {chapter} ({len(text.split())} words)")
    # Extract first 300 chars preview
    print("Preview:", text[:350] + "...")
