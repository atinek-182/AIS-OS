---
category: template
tags: [autoresearch, templates, boilerplate, configurations, dockerfile]
created: 2026-07-17
updated: 2026-07-17
sources:
  - "[[raw/web-clips/2026-07-17-stop-fixing-your-claude-skills.-autoresearch-does-it-for-you 1.md]]"
---

# Template: Autoresearch Configuration

This page provides the boilerplate files and configurations needed to initialize a safe, low-resource Autoresearch loop in ZORIXEL AIOS.

---

## 1. Boilerplate `program.md` (Prompt/Skill Tuning)
Create this file as `trials/skill-optimizer/program.md` to guide the optimization agent:

```markdown
# Autoresearch: Skill Optimization Protocol

You are an autonomous agent tasked with optimizing the custom AIOS skill prompt in `train.py`.

## Objectives
* Improve the quality, formatting, and reliability of generated outputs.
* Your goal is to maximize the score returned by the evaluation script.

## Setup Instructions
1. Run `git checkout -b autoresearch/prompt-tuning` (if not already on the branch).
2. Establish the baseline by running the unmodified prompt through `python prepare.py`.
3. Log the initial score to `results.tsv`.

## Experimentation Rules
1. **Target File**: You are only allowed to edit `train.py` (which contains the prompt instructions).
2. **Read-Only Lock**: Do NOT modify `prepare.py` or the files under `/tests/`.
3. **Execution**: Run the evaluation using `uv run python prepare.py`.
4. **Git Controls**:
   * If the evaluation score increases: Commit the change with `git commit -am "optimized prompt: [short hypothesis]"`.
   * If the evaluation score does not improve or the run fails: Discard the edits with `git reset --hard`.
5. **No Interruption**: Run autonomously. Do not pause to ask the user for confirmation.
```

---

## 2. Boilerplate `prepare.py` (Secure Evaluation Harness)
Create this file as `trials/skill-optimizer/prepare.py` to handle generation testing and scoring:

```python
import os
import sys
import subprocess

# Strict budget guardrails
MAX_TRIALS = 20
TEST_CASES_PATH = "./tests/"

def load_test_cases():
    # Load inputs from the tests directory
    cases = []
    for file in sorted(os.listdir(TEST_CASES_PATH)):
        with open(os.path.join(TEST_CASES_PATH, file), "r") as f:
            cases.append(f.read())
    return cases

def run_candidate(input_text):
    # Executes the mutated candidate prompt in train.py
    # We call train.py as a subprocess to keep the execution isolated
    try:
        process = subprocess.run(
            ["python", "train.py", input_text],
            capture_output=True,
            text=True,
            timeout=15 # Hard timeout limit in seconds
        )
        return process.stdout
    except subprocess.TimeoutExpired:
        return ""

def evaluate_output(output):
    # Vision or text evaluation checklist (grades 0 or 1 for each rule)
    score = 0
    # Rule 1: Output Legibility
    if output and "ERROR" not in output and len(output.strip()) > 10:
        score += 1
    # Rule 2: Contains expected sections
    if "## Details" in output:
        score += 1
    # Rule 3: Pastel colors (for diagrams)
    if "pastel" in output.lower():
        score += 1
    # Rule 4: No index ordering numbers
    if not any(char.isdigit() for char in output.split("\n")[0]):
        score += 1
    return score

def main():
    test_cases = load_test_cases()
    total_score = 0
    
    for case in test_cases:
        output = run_candidate(case)
        total_score += evaluate_output(output)
        
    # Print the scalar score for the agent to read
    print(f"---")
    print(f"val_score: {total_score}")
    print(f"max_score: {len(test_cases) * 4}")

if __name__ == "__main__":
    main()
```

---

## 3. Boilerplate `Dockerfile` (Sandbox Container)
Save this as `trials/Dockerfile` to construct the isolated runtime container:

```dockerfile
# Use a lightweight python runtime
FROM python:3.10-slim

# Install system dependencies if needed (e.g. git)
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install uv package manager
RUN pip install --no-cache-dir uv

# Create non-root app user
RUN useradd -u 8888 appuser
WORKDIR /app

# Grant permissions and switch to user
RUN chown -R appuser /app
USER appuser

# Set runtime environmental variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
```
