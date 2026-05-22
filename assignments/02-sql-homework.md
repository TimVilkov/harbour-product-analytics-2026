# Session 03 SQL — Homework

> **Deadline:** Monday, May 25, 23:59 (Barcelona time)
> **Total points:** 10
> **Solo work.**

## How to log in to Snowflake

You will run all queries in the same Snowflake account we used during Session 03.

- **Account / login URL:** [https://srjeltv-fi18270.snowflakecomputing.com](https://srjeltv-fi18270.snowflakecomputing.com)
- **Username and password:** posted in Google Classroom alongside this assignment.

Database (`PA_COURSE`), schema (`PUBLIC`), role (`STUDENT`), and warehouse (`PA_COURSE_WH`) are pre-set on your account. After login, open a new worksheet — you can start writing `SELECT * FROM products` straight away.

---

## What this is

A set of SQL tasks you solve in Snowflake on a small product dataset. Each task gives you a goal, the columns you must return, and a one-line call that checks your answer automatically. You get instant feedback. No screenshots, no manual grading.

There are 16 tasks total — 7 easier ones (1–7) and 9 interview-grade ones (8–16). The maximum score is 10/10. Pick any 10 to solve, in any order. The easier seven are designed to cover what we did in class. The harder nine are for students who want to push toward interview-level SQL — windows, sessionization, retention, gaps-and-islands, funnel attribution, SCD2 joins, rolling metrics, percentiles, deduplication, and marketing attribution.

You will write each query yourself, paste it inside a `check_task` call, and run it. The procedure will reply with `PASS` or with the exact number of rows that are missing or extra compared to the canonical answer. Iterate until you get `PASS`.

---

## The dataset

Everything lives in the Snowflake database `PA_COURSE`, schema `PUBLIC`. Five tables. The same ones we used in class.

```
products         (product_id, name, category, price)
users_snapshot   (user_id, name, email, signup_date, country, plan, is_active)
users_history    (user_id, plan, valid_from, valid_to, is_current)
events           (event_id, user_id, event_name, event_ts, device, country, product_id, properties)
orders           (order_id, user_id, product_id, amount, order_date, status)
```

> ⚠ **The data is messy on purpose.** Expect duplicate rows, inconsistent values (different casing, abbreviations, languages for the same thing), and `NULL`s where you might not expect them. Analysing the data before you write each query — running a few exploratory `SELECT` statements to see what's actually there — is part of the job.

---

## How to validate your answer

There is one procedure: `check_task(task_id, your_query)`. You wrap your final SQL inside it, run it, and it tells you whether your result matches the canonical answer.

The `$$ ... $$` is Snowflake's way of letting you paste a multi-line string without escaping quotes inside it. Put your full query between the two `$$`. The semicolon at the end of your query is optional — drop it to be safe.

The procedure replies with one of two things:

- **`PASS task N`** — your result matches the canonical answer. Done.
- **`FAIL task N: missing=A, extra=B`** — your result has `A` rows that the canonical answer has but you don't, and `B` rows that you have but the canonical answer doesn't. Iterate.

A few rules the check uses:

- **Column names, types, and order must match what the task spec says.** If the spec says `Output: user_id (INT), name (STRING), count (INT)`, your `SELECT` must return those three columns in that order with those names.
- **Row order does not matter.** The check uses set semantics. If the spec asks for a sort order, do the sort, but the check itself does not require it.
- **You can call `check_task` as many times as you want.** No penalty for failed attempts.

If you write a query that's syntactically broken or returns the wrong column shape, you will get a `FAIL` with an error message describing what went wrong (e.g. column count mismatch).

---

## Hints for the hard tasks

If you are stuck on any task from 8 onwards, you can ask for a one-line hint that points you to the kind of construct you should be reaching for. Hints do not give you the solution. They suggest the pattern.

```sql
CALL get_hint(11);
-- Hint task 11: Gaps-and-islands trick: DATE - ROW_NUMBER OVER (PARTITION BY user ORDER BY date)...
```

Hints exist for tasks 8–16 only. Tasks 1–7 are deliberately built on what we covered in class — try them without help first.

---

## Worked example — Task 0

This task is not graded. It is here so you can see the full feedback loop before you start the real tasks.

**Task:** For each product category, return the category name and the number of products in it.

**Output:** `category` (STRING), `product_count` (INT)

Let's try a query that is wrong on purpose — we forget the `GROUP BY`:

```sql
CALL check_task(0, $$
  SELECT category, COUNT(*) AS product_count
  FROM products
$$);
```

The procedure replies with something like:

```
FAIL task 0: student SQL error — SQL compilation error: ...
'category' is not a valid group by expression
```

The check tried to run our query and SQL itself complained. Let's fix that — add the `GROUP BY`, but say we only think about electronics for a moment:

```sql
CALL check_task(0, $$
  SELECT category, COUNT(*) AS product_count
  FROM products
  WHERE category = 'electronics'
  GROUP BY category
$$);
```

Reply:

```
FAIL task 0: missing=5, extra=0
```

Our query returns one row (electronics, 5). The canonical answer has 6 rows, one per category. Five of those rows are missing from our output, none of ours is extra. Drop the filter:

```sql
CALL check_task(0, $$
  SELECT category, COUNT(*) AS product_count
  FROM products
  GROUP BY category
$$);
```

Reply:

```
PASS task 0
```

That's the loop. Iterate on your query, run `check_task`, read the diff, adjust, repeat.

---

## How to submit

When you have a `PASS` for every task you want to submit, collect your final queries into a single `.sql` file. One block per task, numbered:

```sql
-- Task 1
SELECT product_id, name, price
FROM products
WHERE category = 'electronics'
ORDER BY price DESC
LIMIT 10;

-- Task 2
...
```

Send the `.sql` file in reply to the assignment thread on Slack by Monday, May 25, 23:59. Do not submit screenshots, query results, or links.

---

## Task 01 — Top expensive electronics (1 pt, easy)

List the ten most expensive products in the `electronics` category.

Output: `product_id` (INT), `name` (STRING), `price` (NUMERIC)

Validate:

```sql
CALL check_task(1, $$
  <your query>
$$);
```

---

## Task 02 — Top buyers (1 pt, easy)

For each customer who has placed five or more orders in total, return their user id, name, and the total number of orders.

Output: `user_id` (INT), `name` (STRING), `order_count` (INT)

Validate:

```sql
CALL check_task(2, $$
  <your query>
$$);
```

---

## Task 03 — Above-average order months (1 pt, easy)

Look at orders placed during 2025. For each calendar month in 2025 that had more orders than the average month in 2025, return the month and the number of orders.

The "average" is computed across all months in 2025 that had at least one order.

Output: `order_month` (DATE — first day of the month), `order_count` (INT)

Validate:

```sql
CALL check_task(3, $$
  <your query>
$$);
```

---

## Task 04 — Distinct active users by country (1 pt, easy)

Count the number of distinct active users per country. A user is active if `is_active = TRUE`.

The `country` column is messy. Treat the following as one and the same country, returning the value in the right-hand column:

| Raw values | Normalised |
|---|---|
| `ES`, `es`, `Spain` | `Spain` |
| `US`, `us`, `USA` | `USA` |
| `UK`, `GB`, `gb` | `UK` |
| `DE`, `germany` | `Germany` |
| `FR` | `France` |
| `IT` | `Italy` |
| `PT` | `Portugal` |
| `NL` | `Netherlands` |
| `NULL` | `Unknown` |

Output: `country` (STRING), `active_user_count` (INT)

Validate:

```sql
CALL check_task(4, $$
  <your query>
$$);
```

---

## Task 05 — Shipped revenue by country (1 pt, easy)

For each normalised country, return the total revenue from orders with status `shipped`. The country comes from the customer who placed the order (`users_snapshot.country`). Use the same country normalisation table as Task 04.

Output: `country` (STRING), `shipped_revenue` (NUMERIC)

Validate:

```sql
CALL check_task(5, $$
  <your query>
$$);
```

---

## Task 06 — Orders by outcome and category (1 pt, easy)

For each combination of order outcome bucket and product category, return the number of orders.

Outcome buckets:

| Raw status | Bucket |
|---|---|
| `shipped` | `successful` |
| `pending` | `pending` |
| `cancelled`, `refunded` | `lost` |
| `NULL` | `unknown` |

The category comes from the product the order is for. If an order's product is missing from the `products` table, the `category` should be `NULL`.

Output: `bucket` (STRING), `category` (STRING), `order_count` (INT)

Validate:

```sql
CALL check_task(6, $$
  <your query>
$$);
```

---

## Task 07 — Recent signups, never bought, never purchased (1 pt, easy)

List users who signed up in the last 180 days (`signup_date >= CURRENT_DATE - 180`) and have **never** appeared in either of these:

- as the buyer in an order with status `shipped`
- as the (non-anonymous) user behind an event with `event_name = 'purchase'`

Output: `user_id` (INT), `signup_date` (DATE)

Validate:

```sql
CALL check_task(7, $$
  <your query>
$$);
```

---

## Task 08 — Top three products per category (1 pt, hard)

For every product category, return the top three products by total shipped revenue. If two products tie on revenue, the one with the smaller `product_id` ranks higher.

Output: `category` (STRING), `rank` (INT — 1, 2 or 3), `product_id` (INT), `name` (STRING), `shipped_revenue` (NUMERIC)

Validate:

```sql
CALL check_task(8, $$
  <your query>
$$);
```

---

## Task 09 — Sessions per user (1 pt, hard)

Define a session for a user as a sequence of events where the gap from the previous event of the same user is at most 15 minutes. A gap of more than 15 minutes starts a new session.

Ignore anonymous events (where `user_id IS NULL`). For each non-anonymous user with at least one event, return the number of sessions.

Output: `user_id` (INT), `session_count` (INT)

Validate:

```sql
CALL check_task(9, $$
  <your query>
$$);
```

---

## Task 10 — Weekly cohort retention (1 pt, hard)

Build a `users_snapshot.signup_date` weekly cohort. For each cohort week (Monday-starting), compute:

- `cohort_size` — number of users who signed up in that week
- `retained_d7` — of those users, how many had at least one event with `event_ts` in the window `[signup_date + 7 days, signup_date + 14 days)`
- `retained_d30` — of those users, how many had at least one event with `event_ts` in the window `[signup_date + 30 days, signup_date + 60 days)`

Return one row per cohort week.

Output: `cohort_week` (DATE — Monday of the week), `cohort_size` (INT), `retained_d7` (INT), `retained_d30` (INT)

Validate:

```sql
CALL check_task(10, $$
  <your query>
$$);
```

---

## Task 11 — Longest active streak (1 pt, hard)

A user's active streak is a sequence of consecutive calendar days on which the user had at least one event. Ignore anonymous events.

For each user who had at any point a streak of two or more consecutive active days, return the start date, end date, and length (in days) of their longest streak. If a user has multiple streaks of equal maximum length, return the earliest one.

Output: `user_id` (INT), `streak_start` (DATE), `streak_end` (DATE), `streak_length` (INT)

Validate:

```sql
CALL check_task(11, $$
  <your query>
$$);
```

---

## Task 12 — Funnel completion with first / last touch (1 pt, hard)

A user completes the funnel if they had a `page_view` event followed in time by an `add_to_cart` event followed in time by a `purchase` event (using the earliest event of each type per user). Ignore anonymous events.

For every user who completed the funnel, return:

- `first_touch_source` — the value of `properties:source::STRING` from the user's very first event (earliest by `event_ts`, then by `event_id`)
- `last_touch_source` — the value of `properties:source::STRING` from the user's last event strictly before their first `purchase` event (latest by `event_ts`, then by `event_id`)

Output: `user_id` (INT), `first_touch_source` (STRING), `last_touch_source` (STRING)

Validate:

```sql
CALL check_task(12, $$
  <your query>
$$);
```

---

## Task 13 — Plan at time of order (1 pt, hard)

For every order, return the customer's plan at the time the order was placed. The plan history lives in `users_history`. A user's plan is active during `[valid_from, valid_to)` — inclusive of `valid_from`, exclusive of `valid_to`. The current plan has `valid_to IS NULL`.

If an order falls outside any history period for the user, return `NULL` for the plan.

Output: `order_id` (INT), `user_id` (INT), `order_date` (DATE), `plan_at_order` (STRING)

Validate:

```sql
CALL check_task(13, $$
  <your query>
$$);
```

---

## Task 14 — Rolling 7-day average with top-10 percent flag (1 pt, hard)

For every day in the last 90 days (`order_date >= CURRENT_DATE - 89`), compute:

- `order_count` — number of orders placed on that day (days with zero orders are not included)
- `rolling_7d_avg` — average daily order count over the day itself plus the six preceding days in the series, computed with the standard `ROWS BETWEEN 6 PRECEDING AND CURRENT ROW` window
- `is_top_10pct` — `TRUE` if the day's `rolling_7d_avg` is greater than or equal to the 90th percentile of all `rolling_7d_avg` values in the series, `FALSE` otherwise. Use `PERCENTILE_CONT(0.9)` as the threshold.

Output: `day` (DATE), `order_count` (INT), `rolling_7d_avg` (NUMERIC), `is_top_10pct` (BOOLEAN)

Validate:

```sql
CALL check_task(14, $$
  <your query>
$$);
```

---

## Task 15 — Latest event per user (1 pt, hard)

For each non-anonymous user with at least one event, return the row of their most recent event. "Most recent" is the row with the largest `event_ts`. If two events for the same user share the same `event_ts`, break the tie by the larger `event_id`.

Output: `user_id` (INT), `event_id` (INT), `event_ts` (TIMESTAMP_NTZ), `event_name` (STRING)

Validate:

```sql
CALL check_task(15, $$
  <your query>
$$);
```

---

## Task 16 — First-touch and last-touch channel attribution (1 pt, hard)

This task uses an extra table, `marketing_visits`. Each row records a user's visit to the site through a marketing channel:

```
marketing_visits (visit_id, user_id, visit_ts, channel, campaign)
```

For every user who placed at least one shipped order, return:

- `first_purchase_date` — the date of their earliest shipped order
- `first_touch_channel` — the `channel` of their earliest visit before that purchase date (earliest by `visit_ts`)
- `last_touch_channel` — the `channel` of their latest visit before that purchase date (latest by `visit_ts`)

Only include users who have at least one marketing visit strictly before their first shipped order.

Output: `user_id` (INT), `first_purchase_date` (DATE), `first_touch_channel` (STRING), `last_touch_channel` (STRING)

Validate:

```sql
CALL check_task(16, $$
  <your query>
$$);
```
