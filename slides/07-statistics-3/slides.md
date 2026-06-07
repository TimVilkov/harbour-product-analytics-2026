---
theme: apple-basic
title: "Session 07: Statistics 3"
info: "Product Analytics · Harbour.Space · 2026"
highlighter: shiki
drawings:
  persist: false
transition: fade
mdc: true
layout: intro
---

# Statistics <span class="pink">3</span>

<div class="absolute bottom-10 left-14" style="font-family:'JetBrains Mono',monospace;font-size:0.75rem;text-transform:uppercase;letter-spacing:0.15em;color:rgba(255,255,255,0.55);">
  Harbour.Space &middot; Barcelona &middot; May 27, 2026
</div>

---

# Today

<div style="display:flex;flex-direction:column;gap:0.9rem;margin-top:1rem;">
  <div style="display:grid;grid-template-columns:60px 1fr;gap:1.5rem;align-items:baseline;">
    <span style="font-family:'JetBrains Mono',monospace;font-size:0.9rem;color:#FF00FF;letter-spacing:0.1em;">01</span>
    <div style="font-size:1.4rem;font-weight:700;color:#1A1A1A;">Hypothesis testing framework</div>
  </div>
  <div style="display:grid;grid-template-columns:60px 1fr;gap:1.5rem;align-items:baseline;">
    <span style="font-family:'JetBrains Mono',monospace;font-size:0.9rem;color:#FF00FF;letter-spacing:0.1em;">02</span>
    <div style="font-size:1.4rem;font-weight:700;color:#1A1A1A;">Controlling Type I error</div>
  </div>
  <div style="display:grid;grid-template-columns:60px 1fr;gap:1.5rem;align-items:baseline;">
    <span style="font-family:'JetBrains Mono',monospace;font-size:0.9rem;color:#FF00FF;letter-spacing:0.1em;">03</span>
    <div style="font-size:1.4rem;font-weight:700;color:#1A1A1A;">Pipeline, two samples, assumptions</div>
  </div>
  <div style="display:grid;grid-template-columns:60px 1fr;gap:1.5rem;align-items:baseline;">
    <span style="font-family:'JetBrains Mono',monospace;font-size:0.9rem;color:#FF00FF;letter-spacing:0.1em;">04</span>
    <div style="font-size:1.4rem;font-weight:700;color:#1A1A1A;">Power, effect size, MDE</div>
  </div>
  <div style="display:grid;grid-template-columns:60px 1fr;gap:1.5rem;align-items:baseline;">
    <span style="font-family:'JetBrains Mono',monospace;font-size:0.9rem;color:#FF00FF;letter-spacing:0.1em;">05</span>
    <div style="font-size:1.4rem;font-weight:700;color:#1A1A1A;">CI duality and replication</div>
  </div>
</div>

---
layout: section
class: tint-lavender
---

## 01

# Hypothesis testing framework

---

# The null hypothesis

A **null hypothesis** $H_0$ is a statement that assumes no effect, no difference, no relationship. It is the baseline default position we test against the research claim $H_1$.

| Setting | $H_0$ |
|---|---|
| Lady Tasting Tea | She is guessing at random, equivalent to $X \sim \text{Hypergeometric}(8, 4, 4)$ |
| Barcelona apartment prices | $\text{median}(F) = 250{,}000$ |
| A/B test on revenue | $\mathbb{E}[\text{revenue}_A] = \mathbb{E}[\text{revenue}_B]$ |

A clean parameter-level $H_0$ pins down a specific distribution for the test statistic, the way "she is guessing" pinned down the hypergeometric.

<!--
The null is always the "boring" version of the world. We frame it that way because we never get to prove anything in NHST. We only collect evidence against the null and either reject it or fail to. The parameter-level form is what gives us a single null distribution to compute tail probabilities from.
-->

---

# Null Hypothesis Significance Testing

The modern framework is called **NHST**, and it runs in one direction only. We collect evidence <span class="pink">against</span> $H_0$ and decide whether the data are unlikely enough under $H_0$ to reject it.

<div style="display:grid;grid-template-columns:1fr 1fr;gap:1.4rem;margin-top:0.8rem;">

<div style="padding:0.8rem 1.1rem;background:#FAFAFA;border-left:3px solid #1A1A1A;">
<div style="font-family:'JetBrains Mono',monospace;font-size:0.76rem;color:#1A1A1A;text-transform:uppercase;letter-spacing:0.1em;">what we can do</div>

Reject $H_0$ when the data is unlikely under it, or fail to reject when it is not.

</div>

<div style="padding:0.8rem 1.1rem;background:#FAFAFA;border-left:3px solid #FF00FF;">
<div style="font-family:'JetBrains Mono',monospace;font-size:0.76rem;color:#FF00FF;text-transform:uppercase;letter-spacing:0.1em;">what we cannot do</div>

Prove $H_0$. Pin down a specific value of $H_1$, because $H_1$ is composite.

</div>

</div>

<div style="margin-top:1.2rem;text-align:center;color:#E5142B;font-family:'Bricolage Grotesque','Inter',sans-serif;font-weight:800;font-size:1.5rem;line-height:1.25;letter-spacing:-0.01em;">

Absence of evidence against $H_0$ is not evidence for it.

</div>

<!--
We never prove the null. The procedure is asymmetric by design. We control the false-positive rate, nothing more. To estimate the actual parameter, we go back to point and interval estimates from Statistics 2.
-->

---

# Type I and Type II errors

Two ways the test can be wrong, two ways it can be right.

<div style="display:grid;grid-template-columns:220px 240px 240px;gap:0.6rem;margin:0.6rem auto 0;width:fit-content;justify-content:center;font-family:'Inter',system-ui,sans-serif;">

<div></div>
<div style="text-align:center;font-family:'JetBrains Mono',monospace;font-size:0.78rem;color:#6B6B6B;text-transform:uppercase;letter-spacing:0.1em;padding:0.4rem;">H<sub>0</sub> true</div>
<div style="text-align:center;font-family:'JetBrains Mono',monospace;font-size:0.78rem;color:#6B6B6B;text-transform:uppercase;letter-spacing:0.1em;padding:0.4rem;">H<sub>1</sub> true</div>

<div style="font-family:'JetBrains Mono',monospace;font-size:0.78rem;color:#6B6B6B;text-transform:uppercase;letter-spacing:0.1em;padding:0.8rem 0.6rem;text-align:right;">Reject H<sub>0</sub></div>
<div style="padding:0.9rem;background:#FFF0F0;border-left:3px solid #E5142B;">
<div style="font-weight:700;color:#E5142B;font-size:0.95rem;">Type I error</div>
<div style="color:#6B6B6B;font-size:0.85rem;margin-top:0.2rem;">false positive · rate α</div>
</div>
<div style="padding:0.9rem;background:#F0FAF3;border-left:3px solid #1A8F4F;">
<div style="font-weight:700;color:#1A8F4F;font-size:0.95rem;">Correct</div>
<div style="color:#6B6B6B;font-size:0.85rem;margin-top:0.2rem;">true positive · power 1 − β</div>
</div>

<div style="font-family:'JetBrains Mono',monospace;font-size:0.78rem;color:#6B6B6B;text-transform:uppercase;letter-spacing:0.1em;padding:0.8rem 0.6rem;text-align:right;">Fail to reject H<sub>0</sub></div>
<div style="padding:0.9rem;background:#F0FAF3;border-left:3px solid #1A8F4F;">
<div style="font-weight:700;color:#1A8F4F;font-size:0.95rem;">Correct</div>
<div style="color:#6B6B6B;font-size:0.85rem;margin-top:0.2rem;">true negative · rate 1 − α</div>
</div>
<div style="padding:0.9rem;background:#FFF0F0;border-left:3px solid #E5142B;">
<div style="font-weight:700;color:#E5142B;font-size:0.95rem;">Type II error</div>
<div style="color:#6B6B6B;font-size:0.85rem;margin-top:0.2rem;">false negative · rate β</div>
</div>

</div>

<div v-click style="margin-top:1.2rem;text-align:center;color:#E5142B;font-family:'Bricolage Grotesque','Inter',sans-serif;font-weight:800;font-size:1.4rem;line-height:1.25;letter-spacing:-0.01em;">Errors are unavoidable. We build a procedure that <span style="color:#E5142B;">controls their rates</span>.</div>

<!--
Vocabulary lock-in: "fail to reject", never "accept". Type I first: this is what α controls. Type II comes later once we introduce power.
-->

---
layout: section
class: tint-rose
---

## 02

# Controlling Type I error

---

# Choosing $\alpha$

Under $H_0$ there is no effect. A Type I error is when the procedure rejects $H_0$ anyway, purely by chance. We pick the rate $\alpha$ at which we agree to let this happen, **before** running the test.

| | |
|---|---|
| <span class="pink">**$\alpha = 5\%$**</span> | baseline default in most product and academic settings |
| <span class="pink">**$\alpha = 1\%$**</span> | large companies with high cost of false positives |
| <span class="pink">**$\alpha = 0.1\%$**</span> | very large datasets, many parallel tests, stricter screening |

$\alpha$ is the rate of false positives the procedure is allowed to make when $H_0$ is true.

<!--
α is a commitment, not a number you look up after the fact. Common defaults: 5% in most A/B work, 1% in high-stakes decisions, 0.1% when running thousands of tests in parallel. Engineering the rest of the test happens around this number.
-->

---

# Rejection region and p-value

By design, we reject $H_0$ only when the test statistic $T(X)$ lands in a region whose probability under $H_0$ is exactly $\alpha$.

<div style="display:grid;grid-template-columns:1fr 1fr;gap:1.2rem;margin-top:0.8rem;align-items:start;">

<div style="padding:0.9rem 1.1rem;background:#FAFAFA;border-left:3px solid #1A1A1A;">
<div style="font-family:'JetBrains Mono',monospace;font-size:0.76rem;color:#1A1A1A;text-transform:uppercase;letter-spacing:0.1em;margin-bottom:0.3rem;">rejection region</div>

$$C_\alpha:\ \mathbb{P}_{H_0}\!\left(T(X) \in C_\alpha\right) = \alpha$$

The set of test-statistic values that triggers rejection. Built before seeing the data.

</div>

<div style="padding:0.9rem 1.1rem;background:#FAFAFA;border-left:3px solid #FF00FF;">
<div style="font-family:'JetBrains Mono',monospace;font-size:0.76rem;color:#FF00FF;text-transform:uppercase;letter-spacing:0.1em;margin-bottom:0.3rem;">p-value</div>

$$p = \mathbb{P}_{H_0}\!\left(T(X) \text{ as or more extreme than } t_\text{obs}\right)$$

The probability under $H_0$ of seeing a result at least as extreme as what we observed.

</div>

</div>

<div style="margin-top:1rem;text-align:center;font-family:'Bricolage Grotesque','Inter',sans-serif;font-weight:800;font-size:1.4rem;color:#1A1A1A;">

Decision rule: reject $H_0$ if $p \lt \alpha$

</div>

<!--
Two equivalent formulations of the same decision. Rejection region: decide before looking at the data which T values count as too extreme. p-value: ask how often H₀ would produce something at least this extreme. The two are linked: t_obs is in C_α exactly when p is below α.
-->

---

# Alternative hypothesis: three forms

The shape of the rejection region depends on $H_1$.

<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:1rem;margin-top:0.9rem;">

<div style="padding:0.9rem 1rem;background:#FAFAFA;border-left:3px solid #1A1A1A;">
<div style="font-family:'JetBrains Mono',monospace;font-size:0.72rem;color:#1A1A1A;text-transform:uppercase;letter-spacing:0.1em;margin-bottom:0.4rem;">left-tailed</div>

$H_1: \mu \lt \mu_0$

reject if $Z \lt -z_{1-\alpha}$

</div>

<div style="padding:0.9rem 1rem;background:#FAFAFA;border-left:3px solid #1A1A1A;">
<div style="font-family:'JetBrains Mono',monospace;font-size:0.72rem;color:#1A1A1A;text-transform:uppercase;letter-spacing:0.1em;margin-bottom:0.4rem;">right-tailed</div>

$H_1: \mu \gt \mu_0$

reject if $Z \gt z_{1-\alpha}$

</div>

<div style="padding:0.9rem 1rem;background:#FAFAFA;border-left:3px solid #FF00FF;">
<div style="font-family:'JetBrains Mono',monospace;font-size:0.72rem;color:#FF00FF;text-transform:uppercase;letter-spacing:0.1em;margin-bottom:0.4rem;">two-sided</div>

$H_1: \mu \ne \mu_0$

reject if $\lvert Z \rvert \gt z_{1-\alpha/2}$

</div>

</div>

Same total $\alpha$ budget, different placement on the number line.

<!--
The choice is about where α lives on the number line, not about how much α we spend. Same budget, redistributed. Next slide visualizes the three rejection regions on the standard Normal.
-->

---

# Rejection region: three pictures

<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:0.6rem;margin-top:0.4rem;">

<div style="text-align:center;">
<div style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#6B6B6B;text-transform:uppercase;letter-spacing:0.1em;margin-bottom:0.3rem;">left-tailed</div>
<svg viewBox="0 0 240 130" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;font-family:'Inter',system-ui,sans-serif;">
<polygon points="10,110 10,109.83 17.85,109.59 25.71,109.11 33.57,108.18 41.43,106.49 49.29,103.65 57.14,99.21 65.0,92.74 68.14,89.28 68.14,110" fill="#E5142B" fill-opacity="0.35"/>
<path d="M 10,109.83 Q 21.78,109.41 25.71,109.11 T 33.57,108.18 T 41.43,106.49 T 49.29,103.65 T 57.14,99.21 T 65.0,92.74 T 72.86,84.10 T 80.71,73.47 T 88.57,61.62 T 96.43,49.78 T 104.29,39.58 T 112.14,32.66 T 120,30.21 T 127.86,32.66 T 135.71,39.58 T 143.57,49.78 T 151.43,61.62 T 159.29,73.47 T 167.14,84.10 T 175.0,92.74 T 182.86,99.21 T 190.71,103.65 T 198.57,106.49 T 206.43,108.18 T 214.29,109.11 T 222.14,109.59 T 230,109.83" fill="none" stroke="#1A1A1A" stroke-width="1.4"/>
<line x1="10" y1="110" x2="230" y2="110" stroke="#1A1A1A" stroke-width="1"/>
<line x1="68.14" y1="110" x2="68.14" y2="25" stroke="#E5142B" stroke-width="1.1" stroke-dasharray="3 3"/>
<text x="68.14" y="124" style="font-size:9px;fill:#E5142B;text-anchor:middle;font-weight:700;">−z<tspan baseline-shift="sub" font-size="7px">1−α</tspan></text>
<text x="40" y="103" style="font-size:10px;fill:#E5142B;text-anchor:middle;font-weight:700;">α</text>
</svg>
<div style="font-size:0.8rem;color:#1A1A1A;margin-top:0.2rem;">reject Z &lt; −z<sub>1−α</sub></div>
</div>

<div style="text-align:center;">
<div style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#6B6B6B;text-transform:uppercase;letter-spacing:0.1em;margin-bottom:0.3rem;">right-tailed</div>
<svg viewBox="0 0 240 130" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;font-family:'Inter',system-ui,sans-serif;">
<polygon points="171.86,110 171.86,89.28 175.0,92.74 182.86,99.21 190.71,103.65 198.57,106.49 206.43,108.18 214.29,109.11 222.14,109.59 230,109.83 230,110" fill="#E5142B" fill-opacity="0.35"/>
<path d="M 10,109.83 Q 21.78,109.41 25.71,109.11 T 33.57,108.18 T 41.43,106.49 T 49.29,103.65 T 57.14,99.21 T 65.0,92.74 T 72.86,84.10 T 80.71,73.47 T 88.57,61.62 T 96.43,49.78 T 104.29,39.58 T 112.14,32.66 T 120,30.21 T 127.86,32.66 T 135.71,39.58 T 143.57,49.78 T 151.43,61.62 T 159.29,73.47 T 167.14,84.10 T 175.0,92.74 T 182.86,99.21 T 190.71,103.65 T 198.57,106.49 T 206.43,108.18 T 214.29,109.11 T 222.14,109.59 T 230,109.83" fill="none" stroke="#1A1A1A" stroke-width="1.4"/>
<line x1="10" y1="110" x2="230" y2="110" stroke="#1A1A1A" stroke-width="1"/>
<line x1="171.86" y1="110" x2="171.86" y2="25" stroke="#E5142B" stroke-width="1.1" stroke-dasharray="3 3"/>
<text x="171.86" y="124" style="font-size:9px;fill:#E5142B;text-anchor:middle;font-weight:700;">z<tspan baseline-shift="sub" font-size="7px">1−α</tspan></text>
<text x="200" y="103" style="font-size:10px;fill:#E5142B;text-anchor:middle;font-weight:700;">α</text>
</svg>
<div style="font-size:0.8rem;color:#1A1A1A;margin-top:0.2rem;">reject Z &gt; z<sub>1−α</sub></div>
</div>

<div style="text-align:center;">
<div style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#FF00FF;text-transform:uppercase;letter-spacing:0.1em;margin-bottom:0.3rem;">two-sided</div>
<svg viewBox="0 0 240 130" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;font-family:'Inter',system-ui,sans-serif;">
<polygon points="10,110 10,109.83 17.85,109.59 25.71,109.11 33.57,108.18 41.43,106.49 49.29,103.65 57.14,99.21 58.4,98.31 58.4,110" fill="#E5142B" fill-opacity="0.35"/>
<polygon points="181.6,110 181.6,98.31 182.86,99.21 190.71,103.65 198.57,106.49 206.43,108.18 214.29,109.11 222.14,109.59 230,109.83 230,110" fill="#E5142B" fill-opacity="0.35"/>
<path d="M 10,109.83 Q 21.78,109.41 25.71,109.11 T 33.57,108.18 T 41.43,106.49 T 49.29,103.65 T 57.14,99.21 T 65.0,92.74 T 72.86,84.10 T 80.71,73.47 T 88.57,61.62 T 96.43,49.78 T 104.29,39.58 T 112.14,32.66 T 120,30.21 T 127.86,32.66 T 135.71,39.58 T 143.57,49.78 T 151.43,61.62 T 159.29,73.47 T 167.14,84.10 T 175.0,92.74 T 182.86,99.21 T 190.71,103.65 T 198.57,106.49 T 206.43,108.18 T 214.29,109.11 T 222.14,109.59 T 230,109.83" fill="none" stroke="#1A1A1A" stroke-width="1.4"/>
<line x1="10" y1="110" x2="230" y2="110" stroke="#1A1A1A" stroke-width="1"/>
<line x1="58.4" y1="110" x2="58.4" y2="25" stroke="#E5142B" stroke-width="1.1" stroke-dasharray="3 3"/>
<line x1="181.6" y1="110" x2="181.6" y2="25" stroke="#E5142B" stroke-width="1.1" stroke-dasharray="3 3"/>
<text x="58.4" y="124" style="font-size:8px;fill:#E5142B;text-anchor:middle;font-weight:700;">−z<tspan baseline-shift="sub" font-size="6px">1−α/2</tspan></text>
<text x="181.6" y="124" style="font-size:8px;fill:#E5142B;text-anchor:middle;font-weight:700;">z<tspan baseline-shift="sub" font-size="6px">1−α/2</tspan></text>
<text x="32" y="103" style="font-size:9px;fill:#E5142B;text-anchor:middle;font-weight:700;">α/2</text>
<text x="208" y="103" style="font-size:9px;fill:#E5142B;text-anchor:middle;font-weight:700;">α/2</text>
</svg>
<div style="font-size:0.8rem;color:#1A1A1A;margin-top:0.2rem;">reject |Z| &gt; z<sub>1−α/2</sub></div>
</div>

</div>

<div style="margin-top:0.9rem;padding:0.75rem 1rem;background:#FAFAFA;border-left:3px solid #1A1A1A;font-size:0.92rem;line-height:1.55;">

**At $\alpha = 0.05$:** two-sided splits to $\pm z_{0.975} = \pm 1.96$. One-sided puts all $\alpha$ in one tail at $z_{0.95} \approx 1.65$. Same $\alpha$ budget, smaller critical value, smaller detectable deviation in that direction.

</div>

<!--
The asymmetry is visible: one-sided gives a single fat tail at 1.65, two-sided splits into two thinner tails at ±1.96. Same α, different geometry, different sensitivity.
-->

---

# In practice: default to two-sided

By putting all of $\alpha$ on one side, a one-sided test commits to caring only about deviations in that direction. If the true effect lands on the other side, the test has no ability to detect it.

<div style="margin-top:1rem;padding:0.9rem 1.1rem;background:#FAFAFA;border-left:3px solid #FF00FF;font-size:0.98rem;color:#1A1A1A;line-height:1.55;">

**Two-sided is the industry default** when the direction of the change is not known with certainty before the test.

</div>

Most A/B tests fall here. A UX change can move the metric either way and we want to detect both. One-sided is reserved for cases with a strong prior reason that only one direction matters.

<!--
The cost of one-sided is asymmetric coverage. The cost of two-sided is a slightly larger critical value. In product work the asymmetric coverage is the more dangerous failure mode. You can ship a change that hurts the metric because the test was blind to that direction.
-->

---

# CI and HT are the same decision

A third equivalent form of the decision rule, using the confidence intervals from Statistics 2.

| Form | Decision |
|---|---|
| Rejection region | $t_\text{obs} \in C_\alpha$ |
| p-value | $p \lt \alpha$ |
| CI of $\mu_A - \mu_B$ | the $(1-\alpha)$ CI excludes 0 |

<div style="margin-top:0.8rem;padding:0.85rem 1.1rem;background:#FAFAFA;border-left:3px solid #FF00FF;font-size:0.95rem;line-height:1.55;">

The $(1-\alpha)$ CI for $\mu_A - \mu_B$ contains 0 if and only if the two-sided test of $H_0: \mu_A = \mu_B$ at level $\alpha$ fails to reject.

</div>

Most A/B platforms display the CI of the difference, not p-values.

<!--
This is the bridge from Stats 2 to industry tooling. When you open Eppo, Statsig, or Spotify Confidence, the headline number is the CI of the diff. The fact that 0 is in the CI also gives you the range of plausible effects, which we'll use against misconception #4 later.
-->

---

# Simulating Type I error

One-sample test of $H_0: p = 0.5$ on Bernoulli data, with $H_0$ true by construction. Every rejection is a false positive, and the empirical rate converges to $\alpha$.

<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:0.8rem;margin-top:0.8rem;">

<div style="padding:0.7rem 0.9rem;background:#FAFAFA;border-left:3px solid #1A1A1A;">
<div style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#1A1A1A;text-transform:uppercase;letter-spacing:0.1em;margin-bottom:0.25rem;">data</div>

$X_i \sim \text{Bernoulli}(0.5)$

</div>

<div style="padding:0.7rem 0.9rem;background:#FAFAFA;border-left:3px solid #1A1A1A;">
<div style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#1A1A1A;text-transform:uppercase;letter-spacing:0.1em;margin-bottom:0.25rem;">statistic</div>

$Z = \dfrac{\bar X - 0.5}{0.5/\sqrt{n}} \approx \mathcal{N}(0,1)$

</div>

<div style="padding:0.7rem 0.9rem;background:#FFF0F0;border-left:3px solid #E5142B;">
<div style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#E5142B;text-transform:uppercase;letter-spacing:0.1em;margin-bottom:0.25rem;">decision</div>

reject $H_0$ if $Z \in C_\alpha$

</div>

</div>

<div style="display:flex;justify-content:center;margin-top:1.2rem;">
<a href="/harbour-product-analytics-2026/07-statistics-3/type1-sim.html" target="_blank" rel="noopener" style="display:inline-block;padding:0.8rem 1.4rem;background:#1A1A1A;color:#fff;font-family:'JetBrains Mono',monospace;font-size:0.95rem;font-weight:700;letter-spacing:0.08em;text-transform:uppercase;text-decoration:none;border:2px solid #1A1A1A;">Open simulation ↗</a>
</div>

<!--
Run α = 5%, two-sided, draw 5000: roughly 5% of samples land in the rejection region. Switch to α = 1%: it drops to 1%. Empirical rate is α by construction. Then flip the alternative direction. The rejection region is our design choice, not a property of the data.
-->

---
layout: section
class: tint-mint
---

## 03

# Pipeline, two samples, assumptions

---

# The hypothesis testing pipeline

| | |
|---|---|
| <span class="pink">**01**</span> | State $H_0: \mu = \mu_0$ and collect $X_1, \dots, X_n$ |
| <span class="pink">**02**</span> | Derive the null distribution. CLT gives $Z = \sqrt{n}\,(\bar X - \mu_0)/\sigma \approx \mathcal{N}(0, 1)$ under $H_0$ |
| <span class="pink">**03**</span> | Fix $\alpha$ **before** running the test ($5\%$, $1\%$, $0.1\%$) |
| <span class="pink">**04**</span> | Compute the p-value: $p = \mathbb{P}_{H_0}(\lvert Z \rvert \ge \lvert z_\text{obs} \rvert)$ |
| <span class="pink">**05**</span> | If $p \lt \alpha$, reject $H_0$. Otherwise fail to reject |

CLT covers means only. Other statistics need their own null distribution.

<!--
Five steps, in order. Step 2 is the engineering challenge. Under H₀ we need to know the distribution of our statistic. For sample means we get this for free from CLT. The moment we leave means (median, quantile, ratio) we have to roll our own. Rejecting H₀ does not tell us by how much the truth differs from μ₀. For magnitude we go back to point and interval estimates.
-->

---

# Two samples

Recipe unchanged. Reduce both samples to a single statistic whose null distribution we know. Difference of two independent Normals is Normal, so under $H_0: \mu_A = \mu_B$:

$$Z = \frac{\bar X_A - \bar X_B}{\mathrm{SE}} \approx \mathcal{N}(0, 1), \qquad \mathrm{SE} = \sqrt{\tfrac{\sigma_A^2}{n_A} + \tfrac{\sigma_B^2}{n_B}}$$

Same five steps, same $\alpha$, same p-value. Only the statistic and its standard error change.

<div style="margin-top:0.8rem;padding:0.85rem 1.1rem;background:#FAFAFA;border-left:3px solid #1A1A1A;font-size:0.95rem;line-height:1.55;">

The SE under the square root follows from **independence** of the A and B samples:
$\mathrm{Var}(\bar X_A - \bar X_B) = \mathrm{Var}(\bar X_A) + \mathrm{Var}(\bar X_B)$.

</div>

<!--
The two-sample test is the workhorse of A/B testing. Everything we built today plugs in unchanged. The only new piece is the SE formula, which follows from independence. Recall the variance of a difference from Stats 1.
-->

---

# Two-sample pipeline worked example

| | step | example |
|---|---|---|
| <span class="pink">**01**</span> | State $H_0: \mu_A = \mu_B$, collect A, B | $\bar X_A = 1.05$, $\bar X_B = 1.00$, $n = 1000$, $\sigma = 0.5$ |
| <span class="pink">**02**</span> | $Z = (\bar X_A - \bar X_B)/\mathrm{SE} \approx \mathcal{N}(0,1)$ | $\mathrm{SE} = \sqrt{2 \cdot 0.25/1000} \approx 0.0224$ |
| <span class="pink">**03**</span> | Fix $\alpha$ before computing | $\alpha = 0.05$ |
| <span class="pink">**04**</span> | $p = \mathbb{P}_{H_0}(\lvert Z \rvert \ge \lvert z_\text{obs} \rvert)$ | $z_\text{obs} \approx 2.24$, $p \approx 0.025$ |
| <span class="pink">**05**</span> | Reject $H_0$ if $p \lt \alpha$ | $0.025 \lt 0.05 \Rightarrow$ **reject** |

<!--
Walk this on the board with the class. Same five steps from earlier, instantiated with concrete numbers. The decision flips with a different α: at α = 0.01 we would fail to reject. Same data, different commitment.
-->

---

# In Python: `scipy.stats.ttest_ind`

We built the **asymptotic Z-test** via CLT. SciPy ships `ttest_ind`, not `ztest`. At industry $n$ the t-distribution converges to $\mathcal{N}(0, 1)$, so both make the same decision.

```python
from scipy.stats import ttest_ind

# A, B: arrays of per-user metric values
t, p = ttest_ind(A, B, equal_var=False)  # Welch t-test, default recommended

if p < 0.05:
    print("Reject H_0")
```

`equal_var=False` (Welch) does not assume equal variances. Set `equal_var=True` only when variances are genuinely matched, otherwise leave it off.

<!--
We never derived the t-test or its small-sample distribution; we used Z via CLT throughout. At our n the t and Z decisions agree. In production code we pull α from config and log both t and p for the experiment log.
-->

---

# When assumptions break

A test attains its **nominal** Type I rate $\alpha$ if and only if its assumptions hold. Misspecify any of them and the **actual** Type I rate drifts away from $\alpha$.

<div style="margin-top:0.8rem;padding:0.85rem 1.1rem;background:#FAFAFA;border-left:3px solid #1A1A1A;font-size:0.95rem;line-height:1.55;">

If the true distribution of the data differs from what the test assumes (heavier tails, larger variance, dependent observations), the null distribution of $Z$ is no longer $\mathcal{N}(0, 1)$. The procedure stops controlling $\alpha$.

</div>

Same formula, same critical values, broken assumption. Nominal $\alpha = 0.05$ can become $0.10$, $0.15$, or higher depending on the violation.

<div style="display:flex;justify-content:center;margin-top:1rem;">
<a href="/harbour-product-analytics-2026/07-statistics-3/assumptions-sim.html" target="_blank" rel="noopener" style="display:inline-block;padding:0.8rem 1.4rem;background:#1A1A1A;color:#fff;font-family:'JetBrains Mono',monospace;font-size:0.95rem;font-weight:700;letter-spacing:0.08em;text-transform:uppercase;text-decoration:none;border:2px solid #1A1A1A;">Open simulation ↗</a>
</div>

<!--
Common quiet failure modes in practice: ratio metrics with denominator dependence, time series with day-to-day correlation, A/B tests where users have multiple sessions. The fix is not to lower α. The fix is to use the right null distribution: delta method, bootstrap, cluster-robust SE. We come back to this in Session 9.
-->

---

# The p-value under $H_0$ is uniform

Under $H_0$ the p-value follows $\text{Uniform}[0, 1]$. That is why "reject if $p \lt \alpha$" controls the Type I rate at exactly $\alpha$: a fraction $\alpha$ of p-values fall below $\alpha$ by construction.

<div style="margin-top:0.7rem;padding:0.85rem 1.1rem;background:#FAFAFA;border-left:3px solid #1A1A1A;font-size:0.95rem;line-height:1.55;">

**Why.** For a continuous test statistic $T$ with null CDF $F$, the random variable $p = 1 - F(T)$ has $\mathbb{P}_{H_0}(p \le u) = u$ for $u \in [0, 1]$.

</div>

Each decile of $p$ maps to a symmetric pair of tail slices in $Z$. Same total mass per decile.

<div style="display:flex;justify-content:center;margin-top:1rem;">
<a href="/harbour-product-analytics-2026/07-statistics-3/pvalue-sim.html" target="_blank" rel="noopener" style="display:inline-block;padding:0.8rem 1.4rem;background:#1A1A1A;color:#fff;font-family:'JetBrains Mono',monospace;font-size:0.95rem;font-weight:700;letter-spacing:0.08em;text-transform:uppercase;text-decoration:none;border:2px solid #1A1A1A;">Open simulation ↗</a>
</div>

<!--
The Z histogram is bell-shaped but the p histogram is flat. Not a contradiction, it is the change of variables. The same colored band has the same area on both. Z deciles around the center are blue (large p), Z deciles in the tails are red (small p).
-->

---
layout: section
class: tint-cream
---

## 04

# Power, effect size, MDE

---

# FPR is controlled, but $H_1$ is composite

Pick $\alpha$, build the null distribution, the procedure delivers Type I rate at most $\alpha$. **What it does not tell us:** how often we catch a real deviation.

<div style="margin-top:0.7rem;padding:0.85rem 1.1rem;background:#FAFAFA;border-left:3px solid #1A1A1A;font-size:0.95rem;line-height:1.55;">

$H_1: \mu \ne \mu_0$ is **composite**. Many true values of $\mu$ are consistent with it. $\alpha$ says nothing about the true-positive rate when $H_1$ is true.

</div>

$$Z = \frac{\bar X - \mu_0}{\sigma / \sqrt n}$$

The same gap $\bar X - \mu_0$ produces wildly different $Z$ depending on $n$. The <span class="pink">$\sqrt n$</span> is the lever.

<!--
The whole point of this slide is to plant the question: if α controls coverage of H₀, what controls coverage of H₁? Nothing yet. The √n note sets up the next slide where we trace it through.
-->

---

# Detectable effect depends on $n$ and $\sigma$

Same critical value $\lvert Z \rvert \gt 1.96$, two scenarios.

<div style="display:grid;grid-template-columns:1fr 1fr;gap:1.1rem;margin-top:0.7rem;">

<div style="padding:0.8rem 1rem;background:#FAFAFA;border-left:3px solid #1A1A1A;font-size:0.9rem;">
<div style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#1A1A1A;text-transform:uppercase;letter-spacing:0.1em;margin-bottom:0.3rem;">small n</div>
Only large gaps cross 1.96. Moderate deviations go undetected.
</div>

<div style="padding:0.8rem 1rem;background:#FAFAFA;border-left:3px solid #1A1A1A;font-size:0.9rem;">
<div style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#1A1A1A;text-transform:uppercase;letter-spacing:0.1em;margin-bottom:0.3rem;">large n</div>
Even tiny gaps cross 1.96. Trivial deviations get detected too.
</div>

</div>

<div style="margin-top:0.8rem;padding:0.8rem 1.1rem;background:#FAFAFA;border-left:3px solid #FF00FF;font-size:0.95rem;line-height:1.55;">

We need a **second parameter**: the effect size we commit to detect. Together with $\alpha$ and $n$ it determines $\beta$ and the power $1 - \beta$.

</div>

<!--
Two extremes worth stating verbally. Tiny n → FPR under control but power near zero, we reject almost nothing real. Huge n → power near one for any non-zero effect, including ones too small to matter. The second case is the next slide's main subject.
-->

---

# Statistical vs practical significance

The mechanics of the test cannot tell us whether a detected effect is worth acting on.

<div style="display:grid;grid-template-columns:220px 240px 240px;gap:0.6rem;margin:0.6rem auto 0;width:fit-content;justify-content:center;font-family:'Inter',system-ui,sans-serif;">

<div></div>
<div style="text-align:center;font-family:'JetBrains Mono',monospace;font-size:0.78rem;color:#6B6B6B;text-transform:uppercase;letter-spacing:0.1em;padding:0.4rem;">Practically meaningful</div>
<div style="text-align:center;font-family:'JetBrains Mono',monospace;font-size:0.78rem;color:#6B6B6B;text-transform:uppercase;letter-spacing:0.1em;padding:0.4rem;">Practically trivial</div>

<div style="font-family:'JetBrains Mono',monospace;font-size:0.78rem;color:#6B6B6B;text-transform:uppercase;letter-spacing:0.1em;padding:0.8rem 0.6rem;text-align:right;">Stat significant</div>
<div style="padding:0.9rem;background:#F0FAF3;border-left:3px solid #1A8F4F;">
<div style="font-weight:700;color:#1A8F4F;font-size:0.95rem;">Real and matters</div>
<div style="color:#6B6B6B;font-size:0.85rem;margin-top:0.2rem;">usually ship</div>
</div>
<div style="padding:0.9rem;background:#FAFAFA;border-left:3px solid #6B6B6B;">
<div style="font-weight:700;color:#1A1A1A;font-size:0.95rem;">Real but irrelevant</div>
<div style="color:#6B6B6B;font-size:0.85rem;margin-top:0.2rem;">common at huge <em>n</em></div>
</div>

<div style="font-family:'JetBrains Mono',monospace;font-size:0.78rem;color:#6B6B6B;text-transform:uppercase;letter-spacing:0.1em;padding:0.8rem 0.6rem;text-align:right;">Not stat significant</div>
<div style="padding:0.9rem;background:#FFF0F0;border-left:3px solid #E5142B;">
<div style="font-weight:700;color:#E5142B;font-size:0.95rem;">Underpowered</div>
<div style="color:#6B6B6B;font-size:0.85rem;margin-top:0.2rem;">could be real, inconclusive</div>
</div>
<div style="padding:0.9rem;background:#FAFAFA;border-left:3px solid #6B6B6B;">
<div style="font-weight:700;color:#1A1A1A;font-size:0.95rem;">Likely noise</div>
<div style="color:#6B6B6B;font-size:0.85rem;margin-top:0.2rem;">no detectable effect</div>
</div>

</div>

<div v-click style="margin-top:1rem;text-align:center;font-size:1rem;color:#1A1A1A;line-height:1.5;">

Whether an effect matters is a product call.

</div>

<!--
Two failure modes to say out loud. Huge n, trivial effect: 10 million users, +0.01% DAU lift, p below 0.001. Statistically real, business irrelevant. Tiny n, huge effect: 200 users, +30% revenue lift, p around 0.4. Could be very real, we just don't have data to tell. The bridge to MDE is two steps: business call (smallest effect that matters), then statistical call (design enough power to detect it).
-->

---

# What is an effect

The effect determines how far apart the two distributions, under $H_0$ and $H_1$, sit on the number line.

| Form | Definition | When |
|---|---|---|
| Absolute | $\Delta = \mu_1 - \mu_0$ | Raw metric units, +0.05 conversions per user |
| Relative (lift) | $\Delta / \mu_0$ | Most A/B reports, +5% conversion rate |
| Standardized | $d = \Delta / \sigma$ | Unitless. Enters the power formula |

<!--
Three views of the same gap, equivalent given μ_B and σ. The first two are how product people talk. The third is how the math works. Standardized matters because power depends on √n·d alone, not on the units.
-->

---

# Effect = the gap between two distributions

Fix the true effect $\Delta = \mu_1 - \mu_0$ and $\sigma$. The bell width is $\sigma/\sqrt n$, so more data shrinks both bells. The same gap becomes much easier to distinguish.

<div style="display:grid;grid-template-columns:1fr 1fr;gap:1.2rem;margin-top:0.5rem;">

<div style="text-align:center;">
<div style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#6B6B6B;text-transform:uppercase;letter-spacing:0.1em;margin-bottom:0.3rem;">small n, heavy overlap</div>
<svg viewBox="0 0 280 150" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;font-family:'Inter',system-ui,sans-serif;">
<path d="M 10,114.67 Q 13.75,114.51 17.5,114.35 T 25,113.68 T 32.5,112.54 T 40,110.94 T 47.5,108.69 T 55,105.26 T 62.5,101.16 T 70,96.80 T 77.5,92.35 T 85,88.53 T 92.5,85.92 T 100,85 T 107.5,85.92 T 115,88.53 T 122.5,92.35 T 130,96.80 T 137.5,101.16 T 145,105.26 T 152.5,108.69 T 160,110.94 T 167.5,112.54 T 175,113.68 T 182.5,114.35 T 190,114.67" fill="none" stroke="#1A1A1A" stroke-width="1.6"/>
<path d="M 90,114.67 Q 93.75,114.51 97.5,114.35 T 105,113.68 T 112.5,112.54 T 120,110.94 T 127.5,108.69 T 135,105.26 T 142.5,101.16 T 150,96.80 T 157.5,92.35 T 165,88.53 T 172.5,85.92 T 180,85 T 187.5,85.92 T 195,88.53 T 202.5,92.35 T 210,96.80 T 217.5,101.16 T 225,105.26 T 232.5,108.69 T 240,110.94 T 247.5,112.54 T 255,113.68 T 262.5,114.35 T 270,114.67" fill="none" stroke="#FF00FF" stroke-width="1.6"/>
<line x1="0" y1="115" x2="280" y2="115" stroke="#1A1A1A" stroke-width="1"/>
<line x1="100" y1="85" x2="100" y2="130" stroke="#1A1A1A" stroke-width="0.6" stroke-dasharray="2 2"/>
<line x1="180" y1="85" x2="180" y2="130" stroke="#FF00FF" stroke-width="0.6" stroke-dasharray="2 2"/>
<line x1="100" y1="75" x2="180" y2="75" stroke="#1A1A1A" stroke-width="1.2" marker-start="url(#arr1l)" marker-end="url(#arr1r)"/>
<defs>
<marker id="arr1l" markerWidth="7" markerHeight="7" refX="0" refY="3.5" orient="auto"><polygon points="7 0, 0 3.5, 7 7" fill="#1A1A1A"/></marker>
<marker id="arr1r" markerWidth="7" markerHeight="7" refX="7" refY="3.5" orient="auto"><polygon points="0 0, 7 3.5, 0 7" fill="#1A1A1A"/></marker>
</defs>
<text x="140" y="70" style="font-size:11px;fill:#1A1A1A;text-anchor:middle;font-weight:700;">Δ</text>
<text x="100" y="143" style="font-size:10px;fill:#1A1A1A;text-anchor:middle;">μ₀</text>
<text x="180" y="143" style="font-size:10px;fill:#FF00FF;text-anchor:middle;font-weight:700;">μ₁</text>
</svg>
</div>

<div style="text-align:center;">
<div style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#6B6B6B;text-transform:uppercase;letter-spacing:0.1em;margin-bottom:0.3rem;">large n, little overlap</div>
<svg viewBox="0 0 280 150" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;font-family:'Inter',system-ui,sans-serif;">
<path d="M 64,114.67 Q 65.5,114.51 67,114.35 T 70,113.68 T 73,112.54 T 76,110.94 T 79,108.69 T 82,105.26 T 85,101.16 T 88,96.80 T 91,92.35 T 94,88.53 T 97,85.92 T 100,85 T 103,85.92 T 106,88.53 T 109,92.35 T 112,96.80 T 115,101.16 T 118,105.26 T 121,108.69 T 124,110.94 T 127,112.54 T 130,113.68 T 133,114.35 T 136,114.67" fill="none" stroke="#1A1A1A" stroke-width="1.6"/>
<path d="M 144,114.67 Q 145.5,114.51 147,114.35 T 150,113.68 T 153,112.54 T 156,110.94 T 159,108.69 T 162,105.26 T 165,101.16 T 168,96.80 T 171,92.35 T 174,88.53 T 177,85.92 T 180,85 T 183,85.92 T 186,88.53 T 189,92.35 T 192,96.80 T 195,101.16 T 198,105.26 T 201,108.69 T 204,110.94 T 207,112.54 T 210,113.68 T 213,114.35 T 216,114.67" fill="none" stroke="#FF00FF" stroke-width="1.6"/>
<line x1="0" y1="115" x2="280" y2="115" stroke="#1A1A1A" stroke-width="1"/>
<line x1="100" y1="85" x2="100" y2="130" stroke="#1A1A1A" stroke-width="0.6" stroke-dasharray="2 2"/>
<line x1="180" y1="85" x2="180" y2="130" stroke="#FF00FF" stroke-width="0.6" stroke-dasharray="2 2"/>
<line x1="100" y1="75" x2="180" y2="75" stroke="#1A1A1A" stroke-width="1.2" marker-start="url(#arr2l)" marker-end="url(#arr2r)"/>
<defs>
<marker id="arr2l" markerWidth="7" markerHeight="7" refX="0" refY="3.5" orient="auto"><polygon points="7 0, 0 3.5, 7 7" fill="#1A1A1A"/></marker>
<marker id="arr2r" markerWidth="7" markerHeight="7" refX="7" refY="3.5" orient="auto"><polygon points="0 0, 7 3.5, 0 7" fill="#1A1A1A"/></marker>
</defs>
<text x="140" y="70" style="font-size:11px;fill:#1A1A1A;text-anchor:middle;font-weight:700;">Δ</text>
<text x="100" y="143" style="font-size:10px;fill:#1A1A1A;text-anchor:middle;">μ₀</text>
<text x="180" y="143" style="font-size:10px;fill:#FF00FF;text-anchor:middle;font-weight:700;">μ₁</text>
</svg>
</div>

</div>

Same true $\Delta$. With small $n$ the test cannot separate the two distributions. With large $n$ the same gap stands out clearly.

<!--
The static intuition behind power. Same Δ, same σ, only n changes. Bell width = σ/√n shrinks with more data, so the same true effect goes from "barely detectable" to "obviously detectable". The Power simulation later lets the class drag n and μ₁ to see this dynamically with α, β, and power shaded.
-->

---

# Minimum detectable effect (MDE)

Power function: $\text{Power}(\Delta) := \mathbb{P}_{\Delta}(\text{reject } H_0) = 1 - \beta(\Delta)$. At $\Delta = 0$ it equals $\alpha$ and climbs toward 1 as $\Delta$ grows.

<div style="margin-top:0.6rem;padding:0.8rem 1.1rem;background:#FAFAFA;border-left:3px solid #FF00FF;font-size:0.95rem;line-height:1.55;">

**MDE** is the smallest $\Delta$ at which the test commits to power at least $1 - \beta$: $\text{MDE} := \min \{\, \Delta \gt 0 \,:\, \text{Power}(\Delta) \ge 1 - \beta \,\}$.

</div>

Solving $\text{Power}(\Delta) = 1 - \beta$ under the Normal approximation:

$$\boxed{\;\text{MDE} = (z_{1-\alpha/2} + z_{1-\beta}) \cdot \dfrac{\sigma}{\sqrt n}\;}$$

<!--
Composite H₁ means power is a function, not a number. MDE is the smallest effect at which we commit to the chosen power level. Two-sided form here, matches our default. SDA gives the one-sided variant with z_{1-α} in place of z_{1-α/2}; gap is small at typical α and β.
-->

---

# MDE: four levers

| Lever | Direction | Effect on MDE |
|---|---|---|
| $\alpha$ ↑ (more lenient FP threshold) | $z_{1-\alpha/2}$ ↓ | MDE ↓ |
| $\beta$ ↑ (lower target power) | $z_{1-\beta}$ ↓ | MDE ↓ |
| $\sigma$ ↑ (noisier metric) | numerator ↑ | MDE ↑ (linear in $\sigma$) |
| $n$ ↑ (more data) | $\sqrt n$ ↑ | MDE ↓ (shrinks as $1/\sqrt n$) |

Change one, hold the rest, MDE moves predictably. These are the **four design knobs** every A/B platform exposes.

<!--
Worth pausing on the n lever. Quadrupling sample size halves MDE. This is why platforms emphasize ramp-up and patience over tweaking α. σ is usually fixed by the metric, but variance reduction (CUPED in S9) lets you push it down without growing n.
-->

---

# MDE in real life

The A/B platform reports **MDE = 10% for revenue**. What does it mean?

<div v-click style="margin-top:0.5rem;font-size:0.9rem;line-height:1.5;">

A property of the experiment design at $\alpha = 5\%$ and power 80%:

| True lift | Outcome |
|---|---|
| 15% | very likely to detect |
| 10% | $\approx 80\%$ chance |
| 5% | very likely to miss |

</div>

<div v-click style="margin-top:0.4rem;padding:0.45rem 0.9rem;background:#FAFAFA;border-left:3px solid #1A1A1A;font-size:0.8rem;line-height:1.4;">

**Underpowered:** MDE exceeds the smallest effect that matters $\Delta^*$, so $\text{Power}(\Delta^*) \lt 1 - \beta$.

</div>

<!--
Open the discussion: ask the class what MDE = 10% means for revenue before reading off the answer. Then unpack: it's about the design, not the metric. The underpowered definition lands here and gets reused in the misconceptions slide and in the replication coda.
-->

---

# Power simulation

Set the effect, run the test, watch empirical power converge to the theoretical area.

<div style="display:grid;grid-template-columns:1fr 1fr;gap:0.8rem;margin-top:0.8rem;">

<div style="padding:0.7rem 0.9rem;background:#FAFAFA;border-left:3px solid #1A1A1A;">
<div style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#1A1A1A;text-transform:uppercase;letter-spacing:0.1em;margin-bottom:0.25rem;">setup</div>

$\bar X \sim \mathcal{N}(\mu_0, \sigma^2/n)$ under $H_0$

$\bar X \sim \mathcal{N}(\mu_1, \sigma^2/n)$ under $H_1$

</div>

<div style="padding:0.7rem 0.9rem;background:#FFF0F0;border-left:3px solid #FF00FF;">
<div style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#FF00FF;text-transform:uppercase;letter-spacing:0.1em;margin-bottom:0.25rem;">empirical power = TPR</div>

Fraction of $M$ simulated runs that reject $H_0$ under $H_1$.

</div>

</div>

In statistics this number is called **power**. In ML and diagnostics the same quantity under $H_1$ is the **true positive rate**, also known as sensitivity or recall.

<div style="display:flex;justify-content:center;margin-top:1rem;">
<a href="/harbour-product-analytics-2026/07-statistics-3/power-sim.html" target="_blank" rel="noopener" style="display:inline-block;padding:0.8rem 1.4rem;background:#1A1A1A;color:#fff;font-family:'JetBrains Mono',monospace;font-size:0.95rem;font-weight:700;letter-spacing:0.08em;text-transform:uppercase;text-decoration:none;border:2px solid #1A1A1A;">Open simulation ↗</a>
</div>

<!--
Increase n: both bells narrow, overlap shrinks, empirical TPR climbs, matches theoretical area. Decrease μ₁ − μ₀: bells overlap more, TPR drops. This is the dual of the A/A simulation: A/A calibrates α under H₀, this one calibrates β and power under H₁. Power is earned by data or by a larger true effect, not by tuning α.
-->

---

# Four misconceptions about p-values

| Misconception | Reality |
|---|---|
| $p = \mathbb{P}(H_0 \mid \text{data})$ | $p$ is defined **under** $H_0$, not a posterior on it |
| $1 - p = \mathbb{P}(H_1 \mid \text{data})$ | $H_1$ is composite. No single $\Delta$ to attach a posterior to |
| Small $p$ means large effect | $p$ mixes effect size and $n$. Huge $n$ shrinks $p$ for trivial effects |
| $p \gt 0.05$ means no effect | Failure to reject is silence. Underpowered tests fail to reject under $H_1$ |

<!--
Misconception 3 is where stat sig vs business sig sits. Read the effect size and the CI, not p alone. Misconception 4 connects to underpowered: absence of evidence is not evidence of absence.
-->

---
layout: section
class: tint-sky
---

## 05

# CI duality and replication

---

# Testing via the CI of the difference

Build the CI directly on the difference. Reject $H_0: \mu_A = \mu_B$ when 0 is outside.

$$\mathrm{CI}_{1-\alpha}(\mu_A - \mu_B) = (\bar X_A - \bar X_B) \;\pm\; z_{1-\alpha/2} \cdot \mathrm{SE}, \qquad \mathrm{SE} = \sqrt{\tfrac{\sigma_A^2}{n_A} + \tfrac{\sigma_B^2}{n_B}}$$

<div style="margin-top:0.6rem;padding:0.7rem 1.1rem;background:#FFF0F0;border-left:3px solid #E5142B;font-size:0.9rem;line-height:1.5;">

**Common mistake:** rejecting when individual CIs for $\bar X_A$ and $\bar X_B$ don't overlap. For equal $\sigma$ it needs $\lvert \bar X_A - \bar X_B \rvert \gt 2z\,\mathrm{SE}$ vs proper $\sqrt 2 \, z \,\mathrm{SE}$. **Overly conservative.**

</div>

<div style="display:flex;justify-content:center;margin-top:0.7rem;">
<a href="/harbour-product-analytics-2026/07-statistics-3/ci-diff-sim.html" target="_blank" rel="noopener" style="display:inline-block;padding:0.7rem 1.3rem;background:#1A1A1A;color:#fff;font-family:'JetBrains Mono',monospace;font-size:0.9rem;font-weight:700;letter-spacing:0.08em;text-transform:uppercase;text-decoration:none;border:2px solid #1A1A1A;">Open simulation ↗</a>
</div>

<!--
The proper test corresponds exactly to the CI of the difference excluding 0. Comparing individual-group CIs is the standard shortcut analysts reach for, and it gets the SE wrong. Sim under H₀: empirical FPR via CI-of-diff sits at α; via the "is the other mean inside my CI" rule it climbs above α. Same data, wrong rule.
-->

---

# Replication crisis

A pattern across empirical science of published findings that fail to reproduce when the experiment is run again. Best documented in psychology, biomedicine, and the social sciences, but the failure mode is general: wherever studies are underpowered and the literature is filtered for significance, poorly planned experiments yield wrong conclusions. False positives that do not survive replication, **and** inflated effect estimates even when the underlying effect is real.

<div class="absolute bottom-6 left-14 right-14" style="font-size:0.85rem;color:#6B6B6B;line-height:1.6;">
References:
<a href="https://en.wikipedia.org/wiki/Replication_crisis" target="_blank" rel="noopener" style="color:#6B6B6B;text-decoration:underline;">Wikipedia · Replication crisis</a> ·
<a href="https://en.wikipedia.org/wiki/Reproducibility_Project" target="_blank" rel="noopener" style="color:#6B6B6B;text-decoration:underline;">Wikipedia · Reproducibility Project</a>
</div>

<!--
The "TP inflated even when real effect exists" framing maps to Type M errors (Gelman & Carlin 2014) — a study with low power that does reject typically overstates the magnitude, because only large random deviations were significant. Reproducibility Project (2015) replicated 100 psychology studies; ~39% reproduced, average effect size in replications about half of originals — both failure modes visible. Industry parallels: pre-registration, A/A calibration, MDE-driven sample planning. Deferred to S9: multiple testing, sequential testing, publication bias, p-hacking.
-->

