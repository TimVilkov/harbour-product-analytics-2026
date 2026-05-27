# Homework 3 — Statistics

First hands-on with statistics in Python. Six parts.

- **Deadline:** Monday, June 1, 2026, 23:59 (Barcelona time)
- **Total points:** 10
- **Solo work**
- **Submission:** the completed `homework.ipynb` via Google Classroom

## On using AI

Feel free to use ChatGPT, Claude, Copilot, etc. for **documentation lookup** and **routine coding** — library syntax, plot styling, debugging an `IndexError`. That saves time and is exactly what you would do at work.

Everything that touches the **mathematics, the logic, and the structure of the solution** I am counting on you to do yourself. Setting up the hypothesis test, choosing the statistic, interpreting a p-value, applying the bootstrap recipe — those are the parts where the assignment is supposed to teach you something. If an AI hands you those, you have not learned them.

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

Use whatever you prefer for visualisation — `matplotlib`, `seaborn`, `plotly`, anything else. The grader only checks numerics — plots are for your understanding and for me to read. Numerics via `numpy` and `scipy.stats`.

## Parts

| Part | Topic |
|---|---|
| 1 | Generate and visualise distributions (discrete PMF, continuous PDF, empirical CDF) |
| 2 | Descriptive stats and a CLT-based CI for revenue |
| 3 | One-sample asymptotic Z-test against a baseline (with a brief primer on the t-distribution and SciPy) |
| 4 | Two-sample test: asymptotic Z-test (numerically via `ttest_ind`) and permutation test |
| 5 | Simulation: p-value distribution under $H_0$, power under $H_1$, what happens when assumptions break |
| 6 | Bootstrap: CI for the mean (compare with Part 2), bonus CI for the median |

## How to submit

1. Run all cells from top to bottom. Every `check_answer(...)` should print `PASS`.
2. Make sure the plots are rendered (not hidden / commented out).
3. Save the notebook with outputs preserved.
4. Upload `homework.ipynb` to Google Classroom.
