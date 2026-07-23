# Autoresearch: Skill Optimization Protocol

You are an autonomous agent tasked with optimizing the custom AIOS skill prompt in `train.py` to maximize the diagram quality score.

## Objectives
* Improve the layout structure, color harmony, and text contrast of the generated Excalidraw diagrams.
* Maximize the legibility score returned by the evaluation script `prepare.py`.

## Experimentation Rules
1. **Target File**: You are only allowed to edit `train.py` (specifically, the system prompt text inside `SYSTEM_PROMPT = """..."""`).
2. **Read-Only Lock**: Do NOT modify `prepare.py` or the test cases under `/tests/`.
3. **Execution**: Run the evaluation using `python prepare.py` (which runs in the sandbox).
4. **Git Controls**:
   * If the evaluation score increases: The host runner will commit the change with `git commit -am "optimized prompt: [short hypothesis]"`.
   * If the score does not improve or fails: The host runner will discard the edits with `git checkout -- train.py`.
5. **No Interruption**: Run autonomously.
