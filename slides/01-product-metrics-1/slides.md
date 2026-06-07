---
theme: apple-basic
title: "Session 01: Product Metrics"
info: "Product Analytics · Harbour.Space · 2026"
highlighter: shiki
drawings:
  persist: false
transition: fade
mdc: true
layout: intro
---

# Product <span class="pink">Metrics</span>

Why metrics exist and how to choose the right ones

<div class="absolute bottom-10 left-14" style="font-family:'JetBrains Mono',monospace;font-size:0.75rem;text-transform:uppercase;letter-spacing:0.15em;color:rgba(255,255,255,0.55);">
  Harbour.Space &middot; Barcelona &middot; May 18, 2026
</div>

---

# Today and tomorrow

<div style="display:grid;grid-template-columns:1fr 1fr;gap:2.5rem;margin-top:0.6rem;">

  <div style="display:flex;flex-direction:column;gap:0.55rem;">
    <div style="font-family:'JetBrains Mono',monospace;font-size:0.72rem;color:#FF00FF;letter-spacing:0.14em;text-transform:uppercase;margin-bottom:0.4rem;">Today</div>
    <div style="display:grid;grid-template-columns:42px 1fr;gap:1rem;align-items:baseline;">
      <span style="font-family:'JetBrains Mono',monospace;font-size:0.85rem;color:#FF00FF;letter-spacing:0.1em;">01</span>
      <div style="font-size:1.05rem;font-weight:700;color:#1A1A1A;">Why metrics exist at all</div>
    </div>
    <div style="display:grid;grid-template-columns:42px 1fr;gap:1rem;align-items:baseline;">
      <span style="font-family:'JetBrains Mono',monospace;font-size:0.85rem;color:#FF00FF;letter-spacing:0.1em;">02</span>
      <div style="font-size:1.05rem;font-weight:700;color:#1A1A1A;">What is a metric</div>
    </div>
    <div style="display:grid;grid-template-columns:42px 1fr;gap:1rem;align-items:baseline;">
      <span style="font-family:'JetBrains Mono',monospace;font-size:0.85rem;color:#FF00FF;letter-spacing:0.1em;">03</span>
      <div style="font-size:1.05rem;font-weight:700;color:#1A1A1A;">Product metrics vs business metrics</div>
    </div>
    <div style="display:grid;grid-template-columns:42px 1fr;gap:1rem;align-items:baseline;">
      <span style="font-family:'JetBrains Mono',monospace;font-size:0.85rem;color:#FF00FF;letter-spacing:0.1em;">04</span>
      <div style="font-size:1.05rem;font-weight:700;color:#1A1A1A;">Metrics frameworks</div>
    </div>
    <div style="display:grid;grid-template-columns:42px 1fr;gap:1rem;align-items:baseline;">
      <span style="font-family:'JetBrains Mono',monospace;font-size:0.85rem;color:#FF00FF;letter-spacing:0.1em;">05</span>
      <div style="font-size:1.05rem;font-weight:700;color:#1A1A1A;">Funnel stage</div>
    </div>
    <div style="display:grid;grid-template-columns:42px 1fr;gap:1rem;align-items:baseline;">
      <span style="font-family:'JetBrains Mono',monospace;font-size:0.85rem;color:#FF00FF;letter-spacing:0.1em;">06</span>
      <div style="font-size:1.05rem;font-weight:700;color:#1A1A1A;">Domain</div>
    </div>
  </div>

  <div style="display:flex;flex-direction:column;gap:0.55rem;">
    <div style="font-family:'JetBrains Mono',monospace;font-size:0.72rem;color:#FF00FF;letter-spacing:0.14em;text-transform:uppercase;margin-bottom:0.4rem;">Tomorrow</div>
    <div style="display:grid;grid-template-columns:42px 1fr;gap:1rem;align-items:baseline;">
      <span style="font-family:'JetBrains Mono',monospace;font-size:0.85rem;color:#FF00FF;letter-spacing:0.1em;">07</span>
      <div style="font-size:1.05rem;font-weight:700;color:#1A1A1A;">Time orientation</div>
    </div>
    <div style="display:grid;grid-template-columns:42px 1fr;gap:1rem;align-items:baseline;">
      <span style="font-family:'JetBrains Mono',monospace;font-size:0.85rem;color:#FF00FF;letter-spacing:0.1em;">08</span>
      <div style="font-size:1.05rem;font-weight:700;color:#1A1A1A;">North Star Metric</div>
    </div>
    <div style="display:grid;grid-template-columns:42px 1fr;gap:1rem;align-items:baseline;">
      <span style="font-family:'JetBrains Mono',monospace;font-size:0.85rem;color:#FF00FF;letter-spacing:0.1em;">09</span>
      <div style="font-size:1.05rem;font-weight:700;color:#1A1A1A;">Metric tree</div>
    </div>
    <div style="display:grid;grid-template-columns:42px 1fr;gap:1rem;align-items:baseline;">
      <span style="font-family:'JetBrains Mono',monospace;font-size:0.85rem;color:#FF00FF;letter-spacing:0.1em;">10</span>
      <div style="font-size:1.05rem;font-weight:700;color:#1A1A1A;">Granularity</div>
    </div>
    <div style="display:grid;grid-template-columns:42px 1fr;gap:1rem;align-items:baseline;">
      <span style="font-family:'JetBrains Mono',monospace;font-size:0.85rem;color:#FF00FF;letter-spacing:0.1em;">11</span>
      <div style="font-size:1.05rem;font-weight:700;color:#1A1A1A;">Trade-offs and failure modes</div>
    </div>
  </div>

</div>

---

# About me

<div style="display:flex;flex-direction:column;gap:1.6rem;margin-top:2rem;">
  <div style="display:grid;grid-template-columns:10rem 1fr;align-items:baseline;gap:1rem;">
    <div style="font-family:'JetBrains Mono',monospace;font-size:0.75rem;text-transform:uppercase;letter-spacing:0.12em;color:#FF00FF;">Call me</div>
    <div style="font-weight:700;font-size:1.4rem;">Tim</div>
  </div>
  <div style="display:grid;grid-template-columns:10rem 1fr;align-items:baseline;gap:1rem;">
    <div style="font-family:'JetBrains Mono',monospace;font-size:0.75rem;text-transform:uppercase;letter-spacing:0.12em;color:#FF00FF;">Role</div>
    <div style="font-weight:700;font-size:1.4rem;">Senior Product Analyst</div>
  </div>
  <div style="display:grid;grid-template-columns:10rem 1fr;align-items:baseline;gap:1rem;">
    <div style="font-family:'JetBrains Mono',monospace;font-size:0.75rem;text-transform:uppercase;letter-spacing:0.12em;color:#FF00FF;">Domain</div>
    <div style="font-weight:700;font-size:1.4rem;">SaaS</div>
  </div>
  <div style="display:grid;grid-template-columns:10rem 1fr;align-items:baseline;gap:1rem;">
    <div style="font-family:'JetBrains Mono',monospace;font-size:0.75rem;text-transform:uppercase;letter-spacing:0.12em;color:#FF00FF;">Previously</div>
    <div style="font-weight:700;font-size:1.4rem;">Marketplaces &middot; Fintech &middot; Risk</div>
  </div>
  <div style="display:grid;grid-template-columns:10rem 1fr;align-items:baseline;gap:1rem;">
    <div style="font-family:'JetBrains Mono',monospace;font-size:0.75rem;text-transform:uppercase;letter-spacing:0.12em;color:#FF00FF;">Reach me</div>
    <div style="display:flex;flex-direction:column;gap:0.3rem;font-size:1.05rem;color:#1A1A1A;">
      <a href="mailto:timvilkov@gmail.com" style="color:inherit;text-decoration:none;">timvilkov@gmail.com</a>
      <a href="https://wa.me/79162345299" target="_blank" style="color:inherit;text-decoration:none;">WhatsApp · +7 916 234 52 99</a>
      <a href="https://www.linkedin.com/in/tim-vilkov-167278256/" target="_blank" style="color:inherit;text-decoration:none;">linkedin.com/in/tim-vilkov</a>
    </div>
  </div>
</div>

<!--
Ask students to share name, program, why they took this course.
-->

---

# Course philosophy

<div style="margin-top:1.5rem;display:flex;flex-direction:column;gap:1.5rem;">
  <div>
    <div style="font-weight:700;font-size:1.25rem;">A profession introduction</div>
    <div style="color:#6B6B6B;font-size:1.1rem;margin-top:0.2rem;">What a product analyst actually does, so you can decide if you want to go deeper into this track later</div>
  </div>
  <div>
    <div style="font-weight:700;font-size:1.25rem;">Real cases</div>
    <div style="color:#6B6B6B;font-size:1.1rem;margin-top:0.2rem;">Examples and decisions from a wide range of real product teams</div>
  </div>
  <div>
    <div style="font-weight:700;font-size:1.25rem;">Interview-ready</div>
    <div style="color:#6B6B6B;font-size:1.1rem;margin-top:0.2rem;">Homework and cases drawn from real product analyst interviews</div>
  </div>
</div>

<!--
Tim's three personal goals for the course:
1. Overview of the profession — students see the shape of the day-to-day, can deepen later if it interests them
2. Real industry cases (Manychat, Avito, Tinkoff) instead of toy examples
3. Homework and cases based on real interview problems — practical interview prep
-->

---

# How this works

<div style="margin-top:1.5rem;display:flex;flex-direction:column;gap:1.5rem;">
  <div>
    <div style="font-weight:700;font-size:1.25rem;">Questions, always</div>
    <div style="color:#6B6B6B;font-size:1.1rem;margin-top:0.2rem;">Stop me at any point. "Why?" is the best question you can ask</div>
  </div>
  <div>
    <div style="font-weight:700;font-size:1.25rem;">Challenge me</div>
    <div style="color:#6B6B6B;font-size:1.1rem;margin-top:0.2rem;">If something doesn't make sense or you disagree, say it</div>
  </div>
  <div>
    <div style="font-weight:700;font-size:1.25rem;">Kahoot quizzes</div>
    <div style="color:#6B6B6B;font-size:1.1rem;margin-top:0.2rem;">Best score wins a book</div>
  </div>
  <div>
    <div style="font-weight:700;font-size:1.25rem;">Feedback is always open</div>
    <div style="color:#6B6B6B;font-size:1.1rem;margin-top:0.2rem;">Tell me what's working and what isn't</div>
  </div>
</div>

---

# Grading

<table style="width:100%;border-collapse:collapse;margin-top:1rem;">
  <tbody>
    <tr style="border-bottom:1px solid #E0E0E0;"><td style="padding:0.7rem 0;font-size:1.1rem;">Quizzes</td><td style="padding:0.7rem 0;text-align:right;font-weight:700;font-size:1.1rem;">10%</td></tr>
    <tr style="border-bottom:1px solid #E0E0E0;"><td style="padding:0.7rem 0;font-size:1.1rem;">Assignment 1: Product Metrics</td><td style="padding:0.7rem 0;text-align:right;font-weight:700;font-size:1.1rem;">15%</td></tr>
    <tr style="border-bottom:1px solid #E0E0E0;"><td style="padding:0.7rem 0;font-size:1.1rem;">Assignment 2: SQL</td><td style="padding:0.7rem 0;text-align:right;font-weight:700;font-size:1.1rem;">15%</td></tr>
    <tr style="border-bottom:1px solid #E0E0E0;"><td style="padding:0.7rem 0;font-size:1.1rem;">Assignment 3: Statistics</td><td style="padding:0.7rem 0;text-align:right;font-weight:700;font-size:1.1rem;">15%</td></tr>
    <tr style="border-bottom:1px solid #E0E0E0;"><td style="padding:0.7rem 0;font-size:1.1rem;">Assignment 4: A/B Testing</td><td style="padding:0.7rem 0;text-align:right;font-weight:700;font-size:1.1rem;">15%</td></tr>
    <tr style="border-bottom:1px solid #E0E0E0;"><td style="padding:0.7rem 0;font-size:1.1rem;">Final Project</td><td style="padding:0.7rem 0;text-align:right;font-weight:700;font-size:1.1rem;">30%</td></tr>
    <tr style="border-top:2px solid #1A1A1A;"><td style="padding:0.7rem 0;font-weight:800;font-size:1.15rem;">Total</td><td style="padding:0.7rem 0;text-align:right;font-weight:800;font-size:1.15rem;">100%</td></tr>
  </tbody>
</table>

---
layout: section
class: tint-lavender
---

## 01

# Why metrics<br>exist at all

---
layout: statement
---

# It's about <span class="pink">better</span> decisions

---

# Without data, people are bad at knowing what works

<p style="color:#1A1A1A;font-size:1.2rem;margin-top:1.5rem;">Even the most senior person in the room is often <span class="pink">wrong</span>.</p>

---

# Intuition alone is not enough

<div style="display:grid;grid-template-columns:1fr 40px 1fr;grid-template-rows:auto 32px auto;max-width:580px;gap:0.5rem;margin-top:2rem;">
  <div style="border:1px solid #1A1A1A;padding:0.8rem 1rem;text-align:center;">
    <div style="font-family:'JetBrains Mono',monospace;font-size:0.62rem;text-transform:uppercase;letter-spacing:0.12em;color:#AAAAAA;">Step 1</div>
    <div style="font-weight:800;font-size:1.15rem;margin-top:0.2rem;">Action</div>
  </div>
  <div style="display:flex;align-items:center;justify-content:center;color:#1A1A1A;">→</div>
  <div style="border:1px solid #1A1A1A;padding:0.8rem 1rem;text-align:center;">
    <div style="font-family:'JetBrains Mono',monospace;font-size:0.62rem;text-transform:uppercase;letter-spacing:0.12em;color:#AAAAAA;">Step 2</div>
    <div style="font-weight:800;font-size:1.15rem;margin-top:0.2rem;">Artifacts</div>
    <div style="color:#6B6B6B;font-size:0.85rem;margin-top:0.1rem;">quant or qual</div>
  </div>
  <div style="display:flex;align-items:center;justify-content:center;color:#1A1A1A;">↑</div>
  <div></div>
  <div style="display:flex;align-items:center;justify-content:center;color:#1A1A1A;">↓</div>
  <div style="border:1px solid #1A1A1A;padding:0.8rem 1rem;text-align:center;">
    <div style="font-family:'JetBrains Mono',monospace;font-size:0.62rem;text-transform:uppercase;letter-spacing:0.12em;color:#AAAAAA;">Step 4</div>
    <div style="font-weight:800;font-size:1.15rem;margin-top:0.2rem;">Decision</div>
  </div>
  <div style="display:flex;align-items:center;justify-content:center;color:#1A1A1A;">←</div>
  <div style="border:1px solid #1A1A1A;padding:0.8rem 1rem;text-align:center;">
    <div style="font-family:'JetBrains Mono',monospace;font-size:0.62rem;text-transform:uppercase;letter-spacing:0.12em;color:#AAAAAA;">Step 3</div>
    <div style="font-weight:800;font-size:1.15rem;margin-top:0.2rem;">Study</div>
  </div>
</div>

---

# From data to decision

<div style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);width:90%;max-width:60rem;">
  <div style="display:grid;grid-template-columns:1fr 60px 1fr 60px 1fr;align-items:center;">
    <div style="text-align:center;">
      <div style="font-weight:800;font-size:1.6rem;letter-spacing:-0.02em;">Data</div>
      <div style="color:#6B6B6B;font-size:1.05rem;margin-top:0.5rem;">raw, noisy</div>
    </div>
    <div style="text-align:center;">
      <div style="font-family:'JetBrains Mono',monospace;font-size:0.68rem;text-transform:uppercase;letter-spacing:0.12em;color:#AAAAAA;margin-bottom:0.3rem;">extract signal</div>
      <div style="font-size:1.4rem;color:#1A1A1A;">→</div>
    </div>
    <div style="text-align:center;">
      <div style="font-weight:800;font-size:1.6rem;letter-spacing:-0.02em;color:#FF00FF;">Metric</div>
      <div style="color:#6B6B6B;font-size:1.05rem;margin-top:0.5rem;">what we measure</div>
    </div>
    <div style="text-align:center;">
      <div style="font-size:1.4rem;color:#1A1A1A;">→</div>
    </div>
    <div style="text-align:center;">
      <div style="font-weight:800;font-size:1.6rem;letter-spacing:-0.02em;">Decision</div>
      <div style="color:#6B6B6B;font-size:1.05rem;margin-top:0.5rem;">what we do next</div>
    </div>
  </div>
  <p style="margin-top:2.4rem;text-align:center;color:#C0392B;font-size:1.15rem;font-weight:700;line-height:1.4;">Wrong signal &rarr; wrong metric &rarr; wrong decision</p>
</div>

<!--
Tim brings a concrete data → metric → decision walkthrough verbally. Red callout under the schema underlines why metric work deserves the time: if the extracted signal is wrong, the metric is wrong, and the decision built on it is wrong. The whole loop on the next slide depends on the signal being right.
-->

---

# The loop compounds over time

<div style="display:flex;justify-content:center;margin-top:1rem;">
<svg viewBox="0 0 700 280" style="width:60%;max-width:620px;overflow:visible;">
  <defs>
    <marker id="arrGreen" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#2A8C5A"/>
    </marker>
    <marker id="arrRed" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#C0392B"/>
    </marker>
  </defs>

  <!-- X axis -->
  <line x1="50" y1="235" x2="620" y2="235" stroke="#1A1A1A" stroke-width="1.5"/>
  <polygon points="620,235 610,230 610,240" fill="#1A1A1A"/>
  <text x="612" y="248" text-anchor="end" style="font:5px 'JetBrains Mono',monospace;letter-spacing:0.08em;fill:#AAAAAA;text-transform:uppercase;">time</text>

  <!-- Origin dot -->
  <circle cx="60" cy="210" r="4" fill="#1A1A1A"/>

  <!-- LOWER TRAJECTORY: no measurement — green wins and red losses cancel out -->
  <line x1="60" y1="210" x2="150" y2="185" stroke="#2A8C5A" stroke-width="3"/>
  <line x1="150" y1="185" x2="235" y2="210" stroke="#C0392B" stroke-width="3"/>
  <line x1="235" y1="210" x2="325" y2="185" stroke="#2A8C5A" stroke-width="3"/>
  <line x1="325" y1="185" x2="410" y2="215" stroke="#C0392B" stroke-width="3"/>
  <line x1="410" y1="215" x2="500" y2="195" stroke="#2A8C5A" stroke-width="3"/>
  <line x1="500" y1="195" x2="585" y2="220" stroke="#C0392B" stroke-width="3" marker-end="url(#arrRed)"/>

  <!-- UPPER TRAJECTORY: with measurement — green ships, gray "caught, not shipped" plateaus -->
  <line x1="60" y1="210" x2="150" y2="175" stroke="#2A8C5A" stroke-width="4"/>
  <line x1="150" y1="175" x2="235" y2="175" stroke="#AAAAAA" stroke-width="3" stroke-dasharray="5 4"/>
  <line x1="235" y1="175" x2="325" y2="130" stroke="#2A8C5A" stroke-width="4"/>
  <line x1="325" y1="130" x2="410" y2="130" stroke="#AAAAAA" stroke-width="3" stroke-dasharray="5 4"/>
  <line x1="410" y1="130" x2="500" y2="80" stroke="#2A8C5A" stroke-width="4"/>
  <line x1="500" y1="80" x2="585" y2="50" stroke="#2A8C5A" stroke-width="4" marker-end="url(#arrGreen)"/>

  <!-- Compact top-left legend (inline style to beat Slidev theme CSS) -->
  <text x="55" y="20" style="font:700 6px 'JetBrains Mono',monospace;letter-spacing:0.1em;fill:#1A1A1A;">WITH MEASUREMENT</text>
  <text x="55" y="30" style="font:6px 'JetBrains Mono',monospace;letter-spacing:0.1em;fill:#AAAAAA;">NO MEASUREMENT</text>
</svg>
</div>

<div style="display:flex;justify-content:center;gap:2rem;margin-top:0.8rem;font-family:'JetBrains Mono',monospace;font-size:0.68rem;letter-spacing:0.08em;text-transform:uppercase;">
  <span><span style="display:inline-block;width:14px;height:3px;background:#2A8C5A;vertical-align:middle;margin-right:0.4rem;"></span>good change shipped</span>
  <span><span style="display:inline-block;width:14px;height:3px;background:#AAAAAA;vertical-align:middle;margin-right:0.4rem;"></span>caught, not shipped</span>
  <span><span style="display:inline-block;width:14px;height:3px;background:#C0392B;vertical-align:middle;margin-right:0.4rem;"></span>bad change shipped</span>
</div>

<!--
Slide thesis: with measurement, you ship the good changes and catch the bad ones before they harm the product. Without measurement, you ship everything blindly — wins and losses cancel out and you stay near zero. The compounding gap between the two trajectories is what the rest of the course buys you.

Design note: green and red are normally forbidden by the locked palette. Allowed here as a one-off because the pedagogical meaning (universally readable "good = green / bad = red") outweighs design uniformity, and Tim explicitly asked for it.

Speaker beats:
- Both lines start at the same point. Same product.
- Upper line (with measurement): green segments = changes you measured, saw they worked, kept. Gray plateaus = changes you measured, saw they hurt, rolled back before they shipped. No red on this line — the loop filters out the bad ones.
- Lower line (without measurement): you ship everything. Some bets win (green), some lose (red). On average it cancels out.
- The point is not that intuition is wrong. A single intuition-driven bet can be a massive win (iPhone-style). The point is across many decisions, the systematic approach dominates. Data reduces the variance of the bet, it does not eliminate vision.
- Bridge to next section: this only works if you have something to measure. That is the whole rest of the course.
-->

---
layout: section
class: tint-rose
---

## 02

# What is<br>a metric

---

# What is a metric?

<p style="font-size:1.4rem;line-height:1.55;">Product metrics are <span class="pink">quantifiable measures</span> that help teams assess the performance, usage, and overall success of a product or feature.</p>

<div style="position:absolute;bottom:3rem;left:3.5rem;font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#AAAAAA;letter-spacing:0.1em;text-transform:uppercase;">
  <a href="https://www.atlassian.com/agile/product-management/product-metrics" target="_blank" style="color:inherit;text-decoration:none;">atlassian.com / agile / product-management / product-metrics</a>
</div>

---

<div style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);width:90%;max-width:62rem;display:flex;flex-direction:column;gap:3.5rem;text-align:center;">
  <div>
    <h1 style="font-size:2.4rem;line-height:1.3;margin:0;font-family:'Bricolage Grotesque',sans-serif;font-weight:700;">"A good metric changes the way you <span class="pink">behave</span>."</h1>
    <p style="margin-top:1rem;font-family:'JetBrains Mono',monospace;font-size:0.72rem;text-transform:uppercase;letter-spacing:0.15em;color:#AAAAAA;">Alistair Croll &amp; Ben Yoskovitz · Lean Analytics · 2013</p>
  </div>
  <div>
    <h1 style="font-size:2.4rem;line-height:1.3;margin:0;font-family:'Bricolage Grotesque',sans-serif;font-weight:700;">"If you cannot <span class="pink">measure</span> it, you cannot <span class="pink">improve</span> it."</h1>
    <p style="margin-top:1rem;font-family:'JetBrains Mono',monospace;font-size:0.72rem;text-transform:uppercase;letter-spacing:0.15em;color:#AAAAAA;">Lord Kelvin · 1883</p>
  </div>
</div>

<!--
Two foundational quotes for what a metric is. Use Croll & Yoskovitz to frame the behavioral test ("if you can't answer what you'd do differently, the metric is noise"). Use Kelvin to frame the measurement-as-prerequisite-for-improvement angle.

"Whenever you look at a metric, ask yourself: what will I do differently based on this information? If you can't answer that question, you probably shouldn't worry about the metric too much." — Croll & Yoskovitz expanded.

Kelvin's full quote (1883): "When you can measure what you are speaking about, and express it in numbers, you know something about it; but when you cannot measure it, when you cannot express it in numbers, your knowledge is of a meagre and unsatisfactory kind." Often misattributed to Drucker, originally from Kelvin's "Electrical Units of Measurement" lecture.
-->

---
layout: section
class: tint-mint
---

## 03

# Product metrics<br>vs business metrics

---

# What each layer answers

<div style="margin-top:2rem;display:flex;flex-direction:column;gap:1.8rem;">
  <div>
    <div style="font-weight:800;font-size:1.6rem;margin-bottom:0.4rem;">Business metrics</div>
    <div style="color:#1A1A1A;font-size:1.4rem;">How good is your <span class="pink">business</span>?</div>
  </div>
  <div>
    <div style="font-weight:800;font-size:1.6rem;margin-bottom:0.4rem;">Product metrics</div>
    <div style="color:#1A1A1A;font-size:1.4rem;">How good is your <span class="pink">product</span>?</div>
  </div>
</div>

---
layout: statement
---

# Business metrics<br>aren't a <span class="pink">strategy</span>

---

# Optimizing business metrics is not the same as building a better product

<p v-click="1" style="color:#1A1A1A;font-size:1.2rem;margin-top:1.5rem;">You can hit business metrics by raising prices, making cancellation harder, adding friction to the free tier.</p>

<p v-click="2" style="margin-top:1.5rem;font-size:1.2rem;color:#1A1A1A;">In the short term this works, but in the long term you'll lose the competition to whoever is actually building a better product.</p>

<p v-click="3" style="margin-top:2rem;font-size:1.25rem;font-weight:700;">You can win the metric and <span class="pink">lose</span> the product.</p>

---

# Marketplace example

<p style="color:#1A1A1A;font-size:1.2rem;margin-top:0.5rem;">Revenue comes from <span class="pink">sellers</span>. The product is mostly for buyers, who never pay you directly.</p>

<div style="margin-top:3rem;display:flex;align-items:center;justify-content:center;gap:3rem;">
  <div style="width:200px;height:200px;border-radius:50%;border:3px solid #1A1A1A;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:1.5rem;">Buyers</div>
  <div style="font-size:3rem;color:#1A1A1A;line-height:1;">⇄</div>
  <div style="width:200px;height:200px;border-radius:50%;border:3px solid #FF00FF;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:1.5rem;color:#FF00FF;">Sellers</div>
</div>

<p v-click="1" style="margin-top:2rem;text-align:center;font-size:1.25rem;font-weight:700;">No buyers &rarr; no sellers &rarr; no revenue.</p>

---

# Build the best product. Business metrics <span class="pink">follow</span>

<div style="margin-top:2rem;display:flex;flex-direction:column;gap:1.1rem;">
  <div>
    <span style="font-weight:800;font-size:1.25rem;">Spotify</span>
    <span style="margin-left:0.6rem;font-size:1.15rem;color:#1A1A1A;">The best service for listening to music and podcasts</span>
  </div>
  <div>
    <span style="font-weight:800;font-size:1.25rem;">Airbnb</span>
    <span style="margin-left:0.6rem;font-size:1.15rem;color:#1A1A1A;">The best service for travelers looking for a place to stay</span>
  </div>
  <div>
    <span style="font-weight:800;font-size:1.25rem;">Wallapop</span>
    <span style="margin-left:0.6rem;font-size:1.15rem;color:#1A1A1A;">The best service for buying and selling second-hand things</span>
  </div>
</div>

<p style="margin-top:2.5rem;font-size:1.2rem;color:#1A1A1A;line-height:1.5;">Focus on <span class="pink">product metrics</span> as the lever you can pull to move business metrics over time.</p>

<!--
Wallapop is Barcelona. Students know it.
None of these companies said "let's maximize revenue." They said "let's be the best at this one thing."

Merged from prior "Focus on product metrics" slide: a good product metric reflects the value your product delivers AND connects to business metrics. Verbal layer can unpack both criteria using the three examples.
-->

---
layout: statement
---

<h1 style="font-size:2.6rem;line-height:1.2;margin-bottom:2.5rem;">Imagine you're CPO at Spotify.<br>Which metrics would you track?</h1>

<img src="/spotify.png" style="width:110px;margin:0 auto;display:block;" />

<!--
Open discussion. Let the room throw out ideas before steering.
Anchor to the three questions later: which can Spotify track? which are correct? which matter more?
-->

---

# This creates real questions

<ol style="margin-top:1.5rem;list-style:none;padding:0;">
  <li style="display:flex;gap:1rem;margin-bottom:0.85rem;">
    <span style="font-family:'JetBrains Mono',monospace;font-size:0.95rem;color:#AAAAAA;flex-shrink:0;width:2rem;">01</span>
    <span style="font-size:1.15rem;">Which metrics matter more than others?</span>
  </li>
  <li v-click="1" style="display:flex;gap:1rem;margin-bottom:0.85rem;">
    <span style="font-family:'JetBrains Mono',monospace;font-size:0.95rem;color:#AAAAAA;flex-shrink:0;width:2rem;">02</span>
    <span style="font-size:1.15rem;">How do you organize them?</span>
  </li>
  <li v-click="2" style="display:flex;gap:1rem;margin-bottom:0.85rem;">
    <span style="font-family:'JetBrains Mono',monospace;font-size:0.95rem;color:#AAAAAA;flex-shrink:0;width:2rem;">03</span>
    <span style="font-size:1.15rem;">How do you align different teams around shared metric goals?</span>
  </li>
  <li v-click="3" style="display:flex;gap:1rem;margin-bottom:0.85rem;">
    <span style="font-family:'JetBrains Mono',monospace;font-size:0.95rem;color:#AAAAAA;flex-shrink:0;width:2rem;">04</span>
    <span style="font-size:1.15rem;">How do you connect product metrics to business metrics?</span>
  </li>
  <li v-click="4" style="display:flex;gap:1rem;margin-bottom:0.85rem;">
    <span style="font-family:'JetBrains Mono',monospace;font-size:0.95rem;color:#AAAAAA;flex-shrink:0;width:2rem;">05</span>
    <span style="font-size:1.15rem;">How do you choose between two valid product metrics?</span>
  </li>
  <li v-click="5" style="display:flex;gap:1rem;">
    <span style="font-family:'JetBrains Mono',monospace;font-size:0.95rem;color:#AAAAAA;flex-shrink:0;width:2rem;">06</span>
    <span style="font-size:1.15rem;">How do you design a product metric from scratch?</span>
  </li>
</ol>

<!--
Not answering all of them definitively. Building intuition for how different companies and practitioners approach them.
-->

---
layout: section
class: tint-sky
---

## 04

# Metrics<br>frameworks

---

# Why frameworks exist

Every product starts with no metrics, and picking from infinite options is the cold-start problem.

<p style="margin-top:1.5rem;">Frameworks are pre-built starting points that give you a default structure when you have nothing.</p>

<p style="margin-top:2rem;font-size:1.4rem;font-weight:600;">The real question: how <span class="pink">systematizable</span> is metric choice?</p>

---

# Every metric has five properties

<div style="margin-top:1.5rem;display:flex;flex-direction:column;gap:1.1rem;">
  <div style="display:flex;gap:1rem;align-items:baseline;">
    <span style="font-family:'JetBrains Mono',monospace;font-size:0.95rem;color:#AAAAAA;flex-shrink:0;width:2rem;">01</span>
    <span style="font-size:1.15rem;"><strong>Funnel stage.</strong> Where in the user journey: acquisition, activation, retention, referral, revenue.</span>
  </div>
  <div style="display:flex;gap:1rem;align-items:baseline;">
    <span style="font-family:'JetBrains Mono',monospace;font-size:0.95rem;color:#AAAAAA;flex-shrink:0;width:2rem;">02</span>
    <span style="font-size:1.15rem;"><strong>Domain.</strong> What aspect of the company: business, product, or user experience.</span>
  </div>
  <div style="display:flex;gap:1rem;align-items:baseline;">
    <span style="font-family:'JetBrains Mono',monospace;font-size:0.95rem;color:#AAAAAA;flex-shrink:0;width:2rem;">03</span>
    <span style="font-size:1.15rem;"><strong>Time orientation.</strong> Leading or lagging.</span>
  </div>
  <div style="display:flex;gap:1rem;align-items:baseline;">
    <span style="font-family:'JetBrains Mono',monospace;font-size:0.95rem;color:#AAAAAA;flex-shrink:0;width:2rem;">04</span>
    <span style="font-size:1.15rem;"><strong>Level.</strong> L1, L2, L3 and so on. Where in the metric tree.</span>
  </div>
  <div style="display:flex;gap:1rem;align-items:baseline;">
    <span style="font-family:'JetBrains Mono',monospace;font-size:0.95rem;color:#AAAAAA;flex-shrink:0;width:2rem;">05</span>
    <span style="font-size:1.15rem;"><strong>Granularity.</strong> Whole product, feature, cohort, or per-user.</span>
  </div>
</div>

---

# Frameworks are projections

<p style="color:#1A1A1A;font-size:1.2rem;margin-top:0.5rem;">Each framework picks one or two properties and organizes metrics around them.</p>

<div style="margin-top:2rem;display:flex;flex-direction:column;gap:0.9rem;">
  <div style="display:flex;align-items:baseline;gap:1rem;">
    <span style="font-weight:800;font-size:1.15rem;width:14rem;flex-shrink:0;">AARRR</span>
    <span style="color:#AAAAAA;flex-shrink:0;">→</span>
    <span style="font-size:1.15rem;color:#1A1A1A;">Funnel stage</span>
  </div>
  <div style="display:flex;align-items:baseline;gap:1rem;">
    <span style="font-weight:800;font-size:1.15rem;width:14rem;flex-shrink:0;">Metric tree</span>
    <span style="color:#AAAAAA;flex-shrink:0;">→</span>
    <span style="font-size:1.15rem;color:#1A1A1A;">Level (full L1 → Ln)</span>
  </div>
  <div style="display:flex;align-items:baseline;gap:1rem;">
    <span style="font-weight:800;font-size:1.15rem;width:14rem;flex-shrink:0;">North Star Metric</span>
    <span style="color:#AAAAAA;flex-shrink:0;">→</span>
    <span style="font-size:1.15rem;color:#1A1A1A;">Level (L1 vertex)</span>
  </div>
  <div style="display:flex;align-items:baseline;gap:1rem;">
    <span style="font-weight:800;font-size:1.15rem;width:14rem;flex-shrink:0;">HEART</span>
    <span style="color:#AAAAAA;flex-shrink:0;">→</span>
    <span style="font-size:1.15rem;color:#1A1A1A;">Domain, UX cell</span>
  </div>
  <div style="display:flex;align-items:baseline;gap:1rem;">
    <span style="font-weight:800;font-size:1.15rem;width:14rem;flex-shrink:0;">Leading / lagging</span>
    <span style="color:#AAAAAA;flex-shrink:0;">→</span>
    <span style="font-size:1.15rem;color:#1A1A1A;">Time orientation</span>
  </div>
  <div style="display:flex;align-items:baseline;gap:1rem;">
    <span style="font-weight:800;font-size:1.15rem;width:14rem;flex-shrink:0;">Feature usage</span>
    <span style="color:#AAAAAA;flex-shrink:0;">→</span>
    <span style="font-size:1.15rem;color:#1A1A1A;">Granularity</span>
  </div>
</div>

---

# Product vs UX metrics

<p style="color:#1A1A1A;font-size:1.15rem;margin-top:0.5rem;line-height:1.5;">Two adjacent layers of measurement. Same product, different owner and different question.</p>

<div style="margin-top:1.6rem;display:grid;grid-template-columns:1fr 1fr;gap:2.5rem;">

  <div>
    <div style="font-family:'JetBrains Mono',monospace;font-size:0.72rem;color:#FF00FF;letter-spacing:0.12em;text-transform:uppercase;margin-bottom:0.7rem;">Product metrics</div>
    <p style="color:#1A1A1A;font-size:1rem;line-height:1.5;margin:0 0 0.7rem 0;"><strong>Owner</strong>: PM, growth, analytics</p>
    <p style="color:#1A1A1A;font-size:1rem;line-height:1.5;margin:0 0 0.7rem 0;"><strong>Question</strong>: is the business moving</p>
    <p style="color:#1A1A1A;font-size:1rem;line-height:1.5;margin:0;"><strong>Frameworks</strong>: AARRR, NSM, metric tree, OMTM</p>
    <p style="color:#1A1A1A;font-size:1rem;line-height:1.5;margin-top:0.7rem;"><strong>Examples</strong>: DAU, retention, MRR, CAC, LTV, free-to-paid CR</p>
  </div>

  <div>
    <div style="font-family:'JetBrains Mono',monospace;font-size:0.72rem;color:#FF00FF;letter-spacing:0.12em;text-transform:uppercase;margin-bottom:0.7rem;">UX metrics</div>
    <p style="color:#1A1A1A;font-size:1rem;line-height:1.5;margin:0 0 0.7rem 0;"><strong>Owner</strong>: UX research, design</p>
    <p style="color:#1A1A1A;font-size:1rem;line-height:1.5;margin:0 0 0.7rem 0;"><strong>Question</strong>: does the feature work for the user</p>
    <p style="color:#1A1A1A;font-size:1rem;line-height:1.5;margin:0;"><strong>Frameworks</strong>: HEART (Google)</p>
    <p style="color:#1A1A1A;font-size:1rem;line-height:1.5;margin-top:0.7rem;"><strong>Examples</strong>: CSAT, task success rate, time-to-complete, error rate, CES</p>
  </div>

</div>

<div style="position:absolute;bottom:1rem;left:3.5rem;font-family:'JetBrains Mono',monospace;font-size:0.65rem;color:#AAAAAA;letter-spacing:0.1em;text-transform:uppercase;">
  <a href="https://medium.com/design-bootcamp/ux-and-product-metrics-a-guide-to-numbers-worth-measuring-84bc196481b4" target="_blank" style="color:inherit;text-decoration:none;">medium / bootcamp / ux and product metrics</a>
</div>

<!--
Distinction added to disambiguate HEART. HEART comes from Google UX research, measures whether a feature works for the user. AARRR / NSM / metric tree measure whether the product moves business outcomes. Both layers are real, both useful, owned by different roles.

Speaker beats:
- Same product, two adjacent measurement layers
- PM cares: is the business moving (DAU, retention, MRR, conversion)
- UX research cares: is this feature delivering a good experience (task success, CSAT, error rate)
- HEART is the canonical UX framework — Happiness, Engagement, Adoption, Retention, Task success. It's a feature-quality framework, not a funnel framework
- In practice, mature teams use both. PM uses AARRR/NSM at the product level, designer uses HEART for a specific feature being designed or evaluated
-->

---

# A metric is a point on five axes

<p style="color:#1A1A1A;font-size:1.2rem;margin-top:0.3rem;">Example: <strong>DAU / MAU</strong>. Reading top-to-bottom gives its position on each dimension.</p>

<div style="margin-top:2rem;display:flex;flex-direction:column;gap:1.1rem;">

  <div style="display:flex;align-items:center;gap:1.5rem;">
    <span style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#AAAAAA;text-transform:uppercase;letter-spacing:0.1em;width:9rem;flex-shrink:0;">Funnel stage</span>
    <div style="display:flex;gap:1.2rem;flex:1;align-items:center;">
      <span style="color:#CCCCCC;font-size:1.05rem;">acquisition</span>
      <span style="color:#CCCCCC;font-size:1.05rem;">activation</span>
      <span style="color:#FF00FF;font-size:1.05rem;font-weight:800;">engagement</span>
      <span style="color:#CCCCCC;font-size:1.05rem;">retention</span>
      <span style="color:#CCCCCC;font-size:1.05rem;">revenue</span>
    </div>
  </div>

  <div style="display:flex;align-items:center;gap:1.5rem;">
    <span style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#AAAAAA;text-transform:uppercase;letter-spacing:0.1em;width:9rem;flex-shrink:0;">Domain</span>
    <div style="display:flex;gap:1.2rem;flex:1;align-items:center;">
      <span style="color:#CCCCCC;font-size:1.05rem;">business</span>
      <span style="color:#FF00FF;font-size:1.05rem;font-weight:800;">product</span>
      <span style="color:#CCCCCC;font-size:1.05rem;">UX</span>
    </div>
  </div>

  <div style="display:flex;align-items:center;gap:1.5rem;">
    <span style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#AAAAAA;text-transform:uppercase;letter-spacing:0.1em;width:9rem;flex-shrink:0;">Time</span>
    <div style="display:flex;gap:1.2rem;flex:1;align-items:center;">
      <span style="color:#FF00FF;font-size:1.05rem;font-weight:800;">leading</span>
      <span style="color:#CCCCCC;font-size:1.05rem;">lagging</span>
    </div>
  </div>

  <div style="display:flex;align-items:center;gap:1.5rem;">
    <span style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#AAAAAA;text-transform:uppercase;letter-spacing:0.1em;width:9rem;flex-shrink:0;">Level</span>
    <div style="display:flex;gap:1.2rem;flex:1;align-items:center;">
      <span style="color:#FF00FF;font-size:1.05rem;font-weight:800;">L1</span>
      <span style="color:#CCCCCC;font-size:1.05rem;">L2</span>
      <span style="color:#CCCCCC;font-size:1.05rem;">L3</span>
      <span style="color:#CCCCCC;font-size:1.05rem;">…</span>
    </div>
  </div>

  <div style="display:flex;align-items:center;gap:1.5rem;">
    <span style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#AAAAAA;text-transform:uppercase;letter-spacing:0.1em;width:9rem;flex-shrink:0;">Granularity</span>
    <div style="display:flex;gap:1.2rem;flex:1;align-items:center;">
      <span style="color:#FF00FF;font-size:1.05rem;font-weight:800;">whole product</span>
      <span style="color:#CCCCCC;font-size:1.05rem;">feature</span>
      <span style="color:#CCCCCC;font-size:1.05rem;">cohort</span>
      <span style="color:#CCCCCC;font-size:1.05rem;">per-user</span>
    </div>
  </div>

</div>

---
layout: section
class: tint-cream
---

## 05

# Funnel stage

---

# Where in the user journey

<p style="color:#1A1A1A;font-size:1.15rem;margin-bottom:0.6rem;">What the dimension captures: at which point in the user lifecycle this metric lives.</p>

<div style="display:flex;justify-content:center;align-items:center;margin-top:0.3rem;">
  <img src="/spotify-metric-tree-demo.png" alt="Spotify metric tree demo — AARRR overlay" style="max-width:100%;max-height:17rem;object-fit:contain;display:block;" />
</div>

<div style="position:absolute;bottom:1rem;left:3.5rem;font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#AAAAAA;letter-spacing:0.1em;text-transform:uppercase;">
  <a href="https://www.slideshare.net/dmc500hats/startup-metrics-for-pirates-long-version" target="_blank" style="color:inherit;text-decoration:none;">slideshare.net / mcclure / startup metrics for pirates (2007)</a>
</div>

<!--
Speaker beats:
- AARRR origin (McClure, 2007) and the 5 stages
- Growth loops critique (Reforge, 2018). What funnels miss
- Activation as the most underrated stage
- Manychat / Avito anchor example
-->


---

# Layers intuition

<div style="margin-top:1rem;display:flex;flex-direction:column;gap:0.85rem;">
  <div style="display:grid;grid-template-columns:11rem 1fr;gap:1.3rem;align-items:baseline;">
    <span style="font-weight:800;font-size:1.1rem;">Acquisition</span>
    <span style="font-size:1rem;color:#1A1A1A;">How new users discover and arrive at the product</span>
  </div>
  <div style="display:grid;grid-template-columns:11rem 1fr;gap:1.3rem;align-items:baseline;">
    <span style="font-weight:800;font-size:1.1rem;">Activation</span>
    <span style="font-size:1rem;color:#1A1A1A;">User reaches the first moment of meaningful product value</span>
  </div>
  <div style="display:grid;grid-template-columns:11rem 1fr;gap:1.3rem;align-items:baseline;">
    <span style="font-weight:800;font-size:1.1rem;">Engagement</span>
    <span style="font-size:1rem;color:#1A1A1A;">How often and how deeply users interact with the product</span>
  </div>
  <div style="display:grid;grid-template-columns:11rem 1fr;gap:1.3rem;align-items:baseline;">
    <span style="font-weight:800;font-size:1.1rem;">Retention</span>
    <span style="font-size:1rem;color:#1A1A1A;">Users return over time and the product becomes part of their routine</span>
  </div>
  <div style="display:grid;grid-template-columns:11rem 1fr;gap:1.3rem;align-items:baseline;">
    <span style="font-weight:800;font-size:1.1rem;">Churn</span>
    <span style="font-size:1rem;color:#1A1A1A;">Users stop returning and exit the active base</span>
  </div>
  <div style="display:grid;grid-template-columns:11rem 1fr;gap:1.3rem;align-items:baseline;">
    <span style="font-weight:800;font-size:1.1rem;">Monetization</span>
    <span style="font-size:1rem;color:#1A1A1A;">User commits financially and the product captures revenue</span>
  </div>
</div>

<div style="position:absolute;bottom:1rem;left:3.5rem;font-family:'JetBrains Mono',monospace;font-size:0.65rem;color:#AAAAAA;letter-spacing:0.1em;text-transform:uppercase;">
  <a href="https://medium.com/design-bootcamp/product-metrics-for-dummies-ii-how-to-read-data-before-you-use-them-5e79f9e1d737" target="_blank" style="color:inherit;text-decoration:none;">medium / bootcamp / product metrics for dummies ii</a>
</div>

<!--
Sidebar / reference slide. Plain-English intuition for each AARRR stage, restaurant metaphor adapted from Blanca Serrano Marco's Medium article. Drop in right after the journey image and before the metric definitions.

The metaphor:
- Acquisition = curiosity at the door
- Activation = the first bite delivers value (Aha moment in lasagna form)
- Engagement = how long the guest stays inside, depth of interaction
- Retention = guests come back next week as regulars
- Churn = tried once, never returned
- Monetization = curiosity becomes commitment, they order a full plate and pay

Helps anchor the abstract funnel for stat-naive students before the metric definitions land. Reference link sits at the bottom-left for students who want to follow up.
-->

---

# Acquisition metrics

<div style="margin-top:1.5rem;display:flex;flex-direction:column;gap:1.1rem;">
  <div style="display:grid;grid-template-columns:16rem 1fr;gap:1.5rem;align-items:baseline;">
    <span style="font-weight:800;font-size:1.2rem;">Sign-ups</span>
    <span style="font-size:1.1rem;color:#1A1A1A;">Count of new free users in the period</span>
  </div>
  <div style="display:grid;grid-template-columns:16rem 1fr;gap:1.5rem;align-items:baseline;">
    <span style="font-weight:800;font-size:1.2rem;">Visitor → Sign-up CR</span>
    <span style="font-size:1.1rem;color:#1A1A1A;">Share of unique visitors who create an account</span>
  </div>
  <div style="display:grid;grid-template-columns:16rem 1fr;gap:1.5rem;align-items:baseline;">
    <span style="font-weight:800;font-size:1.2rem;">CAC</span>
    <span style="font-size:1.1rem;color:#1A1A1A;">Total acquisition spend ÷ acquired accounts. Most teams report per paying account</span>
  </div>
</div>

---

# Activation metrics

<div style="margin-top:1.2rem;display:flex;flex-direction:column;gap:0.9rem;">
  <div style="display:grid;grid-template-columns:16rem 1fr;gap:1.5rem;align-items:baseline;">
    <span style="font-weight:800;font-size:1.15rem;">Setup rate</span>
    <span style="font-size:1.05rem;color:#1A1A1A;">Share of new users who complete the Setup steps within a defined window</span>
  </div>
  <div style="display:grid;grid-template-columns:16rem 1fr;gap:1.5rem;align-items:baseline;">
    <span style="font-weight:800;font-size:1.15rem;">Aha rate</span>
    <span style="font-size:1.05rem;color:#1A1A1A;">Share of new users who reach the Aha milestone within a defined window</span>
  </div>
  <div style="display:grid;grid-template-columns:16rem 1fr;gap:1.5rem;align-items:baseline;">
    <span style="font-weight:800;font-size:1.15rem;">Activation rate</span>
    <span style="font-size:1.05rem;color:#1A1A1A;">Share of new users who meet the team's full activation criterion within a defined window</span>
  </div>
  <div style="display:grid;grid-template-columns:16rem 1fr;gap:1.5rem;align-items:baseline;">
    <span style="font-weight:800;font-size:1.15rem;">Habit rate</span>
    <span style="font-size:1.05rem;color:#1A1A1A;">Share of new users who reach regular self-driven use within a defined window</span>
  </div>
  <div style="display:grid;grid-template-columns:16rem 1fr;gap:1.5rem;align-items:baseline;">
    <span style="font-weight:800;font-size:1.15rem;">Time-to-Aha</span>
    <span style="font-size:1.05rem;color:#1A1A1A;">Median time from sign-up to the first Aha event</span>
  </div>
</div>

<!--
Aha rate vs Activation rate:
- Aha rate is the strict Reforge value-moment metric (data-validated milestone)
- Activation rate is the team-defined threshold which may equal Aha or include extra criteria (e.g., Aha + day-7 retained, Aha + first-payment, completed onboarding checklist)
- Common in industry to use the words interchangeably. Worth fixing here.
- Free → Paid CR moved to Monetization slide. It is downstream of activation but a monetization conversion, not an activation event.
-->

---

# Setup → Aha → Habit

<div style="display:grid;grid-template-columns:1fr 1.05fr;gap:2.5rem;margin-top:0.8rem;align-items:start;">
  <div>
    <p style="color:#1A1A1A;font-size:1.0rem;margin:0 0 1rem 0;line-height:1.4;">Reforge's activation framework defines three distinct moments inside the activation funnel.</p>
    <div style="display:flex;flex-direction:column;gap:0.85rem;">
      <div>
        <span style="font-weight:800;font-size:1.05rem;">Setup moment</span>
        <p style="font-size:0.9rem;color:#1A1A1A;margin:0.15rem 0 0 0;line-height:1.4;">The minimum required actions a new user must take before they can begin to experience the product's core value</p>
      </div>
      <div>
        <span style="font-weight:800;font-size:1.05rem;">Aha moment</span>
        <p style="font-size:0.9rem;color:#1A1A1A;margin:0.15rem 0 0 0;line-height:1.4;">The first time a user experiences the product's core value</p>
      </div>
      <div>
        <span style="font-weight:800;font-size:1.05rem;">Habit moment</span>
        <p style="font-size:0.9rem;color:#1A1A1A;margin:0.15rem 0 0 0;line-height:1.4;">The point at which usage of the product becomes regular and self-directed</p>
      </div>
    </div>
  </div>
  <div style="display:flex;align-items:start;justify-content:center;">
    <img src="/reforge-setup-aha-habit.avif" alt="Reforge Setup → Aha → Habit activation funnel" style="max-width:100%;max-height:22rem;object-fit:contain;display:block;" />
  </div>
</div>

<div style="position:absolute;bottom:0.9rem;left:3.5rem;font-family:'JetBrains Mono',monospace;font-size:0.65rem;color:#AAAAAA;letter-spacing:0.1em;text-transform:uppercase;">
  <a href="https://www.reforge.com/guides/define-customer-activation-moments" target="_blank" style="color:inherit;text-decoration:none;">reforge.com / guides / define-customer-activation-moments</a>
</div>

---

# Example: Facebook

<p style="color:#1A1A1A;font-size:1.15rem;margin-top:0.8rem;line-height:1.5;">Same framework, walked through one product. The classic case from Facebook's growth team, circa 2008.</p>

<div style="margin-top:1.6rem;display:flex;flex-direction:column;gap:1.1rem;">
  <div style="display:grid;grid-template-columns:14rem 1fr;gap:1.5rem;align-items:baseline;">
    <span style="font-weight:800;font-size:1.15rem;">Setup moment</span>
    <span style="font-size:1.05rem;color:#1A1A1A;">Account created and basic profile filled in</span>
  </div>
  <div style="display:grid;grid-template-columns:14rem 1fr;gap:1.5rem;align-items:baseline;">
    <span style="font-weight:800;font-size:1.15rem;">Aha moment</span>
    <span style="font-size:1.05rem;color:#1A1A1A;"><span class="pink">7 friends added in the first 10 days</span></span>
  </div>
  <div style="display:grid;grid-template-columns:14rem 1fr;gap:1.5rem;align-items:baseline;">
    <span style="font-weight:800;font-size:1.15rem;">Habit moment</span>
    <span style="font-size:1.05rem;color:#1A1A1A;">Returning to the feed across multiple sessions per week, sustained over consecutive weeks*</span>
  </div>
</div>

<p style="margin-top:1.4rem;font-size:1rem;color:#1A1A1A;line-height:1.5;">Each moment is one concrete user action with a defined window. The numbers come from data, not from a brainstorm.</p>

<div style="position:absolute;bottom:0.9rem;left:3.5rem;font-family:'JetBrains Mono',monospace;font-size:0.65rem;color:#AAAAAA;letter-spacing:0.1em;text-transform:uppercase;">
  <a href="https://mode.com/blog/facebook-aha-moment-simpler-than-you-think/" target="_blank" style="color:inherit;text-decoration:none;">mode.com / blog / facebook's aha moment was simpler than you think</a>
</div>

<!--
The Facebook 7-friends-in-10-days finding is widely attributed to the growth team led by Chamath Palihapitiya around 2007–2008. It became the textbook example because it crystallized the shift from "we think users get value when X" to "we measured which milestone separates retained users from churned ones."

Speaker beats:
- Setup is descriptive, not a single number — it's the entry condition (account + profile)
- Aha is a precise threshold: 7 friends, 10-day window. Both numbers came from cohort analysis.
- Habit threshold is less famous publicly. Tim can fill in or leave as "the point where weekly visits sustain over multiple weeks."
- Other industry examples Tim may mention verbally: Slack ~2000 messages in a workspace for Aha, Dropbox's 1-file-in-1-folder-on-1-device for Aha.
-->

---

# Aha is a data-validated segment

<p style="color:#1A1A1A;font-size:1.2rem;margin-top:1rem;line-height:1.5;">The Aha moment is the threshold that separates users who retain from users who do not. It comes out of data, not out of a slogan.</p>

<div style="margin-top:1.8rem;display:flex;flex-direction:column;gap:1.2rem;">
  <div>
    <div style="font-weight:800;font-size:1.15rem;margin-bottom:0.25rem;">Method</div>
    <p style="font-size:1.05rem;color:#1A1A1A;line-height:1.5;margin:0;">For each candidate milestone in the first N days after sign-up, compare long-term retention of users who reach it versus users who do not. The milestone with the largest, durable retention gap is your Aha</p>
  </div>
  <div>
    <div style="font-weight:800;font-size:1.15rem;margin-bottom:0.25rem;">Business meaning</div>
    <p style="font-size:1.05rem;color:#1A1A1A;line-height:1.5;margin:0;">Aha defines the segment your onboarding has to deliver into. Below the threshold churn dominates, above it retention stabilizes. The same logic applies to Setup and Habit, with each moment validated against its own retention curve</p>
  </div>
</div>

<div style="position:absolute;bottom:0.9rem;left:3.5rem;font-family:'JetBrains Mono',monospace;font-size:0.65rem;color:#AAAAAA;letter-spacing:0.1em;text-transform:uppercase;">
  <a href="https://gopractice.io/product/finding-your-products-aha-moment-a-qualitative-plus-quantitative-approach/" target="_blank" style="color:inherit;text-decoration:none;">gopractice.io / finding your product's aha moment</a>
</div>

<!--
This slide carries Tim's main thesis: Setup / Aha / Habit are not qualitative labels, they are data-validated milestones. Each one is defined by what the user data actually shows about retention.

Speaker beats:
- Aha is found, not chosen. The team picks ~10–20 candidate milestones (signed up, posted, invited a friend, completed a session, etc.) and runs the cohort comparison.
- The Aha threshold becomes a segment definition: "users past Aha" is the cohort the team optimizes onboarding to expand.
- Same for Setup (entry condition) and Habit (regular self-directed use): both are validated against retention curves, not chosen by feel.
- Connects back to Activation metrics slide: the rates (Setup rate, Aha rate, Habit rate) are only useful once the underlying thresholds are data-validated. Otherwise you are measuring the wrong segment.
- Bridge to next slide (Aha discussion): "now that we know how the moment is defined, let's discuss what it looks like for some products you actually use."
-->

---

# Where activation framing fits

<p style="color:#1A1A1A;font-size:1.2rem;margin-top:1rem;line-height:1.5;">The Setup → Aha → Habit framework assumes a product with regular use and a short retention cycle on the scale of days or weeks. Social networks, ride-hailing, and food delivery sit cleanly inside it.</p>

<p style="color:#1A1A1A;font-size:1.2rem;margin-top:1.4rem;line-height:1.5;">When the retention horizon stretches to years (car search, real estate, insurance shopping) or use is one-time by design, the activation funnel gives little signal. These products organize around a different system because the user never has the chance to form a <span class="pink">habit</span>.</p>

<!--
Scope caveat. Tim's framing: activation funnel is the right lens only when the natural user cadence is frequent. Pulling it onto a long-cycle or one-time product produces noise.

Speaker beats:
- Activation funnel was developed inside high-cadence consumer products (Facebook, Twitter, Dropbox, Slack). Their unit of value lands within the first session or first week.
- For low-cadence products, the same data tooling still applies (cohort retention, milestone validation) but the unit of analysis is different. The "activation" question becomes "did the user convert on the one big decision," not "did they form a habit."
- For one-time products (car purchase, mortgage, wedding planning), the entire concept of habit is absent. Activation collapses to conversion, retention collapses to revisit probability under a different intent.
- This is the bridge to the broader trade-off: framework choice depends on product economics and cadence, not on what sounds modern.
-->

---
layout: statement
---

<h1 style="font-size:2.4rem;line-height:1.2;margin-bottom:2.5rem;">What is the <span class="pink">Aha moment</span> for these products?</h1>

<div style="display:flex;justify-content:center;gap:3.5rem;font-size:1.5rem;font-weight:700;color:#1A1A1A;">
  <span>Twitter</span>
  <span>Instagram</span>
  <span>Booking</span>
</div>

<!--
Open discussion. Let students propose Aha moments before steering. The question: when does a user first feel the product's core value land?

Canonical answers for reference:
- Twitter: following ~30 accounts (the feed starts to feel useful)
- Instagram: posting first photo / following ~50 accounts
- Booking: completing first booking

Sits after the Setup → Aha → Habit framework so the definition is set first, then students apply Aha to concrete cases.
-->

---
layout: statement
---

<h1 style="font-size:2.4rem;line-height:1.2;margin-bottom:2.5rem;">What is the <span class="pink">setup rate</span> for these products?</h1>

<div style="display:flex;justify-content:center;gap:3.5rem;font-size:1.5rem;font-weight:700;color:#1A1A1A;">
  <span>Pinterest</span>
  <span>Revolut</span>
  <span>Duolingo</span>
</div>

<!--
Open discussion. Students propose what counts as Setup — the required actions before a user can experience product value.

Reference answers:
- Pinterest: pick 5+ interests so the home feed has signal
- Revolut: complete KYC (ID + selfie) and top up the account so the card can be used
- Duolingo: choose a language and finish the placement / first lesson so the daily streak loop can start

Setup rate = share of new users who complete the Setup steps within a defined window. Pairs with the Aha discussion right after the framework slide.
-->

---

# Engagement metrics

<div style="margin-top:1.5rem;display:flex;flex-direction:column;gap:1.1rem;">
  <div style="display:grid;grid-template-columns:16rem 1fr;gap:1.5rem;align-items:baseline;">
    <span style="font-weight:800;font-size:1.2rem;">DAU / WAU / MAU</span>
    <span style="font-size:1.1rem;color:#1A1A1A;">Distinct active* users over a day, week, month</span>
  </div>
  <div style="display:grid;grid-template-columns:16rem 1fr;gap:1.5rem;align-items:baseline;">
    <span style="font-weight:800;font-size:1.2rem;">Stickiness</span>
    <span style="font-size:1.1rem;color:#1A1A1A;">DAU ÷ MAU. Higher means users return more often within a month</span>
  </div>
  <div style="display:grid;grid-template-columns:16rem 1fr;gap:1.5rem;align-items:baseline;">
    <span style="font-weight:800;font-size:1.2rem;">Feature adoption</span>
    <span style="font-size:1.1rem;color:#1A1A1A;">Share of active users who use a specific feature in the period</span>
  </div>
</div>

---
layout: statement
---

<h1 style="font-size:2.2rem;line-height:1.25;margin-bottom:1.4rem;">Guess the healthy <span class="pink">stickiness</span> for Instagram</h1>

<p style="font-size:1.2rem;color:#1A1A1A;text-align:center;font-weight:400;line-height:1.5;">Pick the cadence first, then the baseline. How often would a satisfied IG user actually come back?</p>

<!--
Two-step discussion narrowed to one product.

Step 1 — cadence. Daily-use feed product. Ratio is DAU/MAU.
Step 2 — baseline. Healthy DAU/MAU is 50%+ for top consumer apps. Meta family historically ~60%+. Under 40% on a feed product is a retention/engagement warning.

Class hook. "How often do you actually open Instagram on a healthy day? Now what fraction of your IG-using friends do the same?" Pulls students from pattern-matching into product-economics reasoning. After the baseline lands, point out that DAU/MAU is industry default because Facebook is daily — same ratio understates engagement for weekly or B2B products.
-->

---

# Retention metrics

<div style="margin-top:1.5rem;display:flex;flex-direction:column;gap:1.1rem;">
  <div style="display:grid;grid-template-columns:16rem 1fr;gap:1.5rem;align-items:baseline;">
    <span style="font-weight:800;font-size:1.2rem;">Business retention</span>
    <span style="font-size:1.1rem;color:#1A1A1A;">Share of subscribers still subscribed N periods later. Used in subscription products</span>
  </div>
  <div style="display:grid;grid-template-columns:16rem 1fr;gap:1.5rem;align-items:baseline;">
    <span style="font-weight:800;font-size:1.2rem;">Product retention</span>
    <span style="font-size:1.1rem;color:#1A1A1A;">Share of users who repeat a target action N periods later. Used when the value moment is not a payment</span>
  </div>
  <div style="display:grid;grid-template-columns:16rem 1fr;gap:1.5rem;align-items:baseline;">
    <span style="font-weight:800;font-size:1.2rem;">Churn rate</span>
    <span style="font-size:1.1rem;color:#1A1A1A;">1 − retention rate over the same window</span>
  </div>
  <div style="display:grid;grid-template-columns:16rem 1fr;gap:1.5rem;align-items:baseline;">
    <span style="font-weight:800;font-size:1.2rem;">Revenue retention</span>
    <span style="font-size:1.1rem;color:#1A1A1A;">Share of period-T revenue still earned at period T+N from the same cohort</span>
  </div>
</div>

---

# Monetization metrics

<div style="margin-top:1.5rem;display:flex;flex-direction:column;gap:1.1rem;">
  <div style="display:grid;grid-template-columns:16rem 1fr;gap:1.5rem;align-items:baseline;">
    <span style="font-weight:800;font-size:1.2rem;">Revenue</span>
    <span style="font-size:1.1rem;color:#1A1A1A;">Total revenue earned in the period</span>
  </div>
  <div style="display:grid;grid-template-columns:16rem 1fr;gap:1.5rem;align-items:baseline;">
    <span style="font-weight:800;font-size:1.2rem;">MRR</span>
    <span style="font-size:1.1rem;color:#1A1A1A;">Monthly Recurring Revenue. Sum of contracted monthly revenue across active subscriptions</span>
  </div>
  <div style="display:grid;grid-template-columns:16rem 1fr;gap:1.5rem;align-items:baseline;">
    <span style="font-weight:800;font-size:1.2rem;">NRR</span>
    <span style="font-size:1.1rem;color:#1A1A1A;">Net Revenue Retention. Includes expansions, contractions, and churn within the same cohort</span>
  </div>
  <div style="display:grid;grid-template-columns:16rem 1fr;gap:1.5rem;align-items:baseline;">
    <span style="font-weight:800;font-size:1.2rem;">ARPU</span>
    <span style="font-size:1.1rem;color:#1A1A1A;">Revenue ÷ all users in the period</span>
  </div>
  <div style="display:grid;grid-template-columns:16rem 1fr;gap:1.5rem;align-items:baseline;">
    <span style="font-weight:800;font-size:1.2rem;">ARPPU</span>
    <span style="font-size:1.1rem;color:#1A1A1A;">Revenue ÷ paying users in the period</span>
  </div>
  <div style="display:grid;grid-template-columns:16rem 1fr;gap:1.5rem;align-items:baseline;">
    <span style="font-weight:800;font-size:1.2rem;">Free → Paid CR</span>
    <span style="font-size:1.1rem;color:#1A1A1A;">Share of activated free users who upgrade to a paid plan within a defined window</span>
  </div>
</div>

<div style="position:absolute;bottom:1rem;left:3.5rem;font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#AAAAAA;letter-spacing:0.1em;text-transform:uppercase;">
  <a href="https://stripe.com/en-es/resources/more/what-is-monthly-recurring-revenue" target="_blank" style="color:inherit;text-decoration:none;">stripe.com / resources / monthly recurring revenue (mrr) explained</a>
</div>

---
layout: section
class: tint-lavender
---

## 06

# Domain

---

# Three different questions

<p style="color:#1A1A1A;font-size:1.1rem;margin-top:0.4rem;line-height:1.5;">Each domain answers a question the other two cannot. The same product can look healthy on one and sick on another.</p>

<div style="margin-top:1.4rem;display:grid;grid-template-columns:1fr 1fr 1fr;gap:1.5rem;">

  <div>
    <div style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#FF00FF;letter-spacing:0.12em;text-transform:uppercase;margin-bottom:0.6rem;">Business metrics</div>
    <p style="font-size:0.95rem;color:#1A1A1A;line-height:1.45;margin:0 0 0.6rem 0;font-weight:700;">Is the company making money?</p>
    <p style="font-size:0.9rem;color:#1A1A1A;line-height:1.45;margin:0 0 0.6rem 0;">Revenue, MRR, ARPU, LTV, CAC</p>
    <p style="font-size:0.85rem;color:#6B6B6B;line-height:1.45;margin:0;">Blind to how deeply users actually use the product or get value</p>
  </div>

  <div>
    <div style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#FF00FF;letter-spacing:0.12em;text-transform:uppercase;margin-bottom:0.6rem;">Product metrics</div>
    <p style="font-size:0.95rem;color:#1A1A1A;line-height:1.45;margin:0 0 0.6rem 0;font-weight:700;">Are users getting value?</p>
    <p style="font-size:0.9rem;color:#1A1A1A;line-height:1.45;margin:0 0 0.6rem 0;">DAU, retention, activation, feature adoption</p>
    <p style="font-size:0.85rem;color:#6B6B6B;line-height:1.45;margin:0;">Does not always reveal how much money the product earns</p>
  </div>

  <div>
    <div style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#FF00FF;letter-spacing:0.12em;text-transform:uppercase;margin-bottom:0.6rem;">UX metrics</div>
    <p style="font-size:0.95rem;color:#1A1A1A;line-height:1.45;margin:0 0 0.6rem 0;font-weight:700;">Does the interface actually work?</p>
    <p style="font-size:0.9rem;color:#1A1A1A;line-height:1.45;margin:0 0 0.6rem 0;">Task success rate, CSAT, time-to-complete, error rate</p>
    <p style="font-size:0.85rem;color:#6B6B6B;line-height:1.45;margin:0;">Business and product metrics stay silent on usability and interface friction</p>
  </div>

</div>

<p style="margin-top:1.6rem;text-align:center;color:#1A1A1A;font-size:1.15rem;font-weight:700;">Three domains complement each other. You almost never <span class="pink">substitute</span> one for another.</p>

<!--
Domain dimension. Three metric layers answer three different questions about the same product.

Speaker beats:
- Business metrics: financial outcome. Revenue, ARPU, LTV. Tells you the company is alive. Does not tell you the user is happy.
- Product metrics: usage and value delivery. DAU, retention, activation. Tells you users come back and get value. Does not tell you whether the company is making money on them. Microsoft 365 example: company keeps paying, users stop using. Revenue flat for months until renewal moment.
- UX metrics: usability and friction at the interface level. Task success, CSAT, error rate. Born from Google UX research. Neither business nor product metrics surface this — both can look healthy while the interface is broken.
- Three layers complement, do not substitute. Mature teams maintain all three views and reconcile them. The Microsoft 365 example sits cleanly here: business metric (revenue) lagged the product reality by months. Only product metrics would have surfaced the disengagement on time.
-->

---
layout: section
class: tint-rose
---

## 07

# Time orientation

---

# Past or future?

<div style="margin-top:2rem;display:flex;flex-direction:column;gap:1.8rem;">
  <div>
    <div style="font-weight:800;font-size:1.6rem;margin-bottom:0.4rem;">Lagging indicators</div>
    <div style="color:#1A1A1A;font-size:1.4rem;">Tell you what has <span class="pink">already</span> happened to your business</div>
  </div>
  <div>
    <div style="font-weight:800;font-size:1.6rem;margin-bottom:0.4rem;">Leading indicators</div>
    <div style="color:#1A1A1A;font-size:1.4rem;">Predict what <span class="pink">will</span> happen to your business</div>
  </div>
</div>

---

# Leading or lagging

<p style="color:#1A1A1A;font-size:1.1rem;line-height:1.45;margin-top:0.4rem;">The most important business signals sit in <strong>lagging</strong> metrics (revenue, retention, LTV) but those are already-happened facts. Teams look for <span class="pink">leading</span> proxies that predict the outcome without waiting for it to mature.</p>

<div style="display:flex;justify-content:center;margin-top:1rem;">
<svg viewBox="0 0 700 150" style="width:96%;max-width:760px;overflow:visible;">
  <defs>
    <marker id="larr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#1A1A1A"/>
    </marker>
  </defs>

  <!-- adoption box -->
  <rect x="10" y="50" width="120" height="40" fill="none" stroke="#FF00FF" stroke-width="1.5"/>
  <text x="70" y="68" text-anchor="middle" style="font:700 11px Inter,sans-serif;fill:#1A1A1A;">Adoption</text>
  <text x="70" y="82" text-anchor="middle" style="font:9px Inter,sans-serif;fill:#666;">% who try feature</text>

  <!-- engagement box -->
  <rect x="150" y="50" width="120" height="40" fill="none" stroke="#FF00FF" stroke-width="1.5"/>
  <text x="210" y="68" text-anchor="middle" style="font:700 11px Inter,sans-serif;fill:#1A1A1A;">Engagement</text>
  <text x="210" y="82" text-anchor="middle" style="font:9px Inter,sans-serif;fill:#666;">repeat use</text>

  <!-- conversion box -->
  <rect x="290" y="50" width="120" height="40" fill="none" stroke="#1A1A1A" stroke-width="1.5"/>
  <text x="350" y="68" text-anchor="middle" style="font:700 11px Inter,sans-serif;fill:#1A1A1A;">Conversion</text>
  <text x="350" y="82" text-anchor="middle" style="font:9px Inter,sans-serif;fill:#666;">first payment</text>

  <!-- retention box -->
  <rect x="430" y="50" width="120" height="40" fill="none" stroke="#1A1A1A" stroke-width="1.5"/>
  <text x="490" y="68" text-anchor="middle" style="font:700 11px Inter,sans-serif;fill:#1A1A1A;">Retention</text>
  <text x="490" y="82" text-anchor="middle" style="font:9px Inter,sans-serif;fill:#666;">N-month return</text>

  <!-- revenue box -->
  <rect x="570" y="50" width="120" height="40" fill="none" stroke="#1A1A1A" stroke-width="1.5"/>
  <text x="630" y="68" text-anchor="middle" style="font:700 11px Inter,sans-serif;fill:#1A1A1A;">Revenue / LTV</text>
  <text x="630" y="82" text-anchor="middle" style="font:9px Inter,sans-serif;fill:#666;">cumulative</text>

  <!-- arrows -->
  <line x1="130" y1="70" x2="148" y2="70" stroke="#1A1A1A" stroke-width="1.5" marker-end="url(#larr)"/>
  <line x1="270" y1="70" x2="288" y2="70" stroke="#1A1A1A" stroke-width="1.5" marker-end="url(#larr)"/>
  <line x1="410" y1="70" x2="428" y2="70" stroke="#1A1A1A" stroke-width="1.5" marker-end="url(#larr)"/>
  <line x1="550" y1="70" x2="568" y2="70" stroke="#1A1A1A" stroke-width="1.5" marker-end="url(#larr)"/>

  <!-- range markers -->
  <line x1="10" y1="105" x2="270" y2="105" stroke="#FF00FF" stroke-width="1.5"/>
  <line x1="430" y1="105" x2="690" y2="105" stroke="#1A1A1A" stroke-width="1.5"/>

  <!-- labels -->
  <text x="140" y="125" text-anchor="middle" style="font:700 8px 'JetBrains Mono',monospace;letter-spacing:0.12em;fill:#FF00FF;">LEADING · PREDICTS</text>
  <text x="560" y="125" text-anchor="middle" style="font:700 8px 'JetBrains Mono',monospace;letter-spacing:0.12em;fill:#1A1A1A;">LAGGING · CONFIRMS</text>
</svg>
</div>

<p style="margin-top:0.9rem;font-size:1.05rem;color:#1A1A1A;line-height:1.5;">Low adoption today predicts low revenue next quarter. Decision available now, no need to wait for revenue to settle.</p>

---
layout: statement
---

<h1 style="font-size:2.2rem;line-height:1.25;margin-bottom:1.8rem;">Can retention give you <span class="pink">fast feedback</span> on product quality?</h1>

<p style="font-size:1.3rem;color:#1A1A1A;text-align:center;line-height:1.4;">What does it tell you, and how quickly?</p>

<!--
Open discussion. Retention is a lagging indicator — by the time it moves, the cause is weeks or months in the past. Possible angles to surface:

- Can you make fast decisions about product value or quality from retention alone? Usually no.
- How long is the lag, depending on the product cadence?
- What signals do you watch instead for fast feedback? Activation, engagement deltas, NPS, qualitative.
- When IS retention the right signal? For long-term strategy, post-launch validation, cohort comparison across releases.

Bridge: the next slide answers the "how quickly" part with the Manychat 45-day floor.

Discussion-prompt slide. Section 07 has zero statements; this does not change that.
-->

---

# Lagging metrics delay decisions

<p style="color:#1A1A1A;font-size:1.1rem;margin-top:0.6rem;line-height:1.5;">Even the shortest retention window imposes a long floor before any signal arrives. Manychat's month-1 retention shows the minimum case.</p>

<div style="margin-top:1.4rem;padding:1rem 1.2rem;background:#FAFAFA;border-left:3px solid #FF00FF;">
  <div style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.12em;color:#FF00FF;margin-bottom:0.7rem;">Manychat · month-1 retention</div>

<svg viewBox="0 0 700 100" style="width:100%;max-width:760px;overflow:visible;">
  <!-- bracket on top -->
  <path d="M 40 18 L 40 10 L 660 10 L 660 18" fill="none" stroke="#FF00FF" stroke-width="1.2"/>
  <text x="350" y="6" text-anchor="middle" style="font:700 9px 'JetBrains Mono',monospace;letter-spacing:0.12em;fill:#FF00FF;">45-DAY DECISION DELAY · SHORTEST POSSIBLE</text>

  <!-- time axis -->
  <line x1="40" y1="55" x2="660" y2="55" stroke="#1A1A1A" stroke-width="1.2"/>

  <!-- Day 0 -->
  <line x1="40" y1="49" x2="40" y2="61" stroke="#1A1A1A" stroke-width="1.5"/>
  <text x="40" y="42" text-anchor="middle" style="font:11px Inter,sans-serif;fill:#666;">sign-up</text>
  <text x="40" y="78" text-anchor="middle" style="font:700 12px 'JetBrains Mono',monospace;fill:#1A1A1A;">Day 0</text>

  <!-- Day 14 -->
  <line x1="240" y1="49" x2="240" y2="61" stroke="#1A1A1A" stroke-width="1.5"/>
  <text x="240" y="42" text-anchor="middle" style="font:11px Inter,sans-serif;fill:#666;">first payment</text>
  <text x="240" y="78" text-anchor="middle" style="font:700 12px 'JetBrains Mono',monospace;fill:#1A1A1A;">Day 14</text>

  <!-- Day 45 -->
  <line x1="660" y1="48" x2="660" y2="62" stroke="#FF00FF" stroke-width="2.5"/>
  <text x="660" y="42" text-anchor="middle" style="font:11px Inter,sans-serif;fill:#666;">retention measured</text>
  <text x="660" y="78" text-anchor="middle" style="font:700 12px 'JetBrains Mono',monospace;fill:#FF00FF;">Day 45</text>
</svg>
</div>

<p style="margin-top:1.3rem;font-size:1.05rem;color:#1A1A1A;line-height:1.5;">14-day trial + 30-day retention window = 45 days before the team can read the signal. Longer retention horizons (month-3, month-6) push the floor further. Leading proxies are the only way to steer inside this window.</p>

<!--
Manychat example details:
- Free trial: ~14 days before first paid charge
- Month-1 retention: requires the user to still be paying 30 days after first payment
- Earliest moment month-1 retention is observable = 14 + 30 = 45 days from sign-up
- That is the shortest retention metric the team has. Anything longer (month-3, month-6) takes proportionally more time before it can be read

Pedagogical point:
- Retention is the most trusted signal of product quality (lagging, hard to fake)
- But it imposes a 45-day floor on decisions, and that is the floor for the shortest possible retention window. Real product decisions cannot wait that long
- Leading proxies (activation rate, adoption, engagement deltas, conversion to second payment) are the answer. They are noisier but they give the team a steering signal in days instead of months
- This is the answer slide for the discussion-prompt on the previous slide

Two SVGs are scoped to slide-only inline styles. Palette uses locked black + magenta only, plus #666 for secondary axis labels (within existing gray-text discipline since these are diagram microlabels, not body text).
-->

---
layout: section
class: tint-mint
---

## 08

# North Star<br>Metric

---
layout: statement
---

# The single metric that best captures the <span class="pink">core value</span> that your product delivers to customers

<p style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#AAAAAA;text-transform:uppercase;letter-spacing:0.15em;margin-top:1.8rem;">North Star Metric &middot; Sean Ellis</p>

---

# Is it a North Star Metric?

<p style="color:#1A1A1A;font-size:1.2rem;margin-top:0.5rem;">A candidate should answer yes to all nine.</p>

<div style="margin-top:1.8rem;display:grid;grid-template-columns:1fr 1fr;grid-auto-flow:column;grid-template-rows:repeat(5,auto);gap:0.9rem 2.5rem;">
  <div style="display:flex;align-items:center;gap:1rem;">
    <span style="display:inline-block;width:1.2rem;height:1.2rem;border:2px solid #1A1A1A;flex-shrink:0;"></span>
    <span style="font-size:1.15rem;">Does it express customer value?</span>
  </div>
  <div style="display:flex;align-items:center;gap:1rem;">
    <span style="display:inline-block;width:1.2rem;height:1.2rem;border:2px solid #1A1A1A;flex-shrink:0;"></span>
    <span style="font-size:1.15rem;">Does it represent your vision and strategy?</span>
  </div>
  <div style="display:flex;align-items:center;gap:1rem;">
    <span style="display:inline-block;width:1.2rem;height:1.2rem;border:2px solid #1A1A1A;flex-shrink:0;"></span>
    <span style="font-size:1.15rem;">Is it a leading indicator of success?</span>
  </div>
  <div style="display:flex;align-items:center;gap:1rem;">
    <span style="display:inline-block;width:1.2rem;height:1.2rem;border:2px solid #1A1A1A;flex-shrink:0;"></span>
    <span style="font-size:1.15rem;">Is it actionable?</span>
  </div>
  <div style="display:flex;align-items:center;gap:1rem;">
    <span style="display:inline-block;width:1.2rem;height:1.2rem;border:2px solid #1A1A1A;flex-shrink:0;"></span>
    <span style="font-size:1.15rem;">Is it sensitive to product changes?</span>
  </div>
  <div style="display:flex;align-items:center;gap:1rem;">
    <span style="display:inline-block;width:1.2rem;height:1.2rem;border:2px solid #1A1A1A;flex-shrink:0;"></span>
    <span style="font-size:1.15rem;">Is it understandable to non-technical partners?</span>
  </div>
  <div style="display:flex;align-items:center;gap:1rem;">
    <span style="display:inline-block;width:1.2rem;height:1.2rem;border:2px solid #1A1A1A;flex-shrink:0;"></span>
    <span style="font-size:1.15rem;">Is it measurable?</span>
  </div>
  <div style="display:flex;align-items:center;gap:1rem;">
    <span style="display:inline-block;width:1.2rem;height:1.2rem;border:2px solid #1A1A1A;flex-shrink:0;"></span>
    <span style="font-size:1.15rem;">Is it resistant to manipulation?</span>
  </div>
  <div style="display:flex;align-items:center;gap:1rem;">
    <span style="display:inline-block;width:1.2rem;height:1.2rem;border:2px solid #1A1A1A;flex-shrink:0;"></span>
    <span style="font-size:1.15rem;">It's not a vanity metric?</span>
  </div>
</div>

<!--
Replaces earlier "What makes a good NSM" 3-criterion slide. The 9-criteria checklist functions as the working definition of NSM via positive identification.

Speaker beats:
- Customer value + vision/strategy = core (without these it's not NSM, just a KPI)
- Leading indicator of revenue = the lever — revenue itself fails as NSM because it's lagging (Microsoft 365 subscription example: company drops Outlook/Word usage but keeps paying until renewal — revenue lies for months while value already left)
- Actionable + sensitive = team can move it via product changes
- Understandable + measurable = operational requirements
- Resistant to manipulation + not vanity = guardrails against Goodhart

Why revenue typically fails as NSM (Microsoft 365 example to use verbally):
- Company X subscribed to 365 stops using Outlook (switches to Slack), then stops using Word/Excel (switches to Google Docs). Subscription continues until renewal moment. Revenue stays flat throughout. By the time it drops, the user value left months ago.
- Lesson: choose NSM from leading indicators that reflect user value. Number of messages sent in Outlook, number of docs created in Word — these would have caught the drift immediately.
-->

---

# Guess the NSM

<p style="color:#1A1A1A;font-size:1.2rem;margin-top:0.5rem;">For each, what single metric best captures the core value?</p>

<div style="margin-top:2.5rem;display:flex;flex-direction:column;gap:1.4rem;">
  <div style="display:flex;align-items:baseline;gap:1.5rem;">
    <span style="font-weight:800;font-size:1.4rem;width:16rem;flex-shrink:0;">Airbnb</span>
    <span style="color:#AAAAAA;flex-shrink:0;">→</span>
    <span v-click="1" style="font-size:1.4rem;font-weight:800;">Nights Booked</span>
  </div>
  <div style="display:flex;align-items:baseline;gap:1.5rem;">
    <span style="font-weight:800;font-size:1.4rem;width:16rem;flex-shrink:0;">E-commerce platforms</span>
    <span style="color:#AAAAAA;flex-shrink:0;">→</span>
    <span v-click="2" style="font-size:1.4rem;font-weight:800;">Gross Merchandise Value</span>
  </div>
  <div style="display:flex;align-items:baseline;gap:1.5rem;">
    <span style="font-weight:800;font-size:1.4rem;width:16rem;flex-shrink:0;">Ride-hailing</span>
    <span style="color:#AAAAAA;flex-shrink:0;">→</span>
    <span v-click="3" style="font-size:1.4rem;font-weight:800;">Rides Completed</span>
  </div>
  <div style="display:flex;align-items:baseline;gap:1.5rem;">
    <span style="font-weight:800;font-size:1.4rem;width:16rem;flex-shrink:0;">Messaging apps</span>
    <span style="color:#AAAAAA;flex-shrink:0;">→</span>
    <span v-click="4" style="font-size:1.4rem;font-weight:800;">Messages Sent</span>
  </div>
</div>

<!--
Discussion guide per company (Tim's verbal layer):

Airbnb / Nights Booked. Core value is connecting travelers with unique accommodations. Nights Booked reflects both attracting guests AND ensuring listings are appealing/trustworthy enough to secure bookings. Hard to game. Sensitive to product and business-model changes.

E-commerce / GMV. Total sales value of goods sold over a period. Strong indicator of how much buyers and sellers are deriving value. High GMV signals a vibrant platform with a robust user base and significant transaction volume.

Ride-hailing / Rides Completed. Signifies fulfillment of the service's primary function: transporting users from A to B. Direct reflection of service value and ability to meet customer demand with a reliable network of drivers.

Messaging / Messages Sent. Clear indicator of user engagement and the app's effectiveness in facilitating communication. High volume signals a sticky product embedded in users' daily routines and interactions.
-->

---
layout: statement
---

<h1 style="font-size:2.2rem;line-height:1.25;margin-bottom:2rem;">Your turn: what is the <span class="pink">NSM</span>?</h1>

<div style="display:flex;flex-direction:column;align-items:center;gap:0.7rem;font-size:1.4rem;font-weight:700;color:#1A1A1A;">
  <span>Glovo</span>
  <span>Twitch</span>
  <span>Zoom</span>
  <span>Wise</span>
  <span>Bicing</span>
</div>

<!--
Class discussion. Builds on the canonical "Guess the NSM" exercise on the previous slide.

Sketched answers (Tim's call):
- Glovo: orders delivered (on-demand delivery, Barcelona-local)
- Twitch: hours watched, refined to 5-minute plays per the refinement pattern from previous slide
- Zoom: minutes hosted / weekly active hosts
- Wise (cross-border payments): transfer volume / active sending customers
- Bicing (Barcelona public bike-share): rides completed / weekly active subscribers — local to Barcelona, students will know it

Discussion-prompt slide; does not count toward section statement budget.
-->

---

# Refining the NSM

<p style="color:#1A1A1A;font-size:1.2rem;margin-top:0.5rem;">Each refinement filters something the naive version missed.</p>

<div style="margin-top:2.5rem;display:flex;flex-direction:column;gap:1.4rem;">
  <div style="display:grid;grid-template-columns:7rem 1fr 1.5rem 1fr;gap:1rem;align-items:baseline;">
    <span style="font-weight:800;font-size:1.2rem;">Netflix</span>
    <span style="color:#AAAAAA;font-size:1.1rem;">total view hours</span>
    <span style="color:#CCCCCC;font-size:1.1rem;">→</span>
    <span style="font-size:1.2rem;font-weight:600;"><span class="pink">Median</span> view hours per member</span>
  </div>
  <div style="display:grid;grid-template-columns:7rem 1fr 1.5rem 1fr;gap:1rem;align-items:baseline;">
    <span style="font-weight:800;font-size:1.2rem;">Twitch</span>
    <span style="color:#AAAAAA;font-size:1.1rem;">stream views</span>
    <span style="color:#CCCCCC;font-size:1.1rem;">→</span>
    <span style="font-size:1.2rem;font-weight:600;">5-minute plays</span>
  </div>
  <div style="display:grid;grid-template-columns:7rem 1fr 1.5rem 1fr;gap:1rem;align-items:baseline;">
    <span style="font-weight:800;font-size:1.2rem;">Slack</span>
    <span style="color:#AAAAAA;font-size:1.1rem;">messages sent</span>
    <span style="color:#CCCCCC;font-size:1.1rem;">→</span>
    <span style="font-size:1.2rem;font-weight:600;">Number of paid teams</span>
  </div>
  <div style="display:grid;grid-template-columns:7rem 1fr 1.5rem 1fr;gap:1rem;align-items:baseline;">
    <span style="font-weight:800;font-size:1.2rem;">Miro</span>
    <span style="color:#AAAAAA;font-size:1.1rem;">boards created</span>
    <span style="color:#CCCCCC;font-size:1.1rem;">→</span>
    <span style="font-size:1.2rem;font-weight:600;">Boards with 2+ active users</span>
  </div>
</div>

<!--
Speaker notes — what each refinement filters out:

Netflix. Total or mean view hours is dominated by whales (members who watch 10 hours a day). Median measures the typical member. Direct callback to the Manychat whale problem from Session 1 — different product, same structural fix.

Twitch. Naive "stream view" counts every accidental click and bounce. The 5-minute threshold filters intent and measures actual value delivery. The smallest observable signal that reliably predicts real value was delivered.

Slack. "Messages sent" is an engagement metric — it goes up with spam, noise, over-communication, and bots. "Paid teams" is a growth metric — it measures actual monetized value. Clean product-metric vs. growth-metric demonstration.

Miro. "Boards created" is easy to game and includes solo whiteboards. The "2+ active users" qualifier captures the actual product (collaboration), not the artifact (a board).

Pattern across all four: each refinement embeds a definition of what "real value" means into the metric itself. Naive metrics measure activity. Refined metrics measure value.
-->

---

# Proxy North Star Metrics

<p style="color:#1A1A1A;font-size:1.2rem;margin-top:0.5rem;">Sometimes the ideal goal can't be measured directly, so pick a proxy that leads it.</p>

<div style="margin-top:2.5rem;display:flex;flex-direction:column;gap:1.8rem;">
  <div>
    <div style="font-weight:800;font-size:1.4rem;margin-bottom:0.5rem;">Tinder</div>
    <p style="font-size:1.1rem;color:#1A1A1A;line-height:1.55;margin:0;">Ideal: dates between users, but direct measurement fails because location tracking needs permissions, keyword matching misses users who switch apps, and dates lag days or weeks after first contact.</p>
    <p style="font-size:1.1rem;color:#1A1A1A;line-height:1.55;margin-top:0.4rem;">Proxy: <span class="pink">quality chats</span>, defined as exchanges with N or more messages.</p>
  </div>
  <div>
    <div style="font-weight:800;font-size:1.4rem;margin-bottom:0.5rem;">Avito</div>
    <p style="font-size:1.1rem;color:#1A1A1A;line-height:1.55;margin:0;">Ideal: completed deals, but transactions happen offline outside the platform.</p>
  </div>
</div>

<!--
Teaching point: a proxy is not a compromise; it's the right answer when direct measurement fails.
Criteria for a good proxy: leading indicator of the ultimate goal, sensitive to product changes, hard to game, measurable at the scale you operate.
Tinder's "quality chats" beats "number of dates" on every criterion except direct value-capture — but value-capture only matters if you can actually measure it.
-->

---

# When one metric isn't enough

<div style="margin-top:2rem;display:flex;flex-direction:column;gap:1.4rem;">
  <div>
    <div style="font-weight:800;font-size:1.2rem;margin-bottom:0.3rem;">A single metric can't measure a multi-dimensional business</div>
    <p style="color:#1A1A1A;font-size:1.1rem;line-height:1.55;margin:0;">Products grow on multiple axes simultaneously: acquisition, retention, monetization. One number can be moving in the right direction while another silently breaks.</p>
  </div>
  <div>
    <div style="font-weight:800;font-size:1.2rem;margin-bottom:0.3rem;">Optimizing one NSM creates blind spots</div>
    <p style="color:#1A1A1A;font-size:1.1rem;line-height:1.55;margin:0;">Teams that target a single metric stop noticing what isn't measured. By the time the breakdown shows up in revenue, the structural damage is months old.</p>
  </div>
</div>

<div style="position:absolute;bottom:1rem;left:3.5rem;display:flex;flex-direction:column;gap:0.25rem;">
  <a href="https://www.reforge.com/blog/north-star-metric-growth" target="_blank" style="font-family:'JetBrains Mono',monospace;font-size:0.65rem;color:#AAAAAA;letter-spacing:0.1em;text-transform:uppercase;text-decoration:none;">reforge.com / blog / don't let your north star metric deceive you</a>
  <a href="https://hbsp.harvard.edu/product/H05LYD-PDF-ENG" target="_blank" style="font-family:'JetBrains Mono',monospace;font-size:0.65rem;color:#AAAAAA;letter-spacing:0.1em;text-transform:uppercase;text-decoration:none;">hbsp.harvard.edu / don't let a single metric drive your business</a>
</div>

<!--
Closing of the NSM cluster. Frame the critique constructively: NSMs are useful when treated as one organizing lens. They become dangerous when treated as the only lens.

Balfour's specific argument (source #9): most products have three NSMs in practice — one for acquisition, one for retention, one for monetization. Locking onto a single NSM is what creates the blindspots in the second bullet.

HBR (May 2020, Don't Let a Single Metric Drive Your Business): same critique from a more general business angle — single-metric thinking can lead to short-sighted decisions and missed signals across dimensions of company performance.

After this slide, the section transitions from "NSM" to "metric tree" — which is itself part of the answer to single-metric blindness. A tree gives you the L1 and the inputs.
-->

---

# One Metric That Matters

<p style="color:#1A1A1A;font-size:1.2rem;margin-top:0.5rem;line-height:1.5;">NSM holds a long-term anchor. When a team needs to focus on a shorter horizon and rotate the metric as the product moves to its next stage, the older <span class="pink">OMTM</span> framing fits better. OMTM predates NSM and was its conceptual predecessor.</p>

<div style="margin-top:2rem;display:flex;flex-direction:column;gap:1.4rem;">
  <div>
    <div style="font-weight:800;font-size:1.2rem;margin-bottom:0.3rem;">Reddit</div>
    <p style="color:#1A1A1A;font-size:1.05rem;line-height:1.5;margin:0;">Engagement tier progression: lurking → voting → commenting → submissions. The OMTM is the share of users moving one tier up</p>
  </div>
  <div>
    <div style="font-weight:800;font-size:1.2rem;margin-bottom:0.3rem;">Amazon</div>
    <p style="color:#1A1A1A;font-size:1.05rem;line-height:1.5;margin:0;">Transactional conversion as the primary OMTM, with collaboration signals like reviews tracked alongside</p>
  </div>
</div>

<div style="position:absolute;bottom:1.5rem;left:3.5rem;font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#AAAAAA;letter-spacing:0.1em;text-transform:uppercase;">
  <a href="https://leananalyticsbook.com/one-metric-that-matters/" target="_blank" style="color:inherit;text-decoration:none;">leananalyticsbook.com / one-metric-that-matters</a>
</div>

<!--
OMTM coined by Croll & Yoskovitz in Lean Analytics (2013). Predates Sean Ellis's NSM popularization.

Verbal layer:
- NSM = strategic, stable, enduring (Sean Ellis)
- OMTM = tactical, situational, rotates by stage (Yoskovitz)
- They don't compete: OMTMs ladder up to the NSM
- A startup at "MVP validation" stage has a different OMTM than the same company at "feature optimization"

Reddit example unpacks: at lurker stage, OMTM is conversion to first vote. Once that's healthy, OMTM rotates to comment rate. Then to submission rate. The metric changes, the goal of moving people up the engagement ladder stays.
-->

---

<div style="position:absolute;top:4.5rem;left:1rem;right:1rem;bottom:1rem;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:1rem;">
  <img src="/nsm-amplitude.webp" alt="The North Star Framework — Amplitude" style="flex:1 1 auto;min-height:0;max-width:100%;object-fit:contain;display:block;" />
  <a href="https://amplitude.com/books/north-star/about-the-north-star-framework" target="_blank" style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#AAAAAA;text-transform:uppercase;letter-spacing:0.12em;text-decoration:none;flex-shrink:0;">amplitude.com / books / north-star / about-the-north-star-framework</a>
</div>

<!--
Closing visual of the NSM cluster. Amplitude's North Star Framework diagram: NSM at the center, input metrics around it. Sets up the transition to the next section (Metric tree), where the same hierarchical idea gets formalized as L1 → L2 → Ln.

Tim's framing: NSM alone is not enough (covered on slide 59 "When one metric isn't enough"). To actually drive it you start working with hierarchies — and this diagram is the bridge.
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

