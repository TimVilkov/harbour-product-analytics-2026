---
theme: apple-basic
title: "Session 13: Cohort Analysis & Unit Economics"
info: "Product Analytics · Harbour.Space · 2026"
highlighter: shiki
drawings:
  persist: false
transition: fade
mdc: true
layout: intro
---

# Unit <span class="pink">Economics</span>

<div class="absolute bottom-10 left-14" style="font-family:'JetBrains Mono',monospace;font-size:0.75rem;text-transform:uppercase;letter-spacing:0.15em;color:rgba(255,255,255,0.55);">
  Harbour.Space &middot; Barcelona &middot; June 4, 2026
</div>

---

# Today

<div style="display:flex;flex-direction:column;gap:0.9rem;margin-top:1rem;">
  <div style="display:grid;grid-template-columns:60px 1fr;gap:1.5rem;align-items:baseline;">
    <span style="font-family:'JetBrains Mono',monospace;font-size:0.9rem;color:#FF00FF;letter-spacing:0.1em;">01</span>
    <div style="font-size:1.4rem;font-weight:700;color:#1A1A1A;">Why business metrics</div>
  </div>
  <div style="display:grid;grid-template-columns:60px 1fr;gap:1.5rem;align-items:baseline;">
    <span style="font-family:'JetBrains Mono',monospace;font-size:0.9rem;color:#FF00FF;letter-spacing:0.1em;">02</span>
    <div style="font-size:1.4rem;font-weight:700;color:#1A1A1A;">Unit economics</div>
  </div>
  <div style="display:grid;grid-template-columns:60px 1fr;gap:1.5rem;align-items:baseline;">
    <span style="font-family:'JetBrains Mono',monospace;font-size:0.9rem;color:#FF00FF;letter-spacing:0.1em;">03</span>
    <div style="font-size:1.4rem;font-weight:700;color:#1A1A1A;">Product-market fit</div>
  </div>
</div>

---
layout: section
class: tint-lavender
---

## 01

# Why business metrics

---
layout: statement
---

# Every product bet is a bet about the <span class="pink">business</span>

---

# Duality of business and product

<div style="font-size:1.3rem;color:#1A1A1A;font-weight:600;line-height:1.45;margin-bottom:0.6rem;">You cannot think only about users</div>

<div style="display:grid;grid-template-columns:1fr 56px 1fr;grid-template-rows:auto 40px auto;gap:0.5rem;max-width:660px;margin:1.1rem auto 0;align-items:center;justify-items:center;">

<div style="padding:0.7rem 1rem;background:#FAFAFA;border:1px solid #E0E0E0;border-radius:8px;font-weight:800;text-align:center;width:100%;">Earn money</div>
<div style="font-family:'JetBrains Mono',monospace;color:#AAAAAA;font-size:1.3rem;">&rarr;</div>
<div style="padding:0.7rem 1rem;background:#FAFAFA;border:1px solid #E0E0E0;border-radius:8px;font-weight:800;text-align:center;width:100%;">Build a great product</div>

<div style="font-family:'JetBrains Mono',monospace;color:#AAAAAA;font-size:1.3rem;">&uarr;</div>
<div style="font-family:'JetBrains Mono',monospace;color:#FF00FF;font-size:0.68rem;text-transform:uppercase;letter-spacing:0.12em;">flywheel</div>
<div style="font-family:'JetBrains Mono',monospace;color:#AAAAAA;font-size:1.3rem;">&darr;</div>

<div style="padding:0.7rem 1rem;background:#FAFAFA;border:1px solid #E0E0E0;border-radius:8px;font-weight:800;text-align:center;width:100%;">More money</div>
<div style="font-family:'JetBrains Mono',monospace;color:#AAAAAA;font-size:1.3rem;">&larr;</div>
<div style="padding:0.7rem 1rem;background:#FAFAFA;border:1px solid #E0E0E0;border-radius:8px;font-weight:800;text-align:center;width:100%;">Happier, more users</div>

</div>

<div style="text-align:center;margin-top:1rem;font-size:1rem;color:#1A1A1A;">Money funds a better product, which makes more users happier, which earns more</div>

<!--
You need money to build a great product, and that product makes more users happier and earns even more. Business and product are one loop, not a trade-off. This is why a product person has to care about the money.
-->

---

# Control vs test

<div style="font-size:1.3rem;color:#1A1A1A;font-weight:600;line-height:1.45;margin-bottom:0.6rem;">The Manychat pricing test moves two levers at once: billing default and recommended plan</div>

<div style="display:flex;gap:1.5rem;justify-content:center;margin-top:0.4rem;">
<div style="text-align:center;">
<div style="font-family:'JetBrains Mono',monospace;font-size:0.68rem;color:#AAAAAA;letter-spacing:0.12em;text-transform:uppercase;margin-bottom:0.3rem;">Control &middot; annual default</div>

![](./images/manychat_pricing_annual.png){width=320px}

</div>
<div style="text-align:center;">
<div style="font-family:'JetBrains Mono',monospace;font-size:0.68rem;color:#AAAAAA;letter-spacing:0.12em;text-transform:uppercase;margin-bottom:0.3rem;">Test &middot; monthly default</div>

![](./images/manychat_pricing_monthly.png){width=320px}

</div>
</div>

<!--
Control defaults to annual and recommends Pro. Test defaults to monthly and recommends Essential to small-audience users. Two changes at once, so not a clean causal test, but for the money question we want the aggregate. A monthly default lowers the barrier: more conversions, less annual commitment.
-->

---

# One change, many outcomes

<div style="font-size:1.3rem;color:#1A1A1A;font-weight:600;line-height:1.45;margin-bottom:0.6rem;">The same product change can help or hurt the business, depending on the chain</div>

<div style="text-align:center;margin:0.7rem 0 0.5rem;font-family:'JetBrains Mono',monospace;font-size:0.92rem;color:#6B6B6B;">Monthly default &rarr; higher conversion &rarr; more paying accounts</div>

<div style="display:flex;flex-direction:column;gap:0.55rem;align-items:center;">

<div style="display:flex;align-items:center;gap:0.45rem;">
<span style="padding:0.26rem 0.7rem;border-radius:6px;background:#F2F2F2;color:#555;font-size:0.9rem;font-weight:600;">retention holds</span>
<span style="color:#CCC;">&rarr;</span>
<span style="padding:0.26rem 0.7rem;border-radius:6px;background:rgba(76,120,168,0.16);color:#2F5C8F;font-size:0.9rem;font-weight:600;">LTV &uarr;</span>
<span style="color:#CCC;">&rarr;</span>
<span style="padding:0.26rem 0.7rem;border-radius:6px;background:rgba(76,120,168,0.16);color:#2F5C8F;font-size:0.9rem;font-weight:600;">revenue &uarr;</span>
<span style="font-family:'JetBrains Mono',monospace;font-size:0.72rem;font-weight:700;letter-spacing:0.1em;color:#2F5C8F;margin-left:0.4rem;">WIN</span>
</div>

<div style="display:flex;align-items:center;gap:0.45rem;">
<span style="padding:0.26rem 0.7rem;border-radius:6px;background:#F2F2F2;color:#555;font-size:0.9rem;font-weight:600;">lower ARPPU</span>
<span style="color:#CCC;">&rarr;</span>
<span style="padding:0.26rem 0.7rem;border-radius:6px;background:#F2F2F2;color:#555;font-size:0.9rem;font-weight:600;">LTV flat</span>
<span style="color:#CCC;">&rarr;</span>
<span style="padding:0.26rem 0.7rem;border-radius:6px;background:#F2F2F2;color:#555;font-size:0.9rem;font-weight:600;">revenue flat</span>
<span style="font-family:'JetBrains Mono',monospace;font-size:0.72rem;font-weight:700;letter-spacing:0.1em;color:#999;margin-left:0.4rem;">WASH</span>
</div>

<div style="display:flex;align-items:center;gap:0.45rem;">
<span style="padding:0.26rem 0.7rem;border-radius:6px;background:rgba(228,87,86,0.16);color:#B23A39;font-size:0.9rem;font-weight:600;">lower retention</span>
<span style="color:#CCC;">&rarr;</span>
<span style="padding:0.26rem 0.7rem;border-radius:6px;background:rgba(228,87,86,0.16);color:#B23A39;font-size:0.9rem;font-weight:600;">LTV &darr;</span>
<span style="color:#CCC;">&rarr;</span>
<span style="padding:0.26rem 0.7rem;border-radius:6px;background:rgba(228,87,86,0.16);color:#B23A39;font-size:0.9rem;font-weight:600;">revenue &darr;</span>
<span style="font-family:'JetBrains Mono',monospace;font-size:0.72rem;font-weight:700;letter-spacing:0.1em;color:#B23A39;margin-left:0.4rem;">LOSS</span>
</div>

</div>

<div style="text-align:center;margin-top:0.8rem;font-size:1.05rem;color:#1A1A1A;">You cannot read it off the change alone, you have to model it</div>

<!--
Same starting move: a monthly default lifts conversion and brings more paying accounts. From there the chain branches. If retention holds, LTV and revenue rise, a win. If the cheaper plan drags ARPPU down, LTV is flat, a wash. If retention drops, LTV and revenue fall, a loss. The product change alone does not tell you which branch you are on, so you have to model it. This is exactly why we built the calculator.
-->

---
layout: section
class: tint-rose
---

## 02

# Unit economics

---

# The calculator

<div style="font-size:1.3rem;color:#1A1A1A;font-weight:600;line-height:1.45;margin-bottom:0.6rem;">We work all of this inside one shared model</div>

<div style="display:flex;justify-content:center;margin-top:1.4rem;">
<a href="https://docs.google.com/spreadsheets/d/1K_KC9SL-n5AnfTY5zAWooVN0h9cVpGn5AhDiv8ApaPU/edit?usp=sharing" target="_blank" rel="noopener" style="display:inline-block;padding:0.8rem 1.4rem;background:#1A1A1A;color:#fff;font-family:'JetBrains Mono',monospace;font-size:0.95rem;font-weight:700;letter-spacing:0.08em;text-transform:uppercase;text-decoration:none;border:2px solid #1A1A1A;">Open the calculator ↗</a>
</div>

<!--
This is the handout. Funnel and CAC, plan mix and ARPU, retention, LTV and payback, cohorts all live here. We drive the pricing decision through it together. Tell them to edit the yellow cells.
-->

---

# Unit economics, plainly

<div style="margin-top:0.9rem;padding:1.2rem 1.5rem;background:#FAFAFA;border-left:4px solid #FF00FF;font-size:1.18rem;font-weight:800;line-height:1.5;">
A method of economic analysis that measures a business's profitability per one unit, the base unit being a customer, a deal, or an item
</div>

<div style="margin-top:1rem;font-size:1.05rem;line-height:1.7;">Main goal: understand whether acquiring and serving one unit pays off, and whether the business is worth scaling</div>

<!--
Plain language first: weigh what one unit brings against what it costs. Choosing the unit well is half the work, it has to be something the model rests on and something the team can move.
-->

---

# One business, several units

<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:1rem;margin-top:1rem;">

<div style="padding:0.9rem 1.1rem;background:#FAFAFA;border-left:3px solid #1A1A1A;">
<div style="font-weight:800;font-size:1rem;margin-bottom:0.3rem;">Order</div>
<div style="font-size:0.9rem;color:#6B6B6B;line-height:1.5;">what to optimize on each order</div>
</div>

<div style="padding:0.9rem 1.1rem;background:#FAFAFA;border-left:3px solid #1A1A1A;">
<div style="font-weight:800;font-size:1rem;margin-bottom:0.3rem;">Customer</div>
<div style="font-size:0.9rem;color:#6B6B6B;line-height:1.5;">what they bring vs cost to acquire</div>
</div>

<div style="padding:0.9rem 1.1rem;background:#FAFAFA;border-left:3px solid #1A1A1A;">
<div style="font-weight:800;font-size:1rem;margin-bottom:0.3rem;">Restaurant</div>
<div style="font-size:0.9rem;color:#6B6B6B;line-height:1.5;">cost to acquire and subsidize vs what we earn later</div>
</div>

</div>

<div style="margin-top:1rem;font-size:1.05rem;">Glovo is several unit economies stacked, each pointing at a different lever</div>

<!--
A two-sided business has units on both sides: the order, the demand-side customer, the supply-side restaurant. Each answers a different question.
-->

---

# The order, line by line

<div style="display:flex;justify-content:center;margin-top:0.3rem;">

![](./images/glovo_unit_economics_waterfall.png){width=470px}

</div>

<!--
Average check builds gross revenue. Variable costs bring it to contribution margin. Below that sit marketing and overheads. Key point: a negative EBITDA is not a bad business if per-order contribution margin is positive, that gap is reinvested growth.
-->

---

# CAC, payback, and LTV

<div style="display:flex;justify-content:center;margin-top:0.3rem;">

![](./images/payback.png){width=560px}

</div>

<!--
Spend the CAC up front, earn it back over time. Payback is when cumulative gross profit per account crosses the CAC line. LTV is where the curve lands by the horizon. Compute on gross profit, after variable costs, never on revenue.
-->

---

# A product metric, in money

<div style="display:flex;justify-content:center;margin-top:0.3rem;">

![](./images/metric_to_money.png){width=680px}

</div>

<!--
This is the bridge. Activation lifts retention, retention lifts revenue per signup, and that compounds into LTV. Bake the effect into the calculator and read the impact in money. Crank the uplift, start month, or cohort size live.
-->

---
layout: section
class: tint-sky
---

## 03

# Product-market fit

---

# Read it in retention

<div style="font-size:1.3rem;color:#1A1A1A;font-weight:600;line-height:1.45;margin-bottom:0.4rem;">A product a clear segment keeps coming back to</div>

You read it in the retention curve: a flat tail is a retained base, even a low one

<div style="display:flex;justify-content:center;margin-top:0.2rem;">

![](./images/pmf_curves.png){width=470px}

</div>

<div style="margin-top:0.3rem;font-size:0.85rem;color:#1A1A1A;text-align:center;">Benchmark: B2C around 30 to 40% at three months, B2B around 50%</div>

<!--
PMF means a segment that chooses you over the alternatives and returns. The measurable version is the retention curve: a flat tail is a retained base, a curve that decays to zero is not.
-->

---

# Why retention matters

<div style="font-size:1.3rem;color:#1A1A1A;font-weight:600;line-height:1.45;margin-bottom:0.6rem;">Higher retention is a bigger base and more lifetime value</div>

<div style="display:flex;justify-content:center;margin-top:0.3rem;">

![](./images/retention_to_money.png){width=660px}

</div>

<div style="margin-top:0.4rem;font-size:0.95rem;color:#FF00FF;font-weight:600;">Does a single average churn rate tell you enough?</div>

<!--
LTV is proportional to the area under the retention curve, so the same acquisition pays back very differently. The average-churn question sets up cohorts: one average hides very different groups.
-->

---

# Product-channel fit

<div style="font-size:1.3rem;color:#1A1A1A;font-weight:600;line-height:1.45;margin-bottom:0.3rem;">A great product still dies without a channel where acquisition pays back</div>

<div style="display:flex;justify-content:center;margin-top:0.1rem;">

![](./images/channel_fit.png){width=440px}

</div>

<div style="margin-top:0.2rem;font-size:0.95rem;color:#1A1A1A;text-align:center;">LTV is $250 and the product is loved, but every channel you can scale costs more to acquire</div>

<!--
Product-market fit is necessary but not sufficient. You also need product-channel fit: at least one channel where the cost to acquire a user is below what that user earns you over their life. A brilliant product with no profitable, scalable acquisition channel does not survive. This is unit economics again, now at the channel level.
-->

---

# Materials

<div style="display:grid;grid-template-columns:1fr 1fr;gap:2.4rem;margin-top:0.6rem;font-size:0.9rem;line-height:1.6;color:#1A1A1A;">

<div>
<div style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#AAAAAA;letter-spacing:0.14em;text-transform:uppercase;margin-bottom:0.5rem;">Unit economics</div>
<ul style="margin:0 0 1.2rem;padding-left:1.1rem;">
<li><a href="https://www.forentrepreneurs.com/saas-metrics-2/" target="_blank">SaaS Metrics 2.0</a>, David Skok, the canonical CAC, LTV, payback reference</li>
</ul>
</div>

<div>
<div style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#AAAAAA;letter-spacing:0.14em;text-transform:uppercase;margin-bottom:0.5rem;">Retention and PMF</div>
<ul style="margin:0 0 1.2rem;padding-left:1.1rem;">
<li><a href="https://www.failory.com/blog/retention-rate-metrics" target="_blank">Retention rate and PMF</a>, Failory, flattening curve as the signal</li>
<li><a href="https://www.reforge.com/blog/retention-engagement-growth-silent-killer" target="_blank">Retention is the silent killer</a>, Reforge, why retention compounds</li>
<li><a href="https://gopractice.io/product/what-is-product-market-fit-and-how-to-measure-pmf/" target="_blank">What is PMF and how to measure it</a>, GoPractice</li>
</ul>
</div>

</div>

<!--
The calculator handout carries the worked numbers; these are the readings behind it.
-->
