import os
import sys
import json
import subprocess
import time
from google import genai
from google.genai import types

TEST_CASES_PATH = "./skill-optimizer/tests" if os.path.exists("./skill-optimizer/tests") else "./tests"
RESULTS_PATH = "./skill-optimizer/results.tsv" if os.path.exists("./skill-optimizer") else "./results.tsv"

def load_test_cases():
    cases = []
    if not os.path.exists(TEST_CASES_PATH):
        os.makedirs(TEST_CASES_PATH, exist_ok=True)
    
    files = sorted(os.listdir(TEST_CASES_PATH))
    for file in files:
        if file.endswith(".txt"):
            with open(os.path.join(TEST_CASES_PATH, file), "r") as f:
                cases.append((file, f.read()))
    return cases

def run_candidate(input_text):
    # Runs the candidate prompt script train.py on the host or inside docker
    script_path = "./skill-optimizer/train.py" if os.path.exists("./skill-optimizer/train.py") else "./train.py"
    try:
        process = subprocess.run(
            [sys.executable, script_path, input_text],
            capture_output=True,
            text=True,
            timeout=15
        )
        return process.stdout.strip()
    except subprocess.TimeoutExpired:
        return ""
    except Exception as e:
        return f"ERROR: {str(e)}"

def evaluate_output(output):
    # Rule 1: Is it valid JSON?
    is_valid_json = 0
    try:
        data = json.loads(output)
        if data.get("type") == "excalidraw" and "elements" in data:
            is_valid_json = 1
    except Exception:
        pass
        
    if not is_valid_json:
        return 0, [0, 0, 0, 0] # Fails everything if JSON is broken

    # For the remaining rules, we query the Gemini API to grade the JSON structure
    client = genai.Client()
    
    prompt = f"""
    Review the following Excalidraw diagram JSON structure and answer these three questions with EXACTLY 'Yes' or 'No'.
    Do not add any other text. Follow this format:
    Q1: [Yes/No]
    Q2: [Yes/No]
    Q3: [Yes/No]

    Questions:
    1. Are the colors used in the elements limited to soft, professional pastel colors (e.g. #e7f5ff, #fff9db, #d3f9d8, #f3d9fa) and free of neon borders?
    2. Is the layout linearly spaced with elements clearly offset from one another (no overlapping coordinates or exact same positions)?
    3. Are numeric ordinals (like "1.", "2.", "First", "Second") absent from all labels and annotations?

    Excalidraw JSON:
    {output[:4000]}  # Cap output to avoid token bloating
    """
    
    try:
        response = None
        for attempt in range(5):
            try:
                response = client.models.generate_content(
                    model='gemini-3.1-flash-lite',
                    contents=prompt,
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
        
        rule_pastel = 1 if "q1: yes" in resp_text else 0
        rule_spacing = 1 if "q2: yes" in resp_text else 0
        rule_ordinals = 1 if "q3: yes" in resp_text else 0
    except Exception as e:
        # Fallback to defaults on API error
        rule_pastel, rule_spacing, rule_ordinals = 0, 0, 0

    scores = [is_valid_json, rule_pastel, rule_spacing, rule_ordinals]
    return sum(scores), scores

def main():
    test_cases = load_test_cases()
    if not test_cases:
        print("ERROR: No test cases found in tests/ directory.")
        sys.exit(1)
        
    total_score = 0
    detailed_scores = []
    
    print(f"Running evaluation on {len(test_cases)} test cases...")
    for filename, case in test_cases:
        output = run_candidate(case)
        score, subscores = evaluate_output(output)
        total_score += score
        detailed_scores.append(f"{filename}: {score}/4 (JSON={subscores[0]}, Pastel={subscores[1]}, Spacing={subscores[2]}, Ordinals={subscores[3]})")
        print(f" - {filename}: Score {score}/4")
        time.sleep(0.5) # Avoid API rate limit
        
    max_score = len(test_cases) * 4
    print(f"\n--- Evaluation Complete ---")
    print(f"val_score: {total_score}")
    print(f"max_score: {max_score}")
    
    # Save the score to results.tsv
    with open(RESULTS_PATH, "a") as f:
        f.write(f"{int(time.time())}\t{total_score}\t{max_score}\n")
        
    for detail in detailed_scores:
        print(detail)

if __name__ == "__main__":
    main()
