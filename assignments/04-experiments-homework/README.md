# Homework 4 — Experiments

End-to-end analyst readout of an A/B experiment, framed as a product case. Six parts and a bonus.

- **Deadline:** Tuesday, June 2, 2026, 23:59 (Barcelona time)
- **Total points:** 10
- **Solo work**
- **Submission:** the completed `homework.ipynb` via Google Classroom

## On using AI

Feel free to use ChatGPT, Claude, Copilot, etc. for **documentation lookup** and **routine coding** — library syntax, plot styling, debugging an `IndexError`. That saves time and is exactly what you would do at work.

Everything that touches the **mathematics, the logic, and the structure of the solution** I am counting on you to do yourself. Setting up the MDE formula, picking metrics for the Bonferroni family, reading the readout table, writing the interpretation — those are the parts where the assignment is supposed to teach you something. If an AI hands you those, you have not learned them.

I am trusting you to be honest about this. The intellectual work is yours.

## Files

- `homework.ipynb` — the assignment notebook. Open it, fill in the `...` placeholders, run all cells.
- `ab_data.csv` — the experiment readout (one row per user, 9 columns).
- `_grader.py` — the grader. You import `check_answer` from it. Do not modify.

## How the grader works

After each task you call `check_answer(task_id, your_value)`. It prints either `PASS` or `FAIL` (without the expected value). You iterate until everything passes.

## Library expectations

Use whatever you prefer for visualisation — `matplotlib`, `seaborn`, `plotly`. The grader only checks numerics. Numerics via `numpy`, `pandas`, and `scipy.stats`.

## Parts and grading (10 points total)

| Part | Topic | Points |
|---|---|---|
| 1 | Planning: MDE and weeks per metric (ARPU, ARPPU, usage, paying, latency, error). Uniform $\alpha = 0.05$, $\beta = 0.20$. | — |
| 2 | Health: sample ratio mismatch ($\chi^2$). | — |
| 3 | Analysis: one readout table over all 6 metrics + Bonferroni decision + 2–3 sentence interpretation. | — |
| 4 | CUPED: variance reduction table on `usage_minutes` and `revenue` (with `usage_pre` as the covariate). | — |
| Bonus | Delta-method CI for the relative lift on revenue. | — |
| ★ 5 | Simulation: peeking inflates the FPR. | 1.0 |
| ★ 6 | Simulation: power as a function of $n$. | 1.0 |

**Grading scheme.** The base **8 / 10** comes from completing **Parts 1–4 + Bonus** — the `check_answer` calls in those parts are self-checks for you, their PASS / FAIL does not enter the grade. The remaining **2 / 10** comes from the two ★ simulations, which are graded on PASS / FAIL.

In practice: walk the analyst flow honestly (Parts 1–4 + Bonus) and you have 8 points. Add the two simulations and you have 10.

## How to submit

1. Run all cells from top to bottom.
2. Make sure the plots are rendered (Part 4 CUPED, ★ Part 5 peeking, ★ Part 6 power curve).
3. Replace the placeholder in the interpretation markdown cell (after Part 3) with your own 2–3 sentences.
4. Save the notebook with outputs preserved.
5. Upload `homework.ipynb` to Google Classroom.
