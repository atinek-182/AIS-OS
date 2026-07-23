import os
import sys
import subprocess
import shutil
import time
import re

# Define directories
TRIALS_DIR = os.path.dirname(os.path.abspath(__file__))
TARGETS = ["skill-optimizer", "design-optimizer", "web-optimizer"]

def check_docker():
    """Check if Docker is available in the system PATH."""
    return shutil.which("docker") is not None

def run_evaluation(target, use_docker=True):
    """Run prepare.py for the specified target inside Docker or locally."""
    target_path = os.path.join(TRIALS_DIR, target)
    prepare_script = os.path.join(target_path, "prepare.py")
    
    if not os.path.exists(prepare_script):
        print(f"Error: {prepare_script} not found.")
        return False
        
    print(f"\n==========================================")
    print(f"Evaluating Target: {target}")
    print(f"==========================================")
    
    # Check if GEMINI_API_KEY is available
    if "GEMINI_API_KEY" not in os.environ or not os.environ["GEMINI_API_KEY"]:
        # We try to read it from a local .env file in the workspace root
        dotenv_path = os.path.join(TRIALS_DIR, "..", ".env")
        if os.path.exists(dotenv_path):
            with open(dotenv_path, "r", encoding="utf-8") as f:
                for line in f:
                    # Strip spaces and comments
                    line_clean = line.strip()
                    if line_clean.startswith("#"):
                        continue
                    if "GEMINI_API_KEY" in line_clean:
                        parts = line_clean.split("=", 1)
                        if len(parts) == 2:
                            val = parts[1].split("#")[0].strip().strip('"').strip("'")
                            os.environ["GEMINI_API_KEY"] = val
                            break
                            
    # Fail closed if API key is missing or empty
    if "GEMINI_API_KEY" not in os.environ or not os.environ["GEMINI_API_KEY"]:
        print("CRITICAL ERROR: GEMINI_API_KEY is not set in environment or .env file! Exiting to prevent execution failure.", file=sys.stderr)
        sys.exit(1)

    
    if use_docker:
        print("Using Sandboxed Docker execution...")
        # Compile command
        # Mount the trials folder to /app inside container, set working directory, run python prepare.py
        # Cap resource limits at --cpus="0.5" and --memory="1536m" (1.5 GB)
        cmd = [
            "docker", "run", "--rm",
            "--cpus", "0.5",
            "--memory", "1536m",
            "-e", f"GEMINI_API_KEY={os.environ.get('GEMINI_API_KEY', '')}",
            "-v", f"{TRIALS_DIR}:/app",
            "aios-sandbox",
            "python", f"{target}/prepare.py"
        ]
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            print(result.stdout)
            print(result.stderr)
            return True
        except subprocess.CalledProcessError as e:
            print(f"Docker execution failed: {e}")
            print(f"Stdout:\n{e.stdout}")
            print(f"Stderr:\n{e.stderr}")
            return False
    else:
        print("Docker not found. Falling back to native host execution...")
        # Check if python virtual env exists in trials/
        venv_dir = os.path.join(TRIALS_DIR, ".venv")
        if not os.path.exists(venv_dir):
            print("Initializing local virtual environment in trials/.venv...")
            subprocess.run([sys.executable, "-m", "venv", venv_dir], check=True)
            
            # Install dependencies in the local venv
            pip_executable = os.path.join(venv_dir, "Scripts", "pip") if os.name == "nt" else os.path.join(venv_dir, "bin", "pip")
            print("Installing dependencies: playwright, google-genai...")
            subprocess.run([pip_executable, "install", "playwright", "google-genai"], check=True)
            
            playwright_executable = os.path.join(venv_dir, "Scripts", "playwright") if os.name == "nt" else os.path.join(venv_dir, "bin", "playwright")
            print("Downloading Playwright Chromium binaries...")
            subprocess.run([playwright_executable, "install", "chromium"], check=True)
            
        # Run using virtual env python
        python_executable = os.path.join(venv_dir, "Scripts", "python") if os.name == "nt" else os.path.join(venv_dir, "bin", "python")
        
        # Execute prepare.py from the target directory
        try:
            result = subprocess.run(
                [python_executable, "prepare.py"],
                cwd=target_path,
                capture_output=True,
                text=True,
                check=True
            )
            print(result.stdout)
            return True
        except subprocess.CalledProcessError as e:
            print(f"Local host execution failed: {e}")
            print(f"Stdout:\n{e.stdout}")
            print(f"Stderr:\n{e.stderr}")
            return False

def mutate_candidate(target):
    """Mutate train.py using Gemini instructions in program.md and prior results."""
    target_path = os.path.join(TRIALS_DIR, target)
    program_path = os.path.join(target_path, "program.md")
    train_path = os.path.join(target_path, "train.py")
    results_path = os.path.join(target_path, "results.tsv")
    
    with open(program_path, "r") as f:
        program = f.read()
    with open(train_path, "r") as f:
        train_code = f.read()
        
    history = ""
    if os.path.exists(results_path):
        with open(results_path, "r") as f:
            history = f.read()
            
    from google import genai
    from google.genai import types
    
    client = genai.Client()
    
    prompt = f"""
    You are an Autoresearch Optimization Agent. Your job is to improve the candidate code in `train.py` based on the goals in `program.md`.
    Analyze the current `train.py` code, the program objectives, and the evaluation score history.
    Propose a single, precise mutation hypothesis (e.g. adjust a style variable, improve prompt clarity, optimize regex minifier logic) and rewrite the code to implement it.
    
    Rules:
    - Output ONLY the complete, raw python code for `train.py`.
    - Do not wrap the code in markdown code blocks like ```python.
    - Preserve all structural interfaces, imports, and execution entry points.
    
    Objectives:
    {program}
    
    Current train.py Code:
    {train_code}
    
    Evaluation History (tsv showing timestamps, scores, max_scores):
    {history}
    """
    
    print(f"Querying Gemini to generate a mutation for {target}...")
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=0.7 # Give it some creativity for optimization exploration
            )
        )
        new_code = response.text.strip()
        
        # Clean markdown code wrapper if any was generated
        if new_code.startswith("```"):
            lines = new_code.split("\n")
            if lines[0].startswith("```"):
                lines = lines[1:]
            if lines[-1].startswith("```"):
                lines = lines[:-1]
            new_code = "\n".join(lines)
            
        with open(train_path, "w") as f:
            f.write(new_code)
            
        print("Generated mutation written to train.py.")
        return True
    except Exception as e:
        print(f"Failed to generate mutation: {str(e)}")
        return False

def get_latest_score(target):
    """Retrieve the latest score from results.tsv."""
    results_path = os.path.join(TRIALS_DIR, target, "results.tsv")
    if not os.path.exists(results_path):
        return 0
    with open(results_path, "r") as f:
        lines = f.readlines()
        if not lines:
            return 0
        last_line = lines[-1].strip().split("\t")
        if len(last_line) >= 2:
            return int(last_line[1])
    return 0

def run_optimization_loop(target, iterations=20, use_docker=True):
    """Run the complete mutation-evaluate-select loop."""
    print(f"\n==========================================")
    print(f"Starting Autoresearch Loop for: {target}")
    print(f"Iterations: {iterations}")
    print(f"==========================================")
    
    # 1. Measure baseline
    print("Measuring baseline score...")
    run_evaluation(target, use_docker)
    baseline_score = get_latest_score(target)
    print(f"Baseline Score established: {baseline_score}")
    
    current_best = baseline_score
    
    for i in range(iterations):
        print(f"\n--- Iteration {i+1}/{iterations} ---")
        
        # Mutate
        success = mutate_candidate(target)
        if not success:
            continue
            
        # Evaluate
        eval_success = run_evaluation(target, use_docker)
        if not eval_success:
            print("Evaluation failed, resetting candidate...")
            subprocess.run(["git", "checkout", "--", os.path.join(TRIALS_DIR, target, "train.py")], check=True)
            continue
            
        # Compare
        new_score = get_latest_score(target)
        print(f"Current best: {current_best} | New score: {new_score}")
        
        if new_score > current_best:
            print("Success! Score improved. Committing changes...")
            current_best = new_score
            # Host commit
            train_file_path = os.path.join(TRIALS_DIR, target, "train.py")
            subprocess.run(["git", "add", train_file_path], check=True)
            subprocess.run(["git", "commit", "-m", f"autoresearch: optimized {target} to score {new_score}"], check=True)
        else:
            print("Score did not improve. Resetting changes...")
            train_file_path = os.path.join(TRIALS_DIR, target, "train.py")
            subprocess.run(["git", "checkout", "--", train_file_path], check=True)
            
    print(f"\nAutoresearch loop finished. Final best score: {current_best}")

def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python runner.py verify           - Run a baseline check on all 3 target setups")
        print("  python runner.py optimize [target] - Run a mutation loop on one target (e.g. skill-optimizer)")
        sys.exit(1)
        
    action = sys.argv[1]
    use_docker = check_docker()
    
    if not use_docker:
        print("System Note: docker.exe not detected in PATH. Defaulting to local venv fallback mode.")
        
    if action == "verify":
        print("Starting baseline verification run...")
        for target in TARGETS:
            run_evaluation(target, use_docker)
        print("\nAll baselines completed.")
        
    elif action == "optimize":
        if len(sys.argv) < 3:
            print("Error: Specify a target (skill-optimizer, design-optimizer, or web-optimizer)")
            sys.exit(1)
        target = sys.argv[2]
        if not re.match(r'^[a-zA-Z0-9_-]+$', target):
            print("Error: Invalid target name. Only alphanumeric characters, dashes, and underscores are allowed.")
            sys.exit(1)
        if target not in TARGETS:
            print(f"Error: Target '{target}' not recognized. Must be one of: {TARGETS}")
            sys.exit(1)
        run_optimization_loop(target, iterations=20, use_docker=use_docker)
    else:
        print(f"Error: Action '{action}' not recognized.")

if __name__ == "__main__":
    main()
