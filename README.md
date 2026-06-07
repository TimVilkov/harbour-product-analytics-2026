# Product Analytics — Harbour.Space 2026

Course materials for **Product Analytics**, taught by Timofey Vilkov (Senior Product Analyst, Manychat).

- **Dates:** May 18 – June 5, 2026
- **Format:** Offline, Barcelona, English
- **Sessions:** 15 × 3 hours

## What this course is

A profession introduction to product analytics. We cover what a modern product analyst actually does: how decisions get made with data, what stats and experimentation buy you, and where they break.

Not a deep stats or SQL course. Not enough to make you a senior analyst. Enough to set direction and build the right intuitions for your first analytics role.

## Slides

All decks are hosted live and run in the browser. Open one and navigate with the arrow keys, clicks reveal content step by step.

**Course index: https://timvilkov.github.io/harbour-product-analytics-2026/**

| # | Topic | Open |
|---|-------|------|
| 1 | Product Metrics 1 | [slides](https://timvilkov.github.io/harbour-product-analytics-2026/01-product-metrics-1/) |
| 2 | Product Metrics 2 | [slides](https://timvilkov.github.io/harbour-product-analytics-2026/02-product-metrics-2/) |
| 3 | SQL | [slides](https://timvilkov.github.io/harbour-product-analytics-2026/03-sql/) |
| 4 | Data Visualisation | [slides](https://timvilkov.github.io/harbour-product-analytics-2026/04-data-viz/) |
| 5 | Statistics 1 | [slides](https://timvilkov.github.io/harbour-product-analytics-2026/05-statistics-1/) |
| 6 | Statistics 2 | [slides](https://timvilkov.github.io/harbour-product-analytics-2026/06-statistics-2/) |
| 7 | Statistics 3 | [slides](https://timvilkov.github.io/harbour-product-analytics-2026/07-statistics-3/) |
| 8 | Experiments 1 | [slides](https://timvilkov.github.io/harbour-product-analytics-2026/08-experiments-1/) |
| 9 | Experiments 2 | [slides](https://timvilkov.github.io/harbour-product-analytics-2026/09-experiments-2/) |
| 10 | Experiments 3 | [slides](https://timvilkov.github.io/harbour-product-analytics-2026/10-experiments-3/) |
| 11 | Causal Inference | [slides](https://timvilkov.github.io/harbour-product-analytics-2026/11-causal-inference/) |
| 12 | User Segmentation | [slides](https://timvilkov.github.io/harbour-product-analytics-2026/12-segmentation/) |
| 13 | Cohort Analysis & Unit Economics | [slides](https://timvilkov.github.io/harbour-product-analytics-2026/13-cohort-unit-economics/) |
| 14 | Product Analyst Role | — |
| 15 | Final Project Presentations | — |

## Repository structure

```
assignments/    homework briefs
slides/         interactive Slidev decks, one folder per lecture
scripts/        builds the course index page
materials/      reading lists and reference sources per topic
```

The site is built and published automatically by GitHub Actions on every push to `main` (see `.github/workflows/deploy.yml`).

## Running a deck locally

```bash
cd slides/05-statistics-1
npm install
npx slidev slides.md --open
```

## Contact

Timofey Vilkov · timofey.vilkov@manychat.com
