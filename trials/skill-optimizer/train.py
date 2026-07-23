import os
import sys
import time
from google import genai
from google.genai import types

# The system prompt under optimization. The agent will mutate this text block.
SYSTEM_PROMPT = """
You are an expert technical designer. Generate a clean, well-spaced Excalidraw diagram JSON representing the user's description.
Use Virgil (handwritten) font. Maintain clear linear flow (left-to-right or top-to-bottom).
Color guidelines:
- Blue (#1971c2, fill: #e7f5ff) for input/sources
- Yellow (#f59f00, fill: #fff9db) for processing
- Green (#2f9e44, fill: #d3f9d8) for output/database
- Purple (#862e9c, fill: #f3d9fa) for shared layers
Use soft pastel colors. Ensure high text contrast using #1e1e1e for labels. Do not use numbers or ordinals in main labels.

Output ONLY valid raw JSON conforming to this Excalidraw shell:
{
  "type": "excalidraw",
  "version": 2,
  "source": "https://excalidraw.com",
  "elements": [
    ...
  ],
  "appState": {
    "gridSize": null,
    "viewBackgroundColor": "#ffffff"
  },
  "files": {}
}
Do not wrap it in markdown code blocks like ```json.
"""

def main():
    if len(sys.argv) < 2:
        print("Error: Missing input description")
        sys.exit(1)
    
    input_text = sys.argv[1]
    
    try:
        client = genai.Client()
        response = None
        for attempt in range(5):
            try:
                response = client.models.generate_content(
                    model='gemini-3.1-flash-lite',
                    contents=input_text,
                    config=types.GenerateContentConfig(
                        system_instruction=SYSTEM_PROMPT,
                        temperature=0.1,
                    )
                )
                break
            except Exception as e:
                if attempt < 4 and ("503" in str(e) or "429" in str(e) or "unavailable" in str(e).lower() or "quota" in str(e).lower()):
                    time.sleep(5)
                else:
                    raise e
                    
        if response:
            print(response.text)
        else:
            print("ERROR: API failed to return response after retries")
    except Exception as e:
        print(f"ERROR: {str(e)}")

if __name__ == "__main__":
    main()
