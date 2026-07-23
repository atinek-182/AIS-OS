import os
import sys
import time
import os
import subprocess
import threading
import http.server
import socketserver
from playwright.sync_api import sync_playwright
from google import genai
from google.genai import types

PORT = 8081
BASE_DIR = "./design-optimizer" if os.path.exists("./design-optimizer") else "."
RENDERS_DIR = os.path.join(BASE_DIR, "renders")
RESULTS_PATH = os.path.join(BASE_DIR, "results.tsv")

class SilentHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass

def start_server(httpd):
    httpd.serve_forever()

def evaluate_design_vision(image_path):
    client = genai.Client()
    
    # Read image bytes
    with open(image_path, "rb") as f:
        image_bytes = f.read()
        
    prompt = """
    Review the attached Instagram slide card screenshot and rate it against these four criteria.
    Answer with EXACTLY 'Yes' or 'No'. Do not add any extra explanations.
    Format your response like this:
    Q1: [Yes/No]
    Q2: [Yes/No]
    Q3: [Yes/No]
    Q4: [Yes/No]

    Criteria:
    1. Contrast & Legibility: Is all text clean, high-contrast, and easily readable against the background?
    2. Color Harmony & Taste: Are colors balanced and professional (avoiding plain solid backgrounds, neon clashes, or basic defaults)?
    3. Margins & Padding: Is there breathing room? Elements should be centered with clear margins and not crowded to the edges.
    4. Premium Visual Details: Does the card feel high-end, utilizing delicate borders, subtle shadows, clean gradients, or light backdrop filters?
    """
    
    try:
        response = None
        for attempt in range(5):
            try:
                response = client.models.generate_content(
                    model='gemini-3.1-flash-lite',
                    contents=[
                        types.Part.from_bytes(
                            data=image_bytes,
                            mime_type="image/png",
                        ),
                        prompt
                    ],
                    config=types.GenerateContentConfig(
                        temperature=0.0
                    )
                )
                break
            except Exception as e:
                if attempt < 4 and ("503" in str(e) or "429" in str(e) or "unavailable" in str(e).lower() or "quota" in str(e).lower()):
                    time.sleep(5)
                else:
                    raise e
                    
        resp_text = response.text.strip().lower() if response else ""
        
        score_contrast = 1 if "q1: yes" in resp_text else 0
        score_colors = 1 if "q2: yes" in resp_text else 0
        score_margins = 1 if "q3: yes" in resp_text else 0
        score_details = 1 if "q4: yes" in resp_text else 0
    except Exception as e:
        print(f"Vision API Error: {str(e)}")
        score_contrast, score_colors, score_margins, score_details = 0, 0, 0, 0
        
    subscores = [score_contrast, score_colors, score_margins, score_details]
    return sum(subscores), subscores

def main():
    # 1. Run train.py to compile HTML & CSS
    train_script = "./design-optimizer/train.py" if os.path.exists("./design-optimizer/train.py") else "./train.py"
    subprocess.run(["python", train_script], check=True)
    
    # 2. Start local HTTP server to host the files
    os.makedirs(RENDERS_DIR, exist_ok=True)
    
    # Run the HTTP server from the design-optimizer folder
    original_cwd = os.getcwd()
    os.chdir(BASE_DIR)
    
    handler = SilentHTTPRequestHandler
    socketserver.TCPServer.allow_reuse_address = True
    httpd = socketserver.TCPServer(("", PORT), handler)
    
    server_thread = threading.Thread(target=start_server, args=(httpd,))
    server_thread.daemon = True
    server_thread.start()
    
    print("Serving files locally for Playwright capture...")
    time.sleep(1) # Give server a second to start
    
    screenshot_path = "./renders/slide.png"
    
    # 3. Use Playwright to capture screenshot of slide
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.set_viewport_size({"width": 1080, "height": 1080})
            
            # Navigate to the local server
            page.goto(f"http://localhost:{PORT}/slide.html", wait_until="networkidle")
            page.screenshot(path=screenshot_path)
            browser.close()
            
        print("Screenshot captured successfully.")
        
        # 4. Evaluate using Vision API
        score, subscores = evaluate_design_vision(screenshot_path)
        print(f"Visual Score: {score}/4 (Contrast={subscores[0]}, Harmony={subscores[1]}, Margins={subscores[2]}, Details={subscores[3]})")
        
        # Write results
        with open("results.tsv", "a") as f:
            f.write(f"{int(time.time())}\t{score}\t4\n")
            
    except Exception as e:
        print(f"Error during rendering/evaluation: {str(e)}")
        score = 0
    finally:
        # 5. Terminate server and return directory
        httpd.shutdown()
        httpd.server_close()
        os.chdir(original_cwd)
        
    print(f"Design optimization evaluation complete. Score logged: {score}/4")

if __name__ == "__main__":
    main()
