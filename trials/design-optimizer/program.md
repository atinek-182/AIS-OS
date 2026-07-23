# Autoresearch: Vision-in-the-Loop Design Optimization

You are an autonomous agent tasked with optimizing the visual appearance of an Instagram carousel slide by modifying `train.py` (which contains style properties and layouts).

## Objectives
* Improve the layout aesthetics, typography, color pairing, card containers, and visual hierarchy of the slide.
* Maximize the visual score returned by the multimodal Vision API grading harness in `prepare.py`.

## Experimentation Rules
1. **Target File**: You are only allowed to edit `train.py` (specifically, CSS properties and HTML layout components).
2. **Read-Only Lock**: Do NOT modify `prepare.py` or the reference images.
3. **Execution**: Run the evaluation using `python prepare.py`.
4. **Git Controls**:
   * If the evaluation score increases: Commit the change with `git commit -am "optimized design: [short hypothesis]"`.
   * If the evaluation score does not improve: Discard the edits with `git checkout -- train.py`.
5. **No Interruption**: Run autonomously.
