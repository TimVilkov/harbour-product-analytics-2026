---
theme: apple-basic
title: "Session 05: Statistics 1"
info: "Product Analytics · Harbour.Space · 2026"
highlighter: shiki
drawings:
  persist: false
transition: fade
mdc: true
layout: intro
---

# Statistics <span class="pink">1</span>

<div class="absolute bottom-10 left-14" style="font-family:'JetBrains Mono',monospace;font-size:0.75rem;text-transform:uppercase;letter-spacing:0.15em;color:rgba(255,255,255,0.55);">
  Harbour.Space &middot; Barcelona &middot; May 22, 2026
</div>

---
layout: quote
---

# A real course in probability starts<br><span class="pink">here</span>

<p style="font-family:'JetBrains Mono',monospace;font-size:0.78rem;letter-spacing:0.12em;color:#6B6B6B;margin-top:1.4rem;">
<a href="https://www.youtube.com/playlist?list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo" style="color:#6B6B6B;">Stanford Statistics 110 · Joe Blitzstein · YouTube playlist</a>
</p>

<p style="font-size:0.95rem;color:#1A1A1A;margin-top:1.6rem;line-height:1.5;max-width:36rem;margin-left:auto;margin-right:auto;">Today's session is a fast overview built for intuition, and the full course on probability begins at the playlist above.</p>

---

# Today

<div style="display:flex;flex-direction:column;gap:0.8rem;margin-top:1rem;">

  <div style="display:grid;grid-template-columns:48px 1fr;gap:1.2rem;align-items:baseline;">
    <span style="font-family:'JetBrains Mono',monospace;font-size:0.95rem;color:#FF00FF;letter-spacing:0.1em;">01</span>
    <div style="font-size:1.25rem;font-weight:700;color:#1A1A1A;">Probability</div>
  </div>
  <div style="display:grid;grid-template-columns:48px 1fr;gap:1.2rem;align-items:baseline;">
    <span style="font-family:'JetBrains Mono',monospace;font-size:0.95rem;color:#FF00FF;letter-spacing:0.1em;">02</span>
    <div style="font-size:1.25rem;font-weight:700;color:#1A1A1A;">Random variable</div>
  </div>
  <div style="display:grid;grid-template-columns:48px 1fr;gap:1.2rem;align-items:baseline;">
    <span style="font-family:'JetBrains Mono',monospace;font-size:0.95rem;color:#FF00FF;letter-spacing:0.1em;">03</span>
    <div style="font-size:1.25rem;font-weight:700;color:#1A1A1A;">Distribution</div>
  </div>
  <div style="display:grid;grid-template-columns:48px 1fr;gap:1.2rem;align-items:baseline;">
    <span style="font-family:'JetBrains Mono',monospace;font-size:0.95rem;color:#FF00FF;letter-spacing:0.1em;">04</span>
    <div style="font-size:1.25rem;font-weight:700;color:#1A1A1A;">Descriptive statistics</div>
  </div>
  <div style="display:grid;grid-template-columns:48px 1fr;gap:1.2rem;align-items:baseline;">
    <span style="font-family:'JetBrains Mono',monospace;font-size:0.95rem;color:#FF00FF;letter-spacing:0.1em;">05</span>
    <div style="font-size:1.25rem;font-weight:700;color:#1A1A1A;">Law of large numbers and CLT</div>
  </div>
  <div style="display:grid;grid-template-columns:48px 1fr;gap:1.2rem;align-items:baseline;">
    <span style="font-family:'JetBrains Mono',monospace;font-size:0.95rem;color:#FF00FF;letter-spacing:0.1em;">06</span>
    <div style="font-size:1.25rem;font-weight:700;color:#1A1A1A;">Putting it together</div>
  </div>

</div>

---

# Did anything actually change

<p style="font-size:0.95rem;color:#1A1A1A;margin:0.2rem 0 0.3rem;line-height:1.5;">Daily revenue before and after a feature launch, with the metric looking slightly higher afterwards even though the daily noise is large.</p>

<Chart src="/harbour-product-analytics-2026/05-statistics-1/charts/cold-open.html" height="260px" />

<!--
Do not answer the question now. The next 90 minutes is the answer.
-->

---
layout: section
class: tint-lavender
---

## 01

# Probability

---

# Random experiment

<div style="margin-top:1.2rem;">

<p style="font-size:1.1rem;color:#1A1A1A;margin:0 0 1rem;line-height:1.6;">A random experiment is a process whose outcome is uncertain in advance, but which can be repeated under the same conditions and described by precise rules.</p>

<p style="font-size:1rem;color:#1A1A1A;line-height:1.6;">Flipping a coin, rolling a die, showing a banner to a user, or observing the basket size of one purchase are all random experiments.</p>

</div>

---

# Outcome

<p style="font-size:1.05rem;color:#1A1A1A;margin:0.3rem 0 0.7rem;line-height:1.55;">An outcome is a single specific result of a random experiment. The set of all possible outcomes is the sample space Ω.</p>

<table style="border-collapse:collapse;font-size:0.96rem;color:#1A1A1A;width:100%;">
  <thead>
    <tr style="background:#F5F5F5;">
      <th style="border:1px solid #1A1A1A;padding:0.45rem 0.9rem;text-align:left;font-weight:600;">Experiment</th>
      <th style="border:1px solid #1A1A1A;padding:0.45rem 0.9rem;text-align:left;font-weight:600;">Sample space Ω</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #1A1A1A;padding:0.4rem 0.9rem;">Flip a coin</td><td style="border:1px solid #1A1A1A;padding:0.4rem 0.9rem;font-family:'JetBrains Mono',monospace;">{ heads, tails }</td></tr>
    <tr><td style="border:1px solid #1A1A1A;padding:0.4rem 0.9rem;">Roll a six-sided die</td><td style="border:1px solid #1A1A1A;padding:0.4rem 0.9rem;font-family:'JetBrains Mono',monospace;">{ 1, 2, 3, 4, 5, 6 }</td></tr>
    <tr><td style="border:1px solid #1A1A1A;padding:0.4rem 0.9rem;">Show a banner to a user</td><td style="border:1px solid #1A1A1A;padding:0.4rem 0.9rem;font-family:'JetBrains Mono',monospace;">{ converted, did not convert }</td></tr>
    <tr><td style="border:1px solid #1A1A1A;padding:0.4rem 0.9rem;">Observe one purchase in EUR</td><td style="border:1px solid #1A1A1A;padding:0.4rem 0.9rem;font-family:'JetBrains Mono',monospace;">all positive real numbers</td></tr>
  </tbody>
</table>

---

# Event

<p style="font-size:1.05rem;color:#1A1A1A;margin:0.3rem 0 0.6rem;line-height:1.55;">An event is a collection of outcomes we want to track together. Probability questions are asked about events.</p>

<table style="border-collapse:collapse;font-size:0.94rem;color:#1A1A1A;width:100%;">
  <thead>
    <tr style="background:#F5F5F5;">
      <th style="border:1px solid #1A1A1A;padding:0.4rem 0.8rem;text-align:left;font-weight:600;">Experiment</th>
      <th style="border:1px solid #1A1A1A;padding:0.4rem 0.8rem;text-align:left;font-weight:600;">Event</th>
      <th style="border:1px solid #1A1A1A;padding:0.4rem 0.8rem;text-align:left;font-weight:600;">As a set</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #1A1A1A;padding:0.4rem 0.8rem;">Roll a die</td><td style="border:1px solid #1A1A1A;padding:0.4rem 0.8rem;">even number</td><td style="border:1px solid #1A1A1A;padding:0.4rem 0.8rem;font-family:'JetBrains Mono',monospace;">{ 2, 4, 6 }</td></tr>
    <tr><td style="border:1px solid #1A1A1A;padding:0.4rem 0.8rem;">Roll a die</td><td style="border:1px solid #1A1A1A;padding:0.4rem 0.8rem;">result is at least 5</td><td style="border:1px solid #1A1A1A;padding:0.4rem 0.8rem;font-family:'JetBrains Mono',monospace;">{ 5, 6 }</td></tr>
    <tr><td style="border:1px solid #1A1A1A;padding:0.4rem 0.8rem;">Banner</td><td style="border:1px solid #1A1A1A;padding:0.4rem 0.8rem;">user converts</td><td style="border:1px solid #1A1A1A;padding:0.4rem 0.8rem;font-family:'JetBrains Mono',monospace;">{ converted }</td></tr>
    <tr><td style="border:1px solid #1A1A1A;padding:0.4rem 0.8rem;">Purchase</td><td style="border:1px solid #1A1A1A;padding:0.4rem 0.8rem;">basket above 100 EUR</td><td style="border:1px solid #1A1A1A;padding:0.4rem 0.8rem;font-family:'JetBrains Mono',monospace;">{ amount &gt; 100 }</td></tr>
  </tbody>
</table>

---

# Classical definition of probability

<p style="font-size:1.05rem;color:#1A1A1A;margin:0.3rem 0 0.6rem;line-height:1.55;">When the sample space has a finite number of equally likely outcomes, the probability of an event A is the ratio of favourable outcomes to the total.</p>

<div style="background:#FAFAFA;border-left:3px solid #FF00FF;padding:0.8rem 1.3rem;margin:0.3rem 0;font-size:1rem;color:#1A1A1A;">

$$P(A) = \frac{\text{outcomes favourable to } A}{\text{total outcomes in } \Omega}$$

</div>

<p style="font-size:0.95rem;color:#1A1A1A;line-height:1.55;">Laplace introduced this definition in the eighteenth century, and it works whenever outcomes are equally likely, which holds for a fair coin or a fair die but breaks down for an A/B test where conversion is much rarer than non-conversion.</p>

---

# Worked examples

<div style="background:#FAFAFA;border-left:3px solid #FF00FF;padding:0.9rem 1.3rem;margin:0.5rem 0;font-size:1rem;color:#1A1A1A;line-height:2.1;">

For a fair coin: $\quad P(\text{heads}) = \dfrac{1}{2}$

For a fair die: $\quad P(X = 6) = \dfrac{1}{6}$

For a fair die: $\quad P(\text{even}) = \dfrac{|\{2, 4, 6\}|}{|\{1, 2, 3, 4, 5, 6\}|} = \dfrac{3}{6} = \dfrac{1}{2}$

</div>

<p style="margin-top:0.7rem;font-size:0.95rem;color:#1A1A1A;line-height:1.55;">Conversion is not a classical-probability setting, because converting and not converting are usually not equally likely.</p>

---

# Generate outcomes

<p style="font-size:0.92rem;color:#1A1A1A;margin:0.2rem 0 0.3rem;line-height:1.5;">Each click of the pink button produces one new outcome and updates the observed proportion. Pink dashed lines mark the theoretical probability.</p>

<Chart src="/harbour-product-analytics-2026/05-statistics-1/charts/simulator.html" height="270px" />

<p style="margin-top:0.2rem;font-size:0.85rem;color:#6B6B6B;text-align:center;">Try the die first, then the coin, then a conversion experiment</p>

<!--
Use this to motivate probability as long-run frequency. Click +1 a few times to show the noise, then +100 / +10000 to show convergence toward theoretical probabilities.
-->

---
layout: section
class: tint-mint
---

## 02

# Random<br>variable

---

# Random variable

<p style="font-size:1.05rem;color:#1A1A1A;margin:0.3rem 0 0.6rem;line-height:1.55;">Most outcomes are not already numbers, and to do mathematics with them we convert each outcome into a number using a rule. That rule is a random variable.</p>

<p style="font-size:1rem;color:#1A1A1A;line-height:1.55;">Its value is not known until the experiment is actually performed.</p>

<table style="border-collapse:collapse;font-size:0.93rem;color:#1A1A1A;width:100%;margin-top:0.5rem;">
  <thead>
    <tr style="background:#F5F5F5;">
      <th style="border:1px solid #1A1A1A;padding:0.4rem 0.85rem;text-align:left;font-weight:600;">Experiment</th>
      <th style="border:1px solid #1A1A1A;padding:0.4rem 0.85rem;text-align:left;font-weight:600;">Random variable X</th>
      <th style="border:1px solid #1A1A1A;padding:0.4rem 0.85rem;text-align:left;font-weight:600;">Values</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #1A1A1A;padding:0.4rem 0.85rem;">Flip a coin</td><td style="border:1px solid #1A1A1A;padding:0.4rem 0.85rem;">indicator of heads, 1 or 0</td><td style="border:1px solid #1A1A1A;padding:0.4rem 0.85rem;font-family:'JetBrains Mono',monospace;">0, 1</td></tr>
    <tr><td style="border:1px solid #1A1A1A;padding:0.4rem 0.85rem;">Roll a die</td><td style="border:1px solid #1A1A1A;padding:0.4rem 0.85rem;">number on the top face</td><td style="border:1px solid #1A1A1A;padding:0.4rem 0.85rem;font-family:'JetBrains Mono',monospace;">1, 2, 3, 4, 5, 6</td></tr>
    <tr><td style="border:1px solid #1A1A1A;padding:0.4rem 0.85rem;">Banner</td><td style="border:1px solid #1A1A1A;padding:0.4rem 0.85rem;">conversion indicator</td><td style="border:1px solid #1A1A1A;padding:0.4rem 0.85rem;font-family:'JetBrains Mono',monospace;">0, 1</td></tr>
    <tr><td style="border:1px solid #1A1A1A;padding:0.4rem 0.85rem;">One purchase</td><td style="border:1px solid #1A1A1A;padding:0.4rem 0.85rem;">basket size in EUR</td><td style="border:1px solid #1A1A1A;padding:0.4rem 0.85rem;font-family:'JetBrains Mono',monospace;">any positive real</td></tr>
  </tbody>
</table>

---

# Three coin flips

<p style="font-size:0.98rem;color:#1A1A1A;margin:0.3rem 0 0.5rem;line-height:1.55;">Flip a fair coin three times. The outcome is a sequence such as HTH or TTT, and the sample space has eight equally likely outcomes.</p>

<p style="font-size:0.98rem;color:#1A1A1A;line-height:1.55;">Define X to be the number of heads observed. The random variable X can take only the values 0, 1, 2 or 3, and every outcome maps to one of those four numbers.</p>

<table style="border-collapse:collapse;font-size:0.93rem;color:#1A1A1A;margin-top:0.5rem;">
  <thead>
    <tr style="background:#F5F5F5;">
      <th style="border:1px solid #1A1A1A;padding:0.4rem 0.85rem;text-align:left;font-weight:600;">Outcomes</th>
      <th style="border:1px solid #1A1A1A;padding:0.4rem 0.85rem;text-align:center;font-weight:600;">X</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #1A1A1A;padding:0.4rem 0.85rem;font-family:'JetBrains Mono',monospace;">TTT</td><td style="border:1px solid #1A1A1A;padding:0.4rem 0.85rem;text-align:center;font-family:'JetBrains Mono',monospace;">0</td></tr>
    <tr><td style="border:1px solid #1A1A1A;padding:0.4rem 0.85rem;font-family:'JetBrains Mono',monospace;">HTT, THT, TTH</td><td style="border:1px solid #1A1A1A;padding:0.4rem 0.85rem;text-align:center;font-family:'JetBrains Mono',monospace;">1</td></tr>
    <tr><td style="border:1px solid #1A1A1A;padding:0.4rem 0.85rem;font-family:'JetBrains Mono',monospace;">HHT, HTH, THH</td><td style="border:1px solid #1A1A1A;padding:0.4rem 0.85rem;text-align:center;font-family:'JetBrains Mono',monospace;">2</td></tr>
    <tr><td style="border:1px solid #1A1A1A;padding:0.4rem 0.85rem;font-family:'JetBrains Mono',monospace;">HHH</td><td style="border:1px solid #1A1A1A;padding:0.4rem 0.85rem;text-align:center;font-family:'JetBrains Mono',monospace;">3</td></tr>
  </tbody>
</table>

<p style="margin-top:0.6rem;font-size:0.92rem;color:#6B6B6B;line-height:1.5;">Working with the four numbers is far more convenient than working with the eight letter sequences.</p>

---

# X versus x

<div style="margin-top:3.5rem;">

<table style="border-collapse:collapse;font-size:1rem;color:#1A1A1A;width:100%;">
  <thead>
    <tr style="background:#F5F5F5;">
      <th style="border:1px solid #1A1A1A;padding:0.5rem 0.9rem;text-align:left;font-weight:600;width:32%;">Symbol</th>
      <th style="border:1px solid #1A1A1A;padding:0.5rem 0.9rem;text-align:left;font-weight:600;">Meaning</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #1A1A1A;padding:0.5rem 0.9rem;font-family:'JetBrains Mono',monospace;">X</td><td style="border:1px solid #1A1A1A;padding:0.5rem 0.9rem;">The random variable, the rule that produces a number when the experiment runs.</td></tr>
    <tr><td style="border:1px solid #1A1A1A;padding:0.5rem 0.9rem;font-family:'JetBrains Mono',monospace;">x</td><td style="border:1px solid #1A1A1A;padding:0.5rem 0.9rem;">A specific observed number, also called a realisation of X.</td></tr>
    <tr><td style="border:1px solid #1A1A1A;padding:0.5rem 0.9rem;font-family:'JetBrains Mono',monospace;">X₁, X₂, …, Xₙ</td><td style="border:1px solid #1A1A1A;padding:0.5rem 0.9rem;">A sequence of random variables, one per planned observation.</td></tr>
    <tr><td style="border:1px solid #1A1A1A;padding:0.5rem 0.9rem;font-family:'JetBrains Mono',monospace;">x₁, x₂, …, xₙ</td><td style="border:1px solid #1A1A1A;padding:0.5rem 0.9rem;">An observed sample of size n.</td></tr>
  </tbody>
</table>

</div>

---

# Discrete and continuous

<div style="margin-top:2.4rem;">

<p style="font-size:1.05rem;color:#1A1A1A;margin:0 0 1rem;line-height:1.55;">Random variables come in two flavours depending on the values they can take.</p>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:1.6rem;">

  <div style="border-left:3px solid #FF00FF;padding:0.5rem 0 0.5rem 1.1rem;">
    <div style="font-family:'JetBrains Mono',monospace;font-size:0.72rem;color:#AAAAAA;letter-spacing:0.14em;text-transform:uppercase;margin-bottom:0.4rem;">Discrete</div>
    <div style="font-size:1rem;color:#1A1A1A;line-height:1.5;">Countable values: a die face, a conversion indicator, the number of purchases in a month.</div>
  </div>

  <div style="border-left:3px solid #FF00FF;padding:0.5rem 0 0.5rem 1.1rem;">
    <div style="font-family:'JetBrains Mono',monospace;font-size:0.72rem;color:#AAAAAA;letter-spacing:0.14em;text-transform:uppercase;margin-bottom:0.4rem;">Continuous</div>
    <div style="font-size:1rem;color:#1A1A1A;line-height:1.5;">Real-valued: a student's height, the duration of a session, the revenue from one customer.</div>
  </div>

</div>

</div>

---
layout: section
class: tint-rose
---

## 03

# Distribution

---

# What is a distribution

<p style="font-size:1.02rem;color:#1A1A1A;margin:0.3rem 0 0.6rem;line-height:1.55;">A distribution describes how often each value of a random variable appears in the long run.</p>

<p style="font-size:0.98rem;color:#1A1A1A;line-height:1.55;">For a discrete variable it is a table of probabilities, and for a continuous variable it is a smooth density curve.</p>

<table style="border-collapse:collapse;font-family:'JetBrains Mono',monospace;font-size:0.93rem;color:#1A1A1A;margin-top:0.7rem;">
  <thead>
    <tr style="background:#F5F5F5;">
      <th style="border:1px solid #1A1A1A;padding:0.4rem 0.85rem;">x</th>
      <th style="border:1px solid #1A1A1A;padding:0.4rem 0.85rem;">1</th>
      <th style="border:1px solid #1A1A1A;padding:0.4rem 0.85rem;">2</th>
      <th style="border:1px solid #1A1A1A;padding:0.4rem 0.85rem;">3</th>
      <th style="border:1px solid #1A1A1A;padding:0.4rem 0.85rem;">4</th>
      <th style="border:1px solid #1A1A1A;padding:0.4rem 0.85rem;">5</th>
      <th style="border:1px solid #1A1A1A;padding:0.4rem 0.85rem;">6</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #1A1A1A;padding:0.4rem 0.85rem;">P(X = x)</td><td style="border:1px solid #1A1A1A;padding:0.4rem 0.85rem;">1/6</td><td style="border:1px solid #1A1A1A;padding:0.4rem 0.85rem;">1/6</td><td style="border:1px solid #1A1A1A;padding:0.4rem 0.85rem;">1/6</td><td style="border:1px solid #1A1A1A;padding:0.4rem 0.85rem;">1/6</td><td style="border:1px solid #1A1A1A;padding:0.4rem 0.85rem;">1/6</td><td style="border:1px solid #1A1A1A;padding:0.4rem 0.85rem;">1/6</td></tr>
  </tbody>
</table>

---

# Discrete distribution

<p style="font-size:0.92rem;color:#1A1A1A;margin:0.2rem 0 0.4rem;line-height:1.5;">A discrete distribution can be written as a table of probabilities, one row per possible value, and the table sums to one.</p>

<div style="display:grid;grid-template-columns:1.5fr 1fr;gap:1.2rem;align-items:center;margin-top:0.3rem;">

  <Chart src="/harbour-product-analytics-2026/05-statistics-1/charts/discrete-die.html" height="220px" />

  <table style="border-collapse:collapse;font-family:'JetBrains Mono',monospace;font-size:0.88rem;color:#1A1A1A;">
    <thead>
      <tr style="background:#F5F5F5;">
        <th style="border:1px solid #1A1A1A;padding:0.32rem 0.7rem;text-align:center;font-weight:600;">x</th>
        <th style="border:1px solid #1A1A1A;padding:0.32rem 0.7rem;text-align:center;font-weight:600;">P(X = x)</th>
      </tr>
    </thead>
    <tbody>
      <tr><td style="border:1px solid #1A1A1A;padding:0.28rem 0.7rem;text-align:center;">1</td><td style="border:1px solid #1A1A1A;padding:0.28rem 0.7rem;text-align:center;">1/6</td></tr>
      <tr><td style="border:1px solid #1A1A1A;padding:0.28rem 0.7rem;text-align:center;">2</td><td style="border:1px solid #1A1A1A;padding:0.28rem 0.7rem;text-align:center;">1/6</td></tr>
      <tr><td style="border:1px solid #1A1A1A;padding:0.28rem 0.7rem;text-align:center;">3</td><td style="border:1px solid #1A1A1A;padding:0.28rem 0.7rem;text-align:center;">1/6</td></tr>
      <tr><td style="border:1px solid #1A1A1A;padding:0.28rem 0.7rem;text-align:center;">4</td><td style="border:1px solid #1A1A1A;padding:0.28rem 0.7rem;text-align:center;">1/6</td></tr>
      <tr><td style="border:1px solid #1A1A1A;padding:0.28rem 0.7rem;text-align:center;">5</td><td style="border:1px solid #1A1A1A;padding:0.28rem 0.7rem;text-align:center;">1/6</td></tr>
      <tr><td style="border:1px solid #1A1A1A;padding:0.28rem 0.7rem;text-align:center;">6</td><td style="border:1px solid #1A1A1A;padding:0.28rem 0.7rem;text-align:center;">1/6</td></tr>
    </tbody>
  </table>

</div>

<p style="margin-top:0.3rem;font-size:0.85rem;color:#6B6B6B;text-align:center;">Fair six-sided die</p>

---

# Continuous distribution

<p style="font-size:0.92rem;color:#1A1A1A;margin:0.2rem 0 0.4rem;line-height:1.5;">A continuous variable takes uncountably many values, so the probability of hitting any single one is zero. The distribution is given by a formula for the density f(x), and probability lives in intervals as the area under the curve.</p>

<div style="display:grid;grid-template-columns:1.3fr 1fr;gap:1.2rem;align-items:center;margin-top:0.3rem;">

  <Chart src="/harbour-product-analytics-2026/05-statistics-1/charts/continuous-density.html" height="230px" />

  <div style="background:#FAFAFA;border-left:3px solid #FF00FF;padding:0.7rem 1rem;font-size:0.92rem;color:#1A1A1A;line-height:1.55;">

  $$f(x) = \frac{1}{\sigma\sqrt{2\pi}} \exp\!\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)$$

  $$P(a \le X \le b) = \int_a^b f(x)\, dx$$

  </div>

</div>

<p style="margin-top:0.3rem;font-size:0.86rem;color:#1A1A1A;line-height:1.5;">The cumulative distribution function F(x) = P(X ≤ x) gives the area under f from the left up to x.</p>

---

# Different distributions, different shapes

<p style="font-size:0.95rem;color:#1A1A1A;margin:0.2rem 0 0.3rem;line-height:1.5;">The shape of a distribution carries a lot of information about the underlying process.</p>

<Chart src="/harbour-product-analytics-2026/05-statistics-1/charts/distribution-shapes.html" height="230px" />

<p style="margin-top:0.3rem;font-size:0.9rem;color:#1A1A1A;line-height:1.5;">Heights are roughly symmetric, revenue per user is heavily right-skewed, and a mixture of two user segments often produces a bimodal shape.</p>

---

# Common named distributions

<p style="font-size:0.98rem;color:#1A1A1A;margin:0.3rem 0 0.6rem;line-height:1.55;">Some distributions appear so often that they have names, fixed formulas and tabulated properties. We will mention several today and use them as building blocks in Stats 2.</p>

<div style="display:flex;flex-direction:column;gap:0.6rem;margin-top:0.3rem;">

  <div style="display:grid;grid-template-columns:170px 1fr;gap:1rem;align-items:baseline;border-bottom:1px solid #E0E0E0;padding-bottom:0.5rem;">
    <span style="font-family:'JetBrains Mono',monospace;font-size:0.82rem;color:#FF00FF;letter-spacing:0.12em;text-transform:uppercase;">Bernoulli</span>
    <div style="font-size:0.96rem;color:#1A1A1A;line-height:1.5;">Discrete variable taking value 0 or 1 with probability p, used for any conversion or success indicator</div>
  </div>

  <div style="display:grid;grid-template-columns:170px 1fr;gap:1rem;align-items:baseline;border-bottom:1px solid #E0E0E0;padding-bottom:0.5rem;">
    <span style="font-family:'JetBrains Mono',monospace;font-size:0.82rem;color:#FF00FF;letter-spacing:0.12em;text-transform:uppercase;">Uniform</span>
    <div style="font-size:0.96rem;color:#1A1A1A;line-height:1.5;">Equal probability across a range, either discrete like a die or continuous on an interval</div>
  </div>

  <div style="display:grid;grid-template-columns:170px 1fr;gap:1rem;align-items:baseline;border-bottom:1px solid #E0E0E0;padding-bottom:0.5rem;">
    <span style="font-family:'JetBrains Mono',monospace;font-size:0.82rem;color:#FF00FF;letter-spacing:0.12em;text-transform:uppercase;">Exponential</span>
    <div style="font-size:0.96rem;color:#1A1A1A;line-height:1.5;">Continuous and right-skewed, used to model waiting times and many heavy-tailed metrics</div>
  </div>

  <div style="display:grid;grid-template-columns:170px 1fr;gap:1rem;align-items:baseline;">
    <span style="font-family:'JetBrains Mono',monospace;font-size:0.82rem;color:#FF00FF;letter-spacing:0.12em;text-transform:uppercase;">Normal</span>
    <div style="font-size:0.96rem;color:#1A1A1A;line-height:1.5;">Continuous symmetric bell curve, the most important named distribution in statistics and the one the central limit theorem will produce in a moment</div>
  </div>

</div>

---

# Distributions have parameters

<p style="font-size:0.92rem;color:#1A1A1A;margin:0.2rem 0 0.3rem;line-height:1.5;">Each named distribution is pinned down by a small set of parameters. In probability theory we treat these parameters as known and reason about the data such a model would produce.</p>

<div style="display:grid;grid-template-columns:1.4fr 1fr;gap:1.2rem;align-items:center;margin-top:0.2rem;">

  <Chart src="/harbour-product-analytics-2026/05-statistics-1/charts/parameters-vary.html" height="230px" />

  <table style="border-collapse:collapse;font-size:0.88rem;color:#1A1A1A;">
    <thead>
      <tr style="background:#F5F5F5;">
        <th style="border:1px solid #1A1A1A;padding:0.3rem 0.7rem;text-align:left;font-weight:600;">Distribution</th>
        <th style="border:1px solid #1A1A1A;padding:0.3rem 0.7rem;text-align:left;font-weight:600;">Parameters</th>
      </tr>
    </thead>
    <tbody>
      <tr><td style="border:1px solid #1A1A1A;padding:0.28rem 0.7rem;">Bernoulli</td><td style="border:1px solid #1A1A1A;padding:0.28rem 0.7rem;font-family:'JetBrains Mono',monospace;">p</td></tr>
      <tr><td style="border:1px solid #1A1A1A;padding:0.28rem 0.7rem;">Uniform</td><td style="border:1px solid #1A1A1A;padding:0.28rem 0.7rem;font-family:'JetBrains Mono',monospace;">a, b</td></tr>
      <tr><td style="border:1px solid #1A1A1A;padding:0.28rem 0.7rem;">Exponential</td><td style="border:1px solid #1A1A1A;padding:0.28rem 0.7rem;font-family:'JetBrains Mono',monospace;">λ</td></tr>
      <tr><td style="border:1px solid #1A1A1A;padding:0.28rem 0.7rem;">Normal</td><td style="border:1px solid #1A1A1A;padding:0.28rem 0.7rem;font-family:'JetBrains Mono',monospace;">μ, σ</td></tr>
    </tbody>
  </table>

</div>

<p style="margin-top:0.3rem;font-size:0.88rem;color:#1A1A1A;line-height:1.5;">The chart shows two normal distributions with the same mean μ=0 and different standard deviations, and the parameter σ alone controls the spread of the curve.</p>

---

# Expectation

<p style="font-size:0.98rem;color:#1A1A1A;margin:0.3rem 0 0.4rem;line-height:1.55;">The expectation of a discrete random variable is the long-run average, computed by weighting each value by its probability.</p>

<div style="background:#FAFAFA;border-left:3px solid #FF00FF;padding:0.7rem 1.2rem;margin:0.3rem 0;font-size:0.98rem;color:#1A1A1A;line-height:2;">

$$E[X] = \sum_{x} x \cdot P(X = x)$$

$$E[X_{\text{die}}] = 1 \cdot \tfrac{1}{6} + 2 \cdot \tfrac{1}{6} + 3 \cdot \tfrac{1}{6} + 4 \cdot \tfrac{1}{6} + 5 \cdot \tfrac{1}{6} + 6 \cdot \tfrac{1}{6} = 3.5$$

$$E[X_{\text{conv}}] = 0 \cdot 0.70 + 1 \cdot 0.30 = 0.30$$

</div>

<p style="margin-top:0.4rem;font-size:0.95rem;color:#1A1A1A;line-height:1.5;">For a Bernoulli random variable the expectation is simply its parameter p, the true conversion rate.</p>

---

# Take it or roll again

<p style="font-size:1rem;color:#1A1A1A;margin:0.3rem 0 0.6rem;line-height:1.55;">You may roll a fair die at most twice. After the first roll you may either keep the number or roll again, and after the second roll you must take whatever came up. What strategy gives the largest expected number of points?</p>

<div v-click style="display:grid;grid-template-columns:1fr 1fr;gap:1.2rem;margin-top:0.6rem;">

  <div style="border-left:3px solid #FF00FF;padding:0.5rem 0 0.5rem 1rem;">
    <div style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#AAAAAA;letter-spacing:0.14em;text-transform:uppercase;margin-bottom:0.4rem;">Strategy</div>
    <div style="font-size:0.96rem;color:#1A1A1A;line-height:1.5;">Keep the first roll if it is at least 4, otherwise roll again. The threshold is the expectation of one roll, 3.5.</div>
  </div>

  <div style="border-left:3px solid #FF00FF;padding:0.5rem 0 0.5rem 1rem;">
    <div style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#AAAAAA;letter-spacing:0.14em;text-transform:uppercase;margin-bottom:0.4rem;">Expected value</div>
    <div style="font-size:0.96rem;color:#1A1A1A;line-height:1.5;">E[V] = (1/6) · (3.5 + 3.5 + 3.5 + 4 + 5 + 6) = 4.25</div>
  </div>

</div>

<p v-click style="margin-top:0.8rem;font-size:0.96rem;color:#1A1A1A;line-height:1.5;">The naive strategy of always keeping the first roll gives 3.5, so reasoning with expectation buys 0.75 points on average. The same logic appears in pricing, bidding and stopping problems.</p>

<!--
Show the question first. Wait for the room to propose. Reveal the answer on click.
-->

---

# Variance and standard deviation

<p style="font-size:0.98rem;color:#1A1A1A;margin:0.3rem 0 0.5rem;line-height:1.55;">Variance measures how far the values of a random variable typically sit from its mean. The standard deviation is its square root and brings the spread back into original units.</p>

<div style="background:#FAFAFA;border-left:3px solid #FF00FF;padding:0.8rem 1.3rem;margin:0.3rem 0;font-size:1.05rem;color:#1A1A1A;line-height:1.9;">

$$\mathrm{Var}(X) = E\!\left[(X - \mu)^2\right], \quad \mathrm{SD}(X) = \sqrt{\mathrm{Var}(X)}$$

</div>

<p style="font-size:0.95rem;color:#1A1A1A;line-height:1.5;">A narrow distribution has small variance because the values stay close to the mean, while a wide distribution has large variance because the values spread far from it.</p>

---

# From probability to statistics

<p style="font-size:1rem;color:#1A1A1A;margin:0.3rem 0 0.8rem;line-height:1.55;">Everything we covered so far lives in probability theory, where we assume the model and reason about the data it produces, and we are now ready to flip the arrow and ask the inverse question.</p>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:1.4rem;margin-top:0.4rem;">

  <div style="border-left:3px solid #FF00FF;padding:0.5rem 0 0.5rem 1rem;">
    <div style="font-family:'JetBrains Mono',monospace;font-size:0.72rem;color:#AAAAAA;letter-spacing:0.14em;text-transform:uppercase;margin-bottom:0.4rem;">Probability</div>
    <div style="font-size:0.98rem;color:#1A1A1A;line-height:1.5;">Model is given, we deduce what data looks like. General to specific.</div>
  </div>

  <div style="border-left:3px solid #FF00FF;padding:0.5rem 0 0.5rem 1rem;">
    <div style="font-family:'JetBrains Mono',monospace;font-size:0.72rem;color:#AAAAAA;letter-spacing:0.14em;text-transform:uppercase;margin-bottom:0.4rem;">Statistics</div>
    <div style="font-size:0.98rem;color:#1A1A1A;line-height:1.5;">Data is observed, we infer the model. Specific to general.</div>
  </div>

</div>

<p style="margin-top:0.7rem;font-size:0.94rem;color:#1A1A1A;line-height:1.5;">From this point on we treat the parameters of the underlying distribution as unknown, and one of the main tasks of statistics is to estimate those parameters from the observed sample as accurately as possible.</p>

---
layout: section
class: tint-cream
---

## 04

# Descriptive<br>statistics

---

# Five students

<div style="margin-top:2.4rem;">

<p style="font-size:1rem;color:#6B6B6B;margin:0 0 0.6rem;line-height:1.55;">We compute every descriptive statistic on the same small dataset, the height of five randomly selected students.</p>

<div style="display:flex;justify-content:center;align-items:flex-end;gap:1.4rem;margin:0.6rem 0;">

  <div style="text-align:center;">
    <div style="font-family:'JetBrains Mono',monospace;font-size:1rem;color:#1A1A1A;font-weight:600;">192</div>
    <div style="font-family:'JetBrains Mono',monospace;font-size:0.8rem;color:#6B6B6B;">cm</div>
    <div style="width:30px;height:1px;background:#1A1A1A;margin:0.5rem auto;"></div>
    <div style="font-family:'JetBrains Mono',monospace;font-size:0.85rem;color:#1A1A1A;">A</div>
  </div>

  <div style="text-align:center;">
    <div style="font-family:'JetBrains Mono',monospace;font-size:1rem;color:#1A1A1A;font-weight:600;">170</div>
    <div style="font-family:'JetBrains Mono',monospace;font-size:0.8rem;color:#6B6B6B;">cm</div>
    <div style="width:30px;height:1px;background:#1A1A1A;margin:0.5rem auto;"></div>
    <div style="font-family:'JetBrains Mono',monospace;font-size:0.85rem;color:#1A1A1A;">B</div>
  </div>

  <div style="text-align:center;">
    <div style="font-family:'JetBrains Mono',monospace;font-size:1rem;color:#1A1A1A;font-weight:600;">178</div>
    <div style="font-family:'JetBrains Mono',monospace;font-size:0.8rem;color:#6B6B6B;">cm</div>
    <div style="width:30px;height:1px;background:#1A1A1A;margin:0.5rem auto;"></div>
    <div style="font-family:'JetBrains Mono',monospace;font-size:0.85rem;color:#1A1A1A;">C</div>
  </div>

  <div style="text-align:center;">
    <div style="font-family:'JetBrains Mono',monospace;font-size:1rem;color:#1A1A1A;font-weight:600;">170</div>
    <div style="font-family:'JetBrains Mono',monospace;font-size:0.8rem;color:#6B6B6B;">cm</div>
    <div style="width:30px;height:1px;background:#1A1A1A;margin:0.5rem auto;"></div>
    <div style="font-family:'JetBrains Mono',monospace;font-size:0.85rem;color:#1A1A1A;">D</div>
  </div>

  <div style="text-align:center;">
    <div style="font-family:'JetBrains Mono',monospace;font-size:1rem;color:#1A1A1A;font-weight:600;">183</div>
    <div style="font-family:'JetBrains Mono',monospace;font-size:0.8rem;color:#6B6B6B;">cm</div>
    <div style="width:30px;height:1px;background:#1A1A1A;margin:0.5rem auto;"></div>
    <div style="font-family:'JetBrains Mono',monospace;font-size:0.85rem;color:#1A1A1A;">E</div>
  </div>

</div>

<p style="margin-top:0.4rem;font-size:0.92rem;color:#6B6B6B;line-height:1.5;text-align:center;">x₁ = 192, x₂ = 170, x₃ = 178, x₄ = 170, x₅ = 183, sample size n = 5</p>

</div>

---

# Mean

<p style="font-size:0.98rem;color:#1A1A1A;margin:0.3rem 0 0.5rem;line-height:1.55;">The sample mean is the arithmetic average of observed values and is the most common single-number summary of where the data sits.</p>

<div style="background:#FAFAFA;border-left:3px solid #FF00FF;padding:0.8rem 1.3rem;margin:0.3rem 0;font-size:1rem;color:#1A1A1A;line-height:1.9;">

$$\bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i = \frac{192 + 170 + 178 + 170 + 183}{5} = \frac{893}{5} = 178.6 \text{ cm}$$

</div>

<p style="margin-top:0.5rem;font-size:0.95rem;color:#1A1A1A;line-height:1.5;">The same formula computes the average revenue per user, the average session length, or the sample conversion rate.</p>

---

# Median and mode

<p style="font-size:0.98rem;color:#1A1A1A;margin:0.3rem 0 0.5rem;line-height:1.55;">The median is the middle value once data is sorted, and the mode is the value that appears most often.</p>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:1.4rem;margin-top:0.3rem;">

  <div style="border-left:3px solid #FF00FF;padding:0.5rem 0 0.5rem 1rem;">
    <div style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#AAAAAA;letter-spacing:0.14em;text-transform:uppercase;margin-bottom:0.4rem;">Median</div>
    <div style="font-size:0.95rem;color:#1A1A1A;line-height:1.5;">Sorted heights are <span style="font-family:'JetBrains Mono',monospace;">170, 170, 178, 183, 192</span>. The middle position is the third, so median = 178.</div>
  </div>

  <div style="border-left:3px solid #FF00FF;padding:0.5rem 0 0.5rem 1rem;">
    <div style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#AAAAAA;letter-spacing:0.14em;text-transform:uppercase;margin-bottom:0.4rem;">Mode</div>
    <div style="font-size:0.95rem;color:#1A1A1A;line-height:1.5;">170 appears twice and every other value appears once, so mode = 170.</div>
  </div>

</div>

<p style="margin-top:0.7rem;font-size:0.95rem;color:#1A1A1A;line-height:1.5;">The median is more robust to outliers than the mean, which is why a marketplace usually reports the median basket size rather than the mean.</p>

---

# Median versus mean with one outlier

<p style="font-size:0.98rem;color:#1A1A1A;margin:0.3rem 0 0.5rem;line-height:1.55;">Consider seven recent basket sizes from an online shop, with one unusually large purchase that pulls the mean far away from the typical value.</p>

<div style="background:#FAFAFA;border-left:3px solid #FF00FF;padding:0.7rem 1.2rem;margin:0.3rem 0;font-family:'JetBrains Mono',monospace;font-size:1rem;color:#1A1A1A;">
sorted baskets, EUR: &nbsp; 10, 12, 15, 18, 20, 22, 1000
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:1.4rem;margin-top:0.6rem;">

  <div style="border-left:3px solid #FF00FF;padding:0.5rem 0 0.5rem 1rem;">
    <div style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#AAAAAA;letter-spacing:0.14em;text-transform:uppercase;margin-bottom:0.4rem;">Mean</div>
    <div style="font-size:0.96rem;color:#1A1A1A;line-height:1.5;font-family:'JetBrains Mono',monospace;">(10+12+15+18+20+22+1000)/7 = 156.7 EUR</div>
  </div>

  <div style="border-left:3px solid #FF00FF;padding:0.5rem 0 0.5rem 1rem;">
    <div style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#AAAAAA;letter-spacing:0.14em;text-transform:uppercase;margin-bottom:0.4rem;">Median</div>
    <div style="font-size:0.96rem;color:#1A1A1A;line-height:1.5;font-family:'JetBrains Mono',monospace;">middle position is the fourth, median = 18 EUR</div>
  </div>

</div>

<p style="margin-top:0.7rem;font-size:0.95rem;color:#1A1A1A;line-height:1.5;">One outlier shifts the mean by almost a factor of ten while leaving the median untouched, and so the median describes the typical customer much better here.</p>

---

# Quantiles

<p style="font-size:0.94rem;color:#1A1A1A;margin:0.2rem 0 0.3rem;line-height:1.5;">A quantile is a value below which a given fraction of the distribution lies, and the median is the most familiar one.</p>

<div style="background:#FAFAFA;border-left:3px solid #FF00FF;padding:0.55rem 1.1rem;margin:0.3rem 0;font-size:0.96rem;color:#1A1A1A;">

$$P\!\left(X \le q_p\right) = p, \qquad 0 \le p \le 1$$

</div>

<table style="border-collapse:collapse;font-size:0.9rem;color:#1A1A1A;width:100%;margin-top:0.3rem;">
  <thead>
    <tr style="background:#F5F5F5;">
      <th style="border:1px solid #1A1A1A;padding:0.32rem 0.8rem;text-align:left;font-weight:600;">Name</th>
      <th style="border:1px solid #1A1A1A;padding:0.32rem 0.8rem;text-align:left;font-weight:600;">Fraction below</th>
      <th style="border:1px solid #1A1A1A;padding:0.32rem 0.8rem;text-align:left;font-weight:600;">Notation</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #1A1A1A;padding:0.3rem 0.8rem;">First quartile</td><td style="border:1px solid #1A1A1A;padding:0.3rem 0.8rem;font-family:'JetBrains Mono',monospace;">25%</td><td style="border:1px solid #1A1A1A;padding:0.3rem 0.8rem;font-family:'JetBrains Mono',monospace;">Q₁, q₀.₂₅</td></tr>
    <tr><td style="border:1px solid #1A1A1A;padding:0.3rem 0.8rem;">Median</td><td style="border:1px solid #1A1A1A;padding:0.3rem 0.8rem;font-family:'JetBrains Mono',monospace;">50%</td><td style="border:1px solid #1A1A1A;padding:0.3rem 0.8rem;font-family:'JetBrains Mono',monospace;">Q₂, q₀.₅</td></tr>
    <tr><td style="border:1px solid #1A1A1A;padding:0.3rem 0.8rem;">Third quartile</td><td style="border:1px solid #1A1A1A;padding:0.3rem 0.8rem;font-family:'JetBrains Mono',monospace;">75%</td><td style="border:1px solid #1A1A1A;padding:0.3rem 0.8rem;font-family:'JetBrains Mono',monospace;">Q₃, q₀.₇₅</td></tr>
    <tr><td style="border:1px solid #1A1A1A;padding:0.3rem 0.8rem;">95th percentile</td><td style="border:1px solid #1A1A1A;padding:0.3rem 0.8rem;font-family:'JetBrains Mono',monospace;">95%</td><td style="border:1px solid #1A1A1A;padding:0.3rem 0.8rem;font-family:'JetBrains Mono',monospace;">q₀.₉₅</td></tr>
  </tbody>
</table>

<p style="margin-top:0.5rem;font-size:0.9rem;color:#1A1A1A;line-height:1.45;">In product analytics the 95th percentile of session length or page-load time is reported more often than the mean, because tail behaviour is what users notice.</p>

---

# Skewness changes the picture

<p style="font-size:0.92rem;color:#1A1A1A;margin:0.2rem 0 0.3rem;line-height:1.5;">In a symmetric distribution the mean, median and mode coincide, while in a skewed distribution they separate and the mean is pulled toward the long tail.</p>

<Chart src="/harbour-product-analytics-2026/05-statistics-1/charts/skewness.html" height="230px" />

<p style="margin-top:0.3rem;font-size:0.88rem;color:#1A1A1A;line-height:1.5;text-align:center;">Solid black line marks the <strong>mean</strong>, dotted gray line marks the <strong>median</strong>, solid pink line marks the <strong>mode</strong></p>

---

# Sample variance

<p style="font-size:0.95rem;color:#1A1A1A;margin:0.2rem 0 0.4rem;line-height:1.5;">Sample variance measures how spread out the observed values are around the sample mean. We divide by n−1 for a technical reason we will not derive today.</p>

<div style="background:#FAFAFA;border-left:3px solid #FF00FF;padding:0.7rem 1.2rem;margin:0.3rem 0;font-size:0.95rem;color:#1A1A1A;line-height:1.95;">

$$s^2 = \frac{1}{n - 1} \sum_{i=1}^{n} (x_i - \bar{x})^2$$

$$s^2 = \tfrac{1}{4}\Big[(192-178.6)^2 + (170-178.6)^2 + (178-178.6)^2$$

$$\hphantom{s^2 = \tfrac{1}{4}\Big[\,} {} + (170-178.6)^2 + (183-178.6)^2 \Big]$$

$$s^2 = \tfrac{1}{4} \cdot 346.8 = 86.8 \text{ cm}^2, \quad s \approx 9.32 \text{ cm}$$

</div>

---
layout: section
class: tint-sky
---

## 05

# Law of large<br>numbers and CLT

---

# Resampling

<p style="font-size:0.96rem;color:#1A1A1A;margin:0.3rem 0 0.5rem;line-height:1.55;">If we pick another five random students from the same population we obtain different heights and a different sample mean.</p>

<table style="border-collapse:collapse;font-family:'JetBrains Mono',monospace;font-size:0.93rem;color:#1A1A1A;width:100%;margin-top:0.2rem;">
  <thead>
    <tr style="background:#F5F5F5;">
      <th style="border:1px solid #1A1A1A;padding:0.4rem 0.85rem;text-align:left;font-weight:600;">Sample</th>
      <th style="border:1px solid #1A1A1A;padding:0.4rem 0.85rem;text-align:left;font-weight:600;">Observed heights</th>
      <th style="border:1px solid #1A1A1A;padding:0.4rem 0.85rem;text-align:right;font-weight:600;">sample mean</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #1A1A1A;padding:0.4rem 0.85rem;">1</td><td style="border:1px solid #1A1A1A;padding:0.4rem 0.85rem;">192, 170, 178, 170, 183</td><td style="border:1px solid #1A1A1A;padding:0.4rem 0.85rem;text-align:right;">178.6</td></tr>
    <tr><td style="border:1px solid #1A1A1A;padding:0.4rem 0.85rem;">2</td><td style="border:1px solid #1A1A1A;padding:0.4rem 0.85rem;">165, 181, 174, 179, 172</td><td style="border:1px solid #1A1A1A;padding:0.4rem 0.85rem;text-align:right;">174.2</td></tr>
    <tr><td style="border:1px solid #1A1A1A;padding:0.4rem 0.85rem;">3</td><td style="border:1px solid #1A1A1A;padding:0.4rem 0.85rem;">188, 167, 175, 182, 169</td><td style="border:1px solid #1A1A1A;padding:0.4rem 0.85rem;text-align:right;">176.2</td></tr>
    <tr><td style="border:1px solid #1A1A1A;padding:0.4rem 0.85rem;">4</td><td style="border:1px solid #1A1A1A;padding:0.4rem 0.85rem;">171, 168, 184, 177, 180</td><td style="border:1px solid #1A1A1A;padding:0.4rem 0.85rem;text-align:right;">176.0</td></tr>
    <tr><td style="border:1px solid #1A1A1A;padding:0.4rem 0.85rem;">5</td><td style="border:1px solid #1A1A1A;padding:0.4rem 0.85rem;">177, 173, 190, 165, 179</td><td style="border:1px solid #1A1A1A;padding:0.4rem 0.85rem;text-align:right;">176.8</td></tr>
  </tbody>
</table>

<p style="margin-top:0.5rem;font-size:0.95rem;color:#1A1A1A;line-height:1.5;">Each repetition produces a different sample mean, and the collection of these sample means itself has a distribution.</p>

---
layout: statement
---

# The sample mean is itself<br>a <span class="pink">random variable</span>

---

# Law of large numbers

<p style="font-size:0.92rem;color:#1A1A1A;margin:0.2rem 0 0.3rem;line-height:1.5;">As we collect more observations the sample mean gets closer and closer to the true mean of the population.</p>

<Chart src="/harbour-product-analytics-2026/05-statistics-1/charts/lln.html" height="260px" />

<p style="margin-top:0.2rem;font-size:0.85rem;color:#6B6B6B;text-align:center;">Fair die with true mean 3.5, or conversion with true rate 0.30</p>

---

# Central limit theorem

<p style="font-size:0.92rem;color:#1A1A1A;margin:0.2rem 0 0.3rem;line-height:1.5;">When we draw many samples of size n and collect their means, that collection looks like a bell curve regardless of the shape of the source.</p>

<Chart src="/harbour-product-analytics-2026/05-statistics-1/charts/clt.html" height="260px" />

<p style="margin-top:0.2rem;font-size:0.85rem;color:#6B6B6B;text-align:center;">Switch source distribution and sample size n to watch the sampling distribution change</p>

---

# What CLT does not say

<div style="display:flex;flex-direction:column;gap:0.7rem;margin-top:0.4rem;">

  <div style="display:grid;grid-template-columns:36px 1fr;gap:1rem;align-items:baseline;border-bottom:1px solid #E0E0E0;padding-bottom:0.65rem;">
    <span style="font-family:'JetBrains Mono',monospace;font-size:1.05rem;color:#FF00FF;font-weight:700;">×</span>
    <div style="font-size:1rem;color:#1A1A1A;line-height:1.5;">It does not promise that the original data becomes normal. A skewed distribution stays skewed no matter how much data we collect.</div>
  </div>

  <div style="display:grid;grid-template-columns:36px 1fr;gap:1rem;align-items:baseline;border-bottom:1px solid #E0E0E0;padding-bottom:0.65rem;">
    <span style="font-family:'JetBrains Mono',monospace;font-size:1.05rem;color:#FF00FF;font-weight:700;">&check;</span>
    <div style="font-size:1rem;color:#1A1A1A;line-height:1.5;">It promises only that the distribution of the sample mean approaches a bell shape as the sample size grows large.</div>
  </div>

  <div style="display:grid;grid-template-columns:36px 1fr;gap:1rem;align-items:baseline;border-bottom:1px solid #E0E0E0;padding-bottom:0.65rem;">
    <span style="font-family:'JetBrains Mono',monospace;font-size:1.05rem;color:#FF00FF;font-weight:700;">×</span>
    <div style="font-size:1rem;color:#1A1A1A;line-height:1.5;">It does not apply when variance is infinite. Heavy-tailed metrics such as revenue may need extra care.</div>
  </div>

  <div style="display:grid;grid-template-columns:36px 1fr;gap:1rem;align-items:baseline;">
    <span style="font-family:'JetBrains Mono',monospace;font-size:1.05rem;color:#FF00FF;font-weight:700;">×</span>
    <div style="font-size:1rem;color:#1A1A1A;line-height:1.5;">It is an asymptotic statement. For very small samples it is an approximation that can be inaccurate.</div>
  </div>

</div>

---

# Real data as random

<p style="font-size:0.98rem;color:#1A1A1A;margin:0.3rem 0 0.6rem;line-height:1.55;">In product analytics most processes are not literally random, but as long as we do not know the outcome in advance we model them as the outcome of a random experiment, and the entire machinery of probability applies.</p>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:1.4rem;margin-top:0.4rem;">

  <div style="border-left:3px solid #FF00FF;padding:0.5rem 0 0.5rem 1rem;">
    <div style="font-family:'JetBrains Mono',monospace;font-size:0.72rem;color:#AAAAAA;letter-spacing:0.14em;text-transform:uppercase;margin-bottom:0.4rem;">Sample</div>
    <div style="font-size:0.96rem;color:#1A1A1A;line-height:1.5;">Our observed values are treated as one realisation x₁, …, xₙ of a random sample X₁, …, Xₙ drawn from the population.</div>
  </div>

  <div style="border-left:3px solid #FF00FF;padding:0.5rem 0 0.5rem 1rem;">
    <div style="font-family:'JetBrains Mono',monospace;font-size:0.72rem;color:#AAAAAA;letter-spacing:0.14em;text-transform:uppercase;margin-bottom:0.4rem;">Estimator</div>
    <div style="font-size:0.96rem;color:#1A1A1A;line-height:1.5;">Any function of the sample is itself a random variable, and a statistic computed to estimate a population parameter is called an estimator.</div>
  </div>

</div>

<p style="margin-top:0.7rem;font-size:0.95rem;color:#1A1A1A;line-height:1.5;">The sample mean is the simplest estimator and the one we control through sample size, and Stats 2 will build hypothesis tests directly on top of these objects.</p>

---
layout: section
class: tint-lavender
---

## 06

# Putting it<br>together

---
layout: statement
---

# Statistics reuses the<br>results of probability<br>as <span class="pink">tools</span> for inference

---

# How we put it all together

<div style="display:flex;flex-direction:column;gap:0.6rem;margin-top:0.4rem;">

  <div style="display:grid;grid-template-columns:200px 1fr;gap:1rem;align-items:baseline;border-bottom:1px solid #E0E0E0;padding-bottom:0.5rem;">
    <span style="font-family:'JetBrains Mono',monospace;font-size:0.8rem;color:#FF00FF;letter-spacing:0.14em;text-transform:uppercase;">Sample mean</span>
    <div style="font-size:0.94rem;color:#1A1A1A;line-height:1.45;">Estimator of the unknown population mean and itself a random variable controlled through sample size.</div>
  </div>

  <div style="display:grid;grid-template-columns:200px 1fr;gap:1rem;align-items:baseline;border-bottom:1px solid #E0E0E0;padding-bottom:0.5rem;">
    <span style="font-family:'JetBrains Mono',monospace;font-size:0.8rem;color:#FF00FF;letter-spacing:0.14em;text-transform:uppercase;">Law of large numbers</span>
    <div style="font-size:0.94rem;color:#1A1A1A;line-height:1.45;">With enough data the sample mean lies close to the population mean, so a decent sample size gives a trustworthy estimate.</div>
  </div>

  <div style="display:grid;grid-template-columns:200px 1fr;gap:1rem;align-items:baseline;">
    <span style="font-family:'JetBrains Mono',monospace;font-size:0.8rem;color:#FF00FF;letter-spacing:0.14em;text-transform:uppercase;">Central limit theorem</span>
    <div style="font-size:0.94rem;color:#1A1A1A;line-height:1.45;">Distribution of the sample mean is approximately normal, and this is the shape every hypothesis test in Stats 2 builds on.</div>
  </div>

</div>

---

# Materials

<div style="display:grid;grid-template-columns:1fr 1fr;gap:1.8rem;margin-top:0.6rem;">

  <div>
    <div style="font-family:'JetBrains Mono',monospace;font-size:0.72rem;color:#FF00FF;letter-spacing:0.14em;text-transform:uppercase;margin-bottom:0.6rem;">Required</div>
    <ul style="font-size:0.95rem;line-height:1.7;color:#1A1A1A;margin:0;padding-left:1.2rem;">
      <li><a href="https://www.3blue1brown.com/lessons/clt" style="color:#1A1A1A;">3Blue1Brown &middot; Central limit theorem</a></li>
      <li><a href="https://statisticsbyjim.com/basics/central-limit-theorem/" style="color:#1A1A1A;">Statistics By Jim &middot; CLT explained</a></li>
      <li><a href="https://seeing-theory.brown.edu/" style="color:#1A1A1A;">Seeing Theory &middot; interactive intuition</a></li>
    </ul>
  </div>

  <div>
    <div style="font-family:'JetBrains Mono',monospace;font-size:0.72rem;color:#FF00FF;letter-spacing:0.14em;text-transform:uppercase;margin-bottom:0.6rem;">For depth</div>
    <ul style="font-size:0.95rem;line-height:1.7;color:#1A1A1A;margin:0;padding-left:1.2rem;">
      <li><a href="https://gopractice.io/data/the-product-managers-guide-to-statistical-analysis/" style="color:#1A1A1A;">GoPractice &middot; PM guide to statistics</a></li>
    </ul>
  </div>

</div>
