# Autoresearch: Web Speed Optimization Loop

You are an autonomous agent tasked with minifying, inlining, and optimizing a target website inside `target_site/` to improve page load speed and minimize overall file sizes.

## Objectives
* Reduce the total file size (bytes) of all website assets combined (HTML, CSS, JS).
* Minimize the median page load time measured by Python Playwright inside `prepare.py`.

## Experimentation Rules
1. **Target File**: You are only allowed to edit `train.py` (which contains the minifier and asset-bundling optimization script).
2. **Read-Only Lock**: Do NOT modify `prepare.py` or the test runner parameters.
3. **Execution**: Run the evaluation using `python prepare.py`.
4. **Git Controls**:
   * If the evaluation score increases (representing faster load speed and/or smaller bytesize): Commit the change with `git commit -am "optimized speed: [short hypothesis]"`.
   * If the evaluation score does not improve: Discard the edits with `git checkout -- train.py`.
5. **No Interruption**: Run autonomously.
