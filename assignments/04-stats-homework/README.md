# Homework 4 — Statistics

First hands-on with statistics in Python. Six parts, roughly 3 hours of work.

- **Deadline:** TBD
- **Total points:** 10
- **Solo work**
- **Submission:** the completed `homework.ipynb` via Google Classroom

## On using AI

Feel free to use ChatGPT, Claude, Copilot, etc. for **documentation lookup** and **routine coding** — `numpy` / `scipy` / `matplotlib` syntax, plot styling, debugging an `IndexError`. That saves time and is exactly what you would do at work.

Everything that touches the **mathematics, the logic, and the structure of the solution** I am counting on you to do yourself. The hypothesis-test setup, the choice of statistic, the interpretation of a p-value, the bootstrap recipe, the explanation of why a permutation test agrees with Welch — those are the parts where the assignment is supposed to teach you something. If an AI hands you those, you have not learned them, and the next homework (and the interview that follows) will not go well.

I am trusting you to be honest about this. The intellectual work is yours.

## Files

- `homework.ipynb` — the assignment notebook. Open it, fill in the `...` placeholders, run all cells.
- `ab_data.csv` — the dataset you load in Part 2 (per-user revenue, two buckets: `control` and `treatment`).
- `_grader.py` — the grader. You import `check_answer` from it. Do not modify.

## How the grader works

After each task you call `check_answer(task_id, your_value)`. It prints either:

- `PASS task X` — your value matches the expected answer (within tolerance).
- `FAIL task X: got V — does not match expected` — your value is wrong.

The grader does not print the expected value. You iterate until everything passes.

## Library expectations

I use `numpy`, `scipy.stats`, and `matplotlib` in the scaffold. Feel free to use `seaborn`, `plotly`, or anything else for visualisation. The grader only checks numerics — plots are for your understanding and for me to read.

## Parts

| Part | Topic |
|---|---|
| 1 | Generate and visualise distributions (discrete PMF, continuous PDF, empirical CDF) |
| 2 | Descriptive stats and a CLT-based CI for revenue |
| 3 | One-sample test against a baseline (with a brief primer on the t-distribution) |
| 4 | Two-sample test: Welch's t-test vs permutation test |
| 5 | Simulation: p-value distribution under $H_0$, power under $H_1$, what happens when assumptions break |
| 6 | Bootstrap: CI for the mean (compare with Part 2), bonus CI for the median |

## How to submit

1. Run all cells from top to bottom. Every `check_answer(...)` should print `PASS`.
2. Make sure the plots are rendered (not hidden / commented out).
3. Save the notebook with outputs preserved.
4. Upload `homework.ipynb` to Google Classroom.
