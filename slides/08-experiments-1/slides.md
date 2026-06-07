---
theme: apple-basic
title: "Session 08: Experiments 1"
info: "Product Analytics · Harbour.Space · 2026"
highlighter: shiki
drawings:
  persist: false
transition: fade
mdc: true
layout: intro
---

# Experiments <span class="pink">1</span>

<div class="absolute bottom-10 left-14" style="font-family:'JetBrains Mono',monospace;font-size:0.75rem;text-transform:uppercase;letter-spacing:0.15em;color:rgba(255,255,255,0.55);">
  Harbour.Space &middot; Barcelona &middot; May 27, 2026
</div>

---

# Today

<div style="display:flex;flex-direction:column;gap:0.9rem;margin-top:1rem;">
  <div style="display:grid;grid-template-columns:60px 1fr;gap:1.5rem;align-items:baseline;">
    <span style="font-family:'JetBrains Mono',monospace;font-size:0.9rem;color:#FF00FF;letter-spacing:0.1em;">01</span>
    <div style="font-size:1.4rem;font-weight:700;color:#1A1A1A;">From statistics to causality</div>
  </div>
  <div style="display:grid;grid-template-columns:60px 1fr;gap:1.5rem;align-items:baseline;">
    <span style="font-family:'JetBrains Mono',monospace;font-size:0.9rem;color:#FF00FF;letter-spacing:0.1em;">02</span>
    <div style="font-size:1.4rem;font-weight:700;color:#1A1A1A;">Randomization and its assumptions</div>
  </div>
  <div style="display:grid;grid-template-columns:60px 1fr;gap:1.5rem;align-items:baseline;">
    <span style="font-family:'JetBrains Mono',monospace;font-size:0.9rem;color:#FF00FF;letter-spacing:0.1em;">03</span>
    <div style="font-size:1.4rem;font-weight:700;color:#1A1A1A;">Planning</div>
  </div>
  <div style="display:grid;grid-template-columns:60px 1fr;gap:1.5rem;align-items:baseline;">
    <span style="font-family:'JetBrains Mono',monospace;font-size:0.9rem;color:#FF00FF;letter-spacing:0.1em;">04</span>
    <div style="font-size:1.4rem;font-weight:700;color:#1A1A1A;">Design</div>
  </div>
  <div style="display:grid;grid-template-columns:60px 1fr;gap:1.5rem;align-items:baseline;">
    <span style="font-family:'JetBrains Mono',monospace;font-size:0.9rem;color:#FF00FF;letter-spacing:0.1em;">05</span>
    <div style="font-size:1.4rem;font-weight:700;color:#1A1A1A;">Run</div>
  </div>
  <div style="display:grid;grid-template-columns:60px 1fr;gap:1.5rem;align-items:baseline;">
    <span style="font-family:'JetBrains Mono',monospace;font-size:0.9rem;color:#FF00FF;letter-spacing:0.1em;">06</span>
    <div style="font-size:1.4rem;font-weight:700;color:#1A1A1A;">Decision</div>
  </div>
</div>

---
layout: section
class: tint-lavender
---

## 01

# From statistics to causality

---
layout: statement
---

# We know how to test hypotheses and build estimates <br/>The real job is to make the product <span class="pink">better</span>

<!--
Open with the take. Statistics is the tool we just spent two sessions on, and the room is naturally fixated on it. Reset the frame: that machinery exists to serve product decisions, not the other way around. The rest of the lecture builds the bridge.
-->

---

# Compare two groups, get fooled

Take Revolut premium users and compare the ones who use Feature A with the ones who do not. LTV is much higher in the Feature-A group.

<div style="display:grid;grid-template-columns:1fr 1fr;gap:1.6rem;margin-top:1.3rem;">

<div style="padding:1rem 0.8rem;border:1.5px solid #1A1A1A;background:#FAFAFA;text-align:center;">
<div style="font-family:'JetBrains Mono',monospace;font-size:0.72rem;color:#FF00FF;letter-spacing:0.12em;text-transform:uppercase;margin-bottom:0.5rem;">Uses Feature A</div>
<div style="font-size:2.6rem;line-height:1.1;letter-spacing:0.2rem;">😎 😎 😎 😎 😎</div>
<div style="margin-top:0.55rem;font-weight:700;font-size:1.25rem;">LTV ≈ $$$</div>
</div>

<div style="padding:1rem 0.8rem;border:1.5px solid #1A1A1A;background:#FAFAFA;text-align:center;">
<div style="font-family:'JetBrains Mono',monospace;font-size:0.72rem;color:#6B6B6B;letter-spacing:0.12em;text-transform:uppercase;margin-bottom:0.5rem;">No Feature A</div>
<div style="font-size:2.6rem;line-height:1.1;letter-spacing:0.2rem;">😐 😐 😐 😐 😐</div>
<div style="margin-top:0.55rem;font-weight:700;font-size:1.25rem;">LTV ≈ $</div>
</div>

</div>

<div style="text-align:center;margin-top:1.1rem;font-size:1.1rem;color:#6B6B6B;">Did the feature do it?</div>

<v-click>

<div style="margin-top:1.1rem;text-align:center;font-size:1.2rem;line-height:1.5;max-width:54rem;margin-inline:auto;">

Maybe. Or maybe these users were <span class="pink">more motivated to begin with</span>, and would have paid more anyway.

</div>

</v-click>

<!--
Ask the room first. Let them suggest answers. The 😎 users are the kind that already engage more, log in more, top up more often. They chose to use Feature A because they were curious or motivated. Push Feature A to the 😐 half and the LTV gap will not appear, because the gap was never the feature. Then reveal.
-->

---

# Correlation

We use the **covariance** to measure how two variables move together.

$$\mathrm{Cov}(X, Y) = \mathbb{E}\big[(X - \mu_X)(Y - \mu_Y)\big]$$

Normalising by the standard deviations gives Pearson's correlation, $\rho = \mathrm{Cov}(X,Y)/(\sigma_X \sigma_Y) \in [-1, 1]$. Spearman applies the same idea to ranks and is less sensitive to outliers.

<v-click>

<div style="margin-top:1.7rem;text-align:center;color:#FF00FF;font-family:'Bricolage Grotesque','Inter',sans-serif;font-weight:800;font-size:2.4rem;line-height:1.1;letter-spacing:-0.02em;">

Correlation is not causation.

</div>

</v-click>

<!--
Covariance is the bedrock: positive when X and Y move together, negative when they move opposite, zero when they don't move together at all. Pearson is its scale-free version, and Spearman is the same idea on ranks. The headline is the same one we just demonstrated on Revolut: stat sig in a correlation tells us nothing about whether one caused the other.
-->

---

# The world we never see

For one user, we want to know two things: the metric with the feature, and the metric without it. The difference is the causal effect.

<div style="display:flex;justify-content:center;align-items:stretch;gap:0;margin-top:1.6rem;">

<div style="display:flex;flex-direction:column;justify-content:center;align-items:center;padding:0 1.2rem;">
<div style="font-size:5rem;line-height:1;">🙂</div>
<div style="font-family:'JetBrains Mono',monospace;font-size:0.72rem;color:#6B6B6B;text-transform:uppercase;letter-spacing:0.12em;margin-top:0.6rem;">one user</div>
</div>

<div style="display:flex;flex-direction:column;gap:0.9rem;justify-content:center;flex:1;max-width:560px;">

<div style="display:flex;align-items:center;gap:0.9rem;">
<div style="font-size:1.5rem;color:#1A8F4F;">→</div>
<div style="flex:1;padding:0.7rem 1rem;background:#FAFAFA;border-left:3px solid #1A8F4F;font-size:1.05rem;">world <b>with</b> the feature → outcome A</div>
<div style="font-weight:700;color:#1A8F4F;font-family:'JetBrains Mono',monospace;font-size:0.85rem;">OBSERVED</div>
</div>

<v-click>

<div style="display:flex;align-items:center;gap:0.9rem;opacity:0.65;">
<div style="font-size:1.5rem;color:#E5142B;">→</div>
<div style="flex:1;padding:0.7rem 1rem;background:#FAFAFA;border-left:3px solid #E5142B;font-size:1.05rem;">world <b>without</b> the feature → outcome B</div>
<div style="font-weight:700;color:#E5142B;font-family:'JetBrains Mono',monospace;font-size:0.85rem;">NEVER SEEN</div>
</div>

</v-click>

</div>

</div>

<v-click>

<div style="margin-top:1.6rem;text-align:center;font-size:1.2rem;line-height:1.5;">

For one user, <span class="pink">we always see one side and never the other</span>.

</div>

</v-click>

<!--
There is no twin in an alternate universe to give us the second outcome. The user lives one world. Whatever we did to them, the unobserved counterfactual stays unobserved forever. The next slide shows the way out.
-->

---

# Per group, not per user

If we cannot see both worlds for one user, we look at two groups instead.

<div style="display:flex;justify-content:center;align-items:flex-start;gap:2.4rem;margin-top:1.4rem;">

<div style="display:flex;flex-direction:column;align-items:center;">
<div style="font-family:'JetBrains Mono',monospace;font-size:0.72rem;color:#1A8F4F;text-transform:uppercase;letter-spacing:0.12em;margin-bottom:0.6rem;">Treatment group</div>
<div style="display:flex;align-items:center;gap:0.6rem;">
<div style="font-size:1.8rem;letter-spacing:0.12rem;">🙂🙂🙂</div>
<div style="font-size:1.4rem;color:#1A8F4F;">→</div>
<div style="font-size:3.6rem;line-height:1;">🌍</div>
</div>
<div style="margin-top:0.4rem;font-size:0.8rem;color:#6B6B6B;font-family:'JetBrains Mono',monospace;letter-spacing:0.05em;text-transform:uppercase;">world with the feature</div>
<div style="margin-top:0.7rem;font-family:'JetBrains Mono',monospace;font-size:0.95rem;">average outcome <b>A̅</b></div>
</div>

<div style="font-size:2rem;color:#1A1A1A;font-weight:800;margin-top:1.6rem;">vs</div>

<div style="display:flex;flex-direction:column;align-items:center;">
<div style="font-family:'JetBrains Mono',monospace;font-size:0.72rem;color:#1A8F4F;text-transform:uppercase;letter-spacing:0.12em;margin-bottom:0.6rem;">Control group</div>
<div style="display:flex;align-items:center;gap:0.6rem;">
<div style="font-size:1.8rem;letter-spacing:0.12rem;">🙂🙂🙂</div>
<div style="font-size:1.4rem;color:#1A8F4F;">→</div>
<div style="font-size:3.6rem;line-height:1;">🌎</div>
</div>
<div style="margin-top:0.4rem;font-size:0.8rem;color:#6B6B6B;font-family:'JetBrains Mono',monospace;letter-spacing:0.05em;text-transform:uppercase;">world without the feature</div>
<div style="margin-top:0.7rem;font-family:'JetBrains Mono',monospace;font-size:0.95rem;">average outcome <b>B̅</b></div>
</div>

</div>

<v-click>

<div style="margin-top:1.3rem;text-align:center;font-size:1.2rem;line-height:1.5;">

The <span class="pink">difference of group averages</span>, $\bar A - \bar B$, is our estimate of the causal effect.

</div>

</v-click>

---

# To compare fairly, we <span class="pink">randomize</span>

<div style="margin-top:2.2rem;text-align:center;font-size:1.4rem;font-weight:500;line-height:1.55;max-width:54rem;margin-inline:auto;color:#1A1A1A;">

In a randomized controlled trial, the only difference between groups is the treatment we picked. Any other difference is random noise.

</div>

<v-click>

<div style="margin-top:1.6rem;text-align:center;font-size:1.15rem;line-height:1.5;color:#6B6B6B;max-width:52rem;margin-inline:auto;">

There is no method in modern science that beats this. <span style="color:#FF00FF;font-weight:700;">If you can run one, run it.</span>

</div>

</v-click>

<!--
RCT, randomized controlled trial. The whole rest of the lecture is about how to actually pull it off without breaking the assumptions that make it work.
-->

---
layout: section
class: tint-rose
---

## 02

# Randomization and its assumptions

---

# Why randomization works

Random assignment does not depend on <span class="pink">any</span> user trait, known or unknown. Age, country, tier, history, motivation all end up balanced between the two groups, on average. As $n$ grows, "on average" gets closer to "in practice", and even traits we never measured stay balanced.

<!--
The naive comparison failed because users were free to differ in many ways. Honest randomization removes that channel. What is left is sampling noise, and statistics knows how to handle noise.
-->

---
layout: statement
---

# The only systematic difference between groups is the <span class="pink">treatment</span>

<v-click>

<div style="margin-top:1.8rem;text-align:center;font-size:1.3rem;font-weight:500;line-height:1.6;max-width:56rem;margin-inline:auto;color:#1A1A1A;">

One change, one stat-sig difference, one conclusion: the change moved the metric. The chance of a false positive stays at α, because that is what the test is built to do.

</div>

</v-click>

<!--
This is the payoff of randomization in one line. If we did one thing differently between groups and the metric moves more than chance would explain, we have license to call it the effect of that one thing. Without randomization, this license disappears, regardless of how clean the statistics look.
-->

---

# Balance grows with n, across every covariate

Each user has six traits: age, income, tenure, activity, country, device. With a random splitter, every panel balances as $n$ grows, including traits we did not measure. Switch to a biased splitter that sorts by income, and the income panel splits in two halves. <span class="pink">Age drifts</span> too, because age and income are correlated. The rest stay balanced.

<div style="display:flex;justify-content:center;margin-top:1.2rem;">
<a href="/harbour-product-analytics-2026/08-experiments-1/balance-sim.html" target="_blank" rel="noopener" style="display:inline-block;padding:0.8rem 1.4rem;background:#1A1A1A;color:#fff;font-family:'JetBrains Mono',monospace;font-size:0.95rem;font-weight:700;letter-spacing:0.08em;text-transform:uppercase;text-decoration:none;border:2px solid #1A1A1A;">Open simulation ↗</a>
</div>

<!--
Walk the slider. Random at n=50, visible noise everywhere. Random at n=1000, every panel overlaps. Switch to biased at any n: income splits in half cleanly, age drifts with it, the rest stay balanced. The lesson is what randomization handles for free, and what a broken splitter leaks into.
-->

---

# SUTVA

The **Stable Unit Treatment Value Assumption** says experiment units do not interfere with one another.

Each user's behavior depends on their own variant only. It does not depend on what variant other users got.

---

# Where SUTVA breaks

Some settings make the assumption almost impossible to hold.

- **Social networks**, where a feature can spill over to a user's network
- **Communication tools** like Skype, where peer-to-peer calls cross the bucket
- **Co-authoring tools** like Google Docs and Microsoft Office, where two users edit the same document
- **Two-sided marketplaces** like Airbnb, Uber, eBay, ad auctions, where the "other" side carries the effect. Lowering prices for Treatment moves the auction Controls see

Whenever one user can be affected by another user's variant, SUTVA is at risk.

<div style="margin-top:1.4rem;font-family:'JetBrains Mono',monospace;font-size:0.72rem;color:#AAAAAA;letter-spacing:0.1em;text-transform:uppercase;">Kohavi, Tang, Xu &middot; Trustworthy Online Controlled Experiments &middot; 2020</div>

---

# Wallapop, new badge for sellers

<div style="display:grid;grid-template-columns:1fr 1.4fr;gap:1.6rem;align-items:center;margin-top:0.4rem;">

<div>

![](./images/wallapop-badge.png){width=380px}

</div>

<div style="font-size:1.0rem;line-height:1.55;">

We randomize sellers into control and treatment, and ship a new badge to the treatment arm.

Sellers in the control group are also <b>buyers</b> on the same marketplace. When they buy, they see badges on treatment sellers and change their behavior. Badged sellers also get more attention from buyers, so control sellers receive fewer contacts because of the treatment.

<v-click>

Both paths break SUTVA. The control group is no longer the <span class="pink">"world without the feature"</span>.

</v-click>

</div>

</div>

---

# Ignorability and positivity

**Ignorability** says assignment is independent of user characteristics, which honest randomization gives us for free. It breaks the moment the bucketing logic correlates with an attribute (the broken splitter from a few slides back is exactly this).

**Positivity** says every unit could land in either group with non-zero probability. It breaks when, say, the treatment is iOS-only while control is Web-only, because then ATE is undefined on the population.

---

# Three conditions

| Assumption | What it says |
|---|---|
| **SUTVA** | One user does not affect another, treatment is uniform within the arm |
| **Ignorability** | Assignment is independent of user characteristics |
| **Positivity** | Every unit can land in either group |

Break any one of them, and confounding is back. We will return to each as a failure mode in the limits session.

---
layout: section
class: tint-mint
---

## 03

# Planning

---

# The pipeline

<div style="display:grid;grid-template-columns:1fr auto 1fr auto 1fr auto 1fr;gap:0.6rem;align-items:start;margin-top:2.4rem;">

<div>
<div style="font-family:'JetBrains Mono',monospace;font-size:0.78rem;color:#FF00FF;letter-spacing:0.14em;text-transform:uppercase;font-weight:700;margin-bottom:0.7rem;">Planning</div>
<div style="font-size:1.05rem;line-height:1.6;color:#1A1A1A;">
Hypothesis<br/>
Metrics<br/>
Alignment<br/>
Sample size
</div>
</div>

<div style="font-size:2rem;color:#1A1A1A;padding-top:0.4rem;">→</div>

<div>
<div style="font-family:'JetBrains Mono',monospace;font-size:0.78rem;color:#FF00FF;letter-spacing:0.14em;text-transform:uppercase;font-weight:700;margin-bottom:0.7rem;">Design</div>
<div style="font-size:1.05rem;line-height:1.6;color:#1A1A1A;">
Randomization<br/>
Exposure
</div>
</div>

<div style="font-size:2rem;color:#1A1A1A;padding-top:0.4rem;">→</div>

<div>
<div style="font-family:'JetBrains Mono',monospace;font-size:0.78rem;color:#FF00FF;letter-spacing:0.14em;text-transform:uppercase;font-weight:700;margin-bottom:0.7rem;">Run</div>
<div style="font-size:1.05rem;line-height:1.6;color:#1A1A1A;">
Sanity checks
</div>
</div>

<div style="font-size:2rem;color:#1A1A1A;padding-top:0.4rem;">→</div>

<div>
<div style="font-family:'JetBrains Mono',monospace;font-size:0.78rem;color:#FF00FF;letter-spacing:0.14em;text-transform:uppercase;font-weight:700;margin-bottom:0.7rem;">Decision</div>
<div style="font-size:1.05rem;line-height:1.6;color:#1A1A1A;">
Results<br/>
Ship / kill / iterate
</div>
</div>

</div>

<div style="margin-top:2.8rem;text-align:center;color:#6B6B6B;font-size:1.05rem;">Strict order. A problem shows up at Decision, but the real cause is earlier.</div>

---

# Hypothesis

<div style="margin-top:0.6rem;padding:0.95rem 1.2rem;background:#FAFAFA;border-left:3px solid #FF00FF;font-size:1.2rem;line-height:1.55;">

If we make <b>X</b>, then metric <b>Y</b> will move by <b>Z</b>, because of mechanism <b>Q</b>.

</div>

The form locks the direction, size and mechanism before any data comes in. When we look at the results, there is one thing to check, not many. <span class="pink">One change, one causal claim.</span>

<v-click>

<div style="margin-top:1.4rem;padding:0.85rem 1.1rem;background:#FFF6F8;border-left:3px solid #E5142B;font-size:1.1rem;line-height:1.5;color:#1A1A1A;">

<b style="color:#E5142B;">Experiments do not improve hypothesis quality.</b> A bad hypothesis can still give us a statistically significant result, and that result is useless. Writing the hypothesis matters as much as running the test.

</div>

</v-click>

---

# You test only what you test

<div style="display:grid;grid-template-columns:1.6fr 1fr;gap:1.6rem;align-items:center;margin-top:0.4rem;">

<div>

![](./images/uber-ab.png){width=520px}

</div>

<div style="font-size:1.05rem;line-height:1.55;">

If conversion moves between A and B, which change drove it?

<v-click>

<div style="margin-top:1rem;color:#1A1A1A;">
A and B differ in <b>many</b> things at once: map header, list layout, price format, "Cheaper" badge, arrival time, CTA style.
</div>

<div style="margin-top:0.8rem;color:#FF00FF;font-weight:700;font-size:1.15rem;line-height:1.35;">

We tested a bundle, not the change we claimed.

</div>

</v-click>

</div>

</div>

<!--
Ask the room first. Let them try to point at the change that moved the metric. After a moment, click to show the list of things that actually differ.
-->

---

# The hypothesis card

Before launch, write the experiment down in four lines. Each line is locked before any data comes in.

<div style="display:grid;grid-template-columns:auto 1fr;gap:0.55rem 1.4rem;margin-top:1.2rem;font-size:1.0rem;align-items:center;">

<div style="font-family:'JetBrains Mono',monospace;font-size:0.78rem;color:#FF00FF;letter-spacing:0.14em;text-transform:uppercase;font-weight:700;">Objective</div>
<div style="padding:0.55rem 0.95rem;background:#FAFAFA;border-left:3px solid #1A1A1A;">the business outcome we are chasing</div>

<div style="font-family:'JetBrains Mono',monospace;font-size:0.78rem;color:#FF00FF;letter-spacing:0.14em;text-transform:uppercase;font-weight:700;">Insight</div>
<div style="padding:0.55rem 0.95rem;background:#FAFAFA;border-left:3px solid #1A1A1A;">the data or observation that makes us believe this change will move it</div>

<div style="font-family:'JetBrains Mono',monospace;font-size:0.78rem;color:#FF00FF;letter-spacing:0.14em;text-transform:uppercase;font-weight:700;">Hypothesis</div>
<div style="padding:0.55rem 0.95rem;background:#FAFAFA;border-left:3px solid #1A1A1A;">if we change X, metric Y moves by Z, because of mechanism Q</div>

<div style="font-family:'JetBrains Mono',monospace;font-size:0.78rem;color:#FF00FF;letter-spacing:0.14em;text-transform:uppercase;font-weight:700;">Expectations</div>
<div style="padding:0.55rem 0.95rem;background:#FAFAFA;border-left:3px solid #FF00FF;">what looks like a win, what looks like a loss</div>

</div>

<v-click>

<div style="margin-top:1.1rem;text-align:center;color:#FF00FF;font-family:'Bricolage Grotesque','Inter',sans-serif;font-weight:800;font-size:1.45rem;line-height:1.25;">

If a row is missing, you will guess it later from the data. That answer is rarely the right one.

</div>

</v-click>

---

# Your turn: Airbnb verified host badge

**Feature.** A "Verified host" badge on listings whose host has completed identity verification.

<div style="display:grid;grid-template-columns:auto 1fr;gap:0.4rem 1.2rem;margin-top:0.8rem;font-size:0.92rem;align-items:center;">

<div style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#FF00FF;letter-spacing:0.12em;text-transform:uppercase;font-weight:700;">Objective</div>
<div style="padding:0.4rem 0.85rem;background:#FAFAFA;border-left:3px solid #1A1A1A;">grow gross bookings</div>

<div style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#FF00FF;letter-spacing:0.12em;text-transform:uppercase;font-weight:700;">Insight</div>
<div style="padding:0.4rem 0.85rem;background:#FAFAFA;border-left:3px solid #1A1A1A;">first-time guests cite host trust as the top blocker</div>

<div style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#FF00FF;letter-spacing:0.12em;text-transform:uppercase;font-weight:700;">Hypothesis</div>
<div style="padding:0.4rem 0.85rem;background:#FAFAFA;border-left:3px solid #1A1A1A;">a badge raises booking conversion on verified listings</div>

<div style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#FF00FF;letter-spacing:0.12em;text-transform:uppercase;font-weight:700;">Expectations</div>
<div style="padding:0.4rem 0.85rem;background:#FAFAFA;border-left:3px solid #FF00FF;color:#6B6B6B;font-style:italic;">what looks like a win, what looks like a loss?</div>

</div>

<v-click>

<div style="margin-top:0.7rem;padding:0.55rem 0.9rem;background:#FAFAFA;border-left:3px solid #1A8F4F;font-size:0.88rem;line-height:1.5;">

<b style="color:#1A8F4F;">Ship if</b> booking conversion on verified listings is up by at least 3pp, with no drop in new host signups and no drop on unverified listings. Anything else, do not ship.

</div>

</v-click>

---

# Your turn: Spotify Discover Weekly

**Feature.** A new ranking model for the Discover Weekly playlist.

<div style="display:grid;grid-template-columns:auto 1fr;gap:0.4rem 1.2rem;margin-top:0.8rem;font-size:0.92rem;align-items:center;">

<div style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#FF00FF;letter-spacing:0.12em;text-transform:uppercase;font-weight:700;">Objective</div>
<div style="padding:0.4rem 0.85rem;background:#FAFAFA;border-left:3px solid #1A1A1A;">grow listening minutes per user</div>

<div style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#FF00FF;letter-spacing:0.12em;text-transform:uppercase;font-weight:700;">Insight</div>
<div style="padding:0.4rem 0.85rem;background:#FAFAFA;border-left:3px solid #1A1A1A;">users who like the first 3 tracks listen 2× longer in the session</div>

<div style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#FF00FF;letter-spacing:0.12em;text-transform:uppercase;font-weight:700;">Hypothesis</div>
<div style="padding:0.4rem 0.85rem;background:#FAFAFA;border-left:3px solid #1A1A1A;color:#6B6B6B;font-style:italic;">what change, on what metric, by how much, why?</div>

<div style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#FF00FF;letter-spacing:0.12em;text-transform:uppercase;font-weight:700;">Expectations</div>
<div style="padding:0.4rem 0.85rem;background:#FAFAFA;border-left:3px solid #FF00FF;color:#6B6B6B;font-style:italic;">what looks like a win, what looks like a loss?</div>

</div>

<v-click>

<div style="margin-top:0.7rem;padding:0.55rem 0.9rem;background:#FAFAFA;border-left:3px solid #1A8F4F;font-size:0.88rem;line-height:1.5;">

<b>Hypothesis.</b> A better ranking on positions 1 to 3 lifts listening minutes per user by 2% or more, because a strong start keeps users in the session longer.
<br/>
<b style="color:#1A8F4F;">Ship if</b> listening minutes are up by at least 2%, with skip rate flat or lower and save rate flat or up. Anything else, do not ship.

</div>

</v-click>

---

# Metrics

Every experiment names three roles before it launches.

<div style="display:grid;grid-template-columns:repeat(3, 1fr);gap:1.1rem;margin-top:1.2rem;">

<div style="padding:1rem 0.95rem;background:#FAFAFA;border-left:3px solid #FF00FF;">
<div style="font-family:'JetBrains Mono',monospace;font-size:0.74rem;color:#FF00FF;letter-spacing:0.14em;text-transform:uppercase;margin-bottom:0.5rem;font-weight:700;">Success</div>
<div style="font-size:1.0rem;line-height:1.5;">The metric the ship-or-kill decision rides on.</div>
</div>

<div style="padding:1rem 0.95rem;background:#FAFAFA;border-left:3px solid #1A1A1A;">
<div style="font-family:'JetBrains Mono',monospace;font-size:0.74rem;color:#1A1A1A;letter-spacing:0.14em;text-transform:uppercase;margin-bottom:0.5rem;font-weight:700;">Proxy</div>
<div style="font-size:1.0rem;line-height:1.5;">Faster or more sensitive than success. Stands in when success is too slow or too noisy.</div>
</div>

<div style="padding:1rem 0.95rem;background:#FAFAFA;border-left:3px solid #1A1A1A;">
<div style="font-family:'JetBrains Mono',monospace;font-size:0.74rem;color:#1A1A1A;letter-spacing:0.14em;text-transform:uppercase;margin-bottom:0.5rem;font-weight:700;">Guardrail</div>
<div style="font-size:1.0rem;line-height:1.5;">Must not regress, even if success improves.</div>
</div>

</div>

<v-click>

<div style="margin-top:1.2rem;text-align:center;font-size:1.1rem;line-height:1.5;">

<span class="pink">Pre-declare or lose α.</span> If we choose the success metric after we see the data, we have done multiple testing without admitting it.

</div>

</v-click>

---

# You measure only what you measure

The result of the experiment is whatever your metric captures. If the metric does not reflect the hypothesis, the test produces a valid answer to the wrong question.

Common reasons the mismatch shows up: how the change is built into the product, which variants actually shipped, which event the metric counts, and when.

<v-click>

<div style="margin-top:1.2rem;text-align:center;color:#FF00FF;font-family:'Bricolage Grotesque','Inter',sans-serif;font-weight:800;font-size:1.6rem;line-height:1.2;letter-spacing:-0.01em;">

A misaligned metric gives the correct statistical answer to the wrong question.

</div>

</v-click>

---

# 7 vs 14 day free trial

<div style="display:grid;grid-template-columns:1.5fr 1fr;gap:1.6rem;align-items:center;margin-top:0.4rem;">

<div>

![](./images/trial-ab.png){width=500px}

</div>

<div style="font-size:1.1rem;line-height:1.55;">

What's happening in A vs B?

<v-click>

<div style="margin-top:0.9rem;color:#1A1A1A;">They extended the free trial from <b>7 to 14 days</b>.</div>

</v-click>

<v-click>

<div style="margin-top:1rem;font-family:'JetBrains Mono',monospace;font-size:0.95rem;color:#FF00FF;letter-spacing:0.05em;text-transform:uppercase;">Which metrics go up?</div>

</v-click>

<v-click>

<div style="margin-top:0.6rem;font-family:'JetBrains Mono',monospace;font-size:0.95rem;color:#FF00FF;letter-spacing:0.05em;text-transform:uppercase;">Which metrics go down?</div>

</v-click>

</div>

</div>

<!--
Walk the room through it: first ask what changed (reveal: trial length). Then ask the room which metrics they think will go up (trial start CR, time to charge). Then which go down (trial-to-paid, retention after charge, possibly net revenue). Use the next slide to lay out the full chain.
-->

---

# The full chain

<div style="display:grid;grid-template-columns:repeat(5, 1fr);gap:0.7rem;margin-top:1.4rem;">

<div style="padding:1rem 0.6rem;border:2px solid #1A1A1A;background:#FAFAFA;text-align:center;">
<div style="font-family:'JetBrains Mono',monospace;font-size:0.65rem;color:#AAAAAA;letter-spacing:0.1em;text-transform:uppercase;margin-bottom:0.35rem;">01</div>
<div style="font-weight:700;font-size:1.0rem;">Free users</div>
</div>

<div style="padding:1rem 0.6rem;border:2px solid #1A1A1A;background:#FAFAFA;text-align:center;">
<div style="font-family:'JetBrains Mono',monospace;font-size:0.65rem;color:#AAAAAA;letter-spacing:0.1em;text-transform:uppercase;margin-bottom:0.35rem;">02</div>
<div style="font-weight:700;font-size:1.0rem;">Trial start</div>
</div>

<div style="padding:1rem 0.6rem;border:2px solid #1A1A1A;background:#FAFAFA;text-align:center;">
<div style="font-family:'JetBrains Mono',monospace;font-size:0.65rem;color:#AAAAAA;letter-spacing:0.1em;text-transform:uppercase;margin-bottom:0.35rem;">03</div>
<div style="font-weight:700;font-size:1.0rem;">Paid</div>
</div>

<div style="padding:1rem 0.6rem;border:2px solid #1A1A1A;background:#FAFAFA;text-align:center;">
<div style="font-family:'JetBrains Mono',monospace;font-size:0.65rem;color:#AAAAAA;letter-spacing:0.1em;text-transform:uppercase;margin-bottom:0.35rem;">04</div>
<div style="font-weight:700;font-size:1.0rem;">Paying users</div>
</div>

<div style="padding:1rem 0.6rem;border:2px solid #FF00FF;background:#FAFAFA;text-align:center;">
<div style="font-family:'JetBrains Mono',monospace;font-size:0.65rem;color:#FF00FF;letter-spacing:0.1em;text-transform:uppercase;margin-bottom:0.35rem;">05</div>
<div style="font-weight:700;font-size:1.0rem;color:#FF00FF;">Revenue</div>
</div>

</div>

<div style="display:grid;grid-template-columns:repeat(5, 1fr);gap:0.7rem;margin-top:0.4rem;font-family:'JetBrains Mono',monospace;font-size:0.74rem;color:#6B6B6B;text-align:center;letter-spacing:0.05em;">
<div></div>
<div>trial-start CR</div>
<div>trial-to-paid CR</div>
<div>retention</div>
<div>× ARPU</div>
</div>

<div style="margin-top:1.4rem;font-size:1.05rem;line-height:1.55;">

A change at step 01 has to clear <b>four conversion gates</b> before it touches revenue. A metric on step 02 measures step 02, and it is not a stand-in for step 05.

<v-click>

If the hypothesis is about <span class="pink">revenue</span>, the success metric lives on step 05.

</v-click>

</div>

<!--
Each arrow is a conversion rate. Each conversion is a chance for the effect to vanish, reverse, or get absorbed. Trial-start CR can grow 30% while paying-user count drops, because the long trial caused more starts but the same people who would have paid anyway are now more likely to cancel before charge. Read the chain forward when designing the metric, do not pick the first thing that looks like it moves.
-->

---

# Manychat, CTA on the trial wall

**Hypothesis.** A more product-oriented CTA copy will increase trial activation.

<div style="display:grid;grid-template-columns:1fr 1fr;gap:1.2rem;margin-top:1rem;align-items:center;">

<div>

![](./images/manychat-cta-a.png){width=420px}

</div>

<div>

![](./images/manychat-cta-b.png){width=420px}

</div>

</div>

<div style="margin-top:0.9rem;text-align:center;font-size:1.15rem;">

Conversion grew by <span class="pink">25%</span>. What's the problem?

</div>

<!--
Ask the room. Let them squint at the two screens before clicking through.
-->

---

# What actually changed

We did not just rewrite the copy.

- The headline became product-oriented ("Reply more and grow your followers with Pro")
- The button label changed from <b>Activate Pro Trial</b> to <b>Try for free</b>
- The button placement and visual weight changed
- A secondary "Decide later" link appeared

<v-click>

<div style="margin-top:1.2rem;padding:0.85rem 1.1rem;background:#FFF6F8;border-left:3px solid #E5142B;font-size:1.05rem;line-height:1.55;color:#1A1A1A;">

The hypothesis was about <b>copy</b>, but the change we shipped was a <b>bundle</b>. The 25% lift could come from "Try for free" sounding less risky to users, not from product-oriented copy.

</div>

</v-click>

<v-click>

<div style="margin-top:0.9rem;text-align:center;color:#FF00FF;font-family:'Bricolage Grotesque','Inter',sans-serif;font-weight:800;font-size:1.4rem;line-height:1.25;">

You tested a bundle, not a hypothesis.

</div>

</v-click>

---

# Sample size planning

Lock α, β, the practical effect, and the metric variance before launch. From these we get the weeks we need.

<div style="margin-top:0.7rem;font-size:0.9rem;">

| Metric | α | β | Practical effect | Weeks |
|---|---|---|---|---|
| Revenue per user | 5% | 20% | +2% | 6 |
| Trial-to-paid | 5% | 20% | +1pp | 4 |
| D7 retention | 5% | 20% | +0.5pp | 12 |
| Activation | 5% | 20% | +1pp | 3 |

</div>

<div style="margin-top:0.8rem;font-size:0.95rem;color:#6B6B6B;">Read forward (weeks for this effect?) or backward (given the weeks, what effect can we catch?).</div>

---

# What if the wait is too long

Three things we can try when the planned duration is too long.

<div style="display:grid;grid-template-columns:repeat(3, 1fr);gap:1.1rem;margin-top:1.2rem;">

<div style="padding:1rem 0.95rem;background:#FAFAFA;border-left:3px solid #1A1A1A;">
<div style="font-family:'JetBrains Mono',monospace;font-size:0.72rem;color:#FF00FF;letter-spacing:0.14em;text-transform:uppercase;margin-bottom:0.5rem;font-weight:700;">Pick a different metric</div>
<div style="font-size:0.98rem;line-height:1.5;">A more sensitive proxy may reach the same business question faster than the slow success metric.</div>
</div>

<div style="padding:1rem 0.95rem;background:#FAFAFA;border-left:3px solid #1A1A1A;">
<div style="font-family:'JetBrains Mono',monospace;font-size:0.72rem;color:#FF00FF;letter-spacing:0.14em;text-transform:uppercase;margin-bottom:0.5rem;font-weight:700;">Loosen α or β</div>
<div style="font-size:0.98rem;line-height:1.5;">Accept more false positives or more false negatives. The trade is explicit and goes in the design doc.</div>
</div>

<div style="padding:1rem 0.95rem;background:#FAFAFA;border-left:3px solid #1A1A1A;">
<div style="font-family:'JetBrains Mono',monospace;font-size:0.72rem;color:#FF00FF;letter-spacing:0.14em;text-transform:uppercase;margin-bottom:0.5rem;font-weight:700;">Reduce variance</div>
<div style="font-size:0.98rem;line-height:1.5;">Variance-reduction methods like CUPED cut σ on the analysis estimator. Detailed in the limits session.</div>
</div>

</div>

<v-click>

<div style="margin-top:1.2rem;text-align:center;color:#FF00FF;font-family:'Bricolage Grotesque','Inter',sans-serif;font-weight:800;font-size:1.4rem;line-height:1.25;">

If none of these work, the right answer is to not run the experiment.

</div>

</v-click>

---
layout: section
class: tint-cream
---

## 04

# Design

---

# How the platform splits

The unit of randomization can be user, session, device, account or market, and the choice depends on what changes, who is affected, and where effects can leak between units.

<span class="pink">Random and reproducible</span> are the two properties we need from the platform. The user lands in the same group every time, and the assignment correlates with nothing about the user. Hashing the user_id gives both at once.

---

# Manychat, user vs account

A user runs several accounts, and an account has several admins. The relationship is many-to-many.

Randomizing <b>by user</b> means two admins of the same account see different treatments, and the workspace becomes a mix that breaks consistency.

Randomizing <b>by account</b> means all admins of an account share one treatment, and the workspace stays consistent.

<v-click>

<div style="margin-top:1.4rem;text-align:center;color:#FF00FF;font-family:'Bricolage Grotesque','Inter',sans-serif;font-weight:800;font-size:1.5rem;line-height:1.2;letter-spacing:-0.01em;">

Randomize at the level where the treatment lands and where the effects build up.

</div>

</v-click>

---

# Eligible vs exposed

A user is **eligible** when the experiment conditions match and they were assigned to a bucket. They are **exposed** when they actually saw the change.

<div style="display:grid;grid-template-columns:1fr 1.6rem 1fr 1.6rem 1.5fr;gap:0.7rem;align-items:center;margin-top:1.2rem;">

<div style="padding:0.85rem 0.6rem;border:1.5px solid #1A1A1A;background:#FAFAFA;text-align:center;">
<div style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#FF00FF;letter-spacing:0.12em;text-transform:uppercase;font-weight:700;margin-bottom:0.3rem;">Eligible</div>
<div style="font-size:1.3rem;font-weight:700;">10,000</div>
<div style="font-size:0.72rem;color:#6B6B6B;margin-top:0.15rem;">in a bucket</div>
</div>

<div style="font-size:1.6rem;color:#1A1A1A;text-align:center;">→</div>

<div style="display:flex;flex-direction:column;gap:0.35rem;">
<div style="padding:0.45rem 0.55rem;border:1.5px solid #1A1A1A;background:#FAFAFA;text-align:center;">
<div style="font-family:'JetBrains Mono',monospace;font-size:0.62rem;color:#1A1A1A;letter-spacing:0.1em;text-transform:uppercase;">Treatment</div>
<div style="font-weight:700;font-size:0.95rem;">5,000</div>
</div>
<div style="padding:0.45rem 0.55rem;border:1.5px solid #1A1A1A;background:#FAFAFA;text-align:center;">
<div style="font-family:'JetBrains Mono',monospace;font-size:0.62rem;color:#1A1A1A;letter-spacing:0.1em;text-transform:uppercase;">Control</div>
<div style="font-weight:700;font-size:0.95rem;">5,000</div>
</div>
</div>

<div style="font-size:1.6rem;color:#1A1A1A;text-align:center;">→</div>

<div style="display:flex;flex-direction:column;gap:0.35rem;">
<div style="padding:0.45rem 0.65rem;border:1.5px solid #1A8F4F;background:#FAFAFA;text-align:center;">
<div style="font-family:'JetBrains Mono',monospace;font-size:0.62rem;color:#1A8F4F;letter-spacing:0.1em;text-transform:uppercase;font-weight:700;">Exposed in T</div>
<div style="font-weight:700;font-size:0.95rem;">2,500</div>
<div style="font-size:0.7rem;color:#6B6B6B;">saw the feature</div>
</div>
<div style="padding:0.45rem 0.65rem;border:1.5px solid #E5142B;background:#FFF6F8;text-align:center;">
<div style="font-family:'JetBrains Mono',monospace;font-size:0.62rem;color:#E5142B;letter-spacing:0.1em;text-transform:uppercase;font-weight:700;">Not exposed</div>
<div style="font-weight:700;font-size:0.95rem;">2,500</div>
<div style="font-size:0.7rem;color:#6B6B6B;">never reached it</div>
</div>
</div>

</div>

<v-click>

<div style="margin-top:1.1rem;font-size:1.05rem;line-height:1.55;">

If we count all 5,000 as treatment, half of them never saw the feature, so the signal on the analysis pool is smaller than the true effect. The <span class="pink">MDE we actually reach is larger than the one we planned for</span>, and the test can miss a real effect.

</div>

</v-click>

---
layout: section
class: tint-sky
---

## 05

# Run

---

# While the experiment runs

Three things to watch, three reasons to stop or wait.

<div style="display:grid;grid-template-columns:repeat(3, 1fr);gap:1.1rem;margin-top:1.4rem;">

<div style="padding:1rem 0.95rem;background:#FAFAFA;border-left:3px solid #1A1A1A;">
<div style="font-family:'JetBrains Mono',monospace;font-size:0.72rem;color:#FF00FF;letter-spacing:0.14em;text-transform:uppercase;margin-bottom:0.5rem;font-weight:700;">Health</div>
<div style="font-size:0.98rem;line-height:1.5;">SRM, balance, A/A baseline. The platform should behave the way the design says. If not, we fix it before looking at the results.</div>
</div>

<div style="padding:1rem 0.95rem;background:#FAFAFA;border-left:3px solid #E5142B;">
<div style="font-family:'JetBrains Mono',monospace;font-size:0.72rem;color:#E5142B;letter-spacing:0.14em;text-transform:uppercase;margin-bottom:0.5rem;font-weight:700;">Extreme degradation</div>
<div style="font-size:0.98rem;line-height:1.5;">Hard guardrail breach, kill switch, root-cause diagnostics. Used to stop, never to ship early.</div>
</div>

<div style="padding:1rem 0.95rem;background:#FAFAFA;border-left:3px solid #1A1A1A;">
<div style="font-family:'JetBrains Mono',monospace;font-size:0.72rem;color:#1A1A1A;letter-spacing:0.14em;text-transform:uppercase;margin-bottom:0.5rem;font-weight:700;">No decisions until volume</div>
<div style="font-size:0.98rem;line-height:1.5;">No ship-or-kill calls until the planned $n$ is reached. Peeking is a separate failure mode, covered in the limits session.</div>
</div>

</div>

---
layout: section
class: tint-lavender
---

## 06

# Decision

---

# Stick to the plan

The only way to keep α at the level we picked is to decide on the setup we locked **before** launch. Anything else breaks the guarantee statistics gave us yesterday.

<div style="display:grid;grid-template-columns:1fr 1fr;gap:1.1rem;margin-top:1.2rem;">

<div style="padding:0.95rem 1rem;background:#FFF6F8;border-left:3px solid #E5142B;">
<div style="font-family:'JetBrains Mono',monospace;font-size:0.72rem;color:#E5142B;letter-spacing:0.14em;text-transform:uppercase;margin-bottom:0.45rem;font-weight:700;">Find any significant metric</div>
<div style="font-size:0.95rem;line-height:1.5;">Pick the metric that came out significant after we saw the data. With 20 metrics, the chance that at least one crosses α by noise is far above 5%.</div>
</div>

<div style="padding:0.95rem 1rem;background:#FFF6F8;border-left:3px solid #E5142B;">
<div style="font-family:'JetBrains Mono',monospace;font-size:0.72rem;color:#E5142B;letter-spacing:0.14em;text-transform:uppercase;margin-bottom:0.45rem;font-weight:700;">Check it every day</div>
<div style="font-size:0.95rem;line-height:1.5;">Check the results every day and stop when something crosses α. Same problem, just across days instead of metrics.</div>
</div>

</div>

<v-click>

<div style="margin-top:1.2rem;text-align:center;color:#FF00FF;font-family:'Bricolage Grotesque','Inter',sans-serif;font-weight:800;font-size:1.45rem;line-height:1.25;">

Decide by the plan that was written before launch.

</div>

</v-click>

<!--
Both anti-patterns inflate the effective Type I rate. We discuss multiple testing and sequential analysis in detail tomorrow. Today the rule is simple: the plan is the contract.
-->

---

# When metrics disagree

Two patterns come up often: success is up but a guardrail is down, or two success metrics say opposite things.

Today we just name the problem. Multi-metric decisions come in the next session.

---

# Ship, kill, iterate

Three outcomes, decided by a rule we wrote **before** the experiment ended. **Ship** if success is up, guardrails are OK, and the effect matches the hypothesis. **Kill** if success is flat or down, or a guardrail is broken. **Iterate** if the result is borderline ($p$ near α): rewrite the hypothesis or fix the change, then re-run.

<v-click>

For borderline single-experiment wins, <span class="pink">re-running beats shipping</span>. Replication is the practical fix against single-experiment false positives.

</v-click>

If any earlier step was skipped, the problem shows up here as a normal-looking ship decision, but the error guarantee is already gone.

---
layout: statement
---

# Skip a step, lose <span class="pink">error control</span> <br/>Without error control, the procedure means nothing

---

# Materials

<div style="display:grid;grid-template-columns:1fr 1fr;gap:2.4rem;margin-top:1.2rem;font-size:1rem;line-height:1.65;color:#1A1A1A;">

<div>

<div style="font-family:'JetBrains Mono',monospace;font-size:0.75rem;color:#AAAAAA;letter-spacing:0.14em;text-transform:uppercase;margin-bottom:0.6rem;">Book</div>
<div style="font-weight:700;margin-bottom:0.3rem;">Trustworthy Online Controlled Experiments</div>
<div style="color:#6B6B6B;">Ron Kohavi, Diane Tang, Ya Xu. Cambridge University Press, 2020</div>

</div>

<div>

<div style="font-family:'JetBrains Mono',monospace;font-size:0.75rem;color:#AAAAAA;letter-spacing:0.14em;text-transform:uppercase;margin-bottom:0.6rem;">Curriculum</div>
<div style="font-weight:700;margin-bottom:0.3rem;"><a href="https://confidence.spotify.com/bootcamp/intro-course/introduction" target="_blank">Spotify Confidence Bootcamp</a></div>
<div style="color:#6B6B6B;">Intro course on experimentation methodology</div>

</div>

</div>
