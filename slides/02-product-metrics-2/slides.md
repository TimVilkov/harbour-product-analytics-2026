---
theme: apple-basic
title: "Session 02: Product Metrics 2"
info: "Product Analytics · Harbour.Space · 2026"
highlighter: shiki
drawings:
  persist: false
transition: fade
mdc: true
layout: intro
---

# Product <span class="pink">Metrics</span>

Day 2: trees, granularity, trade-offs

<div class="absolute bottom-10 left-14" style="font-family:'JetBrains Mono',monospace;font-size:0.75rem;text-transform:uppercase;letter-spacing:0.15em;color:rgba(255,255,255,0.55);">
  Harbour.Space &middot; Barcelona &middot; May 19, 2026
</div>

---
layout: section
class: tint-cream
---

## 09

# Metric tree

---

# Same metric, different trees

<div style="display:flex;justify-content:center;gap:1.5rem;margin-top:1.5rem;">

  <svg viewBox="0 0 240 145" style="width:30%;max-width:280px;">
    <text x="120" y="14" text-anchor="middle" style="font:600 10px 'JetBrains Mono',monospace;letter-spacing:0.1em;text-transform:uppercase;fill:#AAAAAA;">by region</text>
    <rect x="85" y="30" width="70" height="26" rx="4" fill="#1A1A1A"/>
    <text x="120" y="48" text-anchor="middle" style="font:700 11px Inter,sans-serif;fill:#FFFFFF;">Revenue</text>
    <text x="120" y="76" text-anchor="middle" style="font:700 14px Inter,sans-serif;fill:#FF00FF;">Σ</text>
    <line x1="120" y1="58" x2="42" y2="98" stroke="#AAAAAA" stroke-width="1.2"/>
    <line x1="120" y1="58" x2="120" y2="98" stroke="#AAAAAA" stroke-width="1.2"/>
    <line x1="120" y1="58" x2="198" y2="98" stroke="#AAAAAA" stroke-width="1.2"/>
    <rect x="15" y="98" width="55" height="24" rx="3" fill="#FFFFFF" stroke="#1A1A1A" stroke-width="1.2"/>
    <text x="42" y="114" text-anchor="middle" style="font:600 10px Inter,sans-serif;fill:#1A1A1A;">EU</text>
    <rect x="92" y="98" width="55" height="24" rx="3" fill="#FFFFFF" stroke="#1A1A1A" stroke-width="1.2"/>
    <text x="120" y="114" text-anchor="middle" style="font:600 10px Inter,sans-serif;fill:#1A1A1A;">US</text>
    <rect x="170" y="98" width="55" height="24" rx="3" fill="#FFFFFF" stroke="#1A1A1A" stroke-width="1.2"/>
    <text x="198" y="114" text-anchor="middle" style="font:600 10px Inter,sans-serif;fill:#1A1A1A;">APAC</text>
  </svg>

  <svg viewBox="0 0 240 145" style="width:30%;max-width:280px;">
    <text x="120" y="14" text-anchor="middle" style="font:600 10px 'JetBrains Mono',monospace;letter-spacing:0.1em;text-transform:uppercase;fill:#AAAAAA;">by product</text>
    <rect x="85" y="30" width="70" height="26" rx="4" fill="#1A1A1A"/>
    <text x="120" y="48" text-anchor="middle" style="font:700 11px Inter,sans-serif;fill:#FFFFFF;">Revenue</text>
    <text x="120" y="76" text-anchor="middle" style="font:700 14px Inter,sans-serif;fill:#FF00FF;">Σ</text>
    <line x1="120" y1="58" x2="42" y2="98" stroke="#AAAAAA" stroke-width="1.2"/>
    <line x1="120" y1="58" x2="120" y2="98" stroke="#AAAAAA" stroke-width="1.2"/>
    <line x1="120" y1="58" x2="198" y2="98" stroke="#AAAAAA" stroke-width="1.2"/>
    <rect x="15" y="98" width="55" height="24" rx="3" fill="#FFFFFF" stroke="#1A1A1A" stroke-width="1.2"/>
    <text x="42" y="114" text-anchor="middle" style="font:600 10px Inter,sans-serif;fill:#1A1A1A;">Product A</text>
    <rect x="92" y="98" width="55" height="24" rx="3" fill="#FFFFFF" stroke="#1A1A1A" stroke-width="1.2"/>
    <text x="120" y="114" text-anchor="middle" style="font:600 10px Inter,sans-serif;fill:#1A1A1A;">Product B</text>
    <rect x="170" y="98" width="55" height="24" rx="3" fill="#FFFFFF" stroke="#1A1A1A" stroke-width="1.2"/>
    <text x="198" y="114" text-anchor="middle" style="font:600 10px Inter,sans-serif;fill:#1A1A1A;">Product C</text>
  </svg>

  <svg viewBox="0 0 240 145" style="width:30%;max-width:280px;">
    <text x="120" y="14" text-anchor="middle" style="font:600 10px 'JetBrains Mono',monospace;letter-spacing:0.1em;text-transform:uppercase;fill:#AAAAAA;">users × check</text>
    <rect x="85" y="30" width="70" height="26" rx="4" fill="#1A1A1A"/>
    <text x="120" y="48" text-anchor="middle" style="font:700 11px Inter,sans-serif;fill:#FFFFFF;">Revenue</text>
    <text x="120" y="78" text-anchor="middle" style="font:700 18px Inter,sans-serif;fill:#FF00FF;">×</text>
    <line x1="120" y1="58" x2="60" y2="98" stroke="#AAAAAA" stroke-width="1.2"/>
    <line x1="120" y1="58" x2="180" y2="98" stroke="#AAAAAA" stroke-width="1.2"/>
    <rect x="20" y="98" width="80" height="24" rx="3" fill="#FFFFFF" stroke="#1A1A1A" stroke-width="1.2"/>
    <text x="60" y="114" text-anchor="middle" style="font:600 9px Inter,sans-serif;fill:#1A1A1A;">Paying users</text>
    <rect x="140" y="98" width="80" height="24" rx="3" fill="#FFFFFF" stroke="#1A1A1A" stroke-width="1.2"/>
    <text x="180" y="114" text-anchor="middle" style="font:600 9px Inter,sans-serif;fill:#1A1A1A;">Avg check</text>
  </svg>

</div>

<p style="text-align:center;font-size:1.4rem;margin-top:2rem;font-weight:700;color:#1A1A1A;">Which one is <span class="pink">right</span>?</p>

<!--
Discussion-prompt slide. Three valid decompositions of Revenue:
- by region (sum across geographies)
- by product (sum across product lines)
- by users × check (multiplicative)

All three are arithmetically clean. None is universally correct. The question forces students to think about what determines the choice — answered on the next slide.

Trees are SVG, palette-compliant (black/white/gray + magenta operation symbols). Pink reserved for the Σ / × operation marks and the word "right" in the question.
-->

---

# Pick the tree your team can <span class="pink">act</span> on

<p style="color:#1A1A1A;font-size:1.2rem;margin-top:1.2rem;line-height:1.55;">The right decomposition is the one your team has levers for. If you do not have regional managers, splitting Revenue by region is decoration. If you have product-line owners with separate budgets, the product decomposition matches the org. If paying-users count and average check sit with different teams, the multiplicative version is the one that helps the team plan.</p>

<!--
Answer to the previous slide's question. The meta-rule: the tree mirrors the org's operating levers. A decomposition you cannot act on is decoration, not a tree.

Speaker beats:
- The decomposition reflects who owns what, where the money comes from operationally, and what the team can decide independently
- Tim's framing: "отталкиваться нужно от того, какая у вас структура компании и взгляд на бизнес"
- Cleo-style LTV-rooted tree on next slide is the same principle applied to the root choice itself
- Bridge: this is why the same KPI gets decomposed differently across companies — it is not a math choice, it is an org choice
-->

---

# The root can be a business metric

<p style="color:#1A1A1A;font-size:1.2rem;margin-top:1rem;line-height:1.55;">The NSM framework puts a product metric at the root. Other teams put a business metric there instead and rebuild the tree under it.</p>

<div style="margin-top:1.5rem;padding:1rem 1.4rem;border-left:3px solid #1A1A1A;">
  <div style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.12em;color:#FF00FF;margin-bottom:0.4rem;">Example · Cleo, UK fintech</div>
  <p style="font-size:1.1rem;color:#1A1A1A;line-height:1.5;margin:0;">Cleo runs its entire metric tree with <strong>LTV</strong> at the root. Every initiative is evaluated by how directly it moves LTV. Every leaf ladders to LTV.</p>
</div>

<!--
Counterpoint to the canonical NSM-as-root pattern. The root choice anchors the team's definition of value, and NSM vs business-metric roots produce different priorities. Cleo's LTV-rooted tree forces every initiative into a financial-impact framing — useful for product-market-fit and unit-economics-sensitive products, riskier for early-stage discovery work.

Pedagogical use:
- Frame after the standard NSM-tree setup so students see NSM is one option, not the only one
- Trade-offs to discuss: LTV-rooted trees push toward short-term measurable impact and away from leading indicators
- LTV is genuinely lagging — see slide 40b (retention as fast feedback) discussion for the parallel concern

Tim's source: Cleo case from personal knowledge / industry conversation. No public-source link.
-->

---

<div style="position:absolute;top:4.5rem;left:1rem;right:1rem;bottom:1rem;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:0.6rem;">
  <img src="/avito-metric-tree-2021.png" alt="Avito metric tree, 2021 — production snapshot from Miro" style="flex:1 1 auto;min-height:0;max-width:100%;object-fit:contain;display:block;" />
  <span style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#AAAAAA;text-transform:uppercase;letter-spacing:0.12em;flex-shrink:0;">Avito &middot; metric tree &middot; 2021</span>
</div>

<!--
Production exhibit. What a real metric tree looks like at marketplace scale — hundreds of nodes, branching from a single L1 down through L2, L3, L4 metrics. Internal Miro screenshot from Avito, 2021.

Pedagogical use:
- Show after the conceptual "L1 → L2 → L3" setup on the previous slide. Lands the contrast: textbook trees are tiny, production trees are this.
- Point out that all leaves still ladder up to a single root — the NSM at the top.
- Color coding (yellow / blue / green nodes) reflects metric domains or ownership inside Avito; specifics not important for students.
- Discussion angles: who owns what part of this? How does a team prioritize when their leaf moves but no one upstream notices? Why is governance hard at this scale?
- Source note: internal screenshot, no public link. Tim references this from personal experience at Avito.

Full-bleed image slide, no H1 — image speaks. Caption in mono caps below for context.
-->

---

<div style="position:absolute;top:4.5rem;left:1rem;right:1rem;bottom:3.5rem;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:0.6rem;">
  <img src="/experian-autocheck-report.png" alt="Experian AutoCheck vehicle history report — sample for a 2015 Acura TLX" style="flex:1 1 auto;min-height:0;max-width:100%;object-fit:contain;display:block;" />
  <span style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#AAAAAA;text-transform:uppercase;letter-spacing:0.12em;flex-shrink:0;">Vehicle report service</span>
</div>

<div style="position:absolute;bottom:1.2rem;left:3.5rem;font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#AAAAAA;letter-spacing:0.1em;text-transform:uppercase;">
  <a href="https://autoteka.ru/vin/example?utm_source=mainPage" target="_blank" style="color:inherit;text-decoration:none;">autoteka.ru / vin / example</a>
</div>

<!--
Anchor the next slide — tangible product before abstract tree.

What this product is:
- Pay-per-report vehicle history service. Buyer pays a single fee, receives a VIN-level report covering title brands, accident records, recalls, odometer history, ownership chain.
- Examples: Experian AutoCheck (US), Carfax (US), Autoteka (RU).
- Buyers: used-car shoppers, dealers, fleet managers.
- Pricing: single-report fee for shoppers; bulk packs for dealers and high-volume buyers.

Unit of analysis is the purchase, not a session. Retention happens only when the user buys another car — typically months or years between purchases for individual buyers, daily for dealers. Two very different customer modes living inside one revenue line.
-->

---

<div style="position:absolute;top:4.5rem;left:1rem;right:1rem;bottom:1rem;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:0.6rem;">
  <img src="/vehicle-report-metric-tree.jpg" alt="Vehicle report service — revenue decomposition with AARRR overlay" style="flex:1 1 auto;min-height:0;max-width:100%;object-fit:contain;display:block;" />
  <span style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#AAAAAA;text-transform:uppercase;letter-spacing:0.12em;flex-shrink:0;">Vehicle report service</span>
</div>

<!--
Same five-axis framework from earlier (every metric is a point on funnel stage, domain, time, level, granularity), now applied to a real revenue tree.

Walk:
1. Revenue = PU × ARPPU. Two L1 branches.
2. PU decomposes into Retained users + New paying users. Retained users itself recurses — today's retained = N-day retention rate × past period's New paying users. The tree references its own past state.
3. ARPPU decomposes into purchases-per-PU × reports-per-purchase × price-per-report.

Flag two things students will miss:
- Reports-per-purchase and price-per-report are negatively correlated through bulk discounts. The three ARPPU children are not independent levers.
- ARPPU itself is a weighted average over the PU mix. Growing PU through cheap acquisition drags ARPPU down compositionally even when nothing else changes.

Color tags show AARRR stage per leaf. Multiple tags on one leaf when the metric is sensitive to two phases (free users feed both acquisition and retention; conversion is both activation and the first monetization moment).
-->

---

# Constellation of metrics

<p style="color:#1A1A1A;font-size:1.1rem;margin-top:0.3rem;line-height:1.5;">A tree is not the only shape. Output metrics (business and product outcomes) sit at the top, input metrics drive them from below. Outputs influence each other; inputs feed specific outputs.</p>

<div style="display:flex;justify-content:center;align-items:center;margin-top:0.5rem;">
  <img src="/constellation-output-input-metrics.jpeg" alt="Constellation of metrics — output and input metrics" style="max-width:100%;max-height:13rem;object-fit:contain;display:block;" />
</div>

<div style="position:absolute;bottom:1rem;left:3.5rem;font-family:'JetBrains Mono',monospace;font-size:0.65rem;color:#AAAAAA;letter-spacing:0.1em;text-transform:uppercase;">
  <a href="https://www.reforge.com/blog/north-star-metric-growth" target="_blank" style="color:inherit;text-decoration:none;">reforge.com / blog / don't let your north star metric deceive you</a>
</div>

<!--
Constellation pattern. Alternative to strict hierarchical tree.

Speaker beats:
- Output metrics = business + product outcomes the team is judged on (Monetization, Retention, Engagement in this example)
- Input metrics = levers the team can pull (feature usage, onboarding completion, push opens, etc.)
- Horizontal arrows between outputs = causal relationships (engagement drives retention, retention drives monetization)
- Vertical arrows from inputs to outputs = the levers that move each output
- This shape is closer to what mature teams actually use: not a single rooted tree, but a small set of named outputs each with their own input set
- When to use a constellation instead of a tree: when the business has multiple co-equal outcomes (B2B SaaS with NRR + new logo growth + product engagement), or when the tree decomposition is non-arithmetic and the cleaner mental model is "outputs at the top, inputs at the bottom"
-->

---

# Branches aren't always arithmetic

<p style="color:#1A1A1A;font-size:1.2rem;margin-top:1rem;line-height:1.55;">Not every parent-child edge in a metric tree is a clean mathematical identity. Some edges are <span class="pink">causal hypotheses</span> you accept on faith or measure indirectly.</p>

<div style="margin-top:1.5rem;">
  <div style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.12em;color:#AAAAAA;margin-bottom:0.5rem;">Where it shows up</div>
  <ul style="list-style:disc;padding-left:1.2rem;color:#1A1A1A;font-size:1.1rem;line-height:1.55;margin:0;">
    <li style="margin-bottom:0.35rem;">Linking activation to retention</li>
    <li style="margin-bottom:0.35rem;">Marginal effect of each new Manychat automation on retention</li>
    <li>Most product-metric to business-metric causal chains</li>
  </ul>
</div>

<!--
Honest-about-limits moment in the metric-tree section. Distinguishes two kinds of edges:

1. Arithmetic identity (clean math): GMV = AOV × orders. DAU = (DAU/WAU) × WAU. These decomposes without assumption.
2. Causal hypothesis (best guess): "better activation → better retention" — we believe it, often can't prove the exact functional form, can't reliably attribute the marginal lift of one specific feature.

Estimation approaches when arithmetic fails:
- Correlation analysis (weak — doesn't prove direction)
- Cohort uplift comparisons (better — but confounded)
- A/B tests on the feature itself (strongest — but expensive and slow)
- Sometimes just accept the link and move on. The tree is a model of the team's beliefs, not an audit-grade financial statement.

Concept slide. The next slide is the worked example using the vehicle-report tree with a red belief-based branch.
-->

---

# Not always arithmetic

<div style="position:absolute;top:9rem;left:1rem;right:1rem;bottom:1rem;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:0.6rem;">
  <img src="/vehicle-report-metric-tree-belief.jpg" alt="Vehicle report service tree with a belief-based branch in red" style="flex:1 1 auto;min-height:0;max-width:100%;object-fit:contain;display:block;" />
</div>

<!--
Worked example for the earlier "branches aren't always arithmetic" slide.

The added node: Amount of insights per report — the volume of useful information a buyer gets out of one report (data depth, signals flagged, scoring richness).

It hangs off Purchases-per-PU through a non-arithmetic link.

The hypothesis: more useful insights per report → user perceives more value → user is more likely to come back next time they buy a car → improves retention. We cannot write Retention = f(Insights) as a formula. We can only test the link indirectly through cohort comparisons, A/B tests on report content changes, qualitative research.

Why include it in the tree at all? The tree is a model of the team's beliefs. Encoding "Amount of insights drives retention" makes that belief explicit and reviewable. Without it on the tree, the team that ships richer reports has no language for why that work matters.

Visual convention worth teaching students:
- Solid edge = arithmetic identity, child multiplies / sums into parent.
- Dashed or red edge = belief / hypothesis, link is best-guess causal.

When students build their own trees in HW1, every belief-based branch should be visually distinct so the reviewer immediately knows which links are formulas and which are bets.
-->

---
layout: section
class: tint-sky
---

## 10

# Granularity

---

# Different questions, different granularity

<p style="color:#1A1A1A;font-size:1.1rem;margin-top:0.4rem;line-height:1.5;">The slice the metric describes. Each granularity answers a question the others can't.</p>

<div style="margin-top:1.5rem;display:flex;flex-direction:column;gap:1.1rem;">

  <div style="display:grid;grid-template-columns:11rem 1fr;gap:1.3rem;align-items:baseline;">
    <span style="font-family:'JetBrains Mono',monospace;font-size:0.72rem;color:#FF00FF;letter-spacing:0.12em;text-transform:uppercase;">Product level</span>
    <span style="font-size:1.05rem;color:#1A1A1A;line-height:1.5;">What is happening with our product overall? Are users sticking, monetizing, growing</span>
  </div>

  <div style="display:grid;grid-template-columns:11rem 1fr;gap:1.3rem;align-items:baseline;">
    <span style="font-family:'JetBrains Mono',monospace;font-size:0.72rem;color:#FF00FF;letter-spacing:0.12em;text-transform:uppercase;">Feature level</span>
    <span style="font-size:1.05rem;color:#1A1A1A;line-height:1.5;">How much do users use this specific feature, do they keep coming back to it</span>
  </div>

  <div style="display:grid;grid-template-columns:11rem 1fr;gap:1.3rem;align-items:baseline;">
    <span style="font-family:'JetBrains Mono',monospace;font-size:0.72rem;color:#FF00FF;letter-spacing:0.12em;text-transform:uppercase;">Cohort level</span>
    <span style="font-size:1.05rem;color:#1A1A1A;line-height:1.5;">Are users we acquire today behaving differently from users we acquired six months ago</span>
  </div>

</div>

<!--
Three granularity layers (product / feature / cohort) — each answers a question the others can't.

Bridge to next slide: the cohort line introduces the question Tim picks up next about rolling churn vs cohort retention.
-->

---

# Is this a good churn metric?

<p style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);text-align:center;font-family:'JetBrains Mono',monospace;font-size:1.6rem;color:#1A1A1A;letter-spacing:0.03em;line-height:1.5;width:90%;margin:0;">Rolling 30d churn  =  <span style="color:#FF00FF;">churned in last 30d</span>  /  <span style="color:#FF00FF;">paying accounts</span></p>

<!--
Discussion-first slide.

Read the formula. Show the chart of paying base decomposed by cohort. Ask the room: is this a good metric?

The trap:
- Numerator (churned in last 30d) is dominated by older, larger cohorts that have aged into churn-prone tails
- Denominator (paying accounts today) is the mix of all cohorts still alive, including a fresh Jun cohort that hasn't had time to churn
- If June acquisition was 3× May, denominator inflates faster than numerator → ratio drops → "churn improved!" headline even when product is worse

Honest answer: rolling churn is a leading-style health indicator at best, but it conflates acquisition velocity with retention quality. For decisions about whether the product is getting better, you have to cut by cohort.

Cohort = group of users who joined the product within the same time window (canonical acquisition cohort). Each cohort tracked over time as its own population.

Pedagogical bridge: this is the preview. Session 12 (Cohort Analysis & Modeling) covers the mechanics (retention curves, LTV, cohort-table heatmaps).

Reveal: <p v-click> hides the "No, here's why" answer until Tim clicks after the discussion lands.
-->

---

# Logo retention by cohort

<p style="color:#1A1A1A;font-size:1.05rem;margin-top:0.3rem;line-height:1.45;">Cohort cut on the same paying base. Each line is one acquisition cohort's logo retention over the months that follow sign-up.</p>

<div style="display:flex;justify-content:center;margin-top:0.6rem;">
<svg viewBox="0 0 700 240" style="width:96%;max-width:760px;overflow:visible;">
  <!-- y-axis -->
  <line x1="60" y1="10" x2="60" y2="200" stroke="#1A1A1A" stroke-width="1.2"/>
  <text x="54" y="14" text-anchor="end" style="font:9px 'JetBrains Mono',monospace;fill:#666;">100%</text>
  <text x="54" y="58" text-anchor="end" style="font:9px 'JetBrains Mono',monospace;fill:#666;">90%</text>
  <text x="54" y="105" text-anchor="end" style="font:9px 'JetBrains Mono',monospace;fill:#666;">80%</text>
  <text x="54" y="152" text-anchor="end" style="font:9px 'JetBrains Mono',monospace;fill:#666;">70%</text>
  <text x="54" y="200" text-anchor="end" style="font:9px 'JetBrains Mono',monospace;fill:#666;">60%</text>

  <text x="20" y="105" text-anchor="middle" transform="rotate(-90 20 105)" style="font:9px 'JetBrains Mono',monospace;letter-spacing:0.1em;text-transform:uppercase;fill:#666;">Logo retention</text>

  <line x1="60" y1="58" x2="660" y2="58" stroke="#E0E0E0" stroke-width="0.6" stroke-dasharray="2 3"/>
  <line x1="60" y1="105" x2="660" y2="105" stroke="#E0E0E0" stroke-width="0.6" stroke-dasharray="2 3"/>
  <line x1="60" y1="152" x2="660" y2="152" stroke="#E0E0E0" stroke-width="0.6" stroke-dasharray="2 3"/>

  <line x1="60" y1="200" x2="660" y2="200" stroke="#1A1A1A" stroke-width="1.2"/>

  <text x="60" y="215" text-anchor="middle" style="font:9px 'JetBrains Mono',monospace;fill:#666;">M0</text>
  <text x="160" y="215" text-anchor="middle" style="font:9px 'JetBrains Mono',monospace;fill:#666;">M1</text>
  <text x="260" y="215" text-anchor="middle" style="font:9px 'JetBrains Mono',monospace;fill:#666;">M2</text>
  <text x="360" y="215" text-anchor="middle" style="font:9px 'JetBrains Mono',monospace;fill:#666;">M3</text>
  <text x="460" y="215" text-anchor="middle" style="font:9px 'JetBrains Mono',monospace;fill:#666;">M4</text>
  <text x="560" y="215" text-anchor="middle" style="font:9px 'JetBrains Mono',monospace;fill:#666;">M5</text>
  <text x="660" y="215" text-anchor="middle" style="font:9px 'JetBrains Mono',monospace;fill:#666;">M6</text>
  <text x="660" y="232" text-anchor="end" style="font:9px 'JetBrains Mono',monospace;letter-spacing:0.1em;text-transform:uppercase;fill:#666;">months since sign-up</text>

  <!-- Q1 cohort (oldest, best retention) -->
  <polyline points="60,10 160,28 260,40 360,50 460,58 560,64 660,68" fill="none" stroke="#1A1A1A" stroke-width="2.2"/>
  <circle cx="60" cy="10" r="3" fill="#1A1A1A"/>
  <circle cx="160" cy="28" r="3" fill="#1A1A1A"/>
  <circle cx="260" cy="40" r="3" fill="#1A1A1A"/>
  <circle cx="360" cy="50" r="3" fill="#1A1A1A"/>
  <circle cx="460" cy="58" r="3" fill="#1A1A1A"/>
  <circle cx="560" cy="64" r="3" fill="#1A1A1A"/>
  <circle cx="660" cy="68" r="3" fill="#1A1A1A"/>
  <text x="610" y="62" style="font:600 10px Inter,sans-serif;fill:#1A1A1A;">Q1 cohort</text>

  <!-- Q2 cohort -->
  <polyline points="60,10 160,42 260,60 360,75 460,88 560,98" fill="none" stroke="#888888" stroke-width="2.2"/>
  <circle cx="60" cy="10" r="3" fill="#888888"/>
  <circle cx="160" cy="42" r="3" fill="#888888"/>
  <circle cx="260" cy="60" r="3" fill="#888888"/>
  <circle cx="360" cy="75" r="3" fill="#888888"/>
  <circle cx="460" cy="88" r="3" fill="#888888"/>
  <circle cx="560" cy="98" r="3" fill="#888888"/>
  <text x="510" y="92" style="font:600 10px Inter,sans-serif;fill:#888888;">Q2 cohort</text>

  <!-- Q3 cohort -->
  <polyline points="60,10 160,58 260,85 360,110 460,128" fill="none" stroke="#BFBFBF" stroke-width="2.2"/>
  <circle cx="60" cy="10" r="3" fill="#BFBFBF"/>
  <circle cx="160" cy="58" r="3" fill="#BFBFBF"/>
  <circle cx="260" cy="85" r="3" fill="#BFBFBF"/>
  <circle cx="360" cy="110" r="3" fill="#BFBFBF"/>
  <circle cx="460" cy="128" r="3" fill="#BFBFBF"/>
  <text x="410" y="122" style="font:600 10px Inter,sans-serif;fill:#888888;">Q3 cohort</text>

  <!-- Q4 cohort (pink, worst) -->
  <polyline points="60,10 160,75 260,115 360,150" fill="none" stroke="#FF00FF" stroke-width="2.5"/>
  <circle cx="60" cy="10" r="3.5" fill="#FF00FF"/>
  <circle cx="160" cy="75" r="3.5" fill="#FF00FF"/>
  <circle cx="260" cy="115" r="3.5" fill="#FF00FF"/>
  <circle cx="360" cy="150" r="3.5" fill="#FF00FF"/>
  <text x="310" y="145" style="font:700 10px Inter,sans-serif;fill:#FF00FF;">Q4 cohort</text>
</svg>
</div>

<p style="margin-top:0.7rem;font-size:0.95rem;color:#1A1A1A;line-height:1.45;">Each new cohort retains <span class="pink">worse</span> than the previous one. Rolling 30d churn missed this because the larger Q4 acquisition inflated the denominator. The product is getting worse, the headline number says otherwise.</p>

<!--
Cohort retention curves on the same paying base from the previous slide.

Reading the chart:
- Each line is one acquisition cohort starting at M0 (sign-up month) at 100%
- Q1 cohort retains well, ~68% at M6
- Q2 worse, Q3 worse, Q4 (pink, newest) worst — ~60% at M3 and still falling

Pedagogical point:
- Previous slide rolling churn looked fine because the recent Q4 cohort was large and most of it hadn't churned yet → inflated the denominator
- Cohort cut exposes the truth: each new cohort retains worse than the previous
- Rolling churn lied. Cohort retention curves tell the real story
- This is the canonical example of why product analysts cut by cohort instead of trusting rolling aggregates

Bridge to Session 12: full mechanics (cohort tables, heatmaps, LTV) covered there. This slide is the preview.
-->

---

# Cohorts

<p style="color:#1A1A1A;font-size:1.1rem;margin-top:0.4rem;line-height:1.5;">A way to look at users acquired in different periods, all at one moment in time.</p>

<div style="display:flex;justify-content:center;margin-top:1rem;">
  <img src="/cohort-retention-table.png" alt="Weekly cohort retention table — new users by sign-up week, retention by week since acquisition" style="max-width:100%;max-height:16rem;object-fit:contain;display:block;" />
</div>

<!--
Cohort table example. Each row is one acquisition cohort (new users signed up in that week). Each column is weeks since acquisition. The cell is retention %.

Reading the table:
- Horizontally: how one cohort's retention decays over weeks since they signed up
- Vertically: how user acquisition or product changes show up at the same week-N point across cohorts (does week-1 retention look different in June vs August?)
- The diagonal staircase: newer cohorts haven't had time to be observed at later weeks

Bridge to next slide: cohort tables expose what rolling aggregates hide. Rolling-churn case follows.
-->

---
layout: section
class: tint-mint
---

## 11

# Product cases

---

# Feature funnel: YouTube offline downloads

<p style="color:#1A1A1A;font-size:1.15rem;margin-top:0.6rem;line-height:1.5;">Free user taps <span class="pink">Download</span> on a video. What metrics would you track at each funnel stage for this feature?</p>

<div style="display:grid;grid-template-columns:1.2fr 0.8fr;gap:1.8rem;margin-top:0.9rem;align-items:start;">

  <div v-click style="display:flex;flex-direction:column;gap:0.6rem;">
    <div style="display:grid;grid-template-columns:9rem 1fr;gap:1rem;align-items:baseline;">
      <span style="font-weight:800;font-size:0.95rem;">Acquisition</span>
      <span style="font-size:0.9rem;color:#1A1A1A;">Free users who saw the Download button on a video</span>
    </div>
    <div style="display:grid;grid-template-columns:9rem 1fr;gap:1rem;align-items:baseline;">
      <span style="font-weight:800;font-size:0.95rem;">Setup</span>
      <span style="font-size:0.9rem;color:#1A1A1A;">Tapped Download, hit the Premium paywall, started the trial</span>
    </div>
    <div style="display:grid;grid-template-columns:9rem 1fr;gap:1rem;align-items:baseline;">
      <span style="font-weight:800;font-size:0.95rem;">Aha</span>
      <span style="font-size:0.9rem;color:#1A1A1A;">Completed first offline playback (full video without network)</span>
    </div>
    <div style="display:grid;grid-template-columns:9rem 1fr;gap:1rem;align-items:baseline;">
      <span style="font-weight:800;font-size:0.95rem;">Retention</span>
      <span style="font-size:0.9rem;color:#1A1A1A;">Played another offline video within 30 days</span>
    </div>
    <div style="display:grid;grid-template-columns:9rem 1fr;gap:1rem;align-items:baseline;">
      <span style="font-weight:800;font-size:0.95rem;">Revenue</span>
      <span style="font-size:0.9rem;color:#1A1A1A;">Trial converted to paid Premium</span>
    </div>
  </div>

  <div style="display:flex;align-items:flex-start;justify-content:center;margin-top:-2.5rem;">
    <img src="/youtube-premium-paywall.jpg" alt="YouTube Premium paywall after tapping Download" style="max-width:100%;max-height:18rem;object-fit:contain;display:block;border:1px solid #E0E0E0;" />
  </div>

</div>

<!--
Notion AI slide follows as a contrast case: paywall sits AFTER value (free quota then upgrade) versus YouTube where paywall sits BEFORE value (download click then upgrade prompt).
-->

---

# Notion AI

<div style="display:grid;grid-template-columns:1fr 1fr;gap:3rem;margin-top:1.5rem;align-items:start;">

  <div style="display:flex;flex-direction:column;align-items:center;gap:0.8rem;">
    <img src="/notion-ai-entry.png" alt="Notion AI entry — Chat about this page button" style="max-width:100%;max-height:8rem;object-fit:contain;display:block;border:1px solid #E0E0E0;" />
    <p style="font-family:'JetBrains Mono',monospace;font-size:0.72rem;color:#AAAAAA;letter-spacing:0.12em;text-transform:uppercase;margin:0;">Entry point</p>
  </div>

  <div style="display:flex;flex-direction:column;align-items:center;gap:0.8rem;">
    <img src="/notion-ai-panel.png" alt="Notion AI interface — How can I help you today" style="max-width:100%;max-height:18rem;object-fit:contain;display:block;border:1px solid #E0E0E0;" />
    <p style="font-family:'JetBrains Mono',monospace;font-size:0.72rem;color:#AAAAAA;letter-spacing:0.12em;text-transform:uppercase;margin:0;">Interface</p>
  </div>

</div>

<!--
Notion AI feature funnel. Same 5-stage pattern as YouTube offline, different paywall geometry.

Where the paywall sits:
- YouTube: paywall BEFORE value (click Download → must subscribe before any offline playback works)
- Notion AI: paywall AFTER value (free quota lets users experience AI, then hits cap)
- Pedagogical point: paywall placement changes which stage owns the conversion. YouTube's Setup IS the paywall; Notion's Revenue stage is the paywall

Stage definitions to discuss:
- Acquisition: exposed-to-feature audience (saw the toolbar button, not yet clicked)
- Setup: clicked button, panel opened — first deliberate engagement, no commitment yet
- Aha: kept the generation (not discarded/regenerated). The "kept" signal filters out users who tried AI but didn't find value
- Retention: returning to AI on a different page validates AI as a habit, not a curiosity
- Revenue: free quota cap forces the upgrade decision after value has been demonstrated

Reveal order (single v-click): all 5 metrics appear together after students propose their own.

YouTube slide (previous) speaker beats:
- Whole-product funnel was acquisition → activation → retention → revenue at the app level. Same shape exists per feature.
- YouTube offline download paywall sits between Setup and Aha: free users see the button, tapping forces a Premium decision, first successful offline playback is the Aha, returning to play offline again is Retention, and trial → paid is Revenue.
- Useful follow-up after reveal: which stage would you optimize first if conversion is the goal? Answer hinges on where the biggest drop in the funnel is. Data, not opinion.
-->

---

# Manychat IG comment automation

<div style="display:grid;grid-template-columns:1.05fr 0.95fr;gap:1.6rem;margin-top:0.5rem;align-items:start;">

  <div style="display:flex;flex-direction:column;gap:0.8rem;">
    <p style="color:#1A1A1A;font-size:1.05rem;line-height:1.5;margin:0;">A no-code automation tool. The creator picks an Instagram post, a trigger word in comments, and a DM that goes back when the trigger fires.</p>
    <p style="color:#1A1A1A;font-size:1.45rem;font-weight:800;margin-top:1.4rem;line-height:1.35;">What metrics would you <span class="pink">track</span> here?</p>
  </div>

  <div style="display:flex;justify-content:center;">
    <img src="/manychat-ig-automation.png" alt="Manychat automation builder for Instagram comments" style="max-width:100%;max-height:22rem;object-fit:contain;display:block;border:1px solid #E0E0E0;" />
  </div>

</div>

<!--
Open discussion. Tim works at Manychat and has direct context on this feature.

Angles to surface:
- Adoption: creators using IG automation, automations created, automations going live (Go Live click)
- Activation: time from sign-up to first published automation, % of new creators with at least one live automation in week 1
- Quality / matching: trigger-fire rate, comment-to-DM delivery success, false positives (irrelevant comments triggering a DM)
- Receiving side: open rate of triggered DMs, response rate, conversion to creator's funnel goal
- Anti-spam guardrails: complaint rate from end-users, Instagram platform policy violations, account flag rate
- Goodhart watch: automation count is easy to game (creators making ten useless rules); quality and revenue from automations are what actually matter
- Revenue link: do creators who set up automations retain better, upgrade to higher Manychat tiers
-->

---

# Traps in engagement metrics

<div style="position:absolute;top:52%;left:50%;transform:translate(-50%,-50%);width:90%;max-width:54rem;display:flex;flex-direction:column;gap:1.5rem;">
  <div style="display:flex;gap:1.2rem;align-items:baseline;">
    <span style="font-family:'JetBrains Mono',monospace;font-size:1rem;color:#AAAAAA;flex-shrink:0;width:2rem;">01</span>
    <span style="font-size:1.3rem;">What can cause DAU to drop?</span>
  </div>
  <div style="display:flex;gap:1.2rem;align-items:baseline;">
    <span style="font-family:'JetBrains Mono',monospace;font-size:1rem;color:#AAAAAA;flex-shrink:0;width:2rem;">02</span>
    <span style="font-size:1.3rem;">If a feature is used rarely, should you delete it?</span>
  </div>
  <div style="display:flex;gap:1.2rem;align-items:baseline;">
    <span style="font-family:'JetBrains Mono',monospace;font-size:1rem;color:#AAAAAA;flex-shrink:0;width:2rem;">03</span>
    <span style="font-size:1.3rem;">If time spent in the app is rising, is that always better?</span>
  </div>
</div>

<div style="position:absolute;bottom:1.5rem;left:3.5rem;font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#AAAAAA;letter-spacing:0.1em;text-transform:uppercase;">
  <a href="https://medium.com/pinterest-engineering/the-quest-to-understand-metric-movements-8ab12ae97cda" target="_blank" style="color:inherit;text-decoration:none;">pinterest engineering / the quest to understand metric movements</a>
</div>

<!--
Three misconception-testing questions for class discussion. Each tests an assumption students often bring in:

01 DAU drop causes — possibilities to surface:
- Seasonality, holidays, weather
- Tracking bug or push notifications stopped firing
- A traffic-source change (paid acquisition cut)
- An actual product issue (often the last assumption to check, not the first)
Lesson: a metric move is a signal, not a verdict.

02 Rare-feature deletion — angles to consider before cutting:
- Used by a small but high-value cohort? Deleting hurts retention there.
- Used as a setup step on a path to a high-impact action?
- Critical for accessibility or compliance?
Lesson: low usage by count is not the same as low value. Check the cohort and the path.

03 Time-spent always good — depends on the product's job:
- TikTok, Reels: yes by their model
- Productivity tools (Slack, Notion, Linear): NO. Time spent up may mean people are stuck or distracted, not productive.
- Banking, Booking: NO. Users want to finish and leave.
Lesson: time-spent only signals value when engagement IS the product's job. For utility products, time-spent up can mean things are getting worse.
-->

---

# Killing the web platform

<p style="color:#1A1A1A;font-size:1.2rem;margin-top:1rem;line-height:1.5;">The team proposes to stop developing the web product entirely. Cut the platform, focus engineering on mobile only, save the cost.</p>

<p style="color:#1A1A1A;font-size:1.45rem;font-weight:800;margin-top:1.6rem;line-height:1.4;">What metrics would you <span class="pink">track</span> to decide whether this is safe?</p>

<!--
Open class discussion. Single scenario, students propose the metric set.

Angles to surface:
- Share of users who are web-only vs. mobile-only vs. cross-platform (the most important segment cut)
- For web-only users: what is their LTV, retention curve, monetization profile? Will they migrate or churn?
- Cross-platform users: do they use web for distinct jobs (longer-form work, admin tasks, exports)?
- Acquisition: which channels convert better to web? SEO traffic landing on web vs paid mobile installs.
- Engagement: retention curves per platform, sessions per platform, feature usage per platform.
- Revenue: ARPU per platform, payment method differences (web often has better card economics than app store fees).
- Guardrails: support volume after migration, refund rate, churn spike in the first 30/60 days post-shutdown.
- Cost side: what does "saving the cost" actually mean? Engineering FTE freed up, hosting, design QA — and against that the LTV at risk.

Generalized pattern after discussion: any platform / surface / channel cut requires segmenting users by where they actually live, valuing each segment, then estimating migration vs. churn. The decision is rarely "shut it off." It is usually "what fraction migrates, at what cost, vs. the engineering savings."
-->

---

# Uber driver payouts

<p style="color:#1A1A1A;font-size:1.2rem;margin-top:1rem;line-height:1.5;">We're moving driver payouts from weekly to anytime, in exchange for a small commission.</p>

<p style="color:#1A1A1A;font-size:1.55rem;font-weight:800;margin-top:1.8rem;line-height:1.35;"><span class="pink">Good</span> initiative or bad one?</p>

<!--
Closing applied exercise. Real interview case Tim was asked at Uber.

Open discussion. No reveal slide. Students propose metrics, Tim moderates.

Angles to surface when students stay narrow:
- Driver-side: adoption % using anytime, frequency per driver, take-home pay change, retention
- Marketplace supply: does faster cash flow attract more part-time drivers or destabilise supply
- Business: commission revenue, cannibalization of weekly payouts, opportunity cost vs other initiatives
- Rider-side guardrails: ride availability, surge frequency, cancellation rate
- Goodhart watch: optimising for anytime-payout adoption could push the team to nudge drivers in ways that hurt overall driver economics

The two-sided marketplace nature is the move. Most students start on one side. Surface the other.
-->

---
layout: section
class: tint-rose
---

## 12

# Trade-offs and<br>failure modes

---

# Every framework can be gamed

<div style="margin-top:1rem;padding:1rem 1.4rem;border-left:3px solid #1A1A1A;">
  <div style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.12em;color:#FF00FF;margin-bottom:0.4rem;">Goodhart's Law · 1975</div>
  <p style="font-size:1.1rem;font-weight:600;margin:0;line-height:1.4;">When a measure becomes a target, it ceases to be a good measure.</p>
</div>

<div style="margin-top:1.3rem;">
  <div style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.12em;color:#AAAAAA;margin-bottom:0.4rem;">Example · AI adoption</div>
  <p style="font-size:1.05rem;color:#1A1A1A;line-height:1.5;margin:0;">Companies track <strong>tokens consumed</strong> as a proxy for how fast their employees adopt AI tools. Employees worried about being replaced start <span class="pink">burning tokens</span> on synthetic queries. The metric goes up. Actual adoption does not.</p>
</div>

<div style="margin-top:1.1rem;">
  <div style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.12em;color:#AAAAAA;margin-bottom:0.4rem;">Example · 2008 financial crisis</div>
  <p style="font-size:1.05rem;color:#1A1A1A;line-height:1.5;margin:0;">Banks had elaborate systems measuring how many loans got sold, and how fast. Loan volume kept rising. The risk those loans carried was not being measured. Many of them turned out far worse than anyone realised.</p>
</div>

<a href="https://theconversation.com/silicon-valleys-ai-tokenmaxxing-obsession-has-a-big-problem-and-philosophers-saw-it-coming-281530" target="_blank" style="display:inline-block;margin-top:1rem;font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#AAAAAA;text-transform:uppercase;letter-spacing:0.12em;text-decoration:none;">theconversation.com / silicon valley's ai tokenmaxxing obsession</a>

<!--
Tim's example, his observation about AI-adoption metrics in industry circa 2026. Classic Goodhart in action: a measure (token consumption) intended to proxy adoption becomes the target, and behavior adapts to game it. The metric loses its information value about the underlying thing it was supposed to measure.

Other angles to bring verbally:
- Soviet nail factory (counted by weight → giant useless nails; counted by quantity → tiny useless nails)
- Tyranny of Metrics (Muller, 2018) — broader critique
- Cargo cult: copying metrics without the mechanism
- Closing question: which framework we covered is most susceptible to Goodhart? Answer: all of them
-->

---

# Or the metric gets read <span class="pink">wrong</span>

<div style="margin-top:1.3rem;">
  <div style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.12em;color:#AAAAAA;margin-bottom:0.5rem;">Example · Manychat, revenue retention</div>
  <p style="font-size:1.1rem;color:#1A1A1A;line-height:1.55;margin:0;">The stakeholder default was that higher revenue retention is better, so the team should optimize for revenue retention. For big B2B SaaS this is real, revenue retention is genuinely critical. But high revenue retention does not guarantee revenue growth, does not maximize LTV, and does not mean the team is earning the most it could.</p>
  <p style="font-size:1.1rem;color:#1A1A1A;line-height:1.55;margin-top:0.7rem;">The metric is fine. The interpretation pushed the team toward a wrong target.</p>
</div>

<!--
Tim's own example from Manychat. A different failure mode from Goodhart-style gaming on the previous slide: here the metric is not gamed, it is misinterpreted by stakeholders who treat it as the optimization target when it is one signal among several.

Speaker beats:
- Set up the stakeholder position: "higher revenue retention is better, full stop"
- Explain why the position is defensible at first glance: large B2B SaaS literature does emphasize NRR / GRR heavily, and for high-ARPU enterprise contracts it really is critical
- Explain the failure: revenue retention measures "did the existing customers keep paying" — it does not measure new revenue, expansion, top-of-funnel, or LTV optimization
- Tim's pushback at Manychat: showed counter-examples where a team could have flat retention and still be leaving significant money on the table — and where chasing retention would have hurt the funnel
- Generalizable lesson: a metric can be analytically correct and still get applied to the wrong decision. Catching that is part of the analyst's job
- Bridge to vanity / cargo cult (next slides): both are about choosing the wrong metric in the first place, rather than misusing a correct one
-->

---

# Vanity metrics

<p style="font-size:1.2rem;line-height:1.55;color:#1A1A1A;margin-top:0.8rem;"><span class="pink">Vanity metrics</span> make you look good to others but do not help you understand your own performance in a way that informs future strategies.</p>

<p style="font-size:1.1rem;line-height:1.55;color:#1A1A1A;margin-top:1.2rem;">Common ones: total registered users, page views, app downloads, social followers, raw event counts. They grow on their own. They don't tell you what to do next.</p>

<div style="position:absolute;bottom:1rem;left:3.5rem;font-family:'JetBrains Mono',monospace;font-size:0.65rem;color:#AAAAAA;letter-spacing:0.1em;text-transform:uppercase;">
  <a href="https://www.statsig.com/perspectives/vanity-metrics-trap-product-analytics-insights" target="_blank" style="color:inherit;text-decoration:none;">statsig.com / vanity metrics trap in product analytics</a>
</div>

<!--
Moved from Section 02. Sits better here as a fourth failure mode after Goodhart, misread, and before cargo cult.

Speaker beats:
- A vanity metric is one you can show off but cannot act on
- Test from Croll & Yoskovitz: "what will I do differently based on this number?" If the answer is nothing — vanity
- Common offenders: total registered users (cumulative, only goes up), page views (no quality signal), social followers (gameable), app downloads (counts installs, not value)
- Tim's own examples: come in here verbally
- Connects to cargo cult (next slide): teams pick vanity metrics because they SOUND like what other companies report. Cargo cult is the upstream cause; vanity is the downstream symptom.
-->

---

# Cargo cult metrics

<p style="color:#1A1A1A;font-size:1.2rem;margin-top:1rem;line-height:1.55;">A result from Netflix, a post about Uber, or a sharp framework from LinkedIn says nothing about whether the pattern transfers to your product, your problem, your situation. Surface similarity between two products rarely implies the underlying mechanism is the same.</p>

<p style="color:#1A1A1A;font-size:1.45rem;font-weight:800;margin-top:1.8rem;line-height:1.35;">Before reusing a pattern, ask why it <span class="pink">worked there</span> and whether the same mechanism exists here.</p>

<div style="position:absolute;bottom:1.5rem;left:3.5rem;font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#AAAAAA;letter-spacing:0.1em;text-transform:uppercase;display:flex;flex-direction:column;gap:0.25rem;">
  <a href="https://debrouwere.org/2013/08/26/cargo-cult-analytics/" target="_blank" style="color:inherit;text-decoration:none;">debrouwere.org / cargo cult analytics</a>
  <a href="https://fs.blog/first-principles/" target="_blank" style="color:inherit;text-decoration:none;">fs.blog / first principles</a>
</div>

<!--
Third failure mode in this section. The first was Goodhart (the metric gets gamed). The second was misinterpretation (the metric is fine, the inference is wrong). This is the third: the metric is fine, the inference is fine, but the metric was lifted from another company whose product, market, stage, or growth model differs in a way that breaks the borrowed conclusion.

Original phrase comes from Feynman's 1974 Caltech speech "Cargo Cult Science" — Pacific islanders built fake airstrips and control towers after the war hoping the planes (and the cargo) would come back. The form looks right but the mechanism is missing, so nothing happens.

Tim's framing:
- A pattern that worked at Netflix, an Uber engineering post, a LinkedIn case study says nothing about your product
- Even when the products look close, the constraints, stage, market, growth model, or team capacity rarely transfer cleanly
- Reusing without checking the mechanism is dangerous, this is how teams pick the wrong NSM, the wrong activation event, the wrong retention window
- The corrective is to ask why the original metric worked there, and whether that same reason holds in this product
- Bridges into the closing thesis: frameworks are starting points, the "why" is the only filter that survives
-->

---

# Frameworks are starting points

<p style="color:#1A1A1A;font-size:1.2rem;margin-top:1rem;line-height:1.55;">They save you the cold start by borrowing what other teams figured out. The borrowed structure still has to be tested against your product, and other companies' choices are not a guarantee that any of it will work for yours.</p>

<p style="color:#1A1A1A;font-size:1.55rem;font-weight:800;margin-top:2rem;line-height:1.35;">Always ask: <span class="pink">why</span> am I doing this?</p>

<!--
Closing thesis for the whole deck. Tim's framing: don't cargo-cult. Frameworks are inspiration drawn from other teams to skip the blank-page problem, but they are baselines, not guarantees. The only filter that tells you whether a borrowed pattern actually fits your product is rational scrutiny on every choice. First principles.

Speaker beats:
- Cargo cult is the failure mode. Copying a metric or a framework from a big company because they used it does not mean it works for your product.
- Frameworks exist precisely because cold-starting from zero is expensive. Use them as a jump-off, not as gospel.
- The discipline is to keep asking why on every choice. Why this metric? Why this framework? Why now? Why not a different one?
- This is the only takeaway that survives the rest of the course's instrumentation collapsing into obsolescence.
-->

---

# Materials

<div style="display:grid;grid-template-columns:1fr 1fr;gap:2rem;margin-top:1rem;">

<div style="display:flex;flex-direction:column;gap:1rem;">

  <div>
    <div style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.12em;color:#FF00FF;margin-bottom:0.35rem;">North Star Metric &amp; OMTM</div>
    <div style="display:flex;flex-direction:column;gap:0.15rem;">
      <a href="https://amplitude.com/books/north-star/about-the-north-star-framework" target="_blank" style="font-family:'JetBrains Mono',monospace;font-size:0.65rem;color:#1A1A1A;text-transform:uppercase;letter-spacing:0.1em;text-decoration:none;">amplitude.com / books / north-star</a>
      <a href="https://www.lennysnewsletter.com/p/choosing-your-north-star-metric" target="_blank" style="font-family:'JetBrains Mono',monospace;font-size:0.65rem;color:#1A1A1A;text-transform:uppercase;letter-spacing:0.1em;text-decoration:none;">lennysnewsletter.com / choosing your north star metric</a>
      <a href="https://gopractice.io/product/the-product-managers-guide-to-north-star-metrics/" target="_blank" style="font-family:'JetBrains Mono',monospace;font-size:0.65rem;color:#1A1A1A;text-transform:uppercase;letter-spacing:0.1em;text-decoration:none;">gopractice.io / north star metrics guide</a>
      <a href="https://leananalyticsbook.com/one-metric-that-matters/" target="_blank" style="font-family:'JetBrains Mono',monospace;font-size:0.65rem;color:#1A1A1A;text-transform:uppercase;letter-spacing:0.1em;text-decoration:none;">leananalyticsbook.com / one metric that matters</a>
    </div>
  </div>

  <div>
    <div style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.12em;color:#FF00FF;margin-bottom:0.35rem;">Critique of NSM</div>
    <div style="display:flex;flex-direction:column;gap:0.15rem;">
      <a href="https://www.reforge.com/blog/north-star-metric-growth" target="_blank" style="font-family:'JetBrains Mono',monospace;font-size:0.65rem;color:#1A1A1A;text-transform:uppercase;letter-spacing:0.1em;text-decoration:none;">reforge.com / north star metric deceive you</a>
      <a href="https://hbsp.harvard.edu/product/H05LYD-PDF-ENG" target="_blank" style="font-family:'JetBrains Mono',monospace;font-size:0.65rem;color:#1A1A1A;text-transform:uppercase;letter-spacing:0.1em;text-decoration:none;">hbsp.harvard.edu / single metric drive your business</a>
    </div>
  </div>

  <div>
    <div style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.12em;color:#FF00FF;margin-bottom:0.35rem;">"Best product wins" critique</div>
    <div style="display:flex;flex-direction:column;gap:0.15rem;">
      <a href="https://www.reforge.com/blog/retention-engagement-growth-silent-killer" target="_blank" style="font-family:'JetBrains Mono',monospace;font-size:0.65rem;color:#1A1A1A;text-transform:uppercase;letter-spacing:0.1em;text-decoration:none;">reforge.com / retention is the silent killer</a>
    </div>
  </div>

</div>

<div style="display:flex;flex-direction:column;gap:1rem;">

  <div>
    <div style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.12em;color:#FF00FF;margin-bottom:0.35rem;">Funnels &amp; growth loops</div>
    <div style="display:flex;flex-direction:column;gap:0.15rem;">
      <a href="https://www.slideshare.net/dmc500hats/startup-metrics-for-pirates-long-version" target="_blank" style="font-family:'JetBrains Mono',monospace;font-size:0.65rem;color:#1A1A1A;text-transform:uppercase;letter-spacing:0.1em;text-decoration:none;">slideshare.net / mcclure / startup metrics for pirates</a>
      <a href="https://www.reforge.com/blog/growth-loops" target="_blank" style="font-family:'JetBrains Mono',monospace;font-size:0.65rem;color:#1A1A1A;text-transform:uppercase;letter-spacing:0.1em;text-decoration:none;">reforge.com / growth loops are the new funnels</a>
    </div>
  </div>

  <div>
    <div style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.12em;color:#FF00FF;margin-bottom:0.35rem;">Goodhart, cargo cult &amp; token-maxing</div>
    <div style="display:flex;flex-direction:column;gap:0.15rem;">
      <a href="https://theconversation.com/silicon-valleys-ai-tokenmaxxing-obsession-has-a-big-problem-and-philosophers-saw-it-coming-281530" target="_blank" style="font-family:'JetBrains Mono',monospace;font-size:0.65rem;color:#1A1A1A;text-transform:uppercase;letter-spacing:0.1em;text-decoration:none;">theconversation.com / ai tokenmaxxing obsession</a>
      <a href="https://calteches.library.caltech.edu/3043/1/CargoCult.pdf" target="_blank" style="font-family:'JetBrains Mono',monospace;font-size:0.65rem;color:#1A1A1A;text-transform:uppercase;letter-spacing:0.1em;text-decoration:none;">caltech.edu / feynman / cargo cult science (1974)</a>
      <a href="https://debrouwere.org/2013/08/26/cargo-cult-analytics/" target="_blank" style="font-family:'JetBrains Mono',monospace;font-size:0.65rem;color:#1A1A1A;text-transform:uppercase;letter-spacing:0.1em;text-decoration:none;">debrouwere.org / cargo cult analytics (2013)</a>
      <a href="https://fs.blog/first-principles/" target="_blank" style="font-family:'JetBrains Mono',monospace;font-size:0.65rem;color:#1A1A1A;text-transform:uppercase;letter-spacing:0.1em;text-decoration:none;">fs.blog / first principles</a>
    </div>
  </div>

  <div>
    <div style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.12em;color:#FF00FF;margin-bottom:0.35rem;">HEART · Google UX paper</div>
    <div style="display:flex;flex-direction:column;gap:0.15rem;">
      <a href="https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/36299.pdf" target="_blank" style="font-family:'JetBrains Mono',monospace;font-size:0.65rem;color:#1A1A1A;text-transform:uppercase;letter-spacing:0.1em;text-decoration:none;">research.google / heart framework (rodden et al., 2010)</a>
    </div>
  </div>

</div>

</div>

<!--
Closing materials slide. Reorganized by TOPIC (not by Books/Frameworks/Articles) per Tim's call. Only links relevant to THIS lecture — textbooks (Lean Analytics, Kohavi, Tyranny of Metrics) dropped because they belong with later lectures (A/B testing, deeper metrics critique) and would dilute the focus here.

Topic blocks chosen to match the deck's argument flow:
- NSM canon (Sean Ellis lineage)
- Critique of NSM (Balfour, HBR)
- "Best product wins" critique (retention as silent killer pairs with slide 22-24)
- Funnels & growth loops (AARRR origin + Reforge critique)
- Goodhart, cargo cult & token-maxing (slide 52 + closing thesis)
- HEART as standalone link (per Tim's call: include Google original)

Cargo cult article defaults to Feynman's Caltech 1974 "Cargo Cult Science" speech — the canonical reference. Tim may have a different article in mind; ask on review.

Reforge links use reforge.com/blog/* (public). HBR link is the hbsp.harvard.edu product page — public preview, full paywalled. Academic citation pattern.

Students photograph this slide at end of class.
-->

---
layout: section
class: tint-cream
---

## Appendix

# Practice

---
layout: statement
---

<h1 style="font-size:2.6rem;line-height:1.2;margin-bottom:2.5rem;">Imagine you're CPO at Spotify.<br>Which metrics would you track?</h1>

<img src="/spotify.png" style="width:110px;margin:0 auto;display:block;" />

<!--
Appendix copy of slide 23. Used at end of class if there is time after all frameworks have been covered. Students now have the full vocabulary (AARRR, NSM, metric tree, leading vs lagging, granularity, trade-offs) and can produce a richer answer than the first time around.
-->



