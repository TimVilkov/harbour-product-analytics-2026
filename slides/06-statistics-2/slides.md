---
theme: apple-basic
title: "Session 06: Statistics 2"
info: "Product Analytics · Harbour.Space · 2026"
highlighter: shiki
drawings:
  persist: false
transition: fade
mdc: true
layout: intro
---

# Statistics <span class="pink">2</span>

<div class="absolute bottom-10 left-14" style="font-family:'JetBrains Mono',monospace;font-size:0.75rem;text-transform:uppercase;letter-spacing:0.15em;color:rgba(255,255,255,0.55);">
  Harbour.Space &middot; Barcelona &middot; May 25, 2026
</div>

---

# Today and tomorrow

A test attains its **nominal** Type I rate $\alpha$ **if and only if its assumptions hold**. Today we build the procedure that promises $\alpha$. Tomorrow we measure when it actually delivers it.

<div style="display:grid;grid-template-columns:1fr 1fr;gap:2rem;margin-top:1.4rem;">

<div>
<div style="font-family:'JetBrains Mono',monospace;font-size:0.78rem;color:#FF00FF;text-transform:uppercase;letter-spacing:0.15em;margin-bottom:0.7rem;">Today</div>

<div style="display:flex;flex-direction:column;gap:0.55rem;">
  <div style="display:grid;grid-template-columns:36px 1fr;gap:0.9rem;align-items:baseline;">
    <span style="font-family:'JetBrains Mono',monospace;font-size:0.9rem;color:#FF00FF;letter-spacing:0.1em;">01</span>
    <div style="font-size:1.1rem;font-weight:700;color:#1A1A1A;">Refresh</div>
  </div>
  <div style="display:grid;grid-template-columns:36px 1fr;gap:0.9rem;align-items:baseline;">
    <span style="font-family:'JetBrains Mono',monospace;font-size:0.9rem;color:#FF00FF;letter-spacing:0.1em;">02</span>
    <div style="font-size:1.1rem;font-weight:700;color:#1A1A1A;">Confidence intervals</div>
  </div>
  <div style="display:grid;grid-template-columns:36px 1fr;gap:0.9rem;align-items:baseline;">
    <span style="font-family:'JetBrains Mono',monospace;font-size:0.9rem;color:#FF00FF;letter-spacing:0.1em;">03</span>
    <div style="font-size:1.1rem;font-weight:700;color:#1A1A1A;">Hypothesis testing</div>
  </div>
  <div style="display:grid;grid-template-columns:36px 1fr;gap:0.9rem;align-items:baseline;">
    <span style="font-family:'JetBrains Mono',monospace;font-size:0.9rem;color:#FF00FF;letter-spacing:0.1em;">04</span>
    <div style="font-size:1.1rem;font-weight:700;color:#1A1A1A;">Errors of two kinds</div>
  </div>
  <div style="display:grid;grid-template-columns:36px 1fr;gap:0.9rem;align-items:baseline;">
    <span style="font-family:'JetBrains Mono',monospace;font-size:0.9rem;color:#FF00FF;letter-spacing:0.1em;">05</span>
    <div style="font-size:1.1rem;font-weight:700;color:#1A1A1A;">The p-value</div>
  </div>
</div>
</div>

<div>
<div style="font-family:'JetBrains Mono',monospace;font-size:0.78rem;color:#6B6B6B;text-transform:uppercase;letter-spacing:0.15em;margin-bottom:0.7rem;">Tomorrow</div>

<div style="display:flex;flex-direction:column;gap:0.55rem;">
  <div style="display:grid;grid-template-columns:36px 1fr;gap:0.9rem;align-items:baseline;">
    <span style="font-family:'JetBrains Mono',monospace;font-size:0.9rem;color:#6B6B6B;letter-spacing:0.1em;">06</span>
    <div style="font-size:1.1rem;font-weight:700;color:#1A1A1A;">Power, effect size, MDE</div>
  </div>
  <div style="display:grid;grid-template-columns:36px 1fr;gap:0.9rem;align-items:baseline;">
    <span style="font-family:'JetBrains Mono',monospace;font-size:0.9rem;color:#6B6B6B;letter-spacing:0.1em;">07</span>
    <div style="font-size:1.1rem;font-weight:700;color:#1A1A1A;">One-sample t-test</div>
  </div>
</div>
</div>

</div>

---
layout: section
class: tint-lavender
---

## 01

# Refresh

---

# Random variable and distribution

A **random variable** $X$ is a number assigned to each outcome, and its **distribution** describes how probability mass is spread across the values $X$ can take.

<div style="display:grid;grid-template-columns:1fr 1fr;gap:1.4rem;margin-top:1.2rem;">

<div style="padding:0.9rem 1.1rem;background:#FAFAFA;border-left:3px solid #1A1A1A;">

**Density**. For discrete $X$ the PMF $\mathbb{P}(X = x)$ gives a probability at each value, and for continuous $X$ the PDF $f(x)$ gives a local density that integrates over a range to give probability.

</div>

<div style="padding:0.9rem 1.1rem;background:#FAFAFA;border-left:3px solid #1A1A1A;">

**CDF**. $F(x) = \mathbb{P}(X \le x)$ accumulates density up to a value.

</div>

</div>

Knowing either function lets us compute <span class="pink">any</span> probability about $X$.

---

# Example · click

A user either clicks or does not. $X = 1$ on click, $X = 0$ otherwise.

<div style="margin-top:1rem;padding:0.7rem 1.2rem;background:#FAFAFA;border-left:3px solid #FF00FF;font-size:1.05rem;color:#1A1A1A;">

$X \sim \mathrm{Bernoulli}(p)$, with $p = \mathbb{P}(\text{click}) = 0.1$

</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:1.4rem;margin-top:0.8rem;">

  <svg viewBox="0 0 300 110" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;font-family:'Inter',system-ui,sans-serif;">
    <text x="30" y="10" style="font-size:9px;font-family:'JetBrains Mono',monospace;fill:#6B6B6B;">PMF · P(X = x)</text>
    <rect x="30" y="14" width="260" height="80" fill="#FAFAFA"/>
    <line x1="30" y1="14" x2="30" y2="94" stroke="#1A1A1A" stroke-width="1"/>
    <line x1="30" y1="94" x2="290" y2="94" stroke="#1A1A1A" stroke-width="1"/>
    <rect x="80" y="22" width="44" height="72" fill="#1A1A1A"/>
    <text x="102" y="19" style="font-size:9px;font-family:'JetBrains Mono',monospace;fill:#1A1A1A;text-anchor:middle;">0.9</text>
    <rect x="200" y="86" width="44" height="8" fill="#FF00FF"/>
    <text x="222" y="83" style="font-size:9px;font-family:'JetBrains Mono',monospace;fill:#1A1A1A;text-anchor:middle;">0.1</text>
    <text x="102" y="106" style="font-size:9px;font-family:'JetBrains Mono',monospace;fill:#1A1A1A;text-anchor:middle;">0</text>
    <text x="222" y="106" style="font-size:9px;font-family:'JetBrains Mono',monospace;fill:#1A1A1A;text-anchor:middle;">1</text>
    <text x="26" y="97" style="font-size:8px;font-family:'JetBrains Mono',monospace;fill:#1A1A1A;text-anchor:end;">0</text>
    <text x="26" y="18" style="font-size:8px;font-family:'JetBrains Mono',monospace;fill:#1A1A1A;text-anchor:end;">1</text>
  </svg>

  <svg viewBox="0 0 300 110" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;font-family:'Inter',system-ui,sans-serif;">
    <text x="30" y="10" style="font-size:9px;font-family:'JetBrains Mono',monospace;fill:#6B6B6B;">CDF · F(x) = P(X ≤ x)</text>
    <rect x="30" y="14" width="260" height="80" fill="#FAFAFA"/>
    <line x1="30" y1="14" x2="30" y2="94" stroke="#1A1A1A" stroke-width="1"/>
    <line x1="30" y1="94" x2="290" y2="94" stroke="#1A1A1A" stroke-width="1"/>
    <!-- F=0 for x ≤ 0 -->
    <line x1="30" y1="94" x2="100" y2="94" stroke="#1A1A1A" stroke-width="2"/>
    <!-- vertical dashed at x=0 -->
    <line x1="100" y1="94" x2="100" y2="22" stroke="#1A1A1A" stroke-width="0.8" stroke-dasharray="2,2"/>
    <!-- F=0.9 for 0 < x ≤ 1 -->
    <line x1="100" y1="22" x2="220" y2="22" stroke="#1A1A1A" stroke-width="2"/>
    <!-- vertical dashed at x=1 -->
    <line x1="220" y1="22" x2="220" y2="14" stroke="#1A1A1A" stroke-width="0.8" stroke-dasharray="2,2"/>
    <!-- F=1 for x > 1 -->
    <line x1="220" y1="14" x2="290" y2="14" stroke="#1A1A1A" stroke-width="2"/>
    <!-- closed dots at the value included in each step (left-continuous: bottom of jump) -->
    <circle cx="100" cy="94" r="2.8" fill="#1A1A1A"/>
    <circle cx="220" cy="22" r="2.8" fill="#1A1A1A"/>
    <!-- open dots at the limit value not included -->
    <circle cx="100" cy="22" r="2.8" fill="#FFFFFF" stroke="#1A1A1A" stroke-width="1.2"/>
    <circle cx="220" cy="14" r="2.8" fill="#FFFFFF" stroke="#1A1A1A" stroke-width="1.2"/>
    <text x="100" y="106" style="font-size:9px;font-family:'JetBrains Mono',monospace;fill:#1A1A1A;text-anchor:middle;">0</text>
    <text x="220" y="106" style="font-size:9px;font-family:'JetBrains Mono',monospace;fill:#1A1A1A;text-anchor:middle;">1</text>
    <text x="26" y="97" style="font-size:8px;font-family:'JetBrains Mono',monospace;fill:#1A1A1A;text-anchor:end;">0</text>
    <text x="26" y="26" style="font-size:8px;font-family:'JetBrains Mono',monospace;fill:#1A1A1A;text-anchor:end;">0.9</text>
    <text x="26" y="17" style="font-size:8px;font-family:'JetBrains Mono',monospace;fill:#1A1A1A;text-anchor:end;">1</text>
  </svg>

</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:1.4rem;margin-top:0.8rem;">

<div>
<div style="font-family:'JetBrains Mono',monospace;font-size:0.75rem;color:#6B6B6B;text-transform:uppercase;letter-spacing:0.1em;">mean</div>

$\mathbb{E}[X] = p = 0.1$

</div>
<div>
<div style="font-family:'JetBrains Mono',monospace;font-size:0.75rem;color:#6B6B6B;text-transform:uppercase;letter-spacing:0.1em;">variance</div>

$\mathrm{Var}(X) = p(1 - p) = 0.09$

</div>
</div>

---

# Example · continuous

User height $H \sim \mathcal{N}(\mu, \sigma^2)$, with mean $\mu$ and standard deviation $\sigma$ as the two parameters.

<svg viewBox="0 0 540 200" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:580px;height:auto;display:block;margin-top:0.3rem;font-family:'Inter',system-ui,sans-serif;">
  <!-- panels backgrounds -->
  <rect x="60" y="14" width="458" height="72" fill="#FAFAFA"/>
  <rect x="60" y="102" width="458" height="72" fill="#FAFAFA"/>
  <!-- panel labels -->
  <text x="64" y="11" style="font-size:10px;font-family:'JetBrains Mono',monospace;fill:#6B6B6B;">PDF · f(h)</text>
  <text x="64" y="99" style="font-size:10px;font-family:'JetBrains Mono',monospace;fill:#6B6B6B;">CDF · F(h) = P(H ≤ h)</text>
  <!-- shaded area on PDF -->
  <path d="M 250.8,86.0 L 250.8,26.8 L 252.7,25.6 L 254.7,24.5 L 256.6,23.5 L 258.5,22.5 L 260.4,21.5 L 262.3,20.6 L 264.2,19.7 L 266.1,18.9 L 268.0,18.1 L 269.9,17.4 L 271.8,16.8 L 273.7,16.2 L 275.6,15.7 L 277.5,15.3 L 279.5,14.9 L 281.4,14.6 L 283.3,14.3 L 285.2,14.1 L 287.1,14.0 L 289.0,14.0 L 290.9,14.0 L 292.8,14.1 L 294.7,14.3 L 296.6,14.6 L 298.5,14.9 L 300.5,15.3 L 302.4,15.7 L 304.3,16.2 L 306.2,16.8 L 308.1,17.4 L 310.0,18.1 L 311.9,18.9 L 313.8,19.7 L 315.7,20.6 L 317.6,21.5 L 319.5,22.5 L 321.4,23.5 L 323.3,24.5 L 325.3,25.6 L 327.2,26.8 L 327.2,86.0 Z" fill="rgba(255,0,255,0.22)" stroke="none"/>
  <!-- PDF curve -->
  <path d="M 60.0,85.9 L 63.8,85.9 L 67.6,85.9 L 71.5,85.9 L 75.3,85.8 L 79.1,85.8 L 82.9,85.8 L 86.7,85.7 L 90.5,85.6 L 94.3,85.6 L 98.2,85.5 L 102.0,85.3 L 105.8,85.2 L 109.6,85.0 L 113.4,84.8 L 117.2,84.6 L 121.1,84.4 L 124.9,84.1 L 128.7,83.7 L 132.5,83.3 L 136.3,82.8 L 140.1,82.3 L 144.0,81.7 L 147.8,81.0 L 151.6,80.3 L 155.4,79.4 L 159.2,78.5 L 163.1,77.4 L 166.9,76.3 L 170.7,75.0 L 174.5,73.6 L 178.3,72.1 L 182.1,70.4 L 186.0,68.7 L 189.8,66.8 L 193.6,64.8 L 197.4,62.6 L 201.2,60.4 L 205.0,58.0 L 208.8,55.6 L 212.7,53.0 L 216.5,50.4 L 220.3,47.8 L 224.1,45.1 L 227.9,42.3 L 231.8,39.6 L 235.6,36.9 L 239.4,34.2 L 243.2,31.7 L 247.0,29.2 L 250.8,26.8 L 254.7,24.5 L 258.5,22.5 L 262.3,20.6 L 266.1,18.9 L 269.9,17.4 L 273.7,16.2 L 277.5,15.3 L 281.4,14.6 L 285.2,14.1 L 289.0,14.0 L 292.8,14.1 L 296.6,14.6 L 300.5,15.3 L 304.3,16.2 L 308.1,17.4 L 311.9,18.9 L 315.7,20.6 L 319.5,22.5 L 323.3,24.5 L 327.2,26.8 L 331.0,29.2 L 334.8,31.7 L 338.6,34.2 L 342.4,36.9 L 346.2,39.6 L 350.1,42.3 L 353.9,45.1 L 357.7,47.8 L 361.5,50.4 L 365.3,53.0 L 369.2,55.6 L 373.0,58.0 L 376.8,60.4 L 380.6,62.6 L 384.4,64.8 L 388.2,66.8 L 392.1,68.7 L 395.9,70.4 L 399.7,72.1 L 403.5,73.6 L 407.3,75.0 L 411.1,76.3 L 414.9,77.4 L 418.8,78.5 L 422.6,79.4 L 426.4,80.3 L 430.2,81.0 L 434.0,81.7 L 437.8,82.3 L 441.7,82.8 L 445.5,83.3 L 449.3,83.7 L 453.1,84.1 L 456.9,84.4 L 460.8,84.6 L 464.6,84.8 L 468.4,85.0 L 472.2,85.2 L 476.0,85.3 L 479.8,85.5 L 483.7,85.6 L 487.5,85.6 L 491.3,85.7 L 495.1,85.8 L 498.9,85.8 L 502.7,85.8 L 506.6,85.9 L 510.4,85.9 L 514.2,85.9 L 518.0,85.9" fill="none" stroke="#1A1A1A" stroke-width="1.6"/>
  <!-- PDF markers at 170, 180 (vertical dashed to x-axis) -->
  <line x1="250.8" y1="14" x2="250.8" y2="86" stroke="#FF00FF" stroke-width="1" stroke-dasharray="3,3" opacity="0.6"/>
  <line x1="327.2" y1="14" x2="327.2" y2="86" stroke="#FF00FF" stroke-width="1" stroke-dasharray="3,3" opacity="0.6"/>
  <!-- CDF curve -->
  <path d="M 60.0,174.0 L 63.8,174.0 L 67.6,174.0 L 71.5,174.0 L 75.3,174.0 L 79.1,174.0 L 82.9,174.0 L 86.7,174.0 L 90.5,174.0 L 94.3,173.9 L 98.2,173.9 L 102.0,173.9 L 105.8,173.9 L 109.6,173.9 L 113.4,173.9 L 117.2,173.8 L 121.1,173.8 L 124.9,173.7 L 128.7,173.7 L 132.5,173.6 L 136.3,173.6 L 140.1,173.5 L 144.0,173.4 L 147.8,173.3 L 151.6,173.1 L 155.4,173.0 L 159.2,172.8 L 163.1,172.6 L 166.9,172.4 L 170.7,172.1 L 174.5,171.8 L 178.3,171.5 L 182.1,171.1 L 186.0,170.7 L 189.8,170.3 L 193.6,169.7 L 197.4,169.2 L 201.2,168.6 L 205.0,167.9 L 208.8,167.2 L 212.7,166.4 L 216.5,165.5 L 220.3,164.6 L 224.1,163.6 L 227.9,162.6 L 231.8,161.5 L 235.6,160.3 L 239.4,159.0 L 243.2,157.7 L 247.0,156.3 L 250.8,154.8 L 254.7,153.3 L 258.5,151.8 L 262.3,150.2 L 266.1,148.5 L 269.9,146.8 L 273.7,145.1 L 277.5,143.4 L 281.4,141.6 L 285.2,139.8 L 289.0,138.0 L 292.8,136.2 L 296.6,134.4 L 300.5,132.6 L 304.3,130.9 L 308.1,129.2 L 311.9,127.5 L 315.7,125.8 L 319.5,124.2 L 323.3,122.7 L 327.2,121.2 L 331.0,119.7 L 334.8,118.3 L 338.6,117.0 L 342.4,115.7 L 346.2,114.5 L 350.1,113.4 L 353.9,112.4 L 357.7,111.4 L 361.5,110.5 L 365.3,109.6 L 369.2,108.8 L 373.0,108.1 L 376.8,107.4 L 380.6,106.8 L 384.4,106.3 L 388.2,105.7 L 392.1,105.3 L 395.9,104.9 L 399.7,104.5 L 403.5,104.2 L 407.3,103.9 L 411.1,103.6 L 414.9,103.4 L 418.8,103.2 L 422.6,103.0 L 426.4,102.9 L 430.2,102.7 L 434.0,102.6 L 437.8,102.5 L 441.7,102.4 L 445.5,102.4 L 449.3,102.3 L 453.1,102.3 L 456.9,102.2 L 460.8,102.2 L 464.6,102.1 L 468.4,102.1 L 472.2,102.1 L 476.0,102.1 L 479.8,102.1 L 483.7,102.1 L 487.5,102.0 L 491.3,102.0 L 495.1,102.0 L 498.9,102.0 L 502.7,102.0 L 506.6,102.0 L 510.4,102.0 L 514.2,102.0 L 518.0,102.0" fill="none" stroke="#1A1A1A" stroke-width="1.6"/>
  <!-- CDF markers -->
  <line x1="250.8" y1="174" x2="250.8" y2="154.8" stroke="#FF00FF" stroke-width="1.2" stroke-dasharray="3,3"/>
  <line x1="60" y1="154.8" x2="250.8" y2="154.8" stroke="#FF00FF" stroke-width="1.2" stroke-dasharray="3,3"/>
  <line x1="327.2" y1="174" x2="327.2" y2="121.2" stroke="#FF00FF" stroke-width="1.2" stroke-dasharray="3,3"/>
  <line x1="60" y1="121.2" x2="327.2" y2="121.2" stroke="#FF00FF" stroke-width="1.2" stroke-dasharray="3,3"/>
  <!-- axes -->
  <line x1="60" y1="86" x2="518" y2="86" stroke="#1A1A1A" stroke-width="1"/>
  <line x1="60" y1="174" x2="518" y2="174" stroke="#1A1A1A" stroke-width="1"/>
  <line x1="60" y1="14" x2="60" y2="86" stroke="#1A1A1A" stroke-width="1"/>
  <line x1="60" y1="102" x2="60" y2="174" stroke="#1A1A1A" stroke-width="1"/>
  <!-- x ticks (shared at bottom) -->
  <text x="60" y="188" style="font-size:10px;font-family:'JetBrains Mono',monospace;fill:#1A1A1A;text-anchor:middle;">150</text>
  <text x="250.8" y="188" style="font-size:10px;font-family:'JetBrains Mono',monospace;fill:#1A1A1A;text-anchor:middle;">170</text>
  <text x="289" y="188" style="font-size:10px;font-family:'JetBrains Mono',monospace;fill:#1A1A1A;text-anchor:middle;">μ=175</text>
  <text x="327.2" y="188" style="font-size:10px;font-family:'JetBrains Mono',monospace;fill:#1A1A1A;text-anchor:middle;">180</text>
  <text x="518" y="188" style="font-size:10px;font-family:'JetBrains Mono',monospace;fill:#1A1A1A;text-anchor:middle;">200</text>
  <!-- y labels for CDF -->
  <text x="56" y="177" style="font-size:9px;font-family:'JetBrains Mono',monospace;fill:#1A1A1A;text-anchor:end;">0</text>
  <text x="56" y="158" style="font-size:9px;font-family:'JetBrains Mono',monospace;fill:#1A1A1A;text-anchor:end;">F(170)</text>
  <text x="56" y="125" style="font-size:9px;font-family:'JetBrains Mono',monospace;fill:#1A1A1A;text-anchor:end;">F(180)</text>
  <text x="56" y="105" style="font-size:9px;font-family:'JetBrains Mono',monospace;fill:#1A1A1A;text-anchor:end;">1</text>
</svg>

<div style="text-align:center;color:#6B6B6B;margin-top:0.4rem;">

shaded area on PDF = gap on CDF = $\mathbb{P}(170 \le H \lt 180) = F(180) - F(170)$

</div>

---

# Same family, different parameters

<svg viewBox="0 0 540 180" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:560px;height:auto;display:block;margin-top:0.3rem;font-family:'Inter',system-ui,sans-serif;">
  <rect x="50" y="14" width="468" height="130" fill="#FAFAFA"/>
  <line x1="50" y1="14" x2="50" y2="144" stroke="#1A1A1A" stroke-width="1"/>
  <line x1="50" y1="144" x2="518" y2="144" stroke="#1A1A1A" stroke-width="1"/>
  <path d="M 50.0,144.0 L 53.9,144.0 L 57.8,144.0 L 61.7,144.0 L 65.6,144.0 L 69.5,144.0 L 73.4,144.0 L 77.3,143.9 L 81.2,143.9 L 85.1,143.9 L 89.0,143.9 L 92.9,143.9 L 96.8,143.9 L 100.7,143.8 L 104.6,143.8 L 108.5,143.8 L 112.4,143.7 L 116.4,143.7 L 120.3,143.6 L 124.2,143.5 L 128.1,143.4 L 132.0,143.3 L 135.9,143.2 L 139.8,143.1 L 143.7,143.0 L 147.6,142.8 L 151.5,142.6 L 155.4,142.4 L 159.3,142.1 L 163.2,141.9 L 167.1,141.6 L 171.0,141.2 L 174.9,140.8 L 178.8,140.4 L 182.7,139.9 L 186.6,139.4 L 190.5,138.8 L 194.4,138.2 L 198.3,137.5 L 202.2,136.7 L 206.1,135.9 L 210.0,135.0 L 213.9,134.0 L 217.8,133.0 L 221.7,131.8 L 225.6,130.6 L 229.5,129.4 L 233.4,128.0 L 237.3,126.6 L 241.3,125.1 L 245.2,123.5 L 249.1,121.8 L 253.0,120.1 L 256.9,118.3 L 260.8,116.4 L 264.7,114.5 L 268.6,112.6 L 272.5,110.6 L 276.4,108.6 L 280.3,106.5 L 284.2,104.5 L 288.1,102.4 L 292.0,100.4 L 295.9,98.3 L 299.8,96.4 L 303.7,94.4 L 307.6,92.6 L 311.5,90.8 L 315.4,89.1 L 319.3,87.4 L 323.2,85.9 L 327.1,84.6 L 331.0,83.3 L 334.9,82.2 L 338.8,81.3 L 342.7,80.5 L 346.6,79.8 L 350.5,79.4 L 354.4,79.1 L 358.3,79.0 L 362.2,79.0 L 366.2,79.3 L 370.1,79.7 L 374.0,80.3 L 377.9,81.0 L 381.8,81.9 L 385.7,83.0 L 389.6,84.2 L 393.5,85.6 L 397.4,87.0 L 401.3,88.6 L 405.2,90.3 L 409.1,92.1 L 413.0,93.9 L 416.9,95.8 L 420.8,97.8 L 424.7,99.8 L 428.6,101.8 L 432.5,103.9 L 436.4,106.0 L 440.3,108.0 L 444.2,110.0 L 448.1,112.0 L 452.0,114.0 L 455.9,115.9 L 459.8,117.8 L 463.7,119.6 L 467.6,121.4 L 471.5,123.0 L 475.4,124.6 L 479.3,126.2 L 483.2,127.6 L 487.1,129.0 L 491.1,130.3 L 495.0,131.5 L 498.9,132.7 L 502.8,133.7 L 506.7,134.7 L 510.6,135.6 L 514.5,136.5" fill="none" stroke="#6B6B6B" stroke-width="1.6"/>
  <path d="M 50.0,143.9 L 53.9,143.9 L 57.8,143.9 L 61.7,143.9 L 65.6,143.9 L 69.5,143.8 L 73.4,143.8 L 77.3,143.7 L 81.2,143.7 L 85.1,143.6 L 89.0,143.5 L 92.9,143.4 L 96.8,143.3 L 100.7,143.1 L 104.6,143.0 L 108.5,142.8 L 112.4,142.5 L 116.3,142.2 L 120.2,141.9 L 124.1,141.6 L 128.0,141.1 L 131.9,140.7 L 135.8,140.1 L 139.7,139.5 L 143.6,138.8 L 147.5,138.1 L 151.4,137.2 L 155.3,136.3 L 159.2,135.2 L 163.1,134.1 L 167.0,132.8 L 170.9,131.4 L 174.8,129.9 L 178.7,128.3 L 182.6,126.6 L 186.5,124.8 L 190.4,122.9 L 194.3,120.9 L 198.2,118.7 L 202.1,116.5 L 206.0,114.2 L 209.9,111.9 L 213.8,109.5 L 217.7,107.0 L 221.6,104.6 L 225.5,102.1 L 229.4,99.7 L 233.3,97.3 L 237.2,94.9 L 241.1,92.7 L 245.0,90.5 L 248.9,88.5 L 252.8,86.6 L 256.7,84.9 L 260.6,83.4 L 264.5,82.1 L 268.4,81.0 L 272.3,80.1 L 276.2,79.5 L 280.1,79.1 L 284.0,79.0 L 287.9,79.1 L 291.8,79.5 L 295.7,80.1 L 299.6,81.0 L 303.5,82.1 L 307.4,83.4 L 311.3,84.9 L 315.2,86.6 L 319.1,88.5 L 323.0,90.5 L 326.9,92.7 L 330.8,94.9 L 334.7,97.3 L 338.6,99.7 L 342.5,102.1 L 346.4,104.6 L 350.3,107.0 L 354.2,109.5 L 358.1,111.9 L 362.0,114.2 L 365.9,116.5 L 369.8,118.7 L 373.7,120.9 L 377.6,122.9 L 381.5,124.8 L 385.4,126.6 L 389.3,128.3 L 393.2,129.9 L 397.1,131.4 L 401.0,132.8 L 404.9,134.1 L 408.8,135.2 L 412.7,136.3 L 416.6,137.2 L 420.5,138.1 L 424.4,138.8 L 428.3,139.5 L 432.2,140.1 L 436.1,140.7 L 440.0,141.1 L 443.9,141.6 L 447.8,141.9 L 451.7,142.2 L 455.6,142.5 L 459.5,142.8 L 463.4,143.0 L 467.3,143.1 L 471.2,143.3 L 475.1,143.4 L 479.0,143.5 L 482.9,143.6 L 486.8,143.7 L 490.7,143.7 L 494.6,143.8 L 498.5,143.8 L 502.4,143.9 L 506.3,143.9 L 510.2,143.9 L 514.1,143.9 L 518.0,143.9" fill="none" stroke="#FF00FF" stroke-width="1.6"/>
  <path d="M 50.0,144.0 L 53.9,144.0 L 57.8,144.0 L 61.7,144.0 L 65.6,144.0 L 69.5,144.0 L 73.4,144.0 L 77.3,144.0 L 81.2,144.0 L 85.1,144.0 L 89.0,144.0 L 92.9,144.0 L 96.8,144.0 L 100.7,144.0 L 104.6,144.0 L 108.5,144.0 L 112.4,144.0 L 116.3,144.0 L 120.2,144.0 L 124.1,144.0 L 128.0,144.0 L 131.9,144.0 L 135.8,144.0 L 139.7,144.0 L 143.6,144.0 L 147.5,144.0 L 151.4,144.0 L 155.3,144.0 L 159.2,144.0 L 163.1,143.9 L 167.0,143.9 L 170.9,143.8 L 174.8,143.7 L 178.7,143.6 L 182.6,143.3 L 186.5,143.0 L 190.4,142.6 L 194.3,141.9 L 198.2,141.0 L 202.1,139.9 L 206.0,138.3 L 209.9,136.3 L 213.8,133.7 L 217.7,130.4 L 221.6,126.4 L 225.5,121.6 L 229.4,115.9 L 233.3,109.3 L 237.2,101.8 L 241.1,93.5 L 245.0,84.5 L 248.9,75.0 L 252.8,65.2 L 256.7,55.3 L 260.6,45.9 L 264.5,37.1 L 268.4,29.3 L 272.3,22.8 L 276.2,18.0 L 280.1,15.0 L 284.0,14.0 L 287.9,15.0 L 291.8,18.0 L 295.7,22.8 L 299.6,29.3 L 303.5,37.1 L 307.4,45.9 L 311.3,55.3 L 315.2,65.2 L 319.1,75.0 L 323.0,84.5 L 326.9,93.5 L 330.8,101.8 L 334.7,109.3 L 338.6,115.9 L 342.5,121.6 L 346.4,126.4 L 350.3,130.4 L 354.2,133.7 L 358.1,136.3 L 362.0,138.3 L 365.9,139.9 L 369.8,141.0 L 373.7,141.9 L 377.6,142.6 L 381.5,143.0 L 385.4,143.3 L 389.3,143.6 L 393.2,143.7 L 397.1,143.8 L 401.0,143.9 L 404.9,143.9 L 408.8,144.0 L 412.7,144.0 L 416.6,144.0 L 420.5,144.0 L 424.4,144.0 L 428.3,144.0 L 432.2,144.0 L 436.1,144.0 L 440.0,144.0 L 443.9,144.0 L 447.8,144.0 L 451.7,144.0 L 455.6,144.0 L 459.5,144.0 L 463.4,144.0 L 467.3,144.0 L 471.2,144.0 L 475.1,144.0 L 479.0,144.0 L 482.9,144.0 L 486.8,144.0 L 490.7,144.0 L 494.6,144.0 L 498.5,144.0 L 502.4,144.0 L 506.3,144.0 L 510.2,144.0 L 514.1,144.0 L 518.0,144.0" fill="none" stroke="#1A1A1A" stroke-width="1.6"/>
  <text x="89" y="158" style="font-size:10px;font-family:'JetBrains Mono',monospace;fill:#1A1A1A;text-anchor:middle;">150</text>
  <text x="186.5" y="158" style="font-size:10px;font-family:'JetBrains Mono',monospace;fill:#1A1A1A;text-anchor:middle;">160</text>
  <text x="284" y="158" style="font-size:10px;font-family:'JetBrains Mono',monospace;fill:#1A1A1A;text-anchor:middle;">μ=175</text>
  <text x="381.5" y="158" style="font-size:10px;font-family:'JetBrains Mono',monospace;fill:#1A1A1A;text-anchor:middle;">190</text>
  <text x="479" y="158" style="font-size:10px;font-family:'JetBrains Mono',monospace;fill:#1A1A1A;text-anchor:middle;">200</text>
  <text x="284" y="173" style="font-size:11px;font-family:'Inter',system-ui,sans-serif;fill:#6B6B6B;text-anchor:middle;">height h (cm)</text>
  <text x="14" y="79" style="font-size:11px;font-family:'Inter',system-ui,sans-serif;fill:#6B6B6B;text-anchor:middle;" transform="rotate(-90 14 79)">density f(h)</text>
  <rect x="60" y="20" width="160" height="62" fill="rgba(255,255,255,0.92)" stroke="#EEEEEE"/>
  <line x1="68" y1="32" x2="90" y2="32" stroke="#1A1A1A" stroke-width="2.2"/>
  <text x="98" y="36" style="font-size:10px;font-family:'JetBrains Mono',monospace;fill:#1A1A1A;">N(175, 4²)</text>
  <line x1="68" y1="48" x2="90" y2="48" stroke="#FF00FF" stroke-width="2.2"/>
  <text x="98" y="52" style="font-size:10px;font-family:'JetBrains Mono',monospace;fill:#1A1A1A;">N(175, 8²)</text>
  <line x1="68" y1="64" x2="90" y2="64" stroke="#6B6B6B" stroke-width="2.2"/>
  <text x="98" y="68" style="font-size:10px;font-family:'JetBrains Mono',monospace;fill:#1A1A1A;">N(183, 8²)</text>
</svg>

Three random variables from the same family (**Normal**) with different parameters. The first two share location and differ in spread, and the third shifts the **location** to a new mean.

---
layout: statement
---

# Distributions known<br>Parameters <span class="pink">known</span>

<!--
The frame of probability theory. The model is given. Our task inside this frame is to deduce.
-->

---
layout: section
class: tint-mint
---

## 02

# LLN and CLT

---

# LLN

For iid random variables $X_1, \ldots, X_n$ with finite mean $\mathbb{E}[X] = \mu$, the sample mean converges in probability to $\mu$:

$$\bar X_n = \frac{X_1 + \cdots + X_n}{n} \xrightarrow{P} \mu \quad \text{as } n \to \infty$$

<div style="margin-top:1.4rem;text-align:center;">
<a href="/harbour-product-analytics-2026/06-statistics-2/lln-sim.html" target="_blank" style="display:inline-block;padding:0.6rem 1.2rem;border:1.5px solid #1A1A1A;background:#FAFAFA;color:#1A1A1A;font-family:'JetBrains Mono',monospace;font-size:0.95rem;text-decoration:none;">↗ Open simulation</a>
</div>

<p style="margin-top:1.6rem;color:#6B6B6B;font-size:0.95rem;text-align:center;">Intuition: with enough data the sample mean settles on the true mean.</p>

<!--
State inside probability framework. RVs with known distributions, result is about their average. Not yet about samples or estimators. The simulation runs in the browser — pick a source distribution, draw n=10000 samples, watch the running mean settle on μ.
-->

---

# CLT

For iid random variables $X_1, \ldots, X_n$ with finite mean $\mu$ and variance $\sigma^2$, the standardised average

$$\sqrt{n} \cdot \frac{\frac{X_1 + \cdots + X_n}{n} - \mu}{\sigma}$$

approaches the standard <span class="pink">Normal</span> distribution $\mathcal{N}(0, 1)$ as $n \to \infty$

<div style="margin-top:1.4rem;text-align:center;">
<a href="/harbour-product-analytics-2026/06-statistics-2/clt-sim.html" target="_blank" style="display:inline-block;padding:0.6rem 1.2rem;border:1.5px solid #1A1A1A;background:#FAFAFA;color:#1A1A1A;font-family:'JetBrains Mono',monospace;font-size:0.95rem;text-decoration:none;">↗ Open simulation</a>
</div>

<p style="margin-top:1.6rem;color:#6B6B6B;font-size:0.95rem;text-align:center;">Intuition: averages of many independent draws look Normal whatever the original distribution is.</p>

<!--
State inside probability framework. The original X can have almost any distribution; the standardised average tends to Normal. Sim lets us flip source distribution and watch the histogram of the standardised mean converge to N(0,1) as n grows. Cauchy is included as the counterexample where variance is infinite and convergence never happens.
-->

---
layout: section
class: tint-rose
---

## 03

# From probability<br>to statistics

---
layout: statement
---

# Distribution unknown<br>Parameters unknown<br>Data is <span class="pink">all</span> we have

<!--
The inverse problem. In probability the model was given. In statistics the data is given and the model is what we infer.
-->

---

# Statistical inference

<svg viewBox="0 0 860 320" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:880px;height:auto;display:block;margin-top:0.4rem;font-family:'Inter',system-ui,sans-serif;">
  <defs>
    <marker id="arr" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto" markerUnits="strokeWidth">
      <polygon points="0 0, 8 4.5, 0 9" fill="#1A1A1A"/>
    </marker>
  </defs>

  <!-- Top row: 3 boxes -->
  <rect x="30" y="20" width="200" height="80" rx="6" fill="#FAFAFA" stroke="#1A1A1A" stroke-width="1.2"/>
  <text x="130" y="50" style="font-size:14px;font-weight:700;fill:#1A1A1A;text-anchor:middle;">Observed data</text>
  <text x="130" y="76" style="font-size:13px;fill:#6B6B6B;text-anchor:middle;font-family:'JetBrains Mono',monospace;">X_1, ..., X_n</text>

  <rect x="290" y="20" width="240" height="80" rx="6" fill="#FAFAFA" stroke="#1A1A1A" stroke-width="1.2"/>
  <text x="410" y="50" style="font-size:14px;font-weight:700;fill:#1A1A1A;text-anchor:middle;">Random variables</text>
  <text x="410" y="76" style="font-size:12px;fill:#6B6B6B;text-anchor:middle;">with an unknown distribution</text>

  <rect x="590" y="20" width="240" height="80" rx="6" fill="#FAFAFA" stroke="#1A1A1A" stroke-width="1.2"/>
  <text x="710" y="50" style="font-size:14px;font-weight:700;fill:#1A1A1A;text-anchor:middle;">Infer the distribution</text>
  <text x="710" y="76" style="font-size:12px;fill:#6B6B6B;text-anchor:middle;">the goal of statistical inference</text>

  <!-- arrows top row -->
  <line x1="232" y1="60" x2="285" y2="60" stroke="#1A1A1A" stroke-width="1.6" marker-end="url(#arr)"/>
  <line x1="532" y1="60" x2="585" y2="60" stroke="#1A1A1A" stroke-width="1.6" marker-end="url(#arr)"/>

  <!-- Junction down from box 3 -->
  <line x1="710" y1="100" x2="710" y2="160" stroke="#1A1A1A" stroke-width="1.6"/>

  <!-- Horizontal junction line at y=160 -->
  <line x1="240" y1="160" x2="710" y2="160" stroke="#1A1A1A" stroke-width="1.6"/>

  <!-- Down arrows to bottom boxes -->
  <line x1="240" y1="160" x2="240" y2="208" stroke="#1A1A1A" stroke-width="1.6" marker-end="url(#arr)"/>
  <line x1="600" y1="160" x2="600" y2="208" stroke="#1A1A1A" stroke-width="1.6" marker-end="url(#arr)"/>

  <!-- Bottom row: 2 boxes -->
  <rect x="60" y="210" width="360" height="90" rx="6" fill="#FAFAFA" stroke="#1A1A1A" stroke-width="1.2"/>
  <text x="240" y="240" style="font-size:15px;font-weight:700;fill:#1A1A1A;text-anchor:middle;">Parametric</text>
  <text x="240" y="266" style="font-size:13px;fill:#6B6B6B;text-anchor:middle;">Assume a family</text>
  <text x="240" y="284" style="font-size:13px;fill:#6B6B6B;text-anchor:middle;">Estimate the parameters</text>

  <rect x="420" y="210" width="360" height="90" rx="6" fill="#FAFAFA" stroke="#1A1A1A" stroke-width="1.2"/>
  <text x="600" y="248" style="font-size:15px;font-weight:700;fill:#1A1A1A;text-anchor:middle;">Non-parametric</text>
  <text x="600" y="274" style="font-size:13px;fill:#6B6B6B;text-anchor:middle;">No family assumption</text>
</svg>

---

# Sample

A sample is $n$ observations $X_1, \ldots, X_n$ that are typically assumed **i.i.d.**, meaning independent and identically distributed, where each $X_i$ is a realisation of the same underlying random variable $X$.

<div style="margin-top:1.2rem;padding:0.8rem 1rem;border-left:3px solid #FF00FF;background:#FAFAFA;font-size:0.95rem;color:#1A1A1A;line-height:1.55;">

**Independent**, in plain words: knowing one observation tells us <span class="pink">nothing</span> about another. The user who came at 10:01 says nothing about the user who comes at 10:02.

</div>

---

# Statistic

A statistic is any <span class="pink">function</span> of the sample

| Statistic | Computed as |
|---|---|
| Sample mean | $\bar X = \frac{1}{n}\sum_{i=1}^{n} X_i$ |
| Sample variance | $S^2 = \frac{1}{n-1}\sum_{i=1}^{n}(X_i - \bar X)^2$ |
| Sample proportion | count of successes divided by $n$ |

---

# Estimator

An **estimator** is a statistic used to estimate an unknown <span class="pink">parameter</span> $\theta$ of the distribution. We write $\hat\theta$ for the estimator.

| Parameter | Common estimator |
|---|---|
| $\mathbb{E}[X] = \mu$ | Sample mean $\hat\mu = \bar X$ |
| $\mathrm{Var}(X) = \sigma^2$ | Sample variance $\hat{\sigma}^2 = S^2$ |
| $\mathbb{P}(A) = p$ | Sample proportion $\hat p$ |

<!--
The estimator is the recipe. The estimate is the number you get when you apply the recipe to a specific sample.
-->

---

# Estimating parameters from a sample

<svg viewBox="0 0 860 290" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:880px;height:auto;display:block;margin-top:0.6rem;font-family:'Inter',system-ui,sans-serif;">
  <defs>
    <marker id="arr2" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto" markerUnits="strokeWidth">
      <polygon points="0 0, 8 4.5, 0 9" fill="#1A1A1A"/>
    </marker>
  </defs>

  <!-- Inputs row (two boxes side by side) -->
  <rect x="60" y="20" width="280" height="76" rx="6" fill="#FAFAFA" stroke="#1A1A1A" stroke-width="1.2"/>
  <text x="200" y="50" style="font-size:14px;font-weight:700;fill:#1A1A1A;text-anchor:middle;">Data</text>
  <text x="200" y="74" style="font-size:13px;fill:#6B6B6B;text-anchor:middle;font-family:'JetBrains Mono',monospace;">X_1, ..., X_n</text>

  <rect x="520" y="20" width="280" height="76" rx="6" fill="#FAFAFA" stroke="#1A1A1A" stroke-width="1.2"/>
  <text x="660" y="50" style="font-size:14px;font-weight:700;fill:#1A1A1A;text-anchor:middle;">Assumptions</text>
  <text x="660" y="74" style="font-size:13px;fill:#6B6B6B;text-anchor:middle;">i.i.d., distribution family, ...</text>

  <!-- Arrows from inputs down into Estimator -->
  <line x1="200" y1="96" x2="380" y2="140" stroke="#1A1A1A" stroke-width="1.6" marker-end="url(#arr2)"/>
  <line x1="660" y1="96" x2="480" y2="140" stroke="#1A1A1A" stroke-width="1.6" marker-end="url(#arr2)"/>

  <!-- Estimator box (center) -->
  <rect x="330" y="142" width="200" height="68" rx="6" fill="#FAFAFA" stroke="#FF00FF" stroke-width="1.6"/>
  <text x="430" y="172" style="font-size:15px;font-weight:700;fill:#1A1A1A;text-anchor:middle;">Estimator</text>
  <text x="430" y="194" style="font-size:12px;fill:#6B6B6B;text-anchor:middle;">function of the sample</text>

  <!-- Down arrow to result -->
  <line x1="430" y1="210" x2="430" y2="234" stroke="#1A1A1A" stroke-width="1.6" marker-end="url(#arr2)"/>

  <!-- Result box -->
  <rect x="180" y="236" width="500" height="44" rx="6" fill="#FAFAFA" stroke="#1A1A1A" stroke-width="1.2"/>
  <text x="430" y="263" style="font-size:14px;font-weight:700;fill:#1A1A1A;text-anchor:middle;">Estimate · answer · prediction · decision</text>
</svg>

---
layout: statement
---

# A statistic is itself<br>a <span class="pink">random variable</span>

<!--
The conceptual hinge. State three times verbatim across this slide and the next.
-->

---

# Why

Each observation is a realisation of a random variable, so any function we build from them is itself a random variable and has its own distribution.

<svg viewBox="0 0 860 280" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:880px;height:auto;display:block;margin-top:0.8rem;font-family:'Inter',system-ui,sans-serif;">
  <defs>
    <marker id="arr3" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto" markerUnits="strokeWidth">
      <polygon points="0 0, 8 4.5, 0 9" fill="#1A1A1A"/>
    </marker>
  </defs>

  <circle cx="180" cy="40" r="24" fill="#FAFAFA" stroke="#1A1A1A" stroke-width="1.2"/>
  <text x="180" y="46" style="font-size:14px;font-family:'JetBrains Mono',monospace;fill:#1A1A1A;text-anchor:middle;">X₁</text>

  <circle cx="290" cy="40" r="24" fill="#FAFAFA" stroke="#1A1A1A" stroke-width="1.2"/>
  <text x="290" y="46" style="font-size:14px;font-family:'JetBrains Mono',monospace;fill:#1A1A1A;text-anchor:middle;">X₂</text>

  <circle cx="400" cy="40" r="24" fill="#FAFAFA" stroke="#1A1A1A" stroke-width="1.2"/>
  <text x="400" y="46" style="font-size:14px;font-family:'JetBrains Mono',monospace;fill:#1A1A1A;text-anchor:middle;">X₃</text>

  <text x="500" y="46" style="font-size:16px;font-family:'JetBrains Mono',monospace;fill:#6B6B6B;text-anchor:middle;">···</text>

  <circle cx="600" cy="40" r="24" fill="#FAFAFA" stroke="#1A1A1A" stroke-width="1.2"/>
  <text x="600" y="46" style="font-size:11px;font-family:'JetBrains Mono',monospace;fill:#1A1A1A;text-anchor:middle;">Xₙ₋₁</text>

  <circle cx="700" cy="40" r="24" fill="#FAFAFA" stroke="#1A1A1A" stroke-width="1.2"/>
  <text x="700" y="46" style="font-size:14px;font-family:'JetBrains Mono',monospace;fill:#1A1A1A;text-anchor:middle;">Xₙ</text>

  <line x1="180" y1="66" x2="370" y2="138" stroke="#1A1A1A" stroke-width="1.4" marker-end="url(#arr3)"/>
  <line x1="290" y1="66" x2="405" y2="138" stroke="#1A1A1A" stroke-width="1.4" marker-end="url(#arr3)"/>
  <line x1="400" y1="66" x2="435" y2="138" stroke="#1A1A1A" stroke-width="1.4" marker-end="url(#arr3)"/>
  <line x1="600" y1="66" x2="490" y2="138" stroke="#1A1A1A" stroke-width="1.4" marker-end="url(#arr3)"/>
  <line x1="700" y1="66" x2="520" y2="138" stroke="#1A1A1A" stroke-width="1.4" marker-end="url(#arr3)"/>

  <rect x="330" y="142" width="200" height="60" rx="6" fill="#FAFAFA" stroke="#FF00FF" stroke-width="1.6"/>
  <text x="430" y="168" style="font-size:14px;font-weight:700;fill:#1A1A1A;text-anchor:middle;">Statistic</text>
  <text x="430" y="190" style="font-size:13px;fill:#6B6B6B;text-anchor:middle;font-family:'JetBrains Mono',monospace;">T = f(X₁, ..., Xₙ)</text>

  <line x1="430" y1="202" x2="430" y2="222" stroke="#1A1A1A" stroke-width="1.6" marker-end="url(#arr3)"/>

  <rect x="220" y="226" width="420" height="46" rx="6" fill="#FAFAFA" stroke="#1A1A1A" stroke-width="1.2"/>
  <text x="430" y="254" style="font-size:13px;fill:#6B6B6B;text-anchor:middle;">a random variable with its own distribution</text>
</svg>

---

# Sampling distribution

The distribution of a statistic across all possible samples of size $n$ from the same population is its <span class="pink">sampling distribution</span>. For the sample mean, CLT tells us this distribution is approximately Normal at large $n$.

<div style="margin-top:1.4rem;text-align:center;">
<a href="/harbour-product-analytics-2026/06-statistics-2/sampling-sim.html" target="_blank" style="display:inline-block;padding:0.6rem 1.2rem;border:1.5px solid #1A1A1A;background:#FAFAFA;color:#1A1A1A;font-family:'JetBrains Mono',monospace;font-size:0.95rem;text-decoration:none;">↗ Open simulation</a>
</div>

<!--
Sim shows the full chain: a fresh sample of n observations appears as dots on a number line, we compute one statistic from it (sample mean), drop that one number onto a second plot, and repeat. The histogram on the second plot fills out — that is the sampling distribution.
-->

---
layout: section
class: tint-mint
---

## 04

# Confidence intervals

---
layout: statement
---

# A point estimate is not enough, so we need to <span class="pink">measure</span> its error

<!--
Combined motivator for CI. Different samples give different estimates, so a number on its own is not an answer — we need to quantify that variability before we can act on it. The rest of the section builds the apparatus.
-->

---

# Same number, different confidence

Two scenarios with the same point estimate $\hat p = 0.6$ for the conversion rate. The estimate by itself does not tell us how likely it is that a new sample would land somewhere close, or somewhere completely different.

<div style="margin-top:1rem;">
  <div style="font-family:'JetBrains Mono',monospace;font-size:0.8rem;color:#6B6B6B;text-transform:uppercase;letter-spacing:0.1em;">Case A · tight</div>
  <svg viewBox="0 0 720 60" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:780px;height:auto;display:block;margin-top:0.2rem;font-family:'Inter',system-ui,sans-serif;">
    <line x1="40" y1="32" x2="680" y2="32" stroke="#1A1A1A" stroke-width="1"/>
    <line x1="40" y1="28" x2="40" y2="36" stroke="#1A1A1A" stroke-width="1"/>
    <line x1="360" y1="28" x2="360" y2="36" stroke="#1A1A1A" stroke-width="1"/>
    <line x1="680" y1="28" x2="680" y2="36" stroke="#1A1A1A" stroke-width="1"/>
    <text x="40" y="52" style="font-size:10px;font-family:'JetBrains Mono',monospace;fill:#1A1A1A;text-anchor:middle;">0.0</text>
    <text x="360" y="52" style="font-size:10px;font-family:'JetBrains Mono',monospace;fill:#1A1A1A;text-anchor:middle;">0.5</text>
    <text x="680" y="52" style="font-size:10px;font-family:'JetBrains Mono',monospace;fill:#1A1A1A;text-anchor:middle;">1.0</text>
    <!-- CI bracket [0.55, 0.65] -->
    <line x1="392" y1="22" x2="424" y2="22" stroke="#1A1A1A" stroke-width="2.4"/>
    <line x1="392" y1="18" x2="392" y2="32" stroke="#1A1A1A" stroke-width="2"/>
    <line x1="424" y1="18" x2="424" y2="32" stroke="#1A1A1A" stroke-width="2"/>
    <!-- estimate dot at 0.6 -->
    <circle cx="408" cy="22" r="4" fill="#FF00FF"/>
    <text x="408" y="14" style="font-size:10px;font-family:'JetBrains Mono',monospace;fill:#1A1A1A;text-anchor:middle;">[0.55, 0.65]</text>
  </svg>
</div>

<div style="margin-top:1.2rem;">
  <div style="font-family:'JetBrains Mono',monospace;font-size:0.8rem;color:#6B6B6B;text-transform:uppercase;letter-spacing:0.1em;">Case B · wide</div>
  <svg viewBox="0 0 720 60" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:780px;height:auto;display:block;margin-top:0.2rem;font-family:'Inter',system-ui,sans-serif;">
    <line x1="40" y1="32" x2="680" y2="32" stroke="#1A1A1A" stroke-width="1"/>
    <line x1="40" y1="28" x2="40" y2="36" stroke="#1A1A1A" stroke-width="1"/>
    <line x1="360" y1="28" x2="360" y2="36" stroke="#1A1A1A" stroke-width="1"/>
    <line x1="680" y1="28" x2="680" y2="36" stroke="#1A1A1A" stroke-width="1"/>
    <text x="40" y="52" style="font-size:10px;font-family:'JetBrains Mono',monospace;fill:#1A1A1A;text-anchor:middle;">0.0</text>
    <text x="360" y="52" style="font-size:10px;font-family:'JetBrains Mono',monospace;fill:#1A1A1A;text-anchor:middle;">0.5</text>
    <text x="680" y="52" style="font-size:10px;font-family:'JetBrains Mono',monospace;fill:#1A1A1A;text-anchor:middle;">1.0</text>
    <!-- CI bracket [0.2, 0.8] -->
    <line x1="168" y1="22" x2="616" y2="22" stroke="#1A1A1A" stroke-width="2.4"/>
    <line x1="168" y1="18" x2="168" y2="32" stroke="#1A1A1A" stroke-width="2"/>
    <line x1="616" y1="18" x2="616" y2="32" stroke="#1A1A1A" stroke-width="2"/>
    <!-- estimate dot at 0.6 -->
    <circle cx="408" cy="22" r="4" fill="#FF00FF"/>
    <text x="392" y="14" style="font-size:10px;font-family:'JetBrains Mono',monospace;fill:#1A1A1A;text-anchor:middle;">[0.2, 0.8]</text>
  </svg>
</div>

<p style="font-size:0.95rem;color:#6B6B6B;margin-top:1.2rem;line-height:1.5;">
Same point estimate leads to very different decisions about whether to ship.
</p>

---

# Confidence interval

A confidence <span class="pink">interval</span> for the unknown parameter $\theta$ is a random interval $[L, U]$ that contains $\theta$ in a chosen fraction of repeated samples:

$$\mathbb{P}(\theta \in [L, U]) \ge 1 - \alpha$$

The endpoints depend on the sample, so a different sample gives a different interval. The confidence level $1 - \alpha$ is typically $0.95$, and we pick it before looking at the data.

The confidence level reflects the **long-run reliability** of the method used to generate the interval: across many repeated samples, a fraction $1 - \alpha$ of the intervals it produces will contain $\theta$.

---

# Quantiles

The **$q$-quantile** of a distribution is the value $x_q$ such that $\mathbb{P}(X \le x_q) = q$. It is the cutoff where a fraction $q$ of the mass lies to the left.

<svg viewBox="0 0 720 170" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:720px;height:auto;display:block;margin-top:0.3rem;font-family:'Inter',system-ui,sans-serif;">
<path d="M 60.0,134.8 L 68.6,134.7 L 77.2,134.5 L 85.7,134.3 L 94.3,134.1 L 102.9,133.7 L 111.4,133.2 L 120.0,132.7 L 128.6,132.0 L 137.2,131.1 L 145.7,130.0 L 154.3,128.6 L 162.9,126.9 L 171.4,124.8 L 180.0,122.4 L 188.6,119.5 L 192.0,118.3 L 192.0,135 L 60.0,135 Z" fill="#FF00FF" fill-opacity="0.28"/>
<path d="M 528.0,118.3 L 531.4,119.5 L 540.0,122.4 L 548.6,124.8 L 557.1,126.9 L 565.7,128.6 L 574.3,130.0 L 582.8,131.1 L 591.4,132.0 L 600.0,132.7 L 608.6,133.2 L 617.1,133.7 L 625.7,134.1 L 634.3,134.3 L 642.8,134.5 L 651.4,134.7 L 660.0,134.8 L 660.0,135 L 528.0,135 Z" fill="#FF00FF" fill-opacity="0.28"/>
<path d="M 192.0,118.3 L 197.2,116.3 L 205.7,112.5 L 214.3,108.2 L 222.9,103.4 L 231.4,98.2 L 240.0,92.4 L 248.6,86.3 L 257.1,79.8 L 265.7,73.1 L 274.3,66.3 L 282.9,59.5 L 291.4,52.9 L 300.0,46.5 L 308.6,40.6 L 317.1,35.2 L 325.7,30.4 L 334.3,26.6 L 342.9,23.9 L 351.4,22.2 L 360.0,21.7 L 368.6,22.2 L 377.1,23.9 L 385.7,26.6 L 394.3,30.4 L 402.9,35.2 L 411.4,40.6 L 420.0,46.5 L 428.6,52.9 L 437.1,59.5 L 445.7,66.3 L 454.3,73.1 L 462.9,79.8 L 471.4,86.3 L 480.0,92.4 L 488.6,98.2 L 497.1,103.4 L 505.7,108.2 L 514.3,112.5 L 522.8,116.3 L 528.0,118.3 L 528.0,135 L 192.0,135 Z" fill="#1A1A1A" fill-opacity="0.06"/>
<path d="M 60.0,134.8 L 68.6,134.7 L 77.2,134.5 L 85.7,134.3 L 94.3,134.1 L 102.9,133.7 L 111.4,133.2 L 120.0,132.7 L 128.6,132.0 L 137.2,131.1 L 145.7,130.0 L 154.3,128.6 L 162.9,126.9 L 171.4,124.8 L 180.0,122.4 L 188.6,119.5 L 197.2,116.3 L 205.7,112.5 L 214.3,108.2 L 222.9,103.4 L 231.4,98.2 L 240.0,92.4 L 248.6,86.3 L 257.1,79.8 L 265.7,73.1 L 274.3,66.3 L 282.9,59.5 L 291.4,52.9 L 300.0,46.5 L 308.6,40.6 L 317.1,35.2 L 325.7,30.4 L 334.3,26.6 L 342.9,23.9 L 351.4,22.2 L 360.0,21.7 L 368.6,22.2 L 377.1,23.9 L 385.7,26.6 L 394.3,30.4 L 402.9,35.2 L 411.4,40.6 L 420.0,46.5 L 428.6,52.9 L 437.1,59.5 L 445.7,66.3 L 454.3,73.1 L 462.9,79.8 L 471.4,86.3 L 480.0,92.4 L 488.6,98.2 L 497.1,103.4 L 505.7,108.2 L 514.3,112.5 L 522.8,116.3 L 531.4,119.5 L 540.0,122.4 L 548.6,124.8 L 557.1,126.9 L 565.7,128.6 L 574.3,130.0 L 582.8,131.1 L 591.4,132.0 L 600.0,132.7 L 608.6,133.2 L 617.1,133.7 L 625.7,134.1 L 634.3,134.3 L 642.8,134.5 L 651.4,134.7 L 660.0,134.8" fill="none" stroke="#1A1A1A" stroke-width="1.6"/>
<line x1="60" y1="135" x2="660" y2="135" stroke="#1A1A1A" stroke-width="1"/>
<line x1="192" y1="135" x2="192" y2="119" stroke="#1A1A1A" stroke-width="1" stroke-dasharray="3 3"/>
<line x1="528" y1="135" x2="528" y2="119" stroke="#1A1A1A" stroke-width="1" stroke-dasharray="3 3"/>
<text x="125" y="128" style="font-size:10px;fill:#FF00FF;font-weight:700;text-anchor:middle;">2.5%</text>
<text x="595" y="128" style="font-size:10px;fill:#FF00FF;font-weight:700;text-anchor:middle;">2.5%</text>
<text x="360" y="92" style="font-size:13px;fill:#1A1A1A;font-weight:700;text-anchor:middle;">95%</text>
<text x="192" y="152" style="font-size:10px;font-family:'JetBrains Mono',monospace;fill:#1A1A1A;text-anchor:middle;">−1.96</text>
<text x="528" y="152" style="font-size:10px;font-family:'JetBrains Mono',monospace;fill:#1A1A1A;text-anchor:middle;">1.96</text>
<text x="360" y="152" style="font-size:10px;font-family:'JetBrains Mono',monospace;fill:#6B6B6B;text-anchor:middle;">0</text>
<text x="676" y="139" style="font-size:11px;font-style:italic;fill:#6B6B6B;">z</text>
</svg>

Quantiles depend on the distribution. **When the statistic is standard Normal**, the central 95% of its mass lies between $z_{0.025} = -1.96$ and $z_{0.975} = 1.96$, with 2.5% in each tail.

<!--
Pedagogical anchor. Quantiles are the building block for both CI and HT. Walk slowly: a q-quantile is a value with q probability to its left. For symmetric distributions like N(0,1), the 0.025 quantile is −1.96 and the 0.975 quantile is +1.96 — so the central 95% sits between them. This is the same logic that will return in HT: rejection regions are quantile cutoffs. Same machinery, different question.
-->

---

# Standard error

The standard error of the sample mean $\bar X$ is

$$\mathrm{SE}(\bar X) = \frac{\sigma}{\sqrt{n}}$$

Bigger $n$ shrinks $\mathrm{SE}$, and the sampling distribution of $\bar X$ tightens around <span class="pink">$\mu$</span>.

<svg viewBox="0 0 720 180" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:560px;height:auto;display:block;margin:0.3rem auto 0;font-family:'Inter',system-ui,sans-serif;">
  <rect x="80" y="14" width="560" height="132" fill="#FAFAFA"/>
  <line x1="80" y1="146" x2="640" y2="146" stroke="#1A1A1A" stroke-width="1"/>
  <line x1="360" y1="146" x2="360" y2="14" stroke="#1A1A1A" stroke-width="1" stroke-dasharray="2,3"/>
  <path d="M 80.0,146.0 L 82.3,146.0 L 84.7,146.0 L 87.0,146.0 L 89.3,146.0 L 91.7,146.0 L 94.0,146.0 L 96.3,146.0 L 98.7,146.0 L 101.0,146.0 L 103.3,146.0 L 105.7,146.0 L 108.0,146.0 L 110.3,146.0 L 112.7,146.0 L 115.0,145.9 L 117.3,145.9 L 119.7,145.9 L 122.0,145.9 L 124.3,145.9 L 126.7,145.9 L 129.0,145.9 L 131.3,145.9 L 133.7,145.9 L 136.0,145.9 L 138.3,145.9 L 140.7,145.8 L 143.0,145.8 L 145.3,145.8 L 147.7,145.8 L 150.0,145.8 L 152.3,145.7 L 154.7,145.7 L 157.0,145.7 L 159.3,145.7 L 161.7,145.6 L 164.0,145.6 L 166.3,145.6 L 168.7,145.5 L 171.0,145.5 L 173.3,145.5 L 175.7,145.4 L 178.0,145.4 L 180.3,145.3 L 182.7,145.3 L 185.0,145.2 L 187.3,145.1 L 189.7,145.1 L 192.0,145.0 L 194.3,144.9 L 196.7,144.9 L 199.0,144.8 L 201.3,144.7 L 203.7,144.6 L 206.0,144.5 L 208.3,144.4 L 210.7,144.3 L 213.0,144.2 L 215.3,144.1 L 217.7,143.9 L 220.0,143.8 L 222.3,143.7 L 224.7,143.5 L 227.0,143.4 L 229.3,143.2 L 231.7,143.1 L 234.0,142.9 L 236.3,142.8 L 238.7,142.6 L 241.0,142.4 L 243.3,142.2 L 245.7,142.0 L 248.0,141.8 L 250.3,141.6 L 252.7,141.4 L 255.0,141.2 L 257.3,141.0 L 259.7,140.8 L 262.0,140.5 L 264.3,140.3 L 266.7,140.1 L 269.0,139.8 L 271.3,139.6 L 273.7,139.3 L 276.0,139.1 L 278.3,138.8 L 280.7,138.6 L 283.0,138.3 L 285.3,138.1 L 287.7,137.8 L 290.0,137.6 L 292.3,137.3 L 294.7,137.1 L 297.0,136.8 L 299.3,136.6 L 301.7,136.3 L 304.0,136.1 L 306.3,135.9 L 308.7,135.6 L 311.0,135.4 L 313.3,135.2 L 315.7,135.0 L 318.0,134.8 L 320.3,134.6 L 322.7,134.4 L 325.0,134.2 L 327.3,134.0 L 329.7,133.9 L 332.0,133.7 L 334.3,133.6 L 336.7,133.4 L 339.0,133.3 L 341.3,133.2 L 343.7,133.1 L 346.0,133.0 L 348.3,133.0 L 350.7,132.9 L 353.0,132.9 L 355.3,132.8 L 357.7,132.8 L 360.0,132.8 L 362.3,132.8 L 364.7,132.8 L 367.0,132.9 L 369.3,132.9 L 371.7,133.0 L 374.0,133.0 L 376.3,133.1 L 378.7,133.2 L 381.0,133.3 L 383.3,133.4 L 385.7,133.6 L 388.0,133.7 L 390.3,133.9 L 392.7,134.0 L 395.0,134.2 L 397.3,134.4 L 399.7,134.6 L 402.0,134.8 L 404.3,135.0 L 406.7,135.2 L 409.0,135.4 L 411.3,135.6 L 413.7,135.9 L 416.0,136.1 L 418.3,136.3 L 420.7,136.6 L 423.0,136.8 L 425.3,137.1 L 427.7,137.3 L 430.0,137.6 L 432.3,137.8 L 434.7,138.1 L 437.0,138.3 L 439.3,138.6 L 441.7,138.8 L 444.0,139.1 L 446.3,139.3 L 448.7,139.6 L 451.0,139.8 L 453.3,140.1 L 455.7,140.3 L 458.0,140.5 L 460.3,140.8 L 462.7,141.0 L 465.0,141.2 L 467.3,141.4 L 469.7,141.6 L 472.0,141.8 L 474.3,142.0 L 476.7,142.2 L 479.0,142.4 L 481.3,142.6 L 483.7,142.8 L 486.0,142.9 L 488.3,143.1 L 490.7,143.2 L 493.0,143.4 L 495.3,143.5 L 497.7,143.7 L 500.0,143.8 L 502.3,143.9 L 504.7,144.1 L 507.0,144.2 L 509.3,144.3 L 511.7,144.4 L 514.0,144.5 L 516.3,144.6 L 518.7,144.7 L 521.0,144.8 L 523.3,144.9 L 525.7,144.9 L 528.0,145.0 L 530.3,145.1 L 532.7,145.1 L 535.0,145.2 L 537.3,145.3 L 539.7,145.3 L 542.0,145.4 L 544.3,145.4 L 546.7,145.5 L 549.0,145.5 L 551.3,145.5 L 553.7,145.6 L 556.0,145.6 L 558.3,145.6 L 560.7,145.7 L 563.0,145.7 L 565.3,145.7 L 567.7,145.7 L 570.0,145.8 L 572.3,145.8 L 574.7,145.8 L 577.0,145.8 L 579.3,145.8 L 581.7,145.9 L 584.0,145.9 L 586.3,145.9 L 588.7,145.9 L 591.0,145.9 L 593.3,145.9 L 595.7,145.9 L 598.0,145.9 L 600.3,145.9 L 602.7,145.9 L 605.0,145.9 L 607.3,146.0 L 609.7,146.0 L 612.0,146.0 L 614.3,146.0 L 616.7,146.0 L 619.0,146.0 L 621.3,146.0 L 623.7,146.0 L 626.0,146.0 L 628.3,146.0 L 630.7,146.0 L 633.0,146.0 L 635.3,146.0 L 637.7,146.0 L 640.0,146.0" fill="none" stroke="#6B6B6B" stroke-width="1.6" opacity="0.85"/>
  <path d="M 80.0,146.0 L 82.3,146.0 L 84.7,146.0 L 87.0,146.0 L 89.3,146.0 L 91.7,146.0 L 94.0,146.0 L 96.3,146.0 L 98.7,146.0 L 101.0,146.0 L 103.3,146.0 L 105.7,146.0 L 108.0,146.0 L 110.3,146.0 L 112.7,146.0 L 115.0,146.0 L 117.3,146.0 L 119.7,146.0 L 122.0,146.0 L 124.3,146.0 L 126.7,146.0 L 129.0,146.0 L 131.3,146.0 L 133.7,146.0 L 136.0,146.0 L 138.3,146.0 L 140.7,146.0 L 143.0,146.0 L 145.3,146.0 L 147.7,146.0 L 150.0,146.0 L 152.3,146.0 L 154.7,146.0 L 157.0,146.0 L 159.3,146.0 L 161.7,146.0 L 164.0,146.0 L 166.3,146.0 L 168.7,146.0 L 171.0,146.0 L 173.3,146.0 L 175.7,146.0 L 178.0,146.0 L 180.3,146.0 L 182.7,146.0 L 185.0,146.0 L 187.3,146.0 L 189.7,146.0 L 192.0,146.0 L 194.3,146.0 L 196.7,146.0 L 199.0,146.0 L 201.3,146.0 L 203.7,146.0 L 206.0,146.0 L 208.3,146.0 L 210.7,146.0 L 213.0,146.0 L 215.3,146.0 L 217.7,146.0 L 220.0,146.0 L 222.3,146.0 L 224.7,146.0 L 227.0,146.0 L 229.3,146.0 L 231.7,146.0 L 234.0,146.0 L 236.3,146.0 L 238.7,146.0 L 241.0,146.0 L 243.3,146.0 L 245.7,146.0 L 248.0,146.0 L 250.3,146.0 L 252.7,146.0 L 255.0,146.0 L 257.3,146.0 L 259.7,146.0 L 262.0,146.0 L 264.3,146.0 L 266.7,146.0 L 269.0,146.0 L 271.3,146.0 L 273.7,146.0 L 276.0,145.9 L 278.3,145.9 L 280.7,145.9 L 283.0,145.8 L 285.3,145.8 L 287.7,145.7 L 290.0,145.5 L 292.3,145.4 L 294.7,145.2 L 297.0,144.9 L 299.3,144.6 L 301.7,144.2 L 304.0,143.7 L 306.3,143.0 L 308.7,142.3 L 311.0,141.4 L 313.3,140.4 L 315.7,139.1 L 318.0,137.7 L 320.3,136.2 L 322.7,134.4 L 325.0,132.4 L 327.3,130.3 L 329.7,128.1 L 332.0,125.7 L 334.3,123.2 L 336.7,120.7 L 339.0,118.2 L 341.3,115.7 L 343.7,113.3 L 346.0,111.1 L 348.3,109.2 L 350.7,107.5 L 353.0,106.1 L 355.3,105.1 L 357.7,104.5 L 360.0,104.3 L 362.3,104.5 L 364.7,105.1 L 367.0,106.1 L 369.3,107.5 L 371.7,109.2 L 374.0,111.1 L 376.3,113.3 L 378.7,115.7 L 381.0,118.2 L 383.3,120.7 L 385.7,123.2 L 388.0,125.7 L 390.3,128.1 L 392.7,130.3 L 395.0,132.4 L 397.3,134.4 L 399.7,136.2 L 402.0,137.7 L 404.3,139.1 L 406.7,140.4 L 409.0,141.4 L 411.3,142.3 L 413.7,143.0 L 416.0,143.7 L 418.3,144.2 L 420.7,144.6 L 423.0,144.9 L 425.3,145.2 L 427.7,145.4 L 430.0,145.5 L 432.3,145.7 L 434.7,145.8 L 437.0,145.8 L 439.3,145.9 L 441.7,145.9 L 444.0,145.9 L 446.3,146.0 L 448.7,146.0 L 451.0,146.0 L 453.3,146.0 L 455.7,146.0 L 458.0,146.0 L 460.3,146.0 L 462.7,146.0 L 465.0,146.0 L 467.3,146.0 L 469.7,146.0 L 472.0,146.0 L 474.3,146.0 L 476.7,146.0 L 479.0,146.0 L 481.3,146.0 L 483.7,146.0 L 486.0,146.0 L 488.3,146.0 L 490.7,146.0 L 493.0,146.0 L 495.3,146.0 L 497.7,146.0 L 500.0,146.0 L 502.3,146.0 L 504.7,146.0 L 507.0,146.0 L 509.3,146.0 L 511.7,146.0 L 514.0,146.0 L 516.3,146.0 L 518.7,146.0 L 521.0,146.0 L 523.3,146.0 L 525.7,146.0 L 528.0,146.0 L 530.3,146.0 L 532.7,146.0 L 535.0,146.0 L 537.3,146.0 L 539.7,146.0 L 542.0,146.0 L 544.3,146.0 L 546.7,146.0 L 549.0,146.0 L 551.3,146.0 L 553.7,146.0 L 556.0,146.0 L 558.3,146.0 L 560.7,146.0 L 563.0,146.0 L 565.3,146.0 L 567.7,146.0 L 570.0,146.0 L 572.3,146.0 L 574.7,146.0 L 577.0,146.0 L 579.3,146.0 L 581.7,146.0 L 584.0,146.0 L 586.3,146.0 L 588.7,146.0 L 591.0,146.0 L 593.3,146.0 L 595.7,146.0 L 598.0,146.0 L 600.3,146.0 L 602.7,146.0 L 605.0,146.0 L 607.3,146.0 L 609.7,146.0 L 612.0,146.0 L 614.3,146.0 L 616.7,146.0 L 619.0,146.0 L 621.3,146.0 L 623.7,146.0 L 626.0,146.0 L 628.3,146.0 L 630.7,146.0 L 633.0,146.0 L 635.3,146.0 L 637.7,146.0 L 640.0,146.0" fill="none" stroke="#1A1A1A" stroke-width="1.8"/>
  <path d="M 80.0,146.0 L 82.3,146.0 L 84.7,146.0 L 87.0,146.0 L 89.3,146.0 L 91.7,146.0 L 94.0,146.0 L 96.3,146.0 L 98.7,146.0 L 101.0,146.0 L 103.3,146.0 L 105.7,146.0 L 108.0,146.0 L 110.3,146.0 L 112.7,146.0 L 115.0,146.0 L 117.3,146.0 L 119.7,146.0 L 122.0,146.0 L 124.3,146.0 L 126.7,146.0 L 129.0,146.0 L 131.3,146.0 L 133.7,146.0 L 136.0,146.0 L 138.3,146.0 L 140.7,146.0 L 143.0,146.0 L 145.3,146.0 L 147.7,146.0 L 150.0,146.0 L 152.3,146.0 L 154.7,146.0 L 157.0,146.0 L 159.3,146.0 L 161.7,146.0 L 164.0,146.0 L 166.3,146.0 L 168.7,146.0 L 171.0,146.0 L 173.3,146.0 L 175.7,146.0 L 178.0,146.0 L 180.3,146.0 L 182.7,146.0 L 185.0,146.0 L 187.3,146.0 L 189.7,146.0 L 192.0,146.0 L 194.3,146.0 L 196.7,146.0 L 199.0,146.0 L 201.3,146.0 L 203.7,146.0 L 206.0,146.0 L 208.3,146.0 L 210.7,146.0 L 213.0,146.0 L 215.3,146.0 L 217.7,146.0 L 220.0,146.0 L 222.3,146.0 L 224.7,146.0 L 227.0,146.0 L 229.3,146.0 L 231.7,146.0 L 234.0,146.0 L 236.3,146.0 L 238.7,146.0 L 241.0,146.0 L 243.3,146.0 L 245.7,146.0 L 248.0,146.0 L 250.3,146.0 L 252.7,146.0 L 255.0,146.0 L 257.3,146.0 L 259.7,146.0 L 262.0,146.0 L 264.3,146.0 L 266.7,146.0 L 269.0,146.0 L 271.3,146.0 L 273.7,146.0 L 276.0,146.0 L 278.3,146.0 L 280.7,146.0 L 283.0,146.0 L 285.3,146.0 L 287.7,146.0 L 290.0,146.0 L 292.3,146.0 L 294.7,146.0 L 297.0,146.0 L 299.3,146.0 L 301.7,146.0 L 304.0,146.0 L 306.3,146.0 L 308.7,146.0 L 311.0,146.0 L 313.3,146.0 L 315.7,146.0 L 318.0,146.0 L 320.3,146.0 L 322.7,146.0 L 325.0,146.0 L 327.3,146.0 L 329.7,146.0 L 332.0,145.9 L 334.3,145.7 L 336.7,145.1 L 339.0,143.7 L 341.3,140.6 L 343.7,134.6 L 346.0,124.2 L 348.3,108.2 L 350.7,86.7 L 353.0,61.8 L 355.3,37.9 L 357.7,20.4 L 360.0,14.0 L 362.3,20.4 L 364.7,37.9 L 367.0,61.8 L 369.3,86.7 L 371.7,108.2 L 374.0,124.2 L 376.3,134.6 L 378.7,140.6 L 381.0,143.7 L 383.3,145.1 L 385.7,145.7 L 388.0,145.9 L 390.3,146.0 L 392.7,146.0 L 395.0,146.0 L 397.3,146.0 L 399.7,146.0 L 402.0,146.0 L 404.3,146.0 L 406.7,146.0 L 409.0,146.0 L 411.3,146.0 L 413.7,146.0 L 416.0,146.0 L 418.3,146.0 L 420.7,146.0 L 423.0,146.0 L 425.3,146.0 L 427.7,146.0 L 430.0,146.0 L 432.3,146.0 L 434.7,146.0 L 437.0,146.0 L 439.3,146.0 L 441.7,146.0 L 444.0,146.0 L 446.3,146.0 L 448.7,146.0 L 451.0,146.0 L 453.3,146.0 L 455.7,146.0 L 458.0,146.0 L 460.3,146.0 L 462.7,146.0 L 465.0,146.0 L 467.3,146.0 L 469.7,146.0 L 472.0,146.0 L 474.3,146.0 L 476.7,146.0 L 479.0,146.0 L 481.3,146.0 L 483.7,146.0 L 486.0,146.0 L 488.3,146.0 L 490.7,146.0 L 493.0,146.0 L 495.3,146.0 L 497.7,146.0 L 500.0,146.0 L 502.3,146.0 L 504.7,146.0 L 507.0,146.0 L 509.3,146.0 L 511.7,146.0 L 514.0,146.0 L 516.3,146.0 L 518.7,146.0 L 521.0,146.0 L 523.3,146.0 L 525.7,146.0 L 528.0,146.0 L 530.3,146.0 L 532.7,146.0 L 535.0,146.0 L 537.3,146.0 L 539.7,146.0 L 542.0,146.0 L 544.3,146.0 L 546.7,146.0 L 549.0,146.0 L 551.3,146.0 L 553.7,146.0 L 556.0,146.0 L 558.3,146.0 L 560.7,146.0 L 563.0,146.0 L 565.3,146.0 L 567.7,146.0 L 570.0,146.0 L 572.3,146.0 L 574.7,146.0 L 577.0,146.0 L 579.3,146.0 L 581.7,146.0 L 584.0,146.0 L 586.3,146.0 L 588.7,146.0 L 591.0,146.0 L 593.3,146.0 L 595.7,146.0 L 598.0,146.0 L 600.3,146.0 L 602.7,146.0 L 605.0,146.0 L 607.3,146.0 L 609.7,146.0 L 612.0,146.0 L 614.3,146.0 L 616.7,146.0 L 619.0,146.0 L 621.3,146.0 L 623.7,146.0 L 626.0,146.0 L 628.3,146.0 L 630.7,146.0 L 633.0,146.0 L 635.3,146.0 L 637.7,146.0 L 640.0,146.0" fill="none" stroke="#FF00FF" stroke-width="2"/>
  <text x="360" y="160" style="font-size:11px;font-family:'JetBrains Mono',monospace;fill:#1A1A1A;text-anchor:middle;">μ</text>
  <rect x="488" y="22" width="142" height="64" fill="rgba(255,255,255,0.92)" stroke="#EEEEEE"/>
  <line x1="498" y1="36" x2="520" y2="36" stroke="#6B6B6B" stroke-width="2"/>
  <text x="526" y="40" style="font-size:11px;font-family:'JetBrains Mono',monospace;fill:#1A1A1A;">n = 10</text>
  <line x1="498" y1="52" x2="520" y2="52" stroke="#1A1A1A" stroke-width="2"/>
  <text x="526" y="56" style="font-size:11px;font-family:'JetBrains Mono',monospace;fill:#1A1A1A;">n = 100</text>
  <line x1="498" y1="68" x2="520" y2="68" stroke="#FF00FF" stroke-width="2"/>
  <text x="526" y="72" style="font-size:11px;font-family:'JetBrains Mono',monospace;fill:#1A1A1A;">n = 1000</text>
</svg>

<p style="font-size:0.95rem;color:#6B6B6B;margin-top:0.6rem;line-height:1.5;">
The same population at three sample sizes, where more data tightens the sampling distribution and narrows the confidence interval.
</p>

---

# How it works

By CLT, the distribution of $\bar X$ is approximately <span class="pink">Normal</span> at large $n$, centred at $\mu$ with standard deviation $\sigma/\sqrt{n}$.

<svg viewBox="0 0 720 200" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:560px;height:auto;display:block;margin:0.3rem auto 0;font-family:'Inter',system-ui,sans-serif;">
  <rect x="40" y="18" width="640" height="140" fill="#FAFAFA"/>
  <text x="360" y="12" style="font-size:11px;font-family:'Inter',system-ui,sans-serif;fill:#6B6B6B;text-anchor:middle;">distribution of X̄: 95% mass lies within ±1.96·SE of μ</text>
  <path d="M 222.8,158.0 L 222.8,137.5 L 226.3,135.4 L 229.8,133.2 L 233.3,130.8 L 236.8,128.2 L 240.3,125.6 L 243.8,122.7 L 247.3,119.7 L 250.8,116.5 L 254.3,113.2 L 257.8,109.8 L 261.3,106.2 L 264.8,102.5 L 268.3,98.6 L 271.8,94.7 L 275.3,90.7 L 278.8,86.6 L 282.3,82.4 L 285.8,78.2 L 289.3,73.9 L 292.8,69.7 L 296.3,65.5 L 299.8,61.3 L 303.3,57.2 L 306.8,53.1 L 310.3,49.2 L 313.8,45.4 L 317.3,41.8 L 320.8,38.3 L 324.3,35.1 L 327.8,32.1 L 331.3,29.3 L 334.8,26.8 L 338.3,24.6 L 341.8,22.7 L 345.3,21.1 L 348.8,19.8 L 352.3,18.8 L 355.8,18.3 L 359.3,18.0 L 362.8,18.1 L 366.3,18.6 L 369.8,19.4 L 373.3,20.5 L 376.8,22.0 L 380.3,23.8 L 383.8,25.9 L 387.3,28.3 L 390.8,30.9 L 394.3,33.8 L 397.8,37.0 L 401.3,40.4 L 404.8,43.9 L 408.3,47.7 L 411.8,51.5 L 415.3,55.5 L 418.8,59.6 L 422.3,63.8 L 425.8,68.0 L 429.3,72.2 L 432.8,76.5 L 436.3,80.7 L 439.8,84.9 L 443.3,89.0 L 446.8,93.1 L 450.3,97.1 L 453.8,101.0 L 457.3,104.7 L 460.8,108.4 L 464.3,111.9 L 467.8,115.2 L 471.3,118.4 L 474.8,121.5 L 478.3,124.4 L 481.8,127.2 L 485.3,129.8 L 488.8,132.2 L 492.3,134.5 L 495.8,136.7 L 497.2,158.0 Z" fill="rgba(255,0,255,0.18)" stroke="none"/>
  <path d="M 80.0,158.0 L 87.0,157.9 L 94.0,157.9 L 101.0,157.9 L 108.0,157.8 L 115.0,157.7 L 122.0,157.6 L 129.0,157.4 L 136.0,157.2 L 143.0,156.9 L 150.0,156.4 L 157.0,155.9 L 164.0,155.2 L 171.0,154.3 L 178.0,153.2 L 185.0,151.8 L 192.0,150.1 L 199.0,148.1 L 206.0,145.6 L 213.0,142.6 L 220.0,139.1 L 227.0,135.0 L 234.0,130.3 L 241.0,125.0 L 248.0,119.1 L 255.0,112.5 L 262.0,105.5 L 269.0,97.9 L 276.0,89.9 L 283.0,81.5 L 290.0,73.1 L 297.0,64.6 L 304.0,56.3 L 311.0,48.4 L 318.0,41.1 L 325.0,34.5 L 332.0,28.8 L 339.0,24.2 L 346.0,20.8 L 353.0,18.7 L 360.0,18.0 L 367.0,18.7 L 374.0,20.8 L 381.0,24.2 L 388.0,28.8 L 395.0,34.5 L 402.0,41.1 L 409.0,48.4 L 416.0,56.3 L 423.0,64.6 L 430.0,73.1 L 437.0,81.5 L 444.0,89.9 L 451.0,97.9 L 458.0,105.5 L 465.0,112.5 L 472.0,119.1 L 479.0,125.0 L 486.0,130.3 L 493.0,135.0 L 500.0,139.1 L 507.0,142.6 L 514.0,145.6 L 521.0,148.1 L 528.0,150.1 L 535.0,151.8 L 542.0,153.2 L 549.0,154.3 L 556.0,155.2 L 563.0,155.9 L 570.0,156.4 L 577.0,156.9 L 584.0,157.2 L 591.0,157.4 L 598.0,157.6 L 605.0,157.7 L 612.0,157.8 L 619.0,157.9 L 626.0,157.9 L 633.0,157.9 L 640.0,158.0" fill="none" stroke="#1A1A1A" stroke-width="1.8"/>
  <line x1="40" y1="158" x2="680" y2="158" stroke="#1A1A1A" stroke-width="1"/>
  <line x1="222.8" y1="158" x2="222.8" y2="137.5" stroke="#FF00FF" stroke-width="1.2" stroke-dasharray="3,3"/>
  <line x1="497.2" y1="158" x2="497.2" y2="137.5" stroke="#FF00FF" stroke-width="1.2" stroke-dasharray="3,3"/>
  <line x1="360" y1="158" x2="360" y2="18" stroke="#1A1A1A" stroke-width="1" stroke-dasharray="2,3"/>
  <text x="360" y="174" style="font-size:11px;font-family:'JetBrains Mono',monospace;fill:#1A1A1A;text-anchor:middle;">μ</text>
  <text x="222.8" y="174" style="font-size:11px;font-family:'JetBrains Mono',monospace;fill:#1A1A1A;text-anchor:middle;">μ − 1.96·SE</text>
  <text x="497.2" y="174" style="font-size:11px;font-family:'JetBrains Mono',monospace;fill:#1A1A1A;text-anchor:middle;">μ + 1.96·SE</text>
</svg>

Flip the statement: $\bar X$ is within $\pm 1.96 \cdot \mathrm{SE}(\bar X)$ of $\mu$ in 95% of samples, so the interval $[\bar X - 1.96 \cdot \mathrm{SE}(\bar X),\ \bar X + 1.96 \cdot \mathrm{SE}(\bar X)]$ covers $\mu$ in 95% of samples.

---

# How NOT to read a CI

The 95% describes how the **procedure** behaves across many samples. The parameter $\theta$ is an unknown <span class="pink">constant</span> and by definition cannot have a distribution, so a realised interval either contains it or does not, and there is no probability statement to make about that single interval.

<div style="display:grid;grid-template-columns:1fr 1fr;gap:1.4rem;margin-top:0.8rem;">

  <div style="padding:0.8rem 1.1rem;background:#FAFAFA;border-left:3px solid #FF00FF;">
    <div style="font-family:'JetBrains Mono',monospace;font-size:0.74rem;color:#FF00FF;text-transform:uppercase;letter-spacing:0.1em;">wrong</div>
    <div style="color:#1A1A1A;font-size:0.95rem;margin-top:0.3rem;line-height:1.5;">"There is a 95% probability that the parameter is inside this particular interval."</div>
  </div>

  <div style="padding:0.8rem 1.1rem;background:#FAFAFA;border-left:3px solid #1A1A1A;">
    <div style="font-family:'JetBrains Mono',monospace;font-size:0.74rem;color:#1A1A1A;text-transform:uppercase;letter-spacing:0.1em;">right</div>
    <div style="color:#1A1A1A;font-size:0.95rem;margin-top:0.3rem;line-height:1.5;">"If we ran this procedure many times, 95% of the intervals would contain the parameter."</div>
  </div>

</div>

<div style="margin-top:1rem;text-align:center;">
<a href="/harbour-product-analytics-2026/06-statistics-2/ci-sim.html" target="_blank" style="display:inline-block;padding:0.6rem 1.2rem;border:1.5px solid #1A1A1A;background:#FAFAFA;color:#1A1A1A;font-family:'JetBrains Mono',monospace;font-size:0.95rem;text-decoration:none;">↗ Open simulation</a>
</div>

<!--
Sim runs the procedure 100s of times against a known μ, draws each interval, colours misses in pink, and shows the running coverage rate. The point students should leave with: the 95% is a frequency over the procedure across many samples. For any single realised interval, the parameter is either in or out — that's a 0 or 1, not a 95%.
-->


---

# Two intervals don't decide

Each variant gives an estimate $\widehat{\text{ARPU}}$ with its CI, and we never see the true value.

<svg viewBox="0 0 720 130" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:600px;height:auto;display:block;margin:0.4rem auto 0;font-family:'Inter',system-ui,sans-serif;">
<rect x="259" y="20" width="179" height="70" fill="#FF00FF" fill-opacity="0.08"/>
<line x1="80" y1="100" x2="640" y2="100" stroke="#1A1A1A" stroke-width="1"/>
<line x1="80" y1="95" x2="80" y2="105" stroke="#1A1A1A" stroke-width="1"/>
<line x1="192" y1="95" x2="192" y2="105" stroke="#1A1A1A" stroke-width="1"/>
<line x1="304" y1="95" x2="304" y2="105" stroke="#1A1A1A" stroke-width="1"/>
<line x1="416" y1="95" x2="416" y2="105" stroke="#1A1A1A" stroke-width="1"/>
<line x1="528" y1="95" x2="528" y2="105" stroke="#1A1A1A" stroke-width="1"/>
<line x1="640" y1="95" x2="640" y2="105" stroke="#1A1A1A" stroke-width="1"/>
<text x="80" y="118" style="font-size:11px;fill:#6B6B6B;text-anchor:middle;">$3.50</text>
<text x="192" y="118" style="font-size:11px;fill:#6B6B6B;text-anchor:middle;">$4.00</text>
<text x="304" y="118" style="font-size:11px;fill:#6B6B6B;text-anchor:middle;">$4.50</text>
<text x="416" y="118" style="font-size:11px;fill:#6B6B6B;text-anchor:middle;">$5.00</text>
<text x="528" y="118" style="font-size:11px;fill:#6B6B6B;text-anchor:middle;">$5.50</text>
<text x="640" y="118" style="font-size:11px;fill:#6B6B6B;text-anchor:middle;">$6.00</text>
<line x1="259" y1="40" x2="573" y2="40" stroke="#1A1A1A" stroke-width="2"/>
<line x1="259" y1="33" x2="259" y2="47" stroke="#1A1A1A" stroke-width="2"/>
<line x1="573" y1="33" x2="573" y2="47" stroke="#1A1A1A" stroke-width="2"/>
<circle cx="416" cy="40" r="5" fill="#1A1A1A"/>
<text x="68" y="44" style="font-size:11px;fill:#1A1A1A;text-anchor:end;font-weight:700;">A: $5.00</text>
<line x1="170" y1="75" x2="438" y2="75" stroke="#1A1A1A" stroke-width="2"/>
<line x1="170" y1="68" x2="170" y2="82" stroke="#1A1A1A" stroke-width="2"/>
<line x1="438" y1="68" x2="438" y2="82" stroke="#1A1A1A" stroke-width="2"/>
<circle cx="304" cy="75" r="5" fill="#1A1A1A"/>
<text x="68" y="79" style="font-size:11px;fill:#1A1A1A;text-anchor:end;font-weight:700;">B: $4.50</text>
<text x="348" y="14" style="font-size:11px;fill:#FF00FF;text-anchor:middle;font-weight:700;font-style:italic;">overlap</text>
</svg>

A looks higher, but the intervals <span class="pink">overlap</span>. The data alone does not say which variant is better, so deciding needs a formal rule, and that framework is **hypothesis testing**.

<div v-click style="margin-top:2rem;text-align:center;color:#E5142B;font-family:'Bricolage Grotesque','Inter',sans-serif;font-weight:800;font-size:1.8rem;line-height:1.2;letter-spacing:-0.01em;">Errors are unavoidable. The best we can do is control their rate.</div>

<!--
Bridge slide from CI to HT. The point: a confidence interval quantifies uncertainty for ONE estimate. It does not formalize the comparison of TWO estimates. When CIs overlap, eyeballing is not a decision rule — we need a procedure with a stated error rate. That procedure is HT. The closing line sets up the HT block — same idea will come back as α (Type I) and β (Type II): we cannot eliminate errors, we choose how often we are willing to make each kind.
-->

---
layout: section
class: tint-rose
---

## 05

# Hypothesis testing

---

# What is a hypothesis

| In plain words | As a statement about a parameter |
|---|---|
| *"The median apartment price in Barcelona is above €250k."* | $\text{price} \sim F$, with $\text{median}(F) \gt 250{,}000$ |
| *"Removing the username field speeds up sign-up."* | $\text{sign-up time} \sim F$, with $\mathbb{E}[\text{time}_\text{new}] \lt \mathbb{E}[\text{time}_\text{old}]$ |
| *"The new recommendation algorithm increases time spent."* | $\text{time spent} \sim G$, with $\mathbb{E}[\text{time}_\text{new}] \gt \mathbb{E}[\text{time}_\text{old}]$ |

A hypothesis is a claim about a <span class="pink">parameter</span> of the metric's distribution.<sup style="color:#6B6B6B;font-size:0.7em;">*</sup>

<!--
* The asterisk is a verbal hook. Hypotheses come in more flavors than parameter claims — goodness-of-fit (does this sample come from F?), independence (are X and Y independent?), non-parametric (no parametric family at all). We focus on parametric hypotheses about a single parameter today because that is the workhorse case in A/B testing. Say this out loud at the asterisk and move on.

The two halves of each row say the same thing in two languages. Left: how a product person phrases it. Right: how a statistician phrases it. The right column does the work of formalisation. Notice we are not yet writing H₀ and H₁ — that comes next. For now: identify the metric, name its parameter, name the direction of the expected change. The distribution itself (F, G) does not need to be known. That is the move from product hypothesis to statistical hypothesis.
-->



---

# Lady Tasting Tea

In Cambridge in the 1920s, Muriel Bristol claimed she could tell whether milk was poured into the cup before the tea or after, and **Ronald Fisher** designed the test in *The Design of Experiments* (1935). It is an early famous example of modern hypothesis testing.

<p style="font-size:0.85rem;color:#6B6B6B;margin-top:1rem;">Background: <a href="https://en.wikipedia.org/wiki/Lady_tasting_tea" style="color:#6B6B6B;text-decoration:underline;">Wikipedia · Lady tasting tea</a></p>

<div style="margin-top:0.8rem;padding:0.7rem 1rem;background:#FAFAFA;border-left:3px solid #FF00FF;font-size:0.98rem;color:#1A1A1A;line-height:1.55;">
Prepare 8 cups, four with milk poured first and four with tea poured first, in a random order hidden from her, then she tastes all eight and sorts them into two groups of four.
</div>

If she gets them all right, either she really can tell or she got lucky, and we need a way to tell the two apart.

---

# Lady Tasting Tea under $H_0$

The true distribution of the count of correct cups $X$ is unknown. **$H_0$ pins it down**: she is guessing at random. Under that assumption the distribution of $X$ is fully specified:

$$X_{H_0} \sim \text{Hypergeometric}(8, 4, 4), \qquad \mathbb{P}_{H_0}(X = k) = \frac{\binom{4}{k}\binom{4}{4-k}}{\binom{8}{4}}$$

<div style="display:grid;grid-template-columns:1.05fr 1fr;gap:1rem;margin-top:0.4rem;align-items:center;">
<div>

If she gets all 4 right, that has probability $\approx 1/70$ under $H_0$. Either she got very lucky, or $H_0$ is wrong, and $1/70$ is small enough that we doubt $H_0$.

</div>
<div>
<svg viewBox="0 0 480 180" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;display:block;font-family:'Inter',system-ui,sans-serif;">
<defs>
<marker id="lt-arr" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto" markerUnits="strokeWidth">
<polygon points="0 0, 8 4.5, 0 9" fill="#FF00FF"/>
</marker>
</defs>
<line x1="50" y1="160" x2="460" y2="160" stroke="#1A1A1A" stroke-width="1.2"/>
<line x1="50" y1="40" x2="50" y2="160" stroke="#1A1A1A" stroke-width="1.2"/>
<rect x="80" y="153" width="50" height="7" fill="#1A1A1A"/>
<rect x="160" y="126" width="50" height="34" fill="#1A1A1A"/>
<rect x="240" y="85" width="50" height="75" fill="#1A1A1A"/>
<rect x="320" y="126" width="50" height="34" fill="#1A1A1A"/>
<rect x="400" y="153" width="50" height="7" fill="#FF00FF"/>
<text x="105" y="148" style="font-size:10.5px;fill:#6B6B6B;text-anchor:middle;">0.014</text>
<text x="185" y="120" style="font-size:10.5px;fill:#6B6B6B;text-anchor:middle;">0.229</text>
<text x="265" y="78" style="font-size:11px;fill:#1A1A1A;text-anchor:middle;font-weight:700;">0.514</text>
<text x="345" y="120" style="font-size:10.5px;fill:#6B6B6B;text-anchor:middle;">0.229</text>
<text x="425" y="148" style="font-size:11px;fill:#FF00FF;text-anchor:middle;font-weight:700;">0.014</text>
<text x="105" y="178" style="font-size:11px;fill:#1A1A1A;text-anchor:middle;">0</text>
<text x="185" y="178" style="font-size:11px;fill:#1A1A1A;text-anchor:middle;">1</text>
<text x="265" y="178" style="font-size:11px;fill:#1A1A1A;text-anchor:middle;">2</text>
<text x="345" y="178" style="font-size:11px;fill:#1A1A1A;text-anchor:middle;">3</text>
<text x="425" y="178" style="font-size:11px;fill:#FF00FF;text-anchor:middle;font-weight:700;">4</text>
<text x="255" y="196" style="font-size:11px;fill:#6B6B6B;text-anchor:middle;font-style:italic;">k = correct cups</text>
<text x="50" y="32" style="font-size:11px;fill:#6B6B6B;text-anchor:middle;">P(X = k)</text>
<line x1="425" y1="48" x2="425" y2="148" stroke="#FF00FF" stroke-width="1.4" stroke-dasharray="3 3" marker-end="url(#lt-arr)"/>
<text x="425" y="40" style="font-size:11px;fill:#FF00FF;text-anchor:middle;font-weight:700;">observed</text>
</svg>
</div>
</div>

<!--
The meta-point of this slide is not the tea. It is HT in miniature: under H₀ the test statistic has a known distribution. The shape (hypergeometric) comes from the structure of the experiment — combinatorics, the math. The specific distribution (this one, with these probabilities) is fixed by H₀ — by the assumption "she's guessing". Without that assumption we have a family of distributions, not one. H₀ does the work of picking one. Same pattern every time we test: H₀ → known null distribution → tail probability → decision.
-->


---

# The null hypothesis

A **null hypothesis** ($H_0$) is a statement that assumes **no effect, no difference, no relationship**. It is the baseline default position we test against the research claim, the alternative hypothesis $H_1$.

| Setting | $H_0$ |
|---|---|
| Lady Tasting Tea | She is guessing at random, equivalent to $X \sim \text{Hypergeometric}(8, 4, 4)$ |
| Barcelona apartment prices | $\text{median}(F) = 250{,}000$ |
| A/B test on revenue | $\mathbb{E}[\text{revenue}_A] = \mathbb{E}[\text{revenue}_B]$ |

<!--
The null is always the "boring" version of the world: no effect, no difference, no link. We frame it that way because we never get to prove anything in NHST — we only collect evidence against the null and either reject it or fail to. The point of having a clear, parameter-level statement of H₀ is that it pins down a specific distribution for the test statistic, the way "she is guessing" pinned down the hypergeometric on the previous slide.
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

Prove $H_0$, and not pin down a specific value of $H_1$, because $H_1$ is **composite** — many possible effect sizes are consistent with it.<sup style="color:#6B6B6B;">*</sup>

</div>

</div>

We never *prove* the null. Absence of evidence against $H_0$ is not evidence for it.

<div style="margin-top:1rem;font-size:0.78rem;color:#6B6B6B;line-height:1.5;border-top:1px solid #EEEEEE;padding-top:0.5rem;">
<span style="color:#FF00FF;font-weight:700;">*</span> NHST does not tell you the true value of the parameter. You can reject H<sub>0</sub> or fail to reject it, and either way the true value stays unknown. To estimate it, we still use the point and interval estimates from earlier.
</div>


---

# Type I and Type II errors

Two ways the test can be wrong, two ways it can be right.

<div style="display:grid;grid-template-columns:220px 240px 240px;gap:0.6rem;margin:0.8rem auto 0;width:fit-content;justify-content:center;font-family:'Inter',system-ui,sans-serif;">

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

<div v-click style="margin-top:1.4rem;text-align:center;color:#E5142B;font-family:'Bricolage Grotesque','Inter',sans-serif;font-weight:800;font-size:1.5rem;line-height:1.25;letter-spacing:-0.01em;">Errors are unavoidable, so we build a procedure that <span style="color:#E5142B;">controls their rates</span>. Significance testing is that procedure.</div>

<!--
The matrix is the standard 2x2 truth table for a binary decision under a binary state of the world. Read row by row: if we reject H₀, we are either making a Type I error (H₀ was actually true) or a correct call (H₁ was true). If we fail to reject, we are either correct (H₀ true) or making a Type II error (H₁ true). The framing question is not "can we avoid errors" — we can't — it is "which error rates do we commit to controlling". NHST commits to capping α, and then we design the experiment (sample size, effect size assumptions) so β stays low. This is exactly the trade-off we will operationalise in the A/B testing sessions.
-->

---

# Choosing $\alpha$

Under $H_0$ there is no effect. A Type I error is when the procedure rejects $H_0$ anyway, purely by chance. We pick the rate $\alpha$ at which we agree to let this happen, **before** running the test.

<div style="display:grid;grid-template-columns:120px 1fr;gap:0.5rem 1.4rem;margin:1rem auto 0;max-width:680px;font-family:'Inter',system-ui,sans-serif;align-items:baseline;">

<div style="font-family:'JetBrains Mono',monospace;font-size:1.1rem;font-weight:700;color:#FF00FF;text-align:right;">α = 5%</div>
<div style="color:#1A1A1A;font-size:0.95rem;">baseline default in most product and academic settings</div>

<div style="font-family:'JetBrains Mono',monospace;font-size:1.1rem;font-weight:700;color:#FF00FF;text-align:right;">α = 1%</div>
<div style="color:#1A1A1A;font-size:0.95rem;">large companies with high cost of false positives</div>

<div style="font-family:'JetBrains Mono',monospace;font-size:1.1rem;font-weight:700;color:#FF00FF;text-align:right;">α = 0.1%</div>
<div style="color:#1A1A1A;font-size:0.95rem;">very large datasets, many parallel tests, stricter screening</div>

</div>

$\alpha$ is the rate of false positives the procedure is allowed to make when $H_0$ is true. The decision rule is built around it.

<!--
α is a commitment, not a number you look up after the fact. Set it before the test. Common defaults: 5% in most A/B work, 1% in high-stakes decisions or where the cost of acting on a false positive is large, 0.1% when running thousands of tests in parallel (search ranking, ML model rollouts). The point is to make the false-positive rate a parameter of the procedure, so we can engineer the rest of the test around it.
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
Two equivalent formulations of the same decision. Rejection region: decide on the values of T that count as "too extreme to be H₀" before looking at the data, total probability mass α under H₀. p-value: after observing t_obs, ask how often H₀ would produce something at least this extreme. The two link up: t_obs ∈ C_α exactly when p < α. Mention that this is what every classical test (z, t, χ², F, hypergeometric) does — the machinery differs only in which distribution under H₀ supplies the tail probability.
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
<a href="/harbour-product-analytics-2026/06-statistics-2/type1-sim.html" target="_blank" rel="noopener" style="display:inline-block;padding:0.8rem 1.4rem;background:#1A1A1A;color:#fff;font-family:'JetBrains Mono',monospace;font-size:0.95rem;font-weight:700;letter-spacing:0.08em;text-transform:uppercase;text-decoration:none;border:2px solid #1A1A1A;">Open simulation ↗</a>
</div>

<!--
The point of this slide is not the chart, it is what the chart does. Run α = 5%, two-sided, draw 5000: roughly 5% of samples land in the rejection region. Switch to α = 1%: it drops to 1%. The empirical rate is α by construction. Then flip the alternative: greater puts all of α on the right, less on the left, two-sided splits it. Same data, same H₀, different rejection region. The rejection region is our design choice, not a property of the data.
-->

---

# The hypothesis testing pipeline

| | |
|---|---|
| <span class="pink">**01**</span> | State $H_0: \mu = \mu_0$ and collect $X_1, \dots, X_n$ |
| <span class="pink">**02**</span> | Derive the null distribution. CLT gives $Z = \sqrt{n}\,(\bar X - \mu_0)/\sigma \approx \mathcal{N}(0, 1)$ under $H_0$<sup style="color:#6B6B6B;font-size:0.7em;">*</sup> |
| <span class="pink">**03**</span> | Fix $\alpha$ **before** running the test ($5\%$, $1\%$, $0.1\%$) |
| <span class="pink">**04**</span> | Compute the p-value: $p = \mathbb{P}_{H_0}(\lvert Z \rvert \ge \lvert z_\text{obs} \rvert)$ |
| <span class="pink">**05**</span> | If $p \lt \alpha$, reject $H_0$. Otherwise fail to reject. |

<span style="font-size:0.78rem;color:#6B6B6B;">* CLT covers means only.</span>

<!--
Five steps, in order. Step 1: state H₀ and pull the sample (for today, one-sample mean, μ₀ is whatever the null claims — for Lady Tasting Tea it was "she's guessing", for Barcelona prices μ₀ = 250k, for an A/B mean comparison μ_treat = μ_ctrl). Step 2 is the engineering challenge — under H₀ we need to know the distribution of our statistic. For sample means we get this for free from CLT, but the moment we leave means (median, quantile, ratio of two metrics) we have to roll our own. Step 3 is a commitment, not a calculation. Step 4 is mechanical once we have step 2. Step 5 is the decision. Important caveat to say verbally: rejecting H₀ does not tell us by how much the truth differs from μ₀. The procedure controls the false-positive rate, nothing more. To estimate the actual parameter we go back to point and interval estimates.
-->

---

# When assumptions break

A test attains its **nominal** Type I rate $\alpha$ **if and only if its assumptions hold**. Misspecify any of them and the **actual** Type I rate drifts away from $\alpha$. In industry language: nominal $\alpha$ is what the test promises, actual $\alpha$ is what you really get.

**Example: $t(3)$ instead of $\mathcal{N}(0, 1)$**. Heavy tails with finite variance $3$, but the test still divides by $\sigma = 1$. So $Z$ has variance $3$ under $H_0$, with tails about three times wider than $\mathcal{N}(0, 1)$, and the actual Type I rate climbs above the nominal $\alpha$.

<div style="display:flex;justify-content:center;margin-top:1.2rem;">
<a href="/harbour-product-analytics-2026/06-statistics-2/assumptions-sim.html" target="_blank" rel="noopener" style="display:inline-block;padding:0.8rem 1.4rem;background:#1A1A1A;color:#fff;font-family:'JetBrains Mono',monospace;font-size:0.95rem;font-weight:700;letter-spacing:0.08em;text-transform:uppercase;text-decoration:none;border:2px solid #1A1A1A;">Open simulation ↗</a>
</div>

<!--
Run α = 5%, ρ = 0: empirical rate sits at 5%. Bump ρ to 0.5: rate climbs to 10–15%. ρ = 0.9: rate explodes, often past 30%. Same H₀, same α, same Z formula. The data simply violated the iid assumption, and the procedure stopped honouring α. This is the most common quiet failure mode in practice: ratio metrics where the denominator carries dependence, time series where adjacent days correlate, A/B tests where users have multiple sessions. The fix is not to bin the alpha lower — it is to use the right null distribution (delta method, bootstrap, cluster-robust SE).
-->

---

# The p-value under $H_0$ is uniform

Under $H_0$ the p-value follows $\text{Uniform}[0, 1]$. That is why "reject if $p \lt \alpha$" controls the Type I rate at exactly $\alpha$: a fraction $\alpha$ of p-values fall below $\alpha$ by construction.

**Why**. For a continuous test statistic $T$ with null CDF $F$, the random variable $p = 1 - F(T)$ has $\mathbb{P}_{H_0}(p \le u) = u$ for $u \in [0, 1]$.

**Link to $Z$**. Each decile of $p$ maps to a symmetric pair of tail slices in $Z$. Same colours on both plots, same total mass per decile.

<div style="display:flex;justify-content:center;margin-top:1.2rem;">
<a href="/harbour-product-analytics-2026/06-statistics-2/pvalue-sim.html" target="_blank" rel="noopener" style="display:inline-block;padding:0.8rem 1.4rem;background:#1A1A1A;color:#fff;font-family:'JetBrains Mono',monospace;font-size:0.95rem;font-weight:700;letter-spacing:0.08em;text-transform:uppercase;text-decoration:none;border:2px solid #1A1A1A;">Open simulation ↗</a>
</div>

<!--
The trick: if T has a continuous distribution under H₀ with CDF F, then the random variable p = 1 - F(T) (or 2(1-F(|T|)) for two-sided) is uniform on [0, 1] under H₀. So the procedure "reject when p < α" rejects exactly α of the time when H₀ is true. The decile colouring is meant to make this visceral: the same colour band has the same area on both the Z and p histograms. Z deciles 5/6 (around the centre of the bell) are blue (large p), Z deciles 1/10 (in the tails) are red (small p). Note: the Z histogram is bell-shaped but the p histogram is flat — that's not a contradiction, it's the change of variables.
-->


---

# What if we have two samples?

Recipe unchanged. Reduce both samples to a single statistic whose null distribution we know. Difference of two independent Normals is Normal, so under $H_0: \mu_A = \mu_B$:

$$Z = \frac{\bar X_A - \bar X_B}{\mathrm{SE}} \approx \mathcal{N}(0, 1), \qquad \mathrm{SE} = \sqrt{\tfrac{\sigma_A^2}{n_A} + \tfrac{\sigma_B^2}{n_B}}$$

Same five steps, same $\alpha$, same p-value. Only the statistic and its standard error change.

---

# Two-sample pipeline

| | step | example |
|---|---|---|
| <span class="pink">**01**</span> | State $H_0: \mu_A = \mu_B$, collect $A$, $B$ | $\bar X_A = 1.05$, $\bar X_B = 1.00$, $n = 1000$, $\sigma = 0.5$ |
| <span class="pink">**02**</span> | $Z = (\bar X_A - \bar X_B)/\mathrm{SE} \approx \mathcal{N}(0,1)$ | $\mathrm{SE} = \sqrt{2 \cdot 0.25/1000} \approx 0.0224$ |
| <span class="pink">**03**</span> | Fix $\alpha$ before computing | $\alpha = 0.05$ |
| <span class="pink">**04**</span> | $p = \mathbb{P}_{H_0}(\lvert Z \rvert \ge \lvert z_\text{obs} \rvert)$ | $z_\text{obs} \approx 2.24$, $p \approx 0.025$ |
| <span class="pink">**05**</span> | Reject $H_0$ if $p \lt \alpha$ | $0.025 \lt 0.05 \Rightarrow$ **reject** |
