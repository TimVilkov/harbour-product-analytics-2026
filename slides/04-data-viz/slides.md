---
theme: apple-basic
title: "Session 04: Data Visualisation"
info: "Product Analytics · Harbour.Space · 2026"
highlighter: shiki
drawings:
  persist: false
transition: fade
mdc: true
layout: intro
---

# Data <span class="pink">Visualisation</span>

<div class="absolute bottom-10 left-14" style="font-family:'JetBrains Mono',monospace;font-size:0.75rem;text-transform:uppercase;letter-spacing:0.15em;color:rgba(255,255,255,0.55);">
  Harbour.Space &middot; Barcelona &middot; May 21, 2026
</div>

---

# Today

<div style="display:flex;flex-direction:column;gap:0.9rem;margin-top:1rem;">

  <div style="display:grid;grid-template-columns:48px 1fr;gap:1.2rem;align-items:baseline;">
    <span style="font-family:'JetBrains Mono',monospace;font-size:0.95rem;color:#FF00FF;letter-spacing:0.1em;">01</span>
    <div style="font-size:1.3rem;font-weight:700;color:#1A1A1A;">Why a chart at all</div>
  </div>
  <div style="display:grid;grid-template-columns:48px 1fr;gap:1.2rem;align-items:baseline;">
    <span style="font-family:'JetBrains Mono',monospace;font-size:0.95rem;color:#FF00FF;letter-spacing:0.1em;">02</span>
    <div style="font-size:1.3rem;font-weight:700;color:#1A1A1A;">Question to chart</div>
  </div>
  <div style="display:grid;grid-template-columns:48px 1fr;gap:1.2rem;align-items:baseline;">
    <span style="font-family:'JetBrains Mono',monospace;font-size:0.95rem;color:#FF00FF;letter-spacing:0.1em;">03</span>
    <div style="font-size:1.3rem;font-weight:700;color:#1A1A1A;">Working with an LLM</div>
  </div>
  <div style="display:grid;grid-template-columns:48px 1fr;gap:1.2rem;align-items:baseline;">
    <span style="font-family:'JetBrains Mono',monospace;font-size:0.95rem;color:#FF00FF;letter-spacing:0.1em;">04</span>
    <div style="font-size:1.3rem;font-weight:700;color:#1A1A1A;">Dashboards</div>
  </div>
  <div style="display:grid;grid-template-columns:48px 1fr;gap:1.2rem;align-items:baseline;">
    <span style="font-family:'JetBrains Mono',monospace;font-size:0.95rem;color:#FF00FF;letter-spacing:0.1em;">05</span>
    <div style="font-size:1.3rem;font-weight:700;color:#1A1A1A;">Same numbers, different stories</div>
  </div>

</div>

---
layout: section
class: tint-lavender
---

## 01

# Why a chart<br>at all

---

# What is data visualization

<p style="font-size:1.3rem;color:#1A1A1A;margin:0 0 2.2rem;line-height:1.5;">The graphical representation of data for understanding and communication.</p>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:2rem;margin-top:0.4rem;">

  <div style="border-left:3px solid #FF00FF;padding:0.6rem 0 0.6rem 1.2rem;">
    <div style="font-family:'JetBrains Mono',monospace;font-size:0.72rem;color:#AAAAAA;letter-spacing:0.14em;text-transform:uppercase;margin-bottom:0.5rem;">Exploratory</div>
    <div style="font-size:1.1rem;color:#1A1A1A;line-height:1.45;">You are trying to explore and understand patterns and trends within your data</div>
  </div>

  <div style="border-left:3px solid #FF00FF;padding:0.6rem 0 0.6rem 1.2rem;">
    <div style="font-family:'JetBrains Mono',monospace;font-size:0.72rem;color:#AAAAAA;letter-spacing:0.14em;text-transform:uppercase;margin-bottom:0.5rem;">Explanatory</div>
    <div style="font-size:1.1rem;color:#1A1A1A;line-height:1.45;">There is something in your data you want to communicate to your audience</div>
  </div>

</div>

<p style="margin-top:2rem;font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#AAAAAA;letter-spacing:0.06em;">Source: guides.library.jhu.edu/datavisualization</p>


---

# What a chart needs to do

<p style="font-size:1.3rem;color:#1A1A1A;margin:0 0 2rem;line-height:1.5;">A chart needs to be readable, help the reader make a decision, and carry your idea across.</p>

<div style="margin-top:1.6rem;padding:1.2rem 1.4rem;border-left:3px solid #FF00FF;background:#FAFAFA;">
  <div style="font-family:'JetBrains Mono',monospace;font-size:0.72rem;color:#FF00FF;letter-spacing:0.14em;text-transform:uppercase;margin-bottom:0.5rem;">A different role</div>
  <div style="font-size:1.05rem;color:#1A1A1A;line-height:1.5;">BI developer and BI analyst are the people who build polished, scalable dashboards as the final product. That is a separate craft from product analytics.</div>
</div>

---

# Before the chart

<p style="font-size:1.25rem;color:#1A1A1A;margin:0 0 2.4rem;line-height:1.5;">Before drawing anything, know what question you are answering and what you want to learn from the answer.</p>

<div style="display:flex;flex-direction:column;gap:1.6rem;margin-top:0.6rem;">

  <div style="display:grid;grid-template-columns:170px 1fr;gap:1.2rem;align-items:baseline;border-bottom:1px solid #E0E0E0;padding-bottom:1.4rem;">
    <span style="font-family:'JetBrains Mono',monospace;font-size:0.85rem;color:#FF00FF;letter-spacing:0.14em;text-transform:uppercase;">Question</span>
    <div style="font-size:1.15rem;color:#1A1A1A;">what you are trying to learn from the data</div>
  </div>

  <div style="display:grid;grid-template-columns:170px 1fr;gap:1.2rem;align-items:baseline;">
    <span style="font-family:'JetBrains Mono',monospace;font-size:0.85rem;color:#FF00FF;letter-spacing:0.14em;text-transform:uppercase;">Goal</span>
    <div style="font-size:1.15rem;color:#1A1A1A;">what extra you want the chart to surface beyond the raw numbers</div>
  </div>

</div>

---
layout: section
class: tint-mint
---

## 02

# Question<br>to chart

---

# Did the metric move over time?

<div style="font-family:'JetBrains Mono',monospace;font-size:0.78rem;color:#FF00FF;letter-spacing:0.14em;text-transform:uppercase;margin:-0.4rem 0 0.6rem;">Line chart</div>

<div style="display:grid;grid-template-columns:1fr 2fr;gap:2rem;margin-top:0.2rem;align-items:start;">

  <div>
    <div style="font-family:'JetBrains Mono',monospace;font-size:0.72rem;color:#AAAAAA;letter-spacing:0.14em;text-transform:uppercase;margin-bottom:0.5rem;">Data</div>
    <table style="border-collapse:collapse;font-family:'JetBrains Mono',monospace;font-size:0.78rem;color:#1A1A1A;">
      <thead><tr style="background:#F5F5F5;">
        <th style="border:1px solid #1A1A1A;padding:0.35rem 0.8rem;text-align:left;font-weight:600;">date</th>
        <th style="border:1px solid #1A1A1A;padding:0.35rem 0.8rem;text-align:right;font-weight:600;">dau</th>
      </tr></thead>
      <tbody>
        <tr><td style="border:1px solid #1A1A1A;padding:0.3rem 0.8rem;">2026-01-01</td><td style="border:1px solid #1A1A1A;padding:0.3rem 0.8rem;text-align:right;">1240</td></tr>
        <tr><td style="border:1px solid #1A1A1A;padding:0.3rem 0.8rem;">2026-01-02</td><td style="border:1px solid #1A1A1A;padding:0.3rem 0.8rem;text-align:right;">1265</td></tr>
        <tr><td style="border:1px solid #1A1A1A;padding:0.3rem 0.8rem;">2026-01-03</td><td style="border:1px solid #1A1A1A;padding:0.3rem 0.8rem;text-align:right;">1280</td></tr>
        <tr><td style="border:1px solid #1A1A1A;padding:0.3rem 0.8rem;">2026-01-04</td><td style="border:1px solid #1A1A1A;padding:0.3rem 0.8rem;text-align:right;">1252</td></tr>
        <tr><td style="border:1px solid #1A1A1A;padding:0.3rem 0.8rem;color:#AAAAAA;">…</td><td style="border:1px solid #1A1A1A;padding:0.3rem 0.8rem;text-align:right;color:#AAAAAA;">…</td></tr>
      </tbody>
    </table>
    <p style="font-family:'JetBrains Mono',monospace;font-size:0.65rem;color:#AAAAAA;margin-top:0.4rem;">90 rows</p>
  </div>

  <v-click>
    <iframe src="/charts/line-dau.html?v=1779373681" style="width:100%;height:300px;border:0;"></iframe>
  </v-click>

</div>

<p style="margin-top:0.6rem;font-size:0.95rem;color:#6B6B6B;">A line chart needs an honest x-axis and a y-axis range that matches the data</p>

---

# Same data, dishonest scale

<div style="font-family:'JetBrains Mono',monospace;font-size:0.78rem;color:#FF00FF;letter-spacing:0.14em;text-transform:uppercase;margin:-0.4rem 0 0.6rem;">Line chart</div>

<iframe src="/charts/line-dau-bad.html?v=1779373681" style="width:100%;height:330px;border:0;"></iframe>

<p style="margin-top:0.5rem;font-size:0.85rem;color:#6B6B6B;">A wider y-axis flattens the same series so the change becomes hard to see</p>

---

# A noisy series, before and after smoothing

<div style="font-family:'JetBrains Mono',monospace;font-size:0.78rem;color:#FF00FF;letter-spacing:0.14em;text-transform:uppercase;margin:-0.4rem 0 0.6rem;">Line chart</div>

<iframe src="/charts/line-smoothing.html?v=1779373681" style="width:100%;height:340px;border:0;"></iframe>

<p style="margin-top:0.5rem;font-size:0.85rem;color:#6B6B6B;">A rolling window helps the eye, with the window size chosen to match the question and not just to look clean</p>

---

# Which category is biggest?

<div style="font-family:'JetBrains Mono',monospace;font-size:0.78rem;color:#FF00FF;letter-spacing:0.14em;text-transform:uppercase;margin:-0.4rem 0 0.6rem;">Bar chart</div>

<div style="display:grid;grid-template-columns:1fr 2fr;gap:2rem;margin-top:0.2rem;align-items:start;">

  <div>
    <div style="font-family:'JetBrains Mono',monospace;font-size:0.72rem;color:#AAAAAA;letter-spacing:0.14em;text-transform:uppercase;margin-bottom:0.5rem;">Data</div>
    <table style="border-collapse:collapse;font-family:'JetBrains Mono',monospace;font-size:0.78rem;color:#1A1A1A;">
      <thead><tr style="background:#F5F5F5;">
        <th style="border:1px solid #1A1A1A;padding:0.35rem 0.8rem;text-align:left;font-weight:600;">country</th>
        <th style="border:1px solid #1A1A1A;padding:0.35rem 0.8rem;text-align:right;font-weight:600;">revenue</th>
      </tr></thead>
      <tbody>
        <tr><td style="border:1px solid #1A1A1A;padding:0.3rem 0.8rem;">US</td><td style="border:1px solid #1A1A1A;padding:0.3rem 0.8rem;text-align:right;">124k</td></tr>
        <tr><td style="border:1px solid #1A1A1A;padding:0.3rem 0.8rem;">BR</td><td style="border:1px solid #1A1A1A;padding:0.3rem 0.8rem;text-align:right;">88k</td></tr>
        <tr><td style="border:1px solid #1A1A1A;padding:0.3rem 0.8rem;">DE</td><td style="border:1px solid #1A1A1A;padding:0.3rem 0.8rem;text-align:right;">71k</td></tr>
        <tr><td style="border:1px solid #1A1A1A;padding:0.3rem 0.8rem;">ES</td><td style="border:1px solid #1A1A1A;padding:0.3rem 0.8rem;text-align:right;">64k</td></tr>
        <tr><td style="border:1px solid #1A1A1A;padding:0.3rem 0.8rem;color:#AAAAAA;">…</td><td style="border:1px solid #1A1A1A;padding:0.3rem 0.8rem;text-align:right;color:#AAAAAA;">…</td></tr>
      </tbody>
    </table>
    <p style="font-family:'JetBrains Mono',monospace;font-size:0.65rem;color:#AAAAAA;margin-top:0.4rem;">10 rows</p>
  </div>

  <v-click>
    <iframe src="/charts/bar-revenue.html?v=1779373681" style="width:100%;height:300px;border:0;"></iframe>
  </v-click>

</div>

<p style="margin-top:0.6rem;font-size:0.95rem;color:#6B6B6B;">A bar chart starts at zero and is sorted by value so the comparison reads honestly</p>

---

# Same data, sorted by name

<div style="font-family:'JetBrains Mono',monospace;font-size:0.78rem;color:#FF00FF;letter-spacing:0.14em;text-transform:uppercase;margin:-0.4rem 0 0.6rem;">Bar chart</div>

<iframe src="/charts/bar-revenue-bad.html?v=1779373681" style="width:100%;height:330px;border:0;"></iframe>

<p style="margin-top:0.5rem;font-size:0.85rem;color:#6B6B6B;">Alphabetical order and a different colour for every bar turn the comparison into a search task</p>

---

# One noisy category crushes the scale

<div style="font-family:'JetBrains Mono',monospace;font-size:0.78rem;color:#FF00FF;letter-spacing:0.14em;text-transform:uppercase;margin:-0.4rem 0 0.6rem;">Bar chart</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:1.5rem;margin-top:0.4rem;">

  <div>
    <div style="font-family:'JetBrains Mono',monospace;font-size:0.68rem;color:#AAAAAA;letter-spacing:0.14em;text-transform:uppercase;margin-bottom:0.3rem;">With outlier</div>
    <iframe src="/charts/bar-noisy.html?v=1779373681" style="width:100%;height:280px;border:0;"></iframe>
  </div>

  <v-click>
    <div>
      <div style="font-family:'JetBrains Mono',monospace;font-size:0.68rem;color:#FF00FF;letter-spacing:0.14em;text-transform:uppercase;margin-bottom:0.3rem;">After dropping it</div>
      <iframe src="/charts/bar-noisy-dropped.html?v=1779373681" style="width:100%;height:280px;border:0;"></iframe>
    </div>
  </v-click>

</div>

<p style="margin-top:0.4rem;font-size:0.85rem;color:#6B6B6B;">Decide upstream of the chart whether the outlier is the story or the noise that hides it</p>

---

# Revenue split by country and segment

<div style="font-family:'JetBrains Mono',monospace;font-size:0.78rem;color:#FF00FF;letter-spacing:0.14em;text-transform:uppercase;margin:-0.4rem 0 0.6rem;">Grouped bar chart</div>

<div style="display:grid;grid-template-columns:1fr 2fr;gap:2rem;margin-top:0.2rem;align-items:start;">

  <div>
    <div style="font-family:'JetBrains Mono',monospace;font-size:0.72rem;color:#AAAAAA;letter-spacing:0.14em;text-transform:uppercase;margin-bottom:0.5rem;">Data</div>
    <table style="border-collapse:collapse;font-family:'JetBrains Mono',monospace;font-size:0.72rem;color:#1A1A1A;">
      <thead><tr style="background:#F5F5F5;">
        <th style="border:1px solid #1A1A1A;padding:0.35rem 0.6rem;text-align:left;font-weight:600;">country</th>
        <th style="border:1px solid #1A1A1A;padding:0.35rem 0.6rem;text-align:left;font-weight:600;">plan</th>
        <th style="border:1px solid #1A1A1A;padding:0.35rem 0.6rem;text-align:right;font-weight:600;">revenue</th>
      </tr></thead>
      <tbody>
        <tr><td style="border:1px solid #1A1A1A;padding:0.3rem 0.6rem;">US</td><td style="border:1px solid #1A1A1A;padding:0.3rem 0.6rem;">starter</td><td style="border:1px solid #1A1A1A;padding:0.3rem 0.6rem;text-align:right;">24</td></tr>
        <tr><td style="border:1px solid #1A1A1A;padding:0.3rem 0.6rem;">US</td><td style="border:1px solid #1A1A1A;padding:0.3rem 0.6rem;">pro</td><td style="border:1px solid #1A1A1A;padding:0.3rem 0.6rem;text-align:right;">62</td></tr>
        <tr><td style="border:1px solid #1A1A1A;padding:0.3rem 0.6rem;">US</td><td style="border:1px solid #1A1A1A;padding:0.3rem 0.6rem;">enterprise</td><td style="border:1px solid #1A1A1A;padding:0.3rem 0.6rem;text-align:right;">38</td></tr>
        <tr><td style="border:1px solid #1A1A1A;padding:0.3rem 0.6rem;">BR</td><td style="border:1px solid #1A1A1A;padding:0.3rem 0.6rem;">starter</td><td style="border:1px solid #1A1A1A;padding:0.3rem 0.6rem;text-align:right;">38</td></tr>
        <tr><td style="border:1px solid #1A1A1A;padding:0.3rem 0.6rem;color:#AAAAAA;">…</td><td style="border:1px solid #1A1A1A;padding:0.3rem 0.6rem;color:#AAAAAA;">…</td><td style="border:1px solid #1A1A1A;padding:0.3rem 0.6rem;text-align:right;color:#AAAAAA;">…</td></tr>
      </tbody>
    </table>
    <p style="font-family:'JetBrains Mono',monospace;font-size:0.65rem;color:#AAAAAA;margin-top:0.4rem;">24 rows</p>
  </div>

  <v-click>
    <iframe src="/charts/bar-grouped.html?v=1779373681" style="width:100%;height:300px;border:0;"></iframe>
  </v-click>

</div>

<p style="margin-top:0.6rem;font-size:0.95rem;color:#6B6B6B;">Color carries information here and the legend belongs close to the data it labels</p>

---

# Same data, stacked into a total per country

<div style="font-family:'JetBrains Mono',monospace;font-size:0.78rem;color:#FF00FF;letter-spacing:0.14em;text-transform:uppercase;margin:-0.4rem 0 0.4rem;">Stacked bar chart</div>

<div style="display:grid;grid-template-columns:1fr 2fr;gap:2rem;margin-top:0.2rem;align-items:start;">

  <div>
    <div style="font-family:'JetBrains Mono',monospace;font-size:0.72rem;color:#AAAAAA;letter-spacing:0.14em;text-transform:uppercase;margin-bottom:0.5rem;">Data</div>
    <p style="font-family:'JetBrains Mono',monospace;font-size:0.78rem;color:#1A1A1A;">same as previous slide</p>
  </div>

  <v-click>
    <iframe src="/charts/bar-stacked.html?v=1779373681" style="width:100%;height:300px;border:0;"></iframe>
  </v-click>

</div>

<p style="margin-top:0.6rem;font-size:0.95rem;color:#6B6B6B;">A stacked bar gets hard to read past three or four segments and a different chart will land better at that point</p>

---

# How segments relate to each other inside the country

<div style="font-family:'JetBrains Mono',monospace;font-size:0.78rem;color:#FF00FF;letter-spacing:0.14em;text-transform:uppercase;margin:-0.4rem 0 0.6rem;">100% stacked bar chart</div>

<div style="display:grid;grid-template-columns:1fr 2fr;gap:2rem;margin-top:0.2rem;align-items:start;">

  <div>
    <div style="font-family:'JetBrains Mono',monospace;font-size:0.72rem;color:#AAAAAA;letter-spacing:0.14em;text-transform:uppercase;margin-bottom:0.5rem;">Data</div>
    <p style="font-family:'JetBrains Mono',monospace;font-size:0.78rem;color:#1A1A1A;">same data, normalised to share within each country</p>
  </div>

  <v-click>
    <iframe src="/charts/bar-100pct.html?v=1779373681" style="width:100%;height:300px;border:0;"></iframe>
  </v-click>

</div>

<p style="margin-top:0.6rem;font-size:0.95rem;color:#6B6B6B;">Normalising shows share but drops absolute scale, so both views belong on the page when scale is part of the story</p>

---

# Same chart, labels and highlight on top

<div style="font-family:'JetBrains Mono',monospace;font-size:0.78rem;color:#FF00FF;letter-spacing:0.14em;text-transform:uppercase;margin:-0.4rem 0 0.6rem;">100% stacked bar chart</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:1.5rem;margin-top:0.4rem;">

  <div>
    <div style="font-family:'JetBrains Mono',monospace;font-size:0.68rem;color:#AAAAAA;letter-spacing:0.14em;text-transform:uppercase;margin-bottom:0.3rem;">Bare</div>
    <iframe src="/charts/bar-100pct.html?v=1779373681" style="width:100%;height:300px;border:0;"></iframe>
  </div>

  <v-click>
    <div>
      <div style="font-family:'JetBrains Mono',monospace;font-size:0.68rem;color:#FF00FF;letter-spacing:0.14em;text-transform:uppercase;margin-bottom:0.3rem;">% printed inside each segment</div>
      <iframe src="/charts/bar-100pct-labeled.html?v=1779373681" style="width:100%;height:300px;border:0;"></iframe>
    </div>
  </v-click>

</div>

<p style="margin-top:0.4rem;font-size:0.85rem;color:#6B6B6B;">Numbers printed inside each segment mean the reader scans share without bouncing to the axis</p>

---

# How does each part contribute to the trend?

<div style="font-family:'JetBrains Mono',monospace;font-size:0.78rem;color:#FF00FF;letter-spacing:0.14em;text-transform:uppercase;margin:-0.4rem 0 0.6rem;">Stacked area chart</div>

<div style="display:grid;grid-template-columns:1fr 2fr;gap:2rem;margin-top:0.2rem;align-items:start;">

  <div>
    <div style="font-family:'JetBrains Mono',monospace;font-size:0.72rem;color:#AAAAAA;letter-spacing:0.14em;text-transform:uppercase;margin-bottom:0.5rem;">Data</div>
    <table style="border-collapse:collapse;font-family:'JetBrains Mono',monospace;font-size:0.74rem;color:#1A1A1A;">
      <thead><tr style="background:#F5F5F5;">
        <th style="border:1px solid #1A1A1A;padding:0.35rem 0.7rem;text-align:left;font-weight:600;">date</th>
        <th style="border:1px solid #1A1A1A;padding:0.35rem 0.7rem;text-align:left;font-weight:600;">channel</th>
        <th style="border:1px solid #1A1A1A;padding:0.35rem 0.7rem;text-align:right;font-weight:600;">signups</th>
      </tr></thead>
      <tbody>
        <tr><td style="border:1px solid #1A1A1A;padding:0.3rem 0.7rem;">2026-01-01</td><td style="border:1px solid #1A1A1A;padding:0.3rem 0.7rem;">organic</td><td style="border:1px solid #1A1A1A;padding:0.3rem 0.7rem;text-align:right;">412</td></tr>
        <tr><td style="border:1px solid #1A1A1A;padding:0.3rem 0.7rem;">2026-01-01</td><td style="border:1px solid #1A1A1A;padding:0.3rem 0.7rem;">paid</td><td style="border:1px solid #1A1A1A;padding:0.3rem 0.7rem;text-align:right;">180</td></tr>
        <tr><td style="border:1px solid #1A1A1A;padding:0.3rem 0.7rem;">2026-01-01</td><td style="border:1px solid #1A1A1A;padding:0.3rem 0.7rem;">referral</td><td style="border:1px solid #1A1A1A;padding:0.3rem 0.7rem;text-align:right;">95</td></tr>
        <tr><td style="border:1px solid #1A1A1A;padding:0.3rem 0.7rem;color:#AAAAAA;">…</td><td style="border:1px solid #1A1A1A;padding:0.3rem 0.7rem;color:#AAAAAA;">…</td><td style="border:1px solid #1A1A1A;padding:0.3rem 0.7rem;text-align:right;color:#AAAAAA;">…</td></tr>
      </tbody>
    </table>
  </div>

  <v-click>
    <iframe src="/charts/area-stacked.html?v=1779373681" style="width:100%;height:300px;border:0;"></iframe>
  </v-click>

</div>

<p style="margin-top:0.6rem;font-size:0.95rem;color:#6B6B6B;">Use area only when the parts genuinely add up to a meaningful whole</p>

---

# Legend on top of the data hides it

<div style="font-family:'JetBrains Mono',monospace;font-size:0.78rem;color:#FF00FF;letter-spacing:0.14em;text-transform:uppercase;margin:-0.4rem 0 0.6rem;">Line chart</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:1.5rem;margin-top:0.4rem;">

  <div>
    <div style="font-family:'JetBrains Mono',monospace;font-size:0.68rem;color:#AAAAAA;letter-spacing:0.14em;text-transform:uppercase;margin-bottom:0.3rem;">Legend covers the data</div>
    <iframe src="/charts/line-bad-legend.html?v=1779373681" style="width:100%;height:300px;border:0;"></iframe>
  </div>

  <v-click>
    <div>
      <div style="font-family:'JetBrains Mono',monospace;font-size:0.68rem;color:#FF00FF;letter-spacing:0.14em;text-transform:uppercase;margin-bottom:0.3rem;">Legend pulled outside</div>
      <iframe src="/charts/line-good-legend.html?v=1779373681" style="width:100%;height:300px;border:0;"></iframe>
    </div>
  </v-click>

</div>

<p style="margin-top:0.4rem;font-size:0.85rem;color:#6B6B6B;">Pull the legend outside the plot so the data keeps the space</p>

---

# What does the distribution look like?

<div style="font-family:'JetBrains Mono',monospace;font-size:0.78rem;color:#FF00FF;letter-spacing:0.14em;text-transform:uppercase;margin:-0.4rem 0 0.6rem;">Histogram</div>

<div style="display:grid;grid-template-columns:1fr 2fr;gap:2rem;margin-top:0.2rem;align-items:start;">

  <div>
    <div style="font-family:'JetBrains Mono',monospace;font-size:0.72rem;color:#AAAAAA;letter-spacing:0.14em;text-transform:uppercase;margin-bottom:0.5rem;">Data</div>
    <table style="border-collapse:collapse;font-family:'JetBrains Mono',monospace;font-size:0.78rem;color:#1A1A1A;">
      <thead><tr style="background:#F5F5F5;">
        <th style="border:1px solid #1A1A1A;padding:0.35rem 0.8rem;text-align:right;font-weight:600;">session_duration_sec</th>
      </tr></thead>
      <tbody>
        <tr><td style="border:1px solid #1A1A1A;padding:0.3rem 0.8rem;text-align:right;">12</td></tr>
        <tr><td style="border:1px solid #1A1A1A;padding:0.3rem 0.8rem;text-align:right;">45</td></tr>
        <tr><td style="border:1px solid #1A1A1A;padding:0.3rem 0.8rem;text-align:right;">78</td></tr>
        <tr><td style="border:1px solid #1A1A1A;padding:0.3rem 0.8rem;text-align:right;">102</td></tr>
        <tr><td style="border:1px solid #1A1A1A;padding:0.3rem 0.8rem;text-align:right;">410</td></tr>
        <tr><td style="border:1px solid #1A1A1A;padding:0.3rem 0.8rem;text-align:right;color:#AAAAAA;">…</td></tr>
      </tbody>
    </table>
    <p style="font-family:'JetBrains Mono',monospace;font-size:0.65rem;color:#AAAAAA;margin-top:0.4rem;">4 000 rows</p>
  </div>

  <v-click>
    <iframe src="/charts/histogram-sessions.html?v=1779373681" style="width:100%;height:300px;border:0;"></iframe>
  </v-click>

</div>

<p style="margin-top:0.6rem;font-size:0.95rem;color:#6B6B6B;">Bin count changes the shape of the story, so it is worth trying two or three before deciding</p>

---

# A second view of the distribution

<div style="font-family:'JetBrains Mono',monospace;font-size:0.78rem;color:#FF00FF;letter-spacing:0.14em;text-transform:uppercase;margin:-0.4rem 0 0.6rem;">Box plot · Violin plot</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:1.5rem;margin-top:0.4rem;">

  <div>
    <div style="font-family:'JetBrains Mono',monospace;font-size:0.68rem;color:#AAAAAA;letter-spacing:0.14em;text-transform:uppercase;margin-bottom:0.3rem;">Box plot</div>
    <iframe src="/charts/box-sessions.html?v=1779373681" style="width:100%;height:300px;border:0;"></iframe>
  </div>

  <v-click>
    <div>
      <div style="font-family:'JetBrains Mono',monospace;font-size:0.68rem;color:#FF00FF;letter-spacing:0.14em;text-transform:uppercase;margin-bottom:0.3rem;">Violin plot</div>
      <iframe src="/charts/violin-sessions.html?v=1779373681" style="width:100%;height:300px;border:0;"></iframe>
    </div>
  </v-click>

</div>

<p style="margin-top:0.4rem;font-size:0.85rem;color:#6B6B6B;">Box shows median, quartiles, outliers. Violin adds the shape, so multimodal segments stop hiding inside a single box</p>

---

# Are these two variables related?

<div style="font-family:'JetBrains Mono',monospace;font-size:0.78rem;color:#FF00FF;letter-spacing:0.14em;text-transform:uppercase;margin:-0.4rem 0 0.6rem;">Scatter plot</div>

<div style="display:grid;grid-template-columns:1fr 2fr;gap:2rem;margin-top:0.2rem;align-items:start;">

  <div>
    <div style="font-family:'JetBrains Mono',monospace;font-size:0.72rem;color:#AAAAAA;letter-spacing:0.14em;text-transform:uppercase;margin-bottom:0.5rem;">Data</div>
    <table style="border-collapse:collapse;font-family:'JetBrains Mono',monospace;font-size:0.72rem;color:#1A1A1A;">
      <thead><tr style="background:#F5F5F5;">
        <th style="border:1px solid #1A1A1A;padding:0.35rem 0.6rem;text-align:left;font-weight:600;">user_id</th>
        <th style="border:1px solid #1A1A1A;padding:0.35rem 0.6rem;text-align:right;font-weight:600;">sessions/wk</th>
        <th style="border:1px solid #1A1A1A;padding:0.35rem 0.6rem;text-align:right;font-weight:600;">revenue_30d</th>
      </tr></thead>
      <tbody>
        <tr><td style="border:1px solid #1A1A1A;padding:0.3rem 0.6rem;">1</td><td style="border:1px solid #1A1A1A;padding:0.3rem 0.6rem;text-align:right;">3.1</td><td style="border:1px solid #1A1A1A;padding:0.3rem 0.6rem;text-align:right;">12.40</td></tr>
        <tr><td style="border:1px solid #1A1A1A;padding:0.3rem 0.6rem;">2</td><td style="border:1px solid #1A1A1A;padding:0.3rem 0.6rem;text-align:right;">7.8</td><td style="border:1px solid #1A1A1A;padding:0.3rem 0.6rem;text-align:right;">34.10</td></tr>
        <tr><td style="border:1px solid #1A1A1A;padding:0.3rem 0.6rem;">3</td><td style="border:1px solid #1A1A1A;padding:0.3rem 0.6rem;text-align:right;">2.4</td><td style="border:1px solid #1A1A1A;padding:0.3rem 0.6rem;text-align:right;">8.05</td></tr>
        <tr><td style="border:1px solid #1A1A1A;padding:0.3rem 0.6rem;">4</td><td style="border:1px solid #1A1A1A;padding:0.3rem 0.6rem;text-align:right;">11.2</td><td style="border:1px solid #1A1A1A;padding:0.3rem 0.6rem;text-align:right;">49.70</td></tr>
        <tr><td style="border:1px solid #1A1A1A;padding:0.3rem 0.6rem;color:#AAAAAA;">…</td><td style="border:1px solid #1A1A1A;padding:0.3rem 0.6rem;text-align:right;color:#AAAAAA;">…</td><td style="border:1px solid #1A1A1A;padding:0.3rem 0.6rem;text-align:right;color:#AAAAAA;">…</td></tr>
      </tbody>
    </table>
    <p style="font-family:'JetBrains Mono',monospace;font-size:0.65rem;color:#AAAAAA;margin-top:0.4rem;">600 rows</p>
  </div>

  <v-click>
    <iframe src="/charts/scatter-sessions-revenue.html?v=1779373681" style="width:100%;height:300px;border:0;"></iframe>
  </v-click>

</div>

<p style="margin-top:0.6rem;font-size:0.95rem;color:#6B6B6B;">Overplotting hides the cloud structure, so alpha transparency or a hexbin restores it at scale</p>

---

# Same data, three lenses

<div style="font-family:'JetBrains Mono',monospace;font-size:0.78rem;color:#FF00FF;letter-spacing:0.14em;text-transform:uppercase;margin:-0.4rem 0 0.6rem;">Scatter · 2D histogram · Density heatmap</div>

<iframe src="/charts/scatter-to-heatmap.html?v=1779373681" style="width:100%;height:340px;border:0;"></iframe>

<p style="margin-top:0.4rem;font-size:0.85rem;color:#6B6B6B;">As points pile up, the right lens shifts from scatter to a 2D histogram to a density contour</p>

---

# What does the 2D structure look like?

<div style="font-family:'JetBrains Mono',monospace;font-size:0.78rem;color:#FF00FF;letter-spacing:0.14em;text-transform:uppercase;margin:-0.4rem 0 0.6rem;">Heatmap · correlation matrix</div>

<iframe src="/charts/heatmap-corr.html?v=1779373681" style="width:80%;height:400px;border:0;display:block;margin:0.4rem auto 0;"></iframe>

<p style="margin-top:0.4rem;font-size:0.85rem;color:#6B6B6B;text-align:center;">Diverging red-white-green anchored at zero. Strong positive correlations land green, strong negative land red, near-zero stays white</p>

---

# How does the conversion sequence drop off?

<div style="font-family:'JetBrains Mono',monospace;font-size:0.78rem;color:#FF00FF;letter-spacing:0.14em;text-transform:uppercase;margin:-0.6rem 0 0.2rem;">Funnel chart</div>

<div style="display:grid;grid-template-columns:1fr 2fr;gap:2rem;margin-top:0;align-items:start;">

  <div>
    <div style="font-family:'JetBrains Mono',monospace;font-size:0.72rem;color:#AAAAAA;letter-spacing:0.14em;text-transform:uppercase;margin-bottom:0.5rem;">Data</div>
    <table style="border-collapse:collapse;font-family:'JetBrains Mono',monospace;font-size:0.72rem;color:#1A1A1A;">
      <thead><tr style="background:#F5F5F5;">
        <th style="border:1px solid #1A1A1A;padding:0.35rem 0.6rem;text-align:left;font-weight:600;">stage</th>
        <th style="border:1px solid #1A1A1A;padding:0.35rem 0.6rem;text-align:right;font-weight:600;">users</th>
      </tr></thead>
      <tbody>
        <tr><td style="border:1px solid #1A1A1A;padding:0.3rem 0.6rem;">Visited</td><td style="border:1px solid #1A1A1A;padding:0.3rem 0.6rem;text-align:right;">12 000</td></tr>
        <tr><td style="border:1px solid #1A1A1A;padding:0.3rem 0.6rem;">Signed up</td><td style="border:1px solid #1A1A1A;padding:0.3rem 0.6rem;text-align:right;">4 200</td></tr>
        <tr><td style="border:1px solid #1A1A1A;padding:0.3rem 0.6rem;">Activated</td><td style="border:1px solid #1A1A1A;padding:0.3rem 0.6rem;text-align:right;">2 600</td></tr>
        <tr><td style="border:1px solid #1A1A1A;padding:0.3rem 0.6rem;">Used 7d</td><td style="border:1px solid #1A1A1A;padding:0.3rem 0.6rem;text-align:right;">1 700</td></tr>
        <tr><td style="border:1px solid #1A1A1A;padding:0.3rem 0.6rem;">Paid</td><td style="border:1px solid #1A1A1A;padding:0.3rem 0.6rem;text-align:right;">480</td></tr>
      </tbody>
    </table>
  </div>

  <v-click>
    <iframe src="/charts/funnel.html?v=1779373681" style="width:100%;height:260px;border:0;display:block;margin:0;"></iframe>
  </v-click>

</div>

<p style="margin-top:0.5rem;font-size:0.85rem;color:#6B6B6B;">A funnel compresses a sequence of conversions into one drop pattern, with the share at each stage written on the bar</p>

---

# Are these cohorts retaining differently?

<div style="font-family:'JetBrains Mono',monospace;font-size:0.78rem;color:#FF00FF;letter-spacing:0.14em;text-transform:uppercase;margin:-0.4rem 0 0.6rem;">Cohort retention curves</div>

<div style="display:grid;grid-template-columns:1fr 2.2fr;gap:2rem;margin-top:0.6rem;align-items:start;">

  <div>
    <div style="font-family:'JetBrains Mono',monospace;font-size:0.72rem;color:#AAAAAA;letter-spacing:0.14em;text-transform:uppercase;margin-bottom:0.5rem;">Data</div>
    <table style="border-collapse:collapse;font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#1A1A1A;">
      <thead><tr style="background:#F5F5F5;">
        <th style="border:1px solid #1A1A1A;padding:0.3rem 0.6rem;text-align:left;font-weight:600;">cohort</th>
        <th style="border:1px solid #1A1A1A;padding:0.3rem 0.6rem;text-align:right;font-weight:600;">month</th>
        <th style="border:1px solid #1A1A1A;padding:0.3rem 0.6rem;text-align:right;font-weight:600;">retained</th>
      </tr></thead>
      <tbody>
        <tr><td style="border:1px solid #1A1A1A;padding:0.25rem 0.6rem;">2026-Q1</td><td style="border:1px solid #1A1A1A;padding:0.25rem 0.6rem;text-align:right;">0</td><td style="border:1px solid #1A1A1A;padding:0.25rem 0.6rem;text-align:right;">100%</td></tr>
        <tr><td style="border:1px solid #1A1A1A;padding:0.25rem 0.6rem;">2026-Q1</td><td style="border:1px solid #1A1A1A;padding:0.25rem 0.6rem;text-align:right;">3</td><td style="border:1px solid #1A1A1A;padding:0.25rem 0.6rem;text-align:right;">49%</td></tr>
        <tr><td style="border:1px solid #1A1A1A;padding:0.25rem 0.6rem;">2026-Q1</td><td style="border:1px solid #1A1A1A;padding:0.25rem 0.6rem;text-align:right;">6</td><td style="border:1px solid #1A1A1A;padding:0.25rem 0.6rem;text-align:right;">38%</td></tr>
        <tr><td style="border:1px solid #1A1A1A;padding:0.25rem 0.6rem;">2026-Q1</td><td style="border:1px solid #1A1A1A;padding:0.25rem 0.6rem;text-align:right;">12</td><td style="border:1px solid #1A1A1A;padding:0.25rem 0.6rem;text-align:right;">33%</td></tr>
        <tr><td style="border:1px solid #1A1A1A;padding:0.25rem 0.6rem;color:#AAAAAA;">…</td><td style="border:1px solid #1A1A1A;padding:0.25rem 0.6rem;text-align:right;color:#AAAAAA;">…</td><td style="border:1px solid #1A1A1A;padding:0.25rem 0.6rem;text-align:right;color:#AAAAAA;">…</td></tr>
      </tbody>
    </table>
    <p style="font-family:'JetBrains Mono',monospace;font-size:0.65rem;color:#AAAAAA;margin-top:0.4rem;">5 cohorts × 13 months</p>
  </div>

  <v-click>
    <iframe src="/charts/retention-cohorts.html?v=1779373681" style="width:100%;height:340px;border:0;"></iframe>
  </v-click>

</div>

<p style="margin-top:0.4rem;font-size:0.85rem;color:#6B6B6B;">Cohort curves separate product changes from acquisition changes, which one blended retention number cannot do</p>

---

# Paying accounts stacked by cohort

<div style="font-family:'JetBrains Mono',monospace;font-size:0.78rem;color:#FF00FF;letter-spacing:0.14em;text-transform:uppercase;margin:-0.4rem 0 0.6rem;">Stacked area chart</div>

<iframe src="/charts/area-cohort-paying.html?v=1779373681" style="width:100%;height:360px;border:0;"></iframe>

<p style="margin-top:0.4rem;font-size:0.85rem;color:#6B6B6B;">Each new cohort piles on top of the surviving older ones, so the total paying base reads as the area sum</p>

---

# Two cohort heatmaps with different palettes

<div style="font-family:'JetBrains Mono',monospace;font-size:0.78rem;color:#FF00FF;letter-spacing:0.14em;text-transform:uppercase;margin:-0.4rem 0 0.6rem;">Heatmap</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:1.2rem;margin-top:0.4rem;">

  <iframe src="/charts/heatmap-cohort-revenue.html?v=1779373681" style="width:100%;height:340px;border:0;"></iframe>
  <iframe src="/charts/heatmap-cohort-log-retention.html?v=1779373681" style="width:100%;height:340px;border:0;"></iframe>

</div>

<p style="margin-top:0.4rem;font-size:0.85rem;color:#6B6B6B;">Revenue uses a pale-to-bright ramp because the value is magnitude. Retention uses a diverging palette because high and low carry directional meaning</p>

---

# Roll the cohorts up into a grand total

<div style="font-family:'JetBrains Mono',monospace;font-size:0.78rem;color:#FF00FF;letter-spacing:0.14em;text-transform:uppercase;margin:-0.4rem 0 0.6rem;">Heatmap with totals</div>

<iframe src="/charts/heatmap-cohort-grand-total.html?v=1779373681" style="width:100%;height:380px;border:0;"></iframe>

<p style="margin-top:0.3rem;font-size:0.85rem;color:#6B6B6B;">Same cohort heatmap with a Total row underneath, so the monthly revenue base across all cohorts becomes one line you can scan</p>

---

# Volume and rate on one chart

<div style="font-family:'JetBrains Mono',monospace;font-size:0.78rem;color:#FF00FF;letter-spacing:0.14em;text-transform:uppercase;margin:-0.4rem 0 0.6rem;">Dual-axis combo chart</div>

<iframe src="/charts/combo-dual-axis.html?v=1779373681" style="width:100%;height:340px;border:0;"></iframe>

<p style="margin-top:0.4rem;font-size:0.85rem;color:#6B6B6B;">Application volume grew across the year while the approval rate dropped, which a single-axis chart would hide</p>

---

# Where do the segments split

<div style="font-family:'JetBrains Mono',monospace;font-size:0.78rem;color:#FF00FF;letter-spacing:0.14em;text-transform:uppercase;margin:-0.4rem 0 0.6rem;">Scatter plot</div>

<div style="display:grid;grid-template-columns:1fr 2fr;gap:2rem;margin-top:0.2rem;align-items:start;">

  <div>
    <div style="font-family:'JetBrains Mono',monospace;font-size:0.72rem;color:#AAAAAA;letter-spacing:0.14em;text-transform:uppercase;margin-bottom:0.5rem;">Data</div>
    <p style="font-family:'JetBrains Mono',monospace;font-size:0.78rem;color:#1A1A1A;">sessions per week vs revenue, coloured by behavioural segment</p>
  </div>

  <v-click>
    <iframe src="/charts/scatter-segments.html?v=1779373681" style="width:100%;height:340px;border:0;"></iframe>
  </v-click>

</div>

<p style="margin-top:0.4rem;font-size:0.85rem;color:#6B6B6B;">Three clouds in the same x and y space: casual users on the low end, power users on the diagonal, whales sitting flat at a high revenue floor</p>

---

<div style="font-family:'Bricolage Grotesque',sans-serif;font-weight:800;font-size:1.7rem;color:#1A1A1A;letter-spacing:-0.02em;margin-bottom:0.4rem;">A heatmap that shows the actual numbers</div>

<iframe src="/charts/heatmap-cohort.html?v=1779373681" style="width:100%;height:380px;border:0;"></iframe>

<p style="margin-top:0.3rem;font-size:0.8rem;color:#6B6B6B;">Segment by country, engagement in each cell, red-yellow-green so the pattern stays visible at a glance</p>

---

<div style="font-family:'Bricolage Grotesque',sans-serif;font-weight:800;font-size:1.7rem;color:#1A1A1A;letter-spacing:-0.02em;margin-bottom:0.4rem;">Where the MRR growth comes from</div>

<div style="font-family:'JetBrains Mono',monospace;font-size:0.78rem;color:#FF00FF;letter-spacing:0.14em;text-transform:uppercase;margin:-0.2rem 0 0.6rem;">Line decomposition</div>

<iframe src="/charts/mrr-decomposition.html?v=1779373681" style="width:100%;height:440px;border:0;"></iframe>

<p style="margin-top:0.3rem;font-size:0.78rem;color:#6B6B6B;">MRR on the left, net new MRR on the right with gains above zero and losses below, pink line marks the monthly net</p>

---

# Same idea, waterfall view

<div style="font-family:'JetBrains Mono',monospace;font-size:0.78rem;color:#FF00FF;letter-spacing:0.14em;text-transform:uppercase;margin:-0.4rem 0 0.6rem;">Waterfall chart</div>

<iframe src="/charts/waterfall-revenue.html?v=1779373681" style="width:100%;height:380px;border:0;"></iframe>

<p style="margin-top:0.3rem;font-size:0.85rem;color:#6B6B6B;">Start with last quarter, walk through each driver in turn, land on the new total. Fewer buyers and discount cost pull down. Higher average order value and repeat purchases more than make up for it</p>

---
layout: statement
---

# A chart lowers complexity so the reader catches the <span class="pink">point</span>

---
layout: section
class: tint-sky
---

## 03

# Working<br>with an LLM

---

# Describe the data, the question, the constraint

<pre style="font-family:'JetBrains Mono',monospace;font-size:0.9rem;background:#F7F7F7;padding:1.2rem 1.4rem;border-radius:6px;color:#1A1A1A;line-height:1.7;margin-top:0.4rem;">Data shape: columns, types, granularity, time range
Constraint: comparison / share / distribution / trend / relationship
Question:   the specific question this chart must answer
Tool:       plotly express, matplotlib, seaborn
Audience:   executive / engineer / yourself
</pre>

<p style="margin-top:1rem;font-size:1.1rem;color:#1A1A1A;">The skill is describing the data and the question well, since the library can be swapped at any time</p>

---

# One example, end to end

<div style="font-family:'JetBrains Mono',monospace;font-size:0.78rem;color:#FF00FF;letter-spacing:0.14em;text-transform:uppercase;margin:-0.4rem 0 0.6rem;">Prompt the LLM for a specific result, not a generic chart</div>

<div style="display:grid;grid-template-columns:1.2fr 1fr;gap:1.6rem;margin-top:0.2rem;align-items:start;">

<pre style="font-family:'JetBrains Mono',monospace;font-size:0.72rem;background:#F7F7F7;padding:1rem 1.2rem;border-radius:6px;color:#1A1A1A;line-height:1.55;margin:0;">Goal:        understand DAU dynamics around the April 15 launch and
             tell whether the launch moved the metric or noise drowned it
Data shape:  daily DAU, single product, 90 days, Feb 1 → May 1
Slice:       split the series into pre-launch and post-launch periods
Smoothing:   add a 7-day rolling mean so the trend reads through noise
Chart type:  line chart, raw series in the back, rolling mean on top,
             vertical marker at the April 15 launch date
Palette:     black for the raw line, magenta for the rolling mean and
             for the launch marker, light grid
Labels:      x axis "date", y axis "DAU", chart title
             "DAU around April 15 launch", value label on last point
Tool:        plotly express in Python, output a standalone HTML file
Audience:    product team in standup, viewed on a laptop
</pre>

  <iframe src="/charts/llm-example.html?v=1779373681" style="width:100%;height:320px;border:0;"></iframe>

</div>

---
layout: section
class: tint-cream
---

## 04

# Dashboards

---

# What a dashboard is

<p style="font-size:1.4rem;color:#1A1A1A;margin:1.4rem 0 2.4rem;line-height:1.5;">A page that refreshes on its own and bundles a few charts, a few headline numbers, and a few filters so one audience can answer one recurring question without writing a query each time.</p>

<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:1.2rem;margin-top:1.6rem;">

  <div style="border-left:3px solid #FF00FF;padding:0.4rem 0 0.4rem 1.1rem;">
    <div style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#AAAAAA;letter-spacing:0.14em;text-transform:uppercase;margin-bottom:0.4rem;">Updatable</div>
    <div style="font-size:1.0rem;color:#1A1A1A;line-height:1.45;">Data refreshes on its own, view stays useful next week</div>
  </div>

  <div style="border-left:3px solid #FF00FF;padding:0.4rem 0 0.4rem 1.1rem;">
    <div style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#AAAAAA;letter-spacing:0.14em;text-transform:uppercase;margin-bottom:0.4rem;">A few visuals</div>
    <div style="font-size:1.0rem;color:#1A1A1A;line-height:1.45;">KPI tiles, trend lines, comparisons, drill-down details</div>
  </div>

  <div style="border-left:3px solid #FF00FF;padding:0.4rem 0 0.4rem 1.1rem;">
    <div style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#AAAAAA;letter-spacing:0.14em;text-transform:uppercase;margin-bottom:0.4rem;">Filters</div>
    <div style="font-size:1.0rem;color:#1A1A1A;line-height:1.45;">Date range, segment, country, sitting under the title</div>
  </div>

</div>

---

# Organise for the eye

<p style="font-size:1.15rem;color:#1A1A1A;margin:0 0 1.2rem;line-height:1.5;">The reader scans top-left first, then sweeps right and down, so the layout should answer questions in that order.</p>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:2rem;margin-top:0.4rem;">

  <div style="border-left:3px solid #FF00FF;padding:0.4rem 0 0.4rem 1.1rem;">
    <div style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#AAAAAA;letter-spacing:0.14em;text-transform:uppercase;margin-bottom:0.4rem;">Top of page</div>
    <div style="font-size:1.05rem;font-weight:700;color:#1A1A1A;line-height:1.4;">Headline numbers, the ones a stakeholder needs at a glance</div>
  </div>

  <div style="border-left:3px solid #FF00FF;padding:0.4rem 0 0.4rem 1.1rem;">
    <div style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#AAAAAA;letter-spacing:0.14em;text-transform:uppercase;margin-bottom:0.4rem;">Middle</div>
    <div style="font-size:1.05rem;font-weight:700;color:#1A1A1A;line-height:1.4;">Trend lines and category comparisons that explain the headline</div>
  </div>

  <div style="border-left:3px solid #FF00FF;padding:0.4rem 0 0.4rem 1.1rem;">
    <div style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#AAAAAA;letter-spacing:0.14em;text-transform:uppercase;margin-bottom:0.4rem;">Bottom</div>
    <div style="font-size:1.05rem;font-weight:700;color:#1A1A1A;line-height:1.4;">Diagnostic detail, funnels, cohorts, drill-downs</div>
  </div>

  <div style="border-left:3px solid #FF00FF;padding:0.4rem 0 0.4rem 1.1rem;">
    <div style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#AAAAAA;letter-spacing:0.14em;text-transform:uppercase;margin-bottom:0.4rem;">Filters</div>
    <div style="font-size:1.05rem;font-weight:700;color:#1A1A1A;line-height:1.4;">Date range, segment, country, sitting at the very top under the title</div>
  </div>

</div>

---

# Best practices

<div style="display:flex;flex-direction:column;gap:0.9rem;margin-top:0.4rem;">

  <div style="display:grid;grid-template-columns:36px 1fr;gap:1rem;align-items:baseline;">
    <span style="font-family:'JetBrains Mono',monospace;font-size:0.85rem;color:#FF00FF;letter-spacing:0.1em;">01</span>
    <div style="font-size:1.05rem;color:#1A1A1A;line-height:1.5;">One question per row, so the reader does not jump between unrelated topics</div>
  </div>

  <div style="display:grid;grid-template-columns:36px 1fr;gap:1rem;align-items:baseline;">
    <span style="font-family:'JetBrains Mono',monospace;font-size:0.85rem;color:#FF00FF;letter-spacing:0.1em;">02</span>
    <div style="font-size:1.05rem;color:#1A1A1A;line-height:1.5;">Consistent colour coding across charts, so the same segment looks the same everywhere</div>
  </div>

  <div style="display:grid;grid-template-columns:36px 1fr;gap:1rem;align-items:baseline;">
    <span style="font-family:'JetBrains Mono',monospace;font-size:0.85rem;color:#FF00FF;letter-spacing:0.1em;">03</span>
    <div style="font-size:1.05rem;color:#1A1A1A;line-height:1.5;">Default the date range to the window people actually look at</div>
  </div>

  <div style="display:grid;grid-template-columns:36px 1fr;gap:1rem;align-items:baseline;">
    <span style="font-family:'JetBrains Mono',monospace;font-size:0.85rem;color:#FF00FF;letter-spacing:0.1em;">04</span>
    <div style="font-size:1.05rem;color:#1A1A1A;line-height:1.5;">Title every chart with the question it answers</div>
  </div>

  <div style="display:grid;grid-template-columns:36px 1fr;gap:1rem;align-items:baseline;">
    <span style="font-family:'JetBrains Mono',monospace;font-size:0.85rem;color:#FF00FF;letter-spacing:0.1em;">05</span>
    <div style="font-size:1.05rem;color:#1A1A1A;line-height:1.5;">Strip every label, axis, and decoration the reader does not need to answer the question</div>
  </div>

</div>

---

# A dashboard, end to end

<p style="font-size:1.2rem;color:#1A1A1A;margin:0 0 2rem;line-height:1.5;">One HTML page, four charts, three KPIs, chips and toggles that filter the data live.</p>

<a href="/harbour-product-analytics-2026/04-data-viz/dashboards/product-overview.html" target="_blank" style="display:inline-block;background:#1A1A1A;color:white;font-family:'JetBrains Mono',monospace;font-size:0.85rem;letter-spacing:0.14em;text-transform:uppercase;padding:0.9rem 1.8rem;border-radius:999px;text-decoration:none;margin-bottom:1.6rem;">Open dashboard →</a>

<p style="font-family:'JetBrains Mono',monospace;font-size:0.75rem;color:#6B6B6B;letter-spacing:0.06em;margin:0;">localhost:3041/dashboards/product-overview.html</p>

<p style="margin-top:2rem;font-size:0.85rem;color:#6B6B6B;">Same HTML deploys unchanged to GitHub Pages, Google Sites, or a Google Apps Script web app</p>

---

# Publish the dashboard with Apps Script

<div style="display:grid;grid-template-columns:1fr 1fr;gap:1.6rem;margin-top:0.6rem;">

  <div>
    <div style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#FF00FF;letter-spacing:0.14em;text-transform:uppercase;margin-bottom:0.4rem;">Code.gs</div>
<pre style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;background:#F7F7F7;padding:0.8rem 1rem;border-radius:6px;color:#1A1A1A;line-height:1.5;margin:0;">function doGet() {
  return HtmlService
    .createHtmlOutputFromFile('index')
    .setTitle('My Plotly Dashboard')
    .setXFrameOptionsMode(
      HtmlService.XFrameOptionsMode.ALLOWALL
    );
}</pre>
    <div style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#FF00FF;letter-spacing:0.14em;text-transform:uppercase;margin:0.8rem 0 0.4rem;">index.html</div>
    <pre style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;background:#F7F7F7;padding:0.8rem 1rem;border-radius:6px;color:#1A1A1A;line-height:1.5;margin:0;">// paste the dashboard HTML here
&lt;!doctype html&gt;
&lt;html&gt;…&lt;/html&gt;</pre>
  </div>

  <div>
    <div style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#AAAAAA;letter-spacing:0.14em;text-transform:uppercase;margin-bottom:0.5rem;">Steps</div>
    <ol style="margin:0;padding-left:1.2rem;font-size:0.95rem;color:#1A1A1A;line-height:1.6;">
      <li>Open <a href="https://script.google.com/home" target="_blank" style="color:#FF00FF;">script.google.com/home</a></li>
      <li>New project, rename to anything</li>
      <li>Paste <code>doGet()</code> into <code>Code.gs</code></li>
      <li>Add file → HTML → name it <code>index</code></li>
      <li>Paste your dashboard HTML inside</li>
      <li>Deploy → New deployment → Web app</li>
      <li>Execute as: Me. Access: Anyone with the link</li>
      <li>Copy the web app URL, share it</li>
    </ol>
  </div>

</div>

---

# Plotly under the hood

<p style="font-size:1.2rem;color:#1A1A1A;margin:0 0 1.6rem;line-height:1.5;">Plotly is a Python library that emits a JavaScript chart inside a plain HTML page.</p>

<div style="display:flex;flex-direction:column;gap:1.2rem;margin-top:0.4rem;">

  <div style="display:grid;grid-template-columns:170px 1fr;gap:1.2rem;align-items:baseline;border-bottom:1px solid #E0E0E0;padding-bottom:1.1rem;">
    <span style="font-family:'JetBrains Mono',monospace;font-size:0.78rem;color:#FF00FF;letter-spacing:0.14em;text-transform:uppercase;">plotly.py</span>
    <div style="font-size:1.05rem;color:#1A1A1A;">the Python package you call from a notebook or a script</div>
  </div>

  <div style="display:grid;grid-template-columns:170px 1fr;gap:1.2rem;align-items:baseline;border-bottom:1px solid #E0E0E0;padding-bottom:1.1rem;">
    <span style="font-family:'JetBrains Mono',monospace;font-size:0.78rem;color:#FF00FF;letter-spacing:0.14em;text-transform:uppercase;">plotly.js</span>
    <div style="font-size:1.05rem;color:#1A1A1A;">the JavaScript engine that draws the chart in the browser</div>
  </div>

  <div style="display:grid;grid-template-columns:170px 1fr;gap:1.2rem;align-items:baseline;">
    <span style="font-family:'JetBrains Mono',monospace;font-size:0.78rem;color:#FF00FF;letter-spacing:0.14em;text-transform:uppercase;">output</span>
    <div style="font-size:1.05rem;color:#1A1A1A;">a self-contained HTML file you can open anywhere, including these slides</div>
  </div>

</div>

---

# Share the chart with anyone

<p style="font-size:1.2rem;color:#1A1A1A;margin:0 0 1.6rem;line-height:1.5;">An HTML chart is a file. A file goes anywhere a link goes.</p>

<div style="display:flex;flex-direction:column;gap:1.2rem;">

  <div style="display:grid;grid-template-columns:200px 1fr;gap:1.2rem;align-items:baseline;border-bottom:1px solid #E0E0E0;padding-bottom:1.1rem;">
    <span style="font-family:'JetBrains Mono',monospace;font-size:0.78rem;color:#FF00FF;letter-spacing:0.14em;text-transform:uppercase;">Static HTML</span>
    <div style="font-size:1.05rem;color:#1A1A1A;">upload to GitHub Pages, Google Sites, or any file host and share the link</div>
  </div>

  <div style="display:grid;grid-template-columns:200px 1fr;gap:1.2rem;align-items:baseline;border-bottom:1px solid #E0E0E0;padding-bottom:1.1rem;">
    <span style="font-family:'JetBrains Mono',monospace;font-size:0.78rem;color:#FF00FF;letter-spacing:0.14em;text-transform:uppercase;">Streamlit</span>
    <div style="font-size:1.05rem;color:#1A1A1A;">wrap a few charts plus filters into a small Python app, deploy in one command</div>
  </div>

  <div style="display:grid;grid-template-columns:200px 1fr;gap:1.2rem;align-items:baseline;">
    <span style="font-family:'JetBrains Mono',monospace;font-size:0.78rem;color:#FF00FF;letter-spacing:0.14em;text-transform:uppercase;">Apps Script</span>
    <div style="font-size:1.05rem;color:#1A1A1A;">paste HTML into a Google Apps Script web app for instant sharing inside the company</div>
  </div>

</div>

---
layout: section
class: tint-rose
---

## 05

# Same numbers,<br>different stories

---

# Four datasets, identical statistics

<div style="margin-top:0.6rem;">

<table style="font-size:0.95rem;border-collapse:collapse;width:100%;max-width:780px;margin:0 auto;">
<thead>
<tr style="border-bottom:1px solid #E0E0E0;color:#1A1A1A;">
<th style="text-align:left;padding:0.4rem 0.8rem;">Statistic</th>
<th style="padding:0.4rem 0.8rem;">I</th>
<th style="padding:0.4rem 0.8rem;">II</th>
<th style="padding:0.4rem 0.8rem;">III</th>
<th style="padding:0.4rem 0.8rem;">IV</th>
</tr>
</thead>
<tbody>
<tr><td style="padding:0.35rem 0.8rem;">Mean of x</td><td style="text-align:center;">9.0</td><td style="text-align:center;">9.0</td><td style="text-align:center;">9.0</td><td style="text-align:center;">9.0</td></tr>
<tr><td style="padding:0.35rem 0.8rem;">Mean of y</td><td style="text-align:center;">7.5</td><td style="text-align:center;">7.5</td><td style="text-align:center;">7.5</td><td style="text-align:center;">7.5</td></tr>
<tr><td style="padding:0.35rem 0.8rem;">Variance of x</td><td style="text-align:center;">11.0</td><td style="text-align:center;">11.0</td><td style="text-align:center;">11.0</td><td style="text-align:center;">11.0</td></tr>
<tr><td style="padding:0.35rem 0.8rem;">Variance of y</td><td style="text-align:center;">4.12</td><td style="text-align:center;">4.12</td><td style="text-align:center;">4.12</td><td style="text-align:center;">4.12</td></tr>
<tr><td style="padding:0.35rem 0.8rem;">Correlation</td><td style="text-align:center;">0.816</td><td style="text-align:center;">0.816</td><td style="text-align:center;">0.816</td><td style="text-align:center;">0.816</td></tr>
<tr><td style="padding:0.35rem 0.8rem;">Regression line</td><td colspan="4" style="text-align:center;">y = 3 + 0.5 x</td></tr>
</tbody>
</table>

</div>

<p style="margin-top:1.2rem;font-size:1.05rem;color:#1A1A1A;text-align:center;">Same numbers across all four</p>

---

<div style="font-family:'Bricolage Grotesque',sans-serif;font-weight:800;font-size:1.7rem;color:#1A1A1A;letter-spacing:-0.02em;margin-bottom:0.4rem;">Four datasets, four different stories</div>

<iframe src="/charts/anscombe.html?v=1779373681" style="width:100%;height:440px;border:0;"></iframe>

---

<div style="font-family:'Bricolage Grotesque',sans-serif;font-weight:800;font-size:1.7rem;color:#1A1A1A;letter-spacing:-0.02em;margin-bottom:0.4rem;">Twelve datasets, identical statistics</div>

<iframe src="/charts/datasaurus.html?v=1779373681" style="width:100%;height:440px;border:0;"></iframe>

<p style="margin-top:0.3rem;font-size:0.7rem;color:#AAAAAA;">Matejka and Fitzmaurice, Autodesk Research, 2017</p>

---
layout: statement
---

# Visualisation is one more <span class="pink">dimension</span> of data work

---

# Materials

<div style="display:grid;grid-template-columns:1fr 1fr;gap:2.4rem;margin-top:0.6rem;font-size:0.9rem;line-height:1.6;color:#1A1A1A;">

<div>
<div style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#AAAAAA;letter-spacing:0.14em;text-transform:uppercase;margin-bottom:0.5rem;">Plotly</div>
<ul style="margin:0 0 1.2rem;padding-left:1.1rem;">
<li><a href="https://plotly.com/python/" target="_blank">plotly.com/python</a>, chart gallery</li>
<li><a href="https://plotly.com/python/plotly-express/" target="_blank">Plotly Express</a>, quick-start chart catalog</li>
<li><a href="https://plotly.com/python/figure-structure/" target="_blank">Figure reference</a>, every parameter, when defaults don't fit</li>
<li><a href="https://plotly.com/python/dash/" target="_blank">Dash</a>, full Python dashboard framework</li>
</ul>

<div style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#AAAAAA;letter-spacing:0.14em;text-transform:uppercase;margin-bottom:0.5rem;">Data viz design</div>
<ul style="margin:0;padding-left:1.1rem;">
<li><a href="https://guides.library.jhu.edu/datavisualization" target="_blank">JHU Library, data visualization guide</a></li>
<li><a href="https://uxmag.medium.com/the-ultimate-data-visualization-handbook-for-designers-efa7d6e0b6fe" target="_blank">UX Magazine, data viz handbook for designers</a></li>
</ul>

</div>

<div>
<div style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#AAAAAA;letter-spacing:0.14em;text-transform:uppercase;margin-bottom:0.5rem;">Dashboard best practices</div>
<ul style="margin:0;padding-left:1.1rem;">
<li><a href="https://www.uxpin.com/studio/blog/dashboard-design-principles/" target="_blank">UXPin, dashboard design principles</a></li>
<li><a href="https://www.gooddata.ai/blog/7-tips-building-dashboards-users-love/" target="_blank">GoodData, 7 tips for dashboards users love</a></li>
<li><a href="https://medium.com/data-science/how-to-build-effective-and-useful-dashboards-711759534639" target="_blank">Medium, how to build effective and useful dashboards</a></li>
<li><a href="https://data.ucop.edu/support-training/tableau-files/building_effective_dashboards.pdf" target="_blank">UCOP, building effective dashboards (PDF)</a></li>
<li><a href="https://www.reddit.com/r/PowerBI/comments/1htzl6b/what_are_the_best_practices_in_dashboard/" target="_blank">r/PowerBI thread on dashboard best practices</a></li>
</ul>
</div>

</div>
