# Homework 1 — Metric Design

- **Deadline:** start of Session 04, 2026-05-21
- **Format:** group, 6 teams, top-down assignment
- **Submission:** Miro board link in Google Classroom

---

## What this is

You're a product analyst joining a product team. Map how the product works, define its North Star, design the metric structure for your squad, and cover one specific feature with metrics.

---

## Deliverables

Your Miro board has four zones.

### Zone 1 — Context

- What the company sells.
- How the company earns money.
- What value the product creates for the user.

### Zone 2 — Company metric tree

- A metric tree for the product slice in your environment card. The North Star metric and the tree are for that slice, not for the company as a whole (e.g., Uber Rides, not Uber including Eats and Freight).
- **≥30 metrics.** No depth limit.
- **One North Star metric** at the top. If you treat it as a constellation (NSM plus a business output), say so. Think about the caveats and the potential problems with the metric you pick.
- **Bridge to revenue** at the end: how does growing the North Star eventually move money. The link can be indirect, but make it explicit.

### Zone 3 — Squad metric structure

- What breaks if your squad disappears.
- **10–15 metrics** organised at the squad level. Tree if you want, any structure if you don't.
- One **main metric** of the squad. It can be a money metric or anything else.
- How your squad's work **contributes to the company-level goals** from Zone 2.

### Zone 4 — Feature deep-dive

- The feature described in your environment card.
- Entry points: how users get into the feature.
- Process: stages a user goes through inside the feature.
- Value: what good outcome looks like.
- Quality and satisfaction signals.
- What could break or get worse when this feature ships.

---

## Environment cards

Each team gets one product. Assigned in class.

### Card A — Uber (Matching system)

| | |
|---|---|
| Company | Uber |
| Macro scope | Rides (rider side) |
| Squad | Matching system — owns rider↔driver pairing, dispatch, ETA prediction, post-match cancellation |
| Stakeholder | VP Engineering for Matching, Rider Product Director |

**Feature: One-tap rematch after driver cancel.** When a driver cancels after being matched, the rider sees a one-tap banner offering an immediate rematch. A new search runs in the background; if a closer driver is found, the rider accepts without re-entering pickup or destination. The point is to stop riders from abandoning the app after a cancellation.

### Card B — Glovo (Courier dispatch & ETA)

| | |
|---|---|
| Company | Glovo |
| Macro scope | Restaurants vertical |
| Squad | Courier dispatch & ETA quality — courier assignment, batching, ETA accuracy, late-delivery handling |
| Stakeholder | VP Operations, Director of Logistics |

**Feature: Reject without penalty.** Couriers can decline an assigned order without affecting their acceptance rate, as long as they pick a structured reason: unsafe area, bad weather, route too far, vehicle issue. The order is returned to dispatch and re-assigned to another courier. Couriers used to take risky orders to avoid getting penalised; the feature lets them opt out honestly.

### Card C — Revolut Investments (Order execution & price quality)

| | |
|---|---|
| Company | Revolut Investments |
| Macro scope | Investments tab (stocks, ETFs, crypto) |
| Squad | Order execution & price quality — spread, slippage, fill rate, execution latency |
| Stakeholder | Head of Trading, Compliance Lead |

**Feature: Price improvement alert at placement.** When a user places an order on a stock with an unusually wide spread, the app shows a one-screen alert: "Your fill is likely to be X% worse than the mid-price. You can wait, proceed, or cancel." If the user chooses to wait, the order is held until the spread normalises or until they manually proceed. The feature exists for retail traders who don't always know what a wide spread is costing them.

### Card D — Etsy (Search & recommendations)

| | |
|---|---|
| Company | Etsy |
| Macro scope | Marketplace (buyer and seller flows) |
| Squad | Search & recommendations — search relevance, query understanding, homepage feed, category recs, related items |
| Stakeholder | VP Discovery, Head of Buyer Experience |

**Feature: Visual search.** A camera icon next to the search bar lets users upload a photo or take one on the spot. Etsy returns visually similar listings — a bag, a dress, a lamp, whatever was in the picture. The flow is: tap camera → upload or shoot → results page → tap a listing → buy. The feature is for buyers who can describe what they want visually but not in words.

### Card E — Strava (Activation)

| | |
|---|---|
| Company | Strava |
| Macro scope | Core app (tracking, social, Premium) |
| Squad | Activation — first-week experience of new users: time to first activity, first social interaction, first habit signal |
| Stakeholder | Director of Growth, Head of New User Experience |

**Feature: Beginner 7-day challenge.** During sign-up, new users are offered an opt-in challenge: log any kind of activity once a day for seven days in a row. Each day Strava sends a short nudge with a streak counter. On day 7 the user gets a digital badge and a one-tap share. The feature is designed to push new users into the habit loop before they decide whether the app is for them.

### Card F — YouTube viewer (Notification & re-engagement)

| | |
|---|---|
| Company | YouTube |
| Macro scope | Main app (viewer side) |
| Squad | Notification & re-engagement — push, email, dormant-user re-activation, homepage surfacing for returning visitors |
| Stakeholder | Director of Growth, VP Viewer Experience |

**Feature: Weekly digest of new uploads from subscribed channels.** Once a week, dormant users (no app open in 7+ days) get a push notification titled "New from channels you follow." Tapping it opens a digest page with the top 3 recent videos from their subscriptions. The flow is: notification → tap → digest page → tap a video → playback. The feature targets users who used to be active but stopped opening the app.

---

## Presentation

15 minutes per team in Session 04. Ideally most of the team speaks, not just one person.

In the presentation you can earn extra points by:

- **Attacking** another team's choices with a clear argument. Don't fear challenging.
- **Defending** your own choices under pressure. Be ready to be challenged.

---

## Grading

| Component | Weight |
|---|---|
| Context + company metric tree (Zones 1 and 2) | 60% |
| Squad metric structure (Zone 3) | 20% |
| Feature deep-dive (Zone 4) | 20% |
| **Content total** | **100%** |
| Presentation (incl. attack and defense) | up to +20% |
| **Max grade** | **120%** |
