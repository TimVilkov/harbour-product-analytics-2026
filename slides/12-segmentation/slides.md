---
theme: apple-basic
title: "Session 12: User Segmentation"
info: "Product Analytics · Harbour.Space · 2026"
highlighter: shiki
drawings:
  persist: false
transition: fade
mdc: true
layout: intro
---

# User <span class="pink">Segmentation</span>

<div class="absolute bottom-10 left-14" style="font-family:'JetBrains Mono',monospace;font-size:0.75rem;text-transform:uppercase;letter-spacing:0.15em;color:rgba(255,255,255,0.55);">
  Harbour.Space &middot; Barcelona &middot; June 02, 2026
</div>

---

# Today

<div style="display:flex;flex-direction:column;gap:0.9rem;margin-top:1rem;">
  <div style="display:grid;grid-template-columns:60px 1fr;gap:1.5rem;align-items:baseline;">
    <span style="font-family:'JetBrains Mono',monospace;font-size:0.9rem;color:#FF00FF;letter-spacing:0.1em;">01</span>
    <div style="font-size:1.4rem;font-weight:700;color:#1A1A1A;">Why we segment</div>
  </div>
  <div style="display:grid;grid-template-columns:60px 1fr;gap:1.5rem;align-items:baseline;">
    <span style="font-family:'JetBrains Mono',monospace;font-size:0.9rem;color:#FF00FF;letter-spacing:0.1em;">02</span>
    <div style="font-size:1.4rem;font-weight:700;color:#1A1A1A;">Segmenting from a user need</div>
  </div>
  <div style="display:grid;grid-template-columns:60px 1fr;gap:1.5rem;align-items:baseline;">
    <span style="font-family:'JetBrains Mono',monospace;font-size:0.9rem;color:#FF00FF;letter-spacing:0.1em;">03</span>
    <div style="font-size:1.4rem;font-weight:700;color:#1A1A1A;">Segmenting from a business rule</div>
  </div>
  <div style="display:grid;grid-template-columns:60px 1fr;gap:1.5rem;align-items:baseline;">
    <span style="font-family:'JetBrains Mono',monospace;font-size:0.9rem;color:#FF00FF;letter-spacing:0.1em;">04</span>
    <div style="font-size:1.4rem;font-weight:700;color:#1A1A1A;">Segmenting from the data</div>
  </div>
  <div style="display:grid;grid-template-columns:60px 1fr;gap:1.5rem;align-items:baseline;">
    <span style="font-family:'JetBrains Mono',monospace;font-size:0.9rem;color:#FF00FF;letter-spacing:0.1em;">05</span>
    <div style="font-size:1.4rem;font-weight:700;color:#1A1A1A;">A universal method</div>
  </div>
  <div style="display:grid;grid-template-columns:60px 1fr;gap:1.5rem;align-items:baseline;">
    <span style="font-family:'JetBrains Mono',monospace;font-size:0.9rem;color:#FF00FF;letter-spacing:0.1em;">06</span>
    <div style="font-size:1.4rem;font-weight:700;color:#1A1A1A;">Bringing it together</div>
  </div>
  <div style="display:grid;grid-template-columns:60px 1fr;gap:1.5rem;align-items:baseline;">
    <span style="font-family:'JetBrains Mono',monospace;font-size:0.9rem;color:#FF00FF;letter-spacing:0.1em;">07</span>
    <div style="font-size:1.4rem;font-weight:700;color:#1A1A1A;">What's expected of an analyst</div>
  </div>
</div>

<!--
This is the provisional spine: the opener plus the three cases Tim dictated. RFM, behavioral, and the clustering methodology block will slot in once locked.
-->

---
layout: section
class: tint-lavender
---

## 01

# Why we segment

---
layout: statement
---

# Analytics is not only about <span class="pink">delivery</span>

<!--
The usual picture of analytics is delivery: we shipped something, here is the evidence it worked or it did not. That is half the job. The other half is discovery.
-->

---

# Two loops

<div style="font-size:1.4rem;color:#1A1A1A;font-weight:600;margin-bottom:0.6rem;line-height:1.4;">
Product analytics is fuel for both loops of product development
</div>

<div style="display:flex;justify-content:center;margin-top:0.2rem;">

![Double Diamond](./images/double-diamond.svg){width=470px}

</div>

<!--
Teaser for tomorrow. The double diamond holds a discipline: do not move to a solution before the hypothesis has been explored and opened up. In discovery, analytics shapes the quality of hypotheses, gives a rough estimate of how much a hypothesis can move, and shows which problems users actually have.
-->

---

# Discovery changes the decision

<div style="font-size:1.3rem;color:#1A1A1A;font-weight:600;margin-bottom:1.3rem;line-height:1.45;">
Before anything is built, the data can tell us an initiative is not worth it
</div>

<div v-click>
<ul style="font-size:1.15rem;line-height:1.95;color:#1A1A1A;margin:0;">
<li>the problem touches only a small slice, maybe 0.5% of users</li>
<li>the initiative will likely return less than it costs to build</li>
<li>the real problem turns out deeper and different, and more expensive to solve</li>
</ul>
</div>

<!--
These are the findings that send an idea back to the shelf instead of into delivery. Sizing the reachable population, weighing the return against the cost, and finding the true shape of the problem are all the analyst's job before the team commits.
-->

---

# We optimize for the whole population

<div style="font-size:1.35rem;color:#1A1A1A;font-weight:600;margin-bottom:1.4rem;line-height:1.45;">
We ship a change and read its average treatment effect across all users
</div>

<div style="font-size:1.15rem;color:#1A1A1A;line-height:1.6;margin-bottom:1.6rem;">
Improving the product and making users happier on average is a good thing
</div>

<div style="display:flex;justify-content:center;gap:2.5rem;font-size:2rem;line-height:1.5;">
<div style="max-width:340px;">🙂 🙂 🙂 🙂 🙂 🙂 🙂 🙂 🙂 🙂</div>
<div style="max-width:340px;">😡 😡 😡 😡 😡 😡 😡 😡 😡 😡</div>
</div>

<!--
Picture the whole population reacting to one change: ten happier, ten angrier. The average barely moves, so on paper the change did nothing. But it clearly helped one group and hurt another.
-->

---

# Different users, different pains

<div style="font-size:1.3rem;color:#1A1A1A;font-weight:600;margin-bottom:1.4rem;line-height:1.45;">
In practice, different users carry different pains and different problems
</div>

<div style="font-size:1.15rem;color:#1A1A1A;line-height:1.6;margin-bottom:1.6rem;">
Focusing on specific segments, and solving the concrete jobs of specific user types, is a <span class="pink">more effective</span> strategy
</div>

<div style="display:flex;justify-content:center;font-size:2rem;line-height:1.5;">
<div style="max-width:340px;">🙂 🙂 🙂 🙂 🙂 🙂 🙂 🙂 🙂 🙂</div>
</div>

<!--
Now keep only the group the change helped. If we can target just them, we ship a clear win instead of a flat average. The angry segment is left out of this rollout.
-->

---

# So we split the population

<div style="font-size:1.3rem;color:#1A1A1A;font-weight:600;margin-bottom:1.3rem;line-height:1.45;">
We break the population into sets, overlapping or not, for sharper discovery and delivery
</div>

<div style="font-size:1.1rem;color:#1A1A1A;line-height:1.7;">
When users share a goal, a problem, or a characteristic, we focus on them instead of the whole population:
</div>

<ul style="margin-top:0.8rem;font-size:1.1rem;line-height:1.8;color:#1A1A1A;">
<li>metrics get more sensitive</li>
<li>effects get brighter</li>
<li>problems get more visible</li>
</ul>

<div style="margin-top:1rem;font-size:1.15rem;color:#1A1A1A;font-weight:600;">
This is where the need for <span class="pink">segmentation</span> comes from
</div>

<!--
The whole-population average hides the groups inside it. Once we want a real effect on users, splitting becomes necessary.
-->

---

# What segmentation is

<div style="font-size:1.3rem;color:#1A1A1A;font-weight:600;margin-bottom:1.4rem;line-height:1.45;">
Segmentation is splitting users into groups we can treat differently
</div>

<div style="font-size:1.05rem;color:#1A1A1A;line-height:1.6;margin-bottom:0.9rem;">
It can run on:
</div>

<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:1.6rem;margin-bottom:1.4rem;">
<div>
<div style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#FF00FF;text-transform:uppercase;letter-spacing:0.14em;margin-bottom:0.4rem;">Behavior</div>
<div style="font-size:1.05rem;color:#1A1A1A;line-height:1.45;">what they do, static or changing over time</div>
</div>
<div>
<div style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#FF00FF;text-transform:uppercase;letter-spacing:0.14em;margin-bottom:0.4rem;">External attributes</div>
<div style="font-size:1.05rem;color:#1A1A1A;line-height:1.45;">traits we know from outside the product</div>
</div>
<div>
<div style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#FF00FF;text-transform:uppercase;letter-spacing:0.14em;margin-bottom:0.4rem;">Problems or use-cases</div>
<div style="font-size:1.05rem;color:#1A1A1A;line-height:1.45;">the job they came to do</div>
</div>
</div>

<div style="padding:1rem 1.2rem;background:#FAFAFA;border-left:3px solid #FF00FF;">
<div style="font-size:1.15rem;font-weight:700;color:#1A1A1A;line-height:1.5;">
How you define "similar" is a business choice, and different choices give different results
</div>
<div style="font-size:1rem;color:#1A1A1A;line-height:1.5;margin-top:0.4rem;">
What does "close" mean, why do you want it, and how will it change your decisions?
</div>
</div>

<!--
This is the key idea. Similarity can be defined in endless ways, and each input gives a different grouping. So the choice is not technical, it is a business one: decide what close means, why you want it, and how it will move your decisions. The rest of today walks these from a user need to the data.
-->

---

# Classification and clustering

<div style="display:grid;grid-template-columns:1fr 1fr;gap:2rem;margin-top:0.4rem;">
<div>
<div style="font-family:'JetBrains Mono',monospace;font-size:0.72rem;color:#AAAAAA;text-transform:uppercase;letter-spacing:0.14em;margin-bottom:0.5rem;">Classification</div>
<div style="font-size:1.1rem;color:#1A1A1A;line-height:1.55;">The business knows what it wants and the segments are known. The job is to learn to assign each user to them.</div>
<div style="font-size:1rem;color:#6B6B6B;line-height:1.45;margin-top:0.5rem;">Like an email spam filter: the labels already exist, you just sort new items into them</div>
</div>
<div>
<div style="font-family:'JetBrains Mono',monospace;font-size:0.72rem;color:#AAAAAA;text-transform:uppercase;letter-spacing:0.14em;margin-bottom:0.5rem;">Clustering</div>
<div style="font-size:1.1rem;color:#1A1A1A;line-height:1.55;">A discovery goal: the problem and the classes are not defined yet. We use the data to establish the groups.</div>
<div style="font-size:1rem;color:#6B6B6B;line-height:1.45;margin-top:0.5rem;">You do not know the segments in advance, the data proposes them</div>
</div>
</div>

<div style="margin-top:1.3rem;padding:0.8rem 1rem;background:#FAFAFA;border-left:3px solid #1A1A1A;font-size:1.05rem;color:#1A1A1A;line-height:1.5;">
When one user can belong to several segments at once, that is <b>multi-label</b>
</div>

<!--
Loose definitions, not rigorous ones. Classification is the supervised case: you already know the segments and learn to place users in them, exactly like a spam filter. Clustering is the unsupervised, discovery case: you do not know the groups and let the data suggest them. Multi-label is just classification where a user can carry several segment tags at once, which is fine.
-->

---
layout: section
class: tint-rose
---

## 02

# Segmenting from a user need

---

# Manychat

<div style="font-size:1.3rem;color:#1A1A1A;font-weight:600;margin-bottom:1.2rem;line-height:1.45;">
The product automates conversations with subscribers on social media
</div>

<div style="font-size:1.1rem;color:#1A1A1A;line-height:1.6;margin-bottom:1rem;">
From interviews we knew the users came for very different jobs:
</div>

<ul style="font-size:1.15rem;line-height:1.9;color:#1A1A1A;margin-top:0.2rem;">
<li>infopreneurs</li>
<li>affiliates</li>
<li>e-commerce brands</li>
<li>offline businesses</li>
<li>restaurants</li>
</ul>

<!--
Infopreneurs sell courses, consulting, or content. Affiliates post product links and earn a commission when someone buys. Then e-commerce brands, offline businesses, and restaurants. We had a qualitative picture of the types, but no way to count them or assign any single account to one.
-->

---

# The same product, very different users

<div style="display:grid;grid-template-columns:1fr 1fr;gap:2.4rem;margin-top:0.4rem;align-items:start;justify-items:center;">
<div style="text-align:center;">
<div style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#FF00FF;text-transform:uppercase;letter-spacing:0.14em;margin-bottom:0.5rem;">Infopreneur</div>

![Infopreneur account](./images/saloni-infopreneur.png){width=300px}

</div>
<div style="text-align:center;">
<div style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#FF00FF;text-transform:uppercase;letter-spacing:0.14em;margin-bottom:0.5rem;">Affiliate</div>

![Affiliate account](./images/sophia-affiliate.png){width=300px}

</div>
</div>

<!--
Saloni is an infopreneur: chef, entrepreneur, building a brand, links out via linktr.ee. Sophia is an affiliate: an interior blog that links to an Amazon shop. The bio and the links already tell you the job.
-->

---

# Different jobs, same bio fields

<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:1rem;margin:0 auto 0.4rem;width:520px;text-align:center;">
<div style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#FF00FF;text-transform:uppercase;letter-spacing:0.14em;">E-commerce</div>
<div style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#FF00FF;text-transform:uppercase;letter-spacing:0.14em;">Offline business</div>
<div style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#FF00FF;text-transform:uppercase;letter-spacing:0.14em;">Restaurant</div>
</div>

<div style="display:flex;justify-content:center;">

![E-commerce, offline business, and restaurant accounts](./images/ecommerce-offline-restaurant.png){width=520px}

</div>

<!--
Beautiful Bastard is an apparel brand with a Shop button. The Room is a Santa Monica nightclub that takes reservations and runs events. Muffin Can Stop Us is a brunch restaurant with an order-and-delivery link. Same product, completely different jobs, all readable from the bio and the buttons.
-->

---

# From knowing to measuring

<div style="font-size:1.25rem;color:#1A1A1A;font-weight:600;margin-bottom:1.1rem;line-height:1.45;">
We understood the types qualitatively, but could not quantify them at scale
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:1.6rem;margin-top:0.6rem;">
<div>
<div style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#AAAAAA;text-transform:uppercase;letter-spacing:0.14em;margin-bottom:0.45rem;">Signals per account</div>
<div style="font-size:1.05rem;color:#1A1A1A;line-height:1.6;">What they post, how, and how often; the bio; links to the products they sell</div>
</div>
<div>
<div style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#AAAAAA;text-transform:uppercase;letter-spacing:0.14em;margin-bottom:0.45rem;">Two steps, both via an LLM</div>
<div style="font-size:1.05rem;color:#1A1A1A;line-height:1.6;">Define the classes, then label every account against them</div>
</div>
</div>

<div style="margin-top:1.2rem;padding:0.8rem 1rem;background:#FAFAFA;border-left:3px solid #1A1A1A;font-size:1.05rem;color:#1A1A1A;line-height:1.5;">
We had a prior about the types, so this was a classification task
</div>

<!--
Unstructured inputs, bio and posts and links, were exactly what the LLM could read. Every account now carries a segment label.
-->

---

# A segmentation earns its place when it changes decisions

<div style="font-size:1.1rem;color:#1A1A1A;line-height:1.6;margin-bottom:1rem;">
With every account labeled, the segments changed what we actually do:
</div>

<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:1.2rem;margin-top:0.6rem;">
<div style="padding:1rem 1.1rem;background:#FAFAFA;border-left:3px solid #FF00FF;font-size:1.1rem;font-weight:600;color:#1A1A1A;line-height:1.4;">Custom onboarding</div>
<div style="padding:1rem 1.1rem;background:#FAFAFA;border-left:3px solid #FF00FF;font-size:1.1rem;font-weight:600;color:#1A1A1A;line-height:1.4;">Different in-product recommendations</div>
<div style="padding:1rem 1.1rem;background:#FAFAFA;border-left:3px solid #FF00FF;font-size:1.1rem;font-weight:600;color:#1A1A1A;line-height:1.4;">A different definition of success</div>
</div>

<!--
This is the test for any segmentation. If nothing downstream changes, the segmentation is a dashboard, not a decision.
-->

---

# Different goals, different tools

<div style="font-size:1.1rem;color:#1A1A1A;line-height:1.6;margin-bottom:1.1rem;">
Success is not one metric. It depends on the job:
</div>

<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:1.6rem;margin-bottom:1.4rem;">
<div>
<div style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#AAAAAA;text-transform:uppercase;letter-spacing:0.14em;margin-bottom:0.4rem;">For some</div>
<div style="font-size:1.05rem;color:#1A1A1A;">selling courses</div>
</div>
<div>
<div style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#AAAAAA;text-transform:uppercase;letter-spacing:0.14em;margin-bottom:0.4rem;">For some</div>
<div style="font-size:1.05rem;color:#1A1A1A;">conversations in DMs</div>
</div>
<div>
<div style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#AAAAAA;text-transform:uppercase;letter-spacing:0.14em;margin-bottom:0.4rem;">For some</div>
<div style="font-size:1.05rem;color:#1A1A1A;">reach through Stories</div>
</div>
</div>

<div style="font-size:1.15rem;color:#1A1A1A;font-weight:600;line-height:1.5;">
Different goals lead to different tools, the product strategy gets more flexible, and more users are served well
</div>

<!--
The payoff is on both sides: more users served well, and more revenue.
-->

---
layout: section
class: tint-mint
---

## 03

# Segmenting from a business rule

---

# The marketplace flywheel

<div style="font-size:1.2rem;color:#1A1A1A;font-weight:600;margin-bottom:0.3rem;line-height:1.45;">
More supply brings more demand, and more demand brings more supply
</div>

<div style="display:flex;justify-content:center;margin-top:0.4rem;">
<svg viewBox="0 0 720 360" width="560" style="font-family:'Inter',sans-serif;">
  <defs>
    <marker id="ah" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto" markerUnits="userSpaceOnUse">
      <path d="M0,0 L9,4.5 L0,9 z" fill="#1A1A1A"></path>
    </marker>
  </defs>
  <text x="360" y="187" text-anchor="middle" fill="#6B6B6B" style="font-size:18px;font-weight:700;">More liquidity</text>
  <line x1="278" y1="58" x2="442" y2="58" stroke="#1A1A1A" stroke-width="2.5" marker-end="url(#ah)"></line>
  <line x1="550" y1="94" x2="550" y2="266" stroke="#1A1A1A" stroke-width="2.5" marker-end="url(#ah)"></line>
  <line x1="442" y1="302" x2="278" y2="302" stroke="#1A1A1A" stroke-width="2.5" marker-end="url(#ah)"></line>
  <line x1="170" y1="266" x2="170" y2="94" stroke="#1A1A1A" stroke-width="2.5" marker-end="url(#ah)"></line>
  <rect x="70" y="30" width="200" height="56" rx="10" fill="#FAFAFA" stroke="#E0E0E0"></rect>
  <text x="170" y="63" text-anchor="middle" fill="#1A1A1A" style="font-size:15px;font-weight:600;">More sellers</text>
  <rect x="450" y="30" width="200" height="56" rx="10" fill="#FAFAFA" stroke="#E0E0E0"></rect>
  <text x="550" y="63" text-anchor="middle" fill="#1A1A1A" style="font-size:15px;font-weight:600;">More listings</text>
  <rect x="450" y="274" width="200" height="56" rx="10" fill="#FAFAFA" stroke="#E0E0E0"></rect>
  <text x="550" y="307" text-anchor="middle" fill="#1A1A1A" style="font-size:15px;font-weight:600;">More buyers</text>
  <rect x="70" y="274" width="200" height="56" rx="10" fill="#FAFAFA" stroke="#E0E0E0"></rect>
  <text x="170" y="307" text-anchor="middle" fill="#1A1A1A" style="font-size:15px;font-weight:600;">Buyers become sellers</text>
</svg>
</div>

<!--
This is how a marketplace is built, and it is about all sellers, not only private ones. More sellers means more listings, listings bring buyers, and buyers turn into sellers. Supply feeds demand and demand feeds supply.
-->

---

# Where the money comes from

<div style="font-size:1.3rem;color:#1A1A1A;font-weight:600;margin-bottom:1.2rem;line-height:1.45;">
Avito earns on sellers
</div>

<div style="display:flex;flex-direction:column;gap:0.8rem;font-size:1.1rem;color:#1A1A1A;line-height:1.5;">
<div>The philosophy has always been that private sellers list for free</div>
<div>The non-obvious reason: private listings are the most interesting content, and they are what brings buyers in</div>
</div>

<div style="margin-top:1.3rem;padding:1rem 1.2rem;background:#FAFAFA;border-left:3px solid #FF00FF;font-size:1.15rem;font-weight:600;color:#1A1A1A;line-height:1.5;">
So we balance it and monetize only professional sellers
</div>

<!--
Charge everyone as hard as possible and users leave, taking their listings with them. The private content is the draw, so we protect it by keeping private sellers free and earning only on the professionals.
-->

---

# The task

<div style="font-size:1.3rem;color:#1A1A1A;font-weight:600;margin-bottom:1.3rem;line-height:1.45;">
Label each seller professional or private
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:1.6rem;margin-bottom:1.3rem;">
<div>
<div style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#AAAAAA;text-transform:uppercase;letter-spacing:0.14em;margin-bottom:0.45rem;">Private</div>
<div style="font-size:1.1rem;color:#1A1A1A;line-height:1.5;">lists for free</div>
</div>
<div>
<div style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#AAAAAA;text-transform:uppercase;letter-spacing:0.14em;margin-bottom:0.45rem;">Professional</div>
<div style="font-size:1.1rem;color:#1A1A1A;line-height:1.5;">pays a commission to sell</div>
</div>
</div>

<div style="font-size:1.15rem;color:#1A1A1A;font-weight:600;line-height:1.5;">
We earn on sellers, charge only the professionals, and leave everyone else free
</div>

<!--
The split decides who pays, which is why getting the label right matters commercially. Now we need a way to assign it.
-->

---

# Signals and the rule

<div style="font-size:1.1rem;color:#1A1A1A;line-height:1.6;margin-bottom:0.7rem;">
We read it off behavior, with some outside help:
</div>

<ul style="font-size:1.1rem;line-height:1.7;color:#1A1A1A;margin:0 0 0.8rem;">
<li>how often they sell cars</li>
<li>how many listings they post</li>
<li>how recently the last car was sold, and when it was re-registered</li>
</ul>

<div style="padding:0.9rem 1.1rem;background:#FAFAFA;border-left:3px solid #FF00FF;font-size:1.1rem;color:#1A1A1A;line-height:1.55;">
Fewer than one car a year, we assume long ownership and label the seller <b>private</b>. Otherwise <b>professional</b>, and a commission applies
</div>

<!--
Number of listings and re-registration date are extra clues: a recently re-registered car points to a fresh acquisition, which looks professional. The threshold is deliberately simple, and simple is fine as long as we know it is a choice we made.
-->

---

# Validating the rule

<div style="font-size:1.25rem;color:#1A1A1A;font-weight:600;margin-bottom:1.1rem;line-height:1.45;">
How do we know the rule is good? Count the errors it makes
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:1.6rem;margin-bottom:1.2rem;">
<div>
<div style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#E5142B;text-transform:uppercase;letter-spacing:0.14em;margin-bottom:0.4rem;">False positive</div>
<div style="font-size:1.05rem;color:#1A1A1A;line-height:1.45;">a private seller charged as professional, and they may leave</div>
</div>
<div>
<div style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#E5142B;text-transform:uppercase;letter-spacing:0.14em;margin-bottom:0.4rem;">False negative</div>
<div style="font-size:1.05rem;color:#1A1A1A;line-height:1.45;">a professional left free, and we miss the revenue</div>
</div>
</div>

<div style="font-size:1.1rem;color:#1A1A1A;line-height:1.6;">
With stakeholders, hand-label a few hundred sellers to get the true classes, then check the rule against them. A simple rule or a model both work. If a simple rule keeps the errors low enough, that is already good.
</div>

<!--
This is the confusion matrix we have used before, applied to a business label. The labeled set is ground truth: it is how you measure false positives and false negatives and decide whether the rule is good enough to ship.
-->

---

# The boundary is gameable

<div style="font-size:1.25rem;color:#1A1A1A;font-weight:600;margin-bottom:1.2rem;line-height:1.45;">
Charge only professionals, and some create several accounts to stay on the free side
</div>

<div style="font-size:1.1rem;color:#1A1A1A;line-height:1.7;">
So the segmentation has to carry:
</div>

<ul style="font-size:1.1rem;line-height:1.9;color:#1A1A1A;margin-top:0.4rem;">
<li>fraud handling</li>
<li>deduplication</li>
<li>a meta-profile that ties one person's profiles together</li>
</ul>

<div style="margin-top:1rem;font-size:1.15rem;color:#1A1A1A;font-weight:600;line-height:1.5;">
Defining the policy is most of the work
</div>

<!--
A value segment is a policy with a fuzzy, contested boundary that people have an incentive to game. The interesting part is robustness, not the threshold itself.
-->

---
layout: section
class: tint-sky
---

## 04

# Segmenting from the data

---

# What we expected

<div style="font-size:1.25rem;color:#1A1A1A;font-weight:600;margin-bottom:1.2rem;line-height:1.45;">
Discovery on a live product: what should we build next?
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:1.6rem;">
<div>
<div style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#AAAAAA;text-transform:uppercase;letter-spacing:0.14em;margin-bottom:0.45rem;">Our vision, from interviews</div>
<div style="font-size:1.1rem;color:#1A1A1A;line-height:1.5;">users need the complex use-cases automated: an agent answers questions and runs the funnel to a deal</div>
</div>
<div>
<div style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#AAAAAA;text-transform:uppercase;letter-spacing:0.14em;margin-bottom:0.45rem;">What we built</div>
<div style="font-size:1.1rem;color:#1A1A1A;line-height:1.5;">agents for those flows, and we ran into quality problems</div>
</div>
</div>

<!--
A live product, looking for the next bet. The vision, shaped by qualitative interviews, pointed at sophisticated automation.
-->

---

# What the data showed

<div style="font-size:1.3rem;color:#1A1A1A;font-weight:600;margin-bottom:1.3rem;line-height:1.45;">
Most of the volume was something far <span class="pink">simpler</span>
</div>

<ul style="font-size:1.15rem;line-height:1.9;color:#1A1A1A;margin:0;">
<li>a huge number of accounts and conversations</li>
<li>per user, many short conversations</li>
<li>one-word replies, especially in comments</li>
<li>the goal: make posts go viral</li>
</ul>

<!--
We dug into the conversations and found the opposite of the vision: enormous volume of tiny, repetitive exchanges, mostly comment replies, all aimed at virality. Simpler than expected, and far bigger.
-->

---

# Answering comments by hand

<div style="display:flex;justify-content:center;margin-top:0.3rem;">

![A creator replying to comments one by one](./images/natalie-comments.png){width=470px}

</div>

<!--
A real post: the creator replies to comment after comment by hand, the same kind of short reply every time. This is the pattern the data surfaced, repeated on every post.
-->

---

# Why they do it

<div style="font-size:1.25rem;color:#1A1A1A;font-weight:600;margin-bottom:1.2rem;line-height:1.45;">
Posts with comment activity get more views
</div>

<div style="font-size:1.1rem;color:#1A1A1A;line-height:1.7;">
<div style="margin-bottom:0.6rem;">In the first hours after a post or reel goes out, they stay maximally active in the comments so it takes off</div>
<div>It is a recurring need, done constantly to keep posts viral</div>
</div>

<!--
The motivation is reach. Early engagement feeds distribution, so the manual work happens again on every single post.
-->

---

# The method

<div style="display:flex;flex-direction:column;gap:0.3rem;font-size:1.08rem;color:#1A1A1A;line-height:1.4;">
<div style="padding:0.55rem 0.9rem;background:#FAFAFA;border-left:3px solid #1A1A1A;"><b>Goal</b>&nbsp;&nbsp;discover what users actually do</div>
<div style="text-align:center;color:#AAAAAA;font-size:0.85rem;line-height:1;">↓</div>
<div style="padding:0.55rem 0.9rem;background:#FAFAFA;border-left:3px solid #1A1A1A;"><b>Data</b>&nbsp;&nbsp;one <span class="pink">conversation</span> as the unit, summarized by its goal</div>
<div style="text-align:center;color:#AAAAAA;font-size:0.85rem;line-height:1;">↓</div>
<div style="padding:0.55rem 0.9rem;background:#FAFAFA;border-left:3px solid #1A1A1A;"><b>Task</b>&nbsp;&nbsp;no prior to classify against, so it is a clustering task</div>
<div style="text-align:center;color:#AAAAAA;font-size:0.85rem;line-height:1;">↓</div>
<div style="padding:0.55rem 0.9rem;background:#FAFAFA;border-left:3px solid #1A1A1A;"><b>Output</b>&nbsp;&nbsp;groups form, but with no readable description yet</div>
</div>

<!--
No prior, so we cluster rather than classify. Choosing the conversation as the unit, instead of the user, is what made the pattern visible. The clustering output is raw: groups without meaning until we read them.
-->

---

# Interpreting the clusters

<div style="font-size:1.25rem;color:#1A1A1A;font-weight:600;margin-bottom:1.2rem;line-height:1.45;">
Clusters are only labels until a human reads them
</div>

<div style="display:flex;flex-direction:column;gap:0.7rem;font-size:1.1rem;color:#1A1A1A;line-height:1.5;">
<div>Read each cluster with business and product judgment</div>
<div>Does it match our vision and the real picture? Are these really similar users? Did we cover everything?</div>
<div>Find where the potential is, re-verify on qualitative interviews</div>
<div>Then decide what to build</div>
</div>

<!--
Interpretation is the real work after clustering. We sanity-check the groups against our vision and reality, confirm they hang together as similar users, look for the highest-potential one, and re-verify with interviews before committing.
-->

---

# Why it won, and what changed

<div style="font-size:1.2rem;color:#1A1A1A;font-weight:600;margin-bottom:1rem;line-height:1.45;">
A simple feature, yet the stronger bet
</div>

<div style="display:grid;grid-template-columns:1fr 1fr 1fr 1fr;gap:1rem;margin-bottom:1.4rem;">
<div style="padding:0.9rem 1rem;background:#FAFAFA;border-left:3px solid #FF00FF;font-size:1.05rem;font-weight:600;color:#1A1A1A;line-height:1.35;">wider segment</div>
<div style="padding:0.9rem 1rem;background:#FAFAFA;border-left:3px solid #FF00FF;font-size:1.05rem;font-weight:600;color:#1A1A1A;line-height:1.35;">wider market</div>
<div style="padding:0.9rem 1rem;background:#FAFAFA;border-left:3px solid #FF00FF;font-size:1.05rem;font-weight:600;color:#1A1A1A;line-height:1.35;">more users</div>
<div style="padding:0.9rem 1rem;background:#FAFAFA;border-left:3px solid #FF00FF;font-size:1.05rem;font-weight:600;color:#1A1A1A;line-height:1.35;">recurring need</div>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr 1fr 1fr;gap:1rem;">
<div>
<div style="font-family:'JetBrains Mono',monospace;font-size:0.65rem;color:#AAAAAA;text-transform:uppercase;letter-spacing:0.12em;margin-bottom:0.3rem;">Strategy</div>
<div style="font-size:1rem;color:#1A1A1A;line-height:1.4;">changed strategy and roadmap</div>
</div>
<div>
<div style="font-family:'JetBrains Mono',monospace;font-size:0.65rem;color:#AAAAAA;text-transform:uppercase;letter-spacing:0.12em;margin-bottom:0.3rem;">Ship</div>
<div style="font-size:1rem;color:#1A1A1A;line-height:1.4;">shipped the feature</div>
</div>
<div>
<div style="font-family:'JetBrains Mono',monospace;font-size:0.65rem;color:#AAAAAA;text-transform:uppercase;letter-spacing:0.12em;margin-bottom:0.3rem;">Invest</div>
<div style="font-size:1rem;color:#1A1A1A;line-height:1.4;">invested more resources</div>
</div>
<div>
<div style="font-family:'JetBrains Mono',monospace;font-size:0.65rem;color:#AAAAAA;text-transform:uppercase;letter-spacing:0.12em;margin-bottom:0.3rem;">Result</div>
<div style="font-size:1rem;color:#1A1A1A;line-height:1.4;">strong results</div>
</div>
</div>

<!--
Breadth and recurrence decided it, not sophistication. This is the upside argument from section 01 in practice.
-->

---
layout: section
class: tint-lavender
---

## 05

# A universal method

---

# Winning users back

<div style="font-size:1.3rem;color:#1A1A1A;font-weight:600;margin-bottom:1.3rem;line-height:1.45;">
A common goal: bring back users who stopped using the product
</div>

<div style="font-size:1.15rem;color:#1A1A1A;line-height:1.6;">
The usual levers are discounts, notifications, and other perks
</div>

<!--
Win-back is a universal product problem. Someone went quiet, and we want them active and paying again.
-->

---

# But not everyone

<div style="font-size:1.25rem;color:#1A1A1A;font-weight:600;margin-bottom:1.1rem;line-height:1.45;">
Treating everyone is wasteful, and sometimes harmful
</div>

<ul style="font-size:1.1rem;line-height:1.8;color:#1A1A1A;margin:0 0 1rem;">
<li>discounts and perks are a direct financial cost</li>
<li>notifications annoy the users who do not need them</li>
<li>rewarding users who would have returned anyway buys nothing</li>
</ul>

<div style="padding:0.9rem 1.1rem;background:#FAFAFA;border-left:3px solid #FF00FF;font-size:1.1rem;font-weight:600;color:#FF00FF;line-height:1.5;">
Spend only on the users whose behavior the treatment would change
</div>

<div style="font-size:1.05rem;color:#1A1A1A;line-height:1.6;margin-top:1rem;">
So we segment by churn risk: at risk, likely to return, sleeping
</div>

<!--
This is the core of win-back targeting: do not pay the users who would come back on their own, and do not waste a discount on those who never will. Use all the data you have to act only on the ones a nudge actually moves.
-->

---

# RFM

<div style="font-size:1.25rem;color:#1A1A1A;font-weight:600;margin-bottom:0.5rem;line-height:1.45;">
One method works on almost any product, regardless of domain
</div>

<div style="font-size:1.1rem;color:#1A1A1A;line-height:1.6;margin-bottom:1.3rem;">
It rests on a strong assumption: <span class="pink">three</span> cheap, near-universal signals capture how users differ
</div>

<div style="background:#FAFAFA;border-radius:8px;padding:1.2rem 1.4rem;display:grid;grid-template-columns:1fr 1fr 1fr;gap:1.6rem;">
<div>
<div style="font-family:'JetBrains Mono',monospace;font-size:0.72rem;color:#FF00FF;text-transform:uppercase;letter-spacing:0.14em;margin-bottom:0.45rem;">Recency</div>
<div style="font-size:1.05rem;color:#1A1A1A;line-height:1.45;margin-bottom:0.3rem;">how recently they last acted</div>
<div style="font-size:0.95rem;color:#6B6B6B;line-height:1.4;">flags who is slipping away</div>
</div>
<div>
<div style="font-family:'JetBrains Mono',monospace;font-size:0.72rem;color:#FF00FF;text-transform:uppercase;letter-spacing:0.14em;margin-bottom:0.45rem;">Frequency</div>
<div style="font-size:1.05rem;color:#1A1A1A;line-height:1.45;margin-bottom:0.3rem;">how often they act</div>
<div style="font-size:0.95rem;color:#6B6B6B;line-height:1.4;">shows engagement and habit</div>
</div>
<div>
<div style="font-family:'JetBrains Mono',monospace;font-size:0.72rem;color:#FF00FF;text-transform:uppercase;letter-spacing:0.14em;margin-bottom:0.45rem;">Monetary</div>
<div style="font-size:1.05rem;color:#1A1A1A;line-height:1.45;margin-bottom:0.3rem;">how much they spend</div>
<div style="font-size:0.95rem;color:#6B6B6B;line-height:1.4;">shows where the value sits</div>
</div>
</div>

<!--
Almost every product records when a user last acted, how often, and how much they spend. RFM bets these three are enough to tell user types apart, which is why it ports across domains. Recency ties straight back to win-back: a long gap is a user slipping away.
-->

---

# Demo: RFM in code

<div style="font-size:1.2rem;color:#1A1A1A;font-weight:600;margin-bottom:1.4rem;line-height:1.45;">
A short notebook builds a synthetic shop, scores every customer, and lands on the win-back list
</div>

<div style="display:flex;justify-content:center;margin-top:2.2rem;">
<a href="/harbour-product-analytics-2026/12-segmentation/rfm-segmentation.html" target="_blank" rel="noopener" style="display:inline-block;padding:0.9rem 1.6rem;background:#1A1A1A;color:#fff;font-family:'JetBrains Mono',monospace;font-size:1rem;font-weight:700;letter-spacing:0.08em;text-transform:uppercase;text-decoration:none;border:2px solid #1A1A1A;">Open the notebook ↗</a>
</div>

<!--
Open this live in JupyterLab and walk through it with the class: synthetic coffee-shop orders, R/F/M scoring, the segment map, and the win-back list. Swap the file link for your local Jupyter URL if you run the server.
-->

---
layout: section
class: tint-cream
---

## 06

# Bringing it together

---
layout: statement
---

# What works for some does not work for others

<!--
This is the bookend to the opening. The whole-population average is one number, and it hides the groups underneath it.
-->

---

# A flat average can hide two segments

<div style="font-size:1.3rem;color:#1A1A1A;font-weight:600;margin-bottom:1.4rem;line-height:1.45;">
A flat average does not mean the change did nothing
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:1.6rem;">
<div>
<div style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#AAAAAA;text-transform:uppercase;letter-spacing:0.14em;margin-bottom:0.45rem;">One segment</div>
<div style="font-size:1.1rem;color:#1A1A1A;line-height:1.5;">clearly improved</div>
</div>
<div>
<div style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#AAAAAA;text-transform:uppercase;letter-spacing:0.14em;margin-bottom:0.45rem;">Another segment</div>
<div style="font-size:1.1rem;color:#1A1A1A;line-height:1.5;">was dropped, and the two cancel out</div>
</div>
</div>

<!--
A zero average effect can be a real win for one group plus a real loss for another. Without segments you never see it, and you may ship something that quietly hurts people.
-->

---

# How to approach it

<div style="font-size:1.25rem;color:#1A1A1A;font-weight:600;margin-bottom:0.5rem;line-height:1.45;">
Always start from a clearly formulated business problem
</div>

<div style="font-size:1.1rem;color:#1A1A1A;line-height:1.6;margin-bottom:1.2rem;">
What do we actually want to get? The problem then becomes a concrete task:
</div>

<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:1.6rem;">
<div>
<div style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#AAAAAA;text-transform:uppercase;letter-spacing:0.14em;margin-bottom:0.4rem;">Prior known</div>
<div style="font-size:1.05rem;color:#1A1A1A;">classification</div>
</div>
<div>
<div style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#AAAAAA;text-transform:uppercase;letter-spacing:0.14em;margin-bottom:0.4rem;">No prior</div>
<div style="font-size:1.05rem;color:#1A1A1A;">clustering</div>
</div>
<div>
<div style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#AAAAAA;text-transform:uppercase;letter-spacing:0.14em;margin-bottom:0.4rem;">Several at once</div>
<div style="font-size:1.05rem;color:#1A1A1A;">multi-label</div>
</div>
</div>

<!--
The task type follows from the problem, not the other way around. We saw all three across the cases today.
-->

---
layout: section
class: tint-rose
---

## 07

# What's expected of an analyst

---

# What changes as you level up

<table style="width:100%;border-collapse:collapse;font-family:'Inter',sans-serif;margin-top:0.3rem;">
<thead>
<tr>
<th style="width:15%;border-bottom:1px solid #E0E0E0;"></th>
<th style="width:26%;text-align:left;vertical-align:bottom;padding:0 0.6rem 0.5rem;border-bottom:1px solid #E0E0E0;font-family:'JetBrains Mono',monospace;font-size:0.66rem;color:#AAAAAA;text-transform:uppercase;letter-spacing:0.1em;">Junior &middot; IC3 / L3</th>
<th style="width:27%;text-align:left;vertical-align:bottom;padding:0 0.6rem 0.5rem;border-bottom:1px solid #E0E0E0;font-family:'JetBrains Mono',monospace;font-size:0.66rem;color:#AAAAAA;text-transform:uppercase;letter-spacing:0.1em;">Senior &middot; IC5 / L5</th>
<th style="width:32%;text-align:left;vertical-align:bottom;padding:0 0.6rem 0.5rem;border-bottom:1px solid #E0E0E0;font-family:'JetBrains Mono',monospace;font-size:0.66rem;color:#AAAAAA;text-transform:uppercase;letter-spacing:0.1em;">Lead / Staff / Manager &middot; IC6+ / M1+</th>
</tr>
</thead>
<tbody>
<tr>
<td style="vertical-align:top;padding:0.6rem;border-bottom:1px solid #E0E0E0;font-weight:700;font-size:0.92rem;color:#1A1A1A;">Ambiguity</td>
<td style="vertical-align:top;padding:0.6rem;border-bottom:1px solid #E0E0E0;font-size:0.82rem;line-height:1.35;color:#1A1A1A;"><b>Low.</b> A clear, scoped task: «Compute this button's conversion for last week»</td>
<td style="vertical-align:top;padding:0.6rem;border-bottom:1px solid #E0E0E0;font-size:0.82rem;line-height:1.35;color:#1A1A1A;"><b>High.</b> «Cart retention is dropping. Find out why and propose a fix»</td>
<td style="vertical-align:top;padding:0.6rem;border-bottom:1px solid #E0E0E0;font-size:0.82rem;line-height:1.35;color:#1A1A1A;"><b>Maximal.</b> «We are entering Latin America. What should our data strategy and success metrics be?»</td>
</tr>
<tr>
<td style="vertical-align:top;padding:0.6rem;border-bottom:1px solid #E0E0E0;font-weight:700;font-size:0.92rem;color:#1A1A1A;">Scope of impact</td>
<td style="vertical-align:top;padding:0.6rem;border-bottom:1px solid #E0E0E0;font-size:0.82rem;line-height:1.35;color:#1A1A1A;"><b>Own task.</b> Answers only for the quality of the code and the numbers in that task</td>
<td style="vertical-align:top;padding:0.6rem;border-bottom:1px solid #E0E0E0;font-size:0.82rem;line-height:1.35;color:#1A1A1A;"><b>Product feature or team.</b> Shapes the decisions of a whole product unit: PM, designers, engineers</td>
<td style="vertical-align:top;padding:0.6rem;border-bottom:1px solid #E0E0E0;font-size:0.82rem;line-height:1.35;color:#1A1A1A;"><b>Whole company or industry.</b> Decisions reshape the company's data architecture or set long-term OKRs</td>
</tr>
<tr>
<td style="vertical-align:top;padding:0.6rem;font-weight:700;font-size:0.92rem;color:#1A1A1A;">Focus</td>
<td style="vertical-align:top;padding:0.6rem;font-size:0.82rem;line-height:1.35;color:#1A1A1A;"><b>Process.</b> How to do what was asked</td>
<td style="vertical-align:top;padding:0.6rem;font-size:0.82rem;line-height:1.35;color:#1A1A1A;"><b>Problem.</b> Which business problem the data is solving</td>
<td style="vertical-align:top;padding:0.6rem;font-size:0.82rem;line-height:1.35;color:#1A1A1A;"><b>Systems and people.</b> Build processes so decisions happen faster, or grow the team</td>
</tr>
</tbody>
</table>

<!--
The titles differ by company, but the axes are nearly universal: as you go up, the ambiguity you absorb grows, your radius of impact widens from your own task to the whole company, and your focus shifts from process to problem to systems and people. Levels (IC3/IC5/IC6+) and the manager split are the common shape.
-->

---

# Competency matrices to read

<div style="display:grid;grid-template-columns:1fr 1fr;gap:2.4rem;margin-top:0.6rem;font-size:0.9rem;line-height:1.6;color:#1A1A1A;">

<div>
<div style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#AAAAAA;letter-spacing:0.14em;text-transform:uppercase;margin-bottom:0.5rem;">Published matrices</div>
<ul style="margin:0 0 1.2rem;padding-left:1.1rem;">
<li><a href="https://cleo-ai.progressionapp.com/teams/product-analytics-m5ea4e3nufps/framework" target="_blank">Cleo</a>, product analytics progression framework</li>
<li><a href="https://monzo.com/documents/data-progression-framework-v2-0.pdf" target="_blank">Monzo</a>, data discipline framework (MIT-licensed)</li>
<li><a href="https://handbook.gitlab.com/job-families/marketing/enterprise-data/data-science/" target="_blank">GitLab</a>, data science job family in the open handbook</li>
<li><a href="https://engineering.atspotify.com/2016/02/spotify-technology-career-steps" target="_blank">Spotify</a>, technology career steps</li>
</ul>
</div>

<div>
<div style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;color:#AAAAAA;letter-spacing:0.14em;text-transform:uppercase;margin-bottom:0.5rem;">Frameworks and role types</div>
<ul style="margin:0 0 1.2rem;padding-left:1.1rem;">
<li><a href="https://ddat-capability-framework.service.gov.uk/role/data-scientist" target="_blank">UK Gov capability framework</a>, skills by level for analyst and data scientist</li>
<li><a href="https://progression.fyi/" target="_blank">progression.fyi</a>, open collection of career ladders</li>
<li><a href="https://www.linkedin.com/pulse/one-data-science-job-doesnt-fit-all-elena-grewal" target="_blank">Airbnb</a>, three types of data scientist</li>
<li><a href="https://towardsdatascience.com/what-10-years-at-uber-meta-and-startups-taught-me-about-data-analytics-fd948b912556/" target="_blank">10 years at Uber, Meta, and startups</a>, lessons on the analytics role</li>
</ul>
</div>

</div>

<!--
Cleo and Avito are the ones I have ready. Monzo, GitLab, Spotify, and the UK Gov framework are fully public and detailed. Airbnb's three-types piece explains why analyst expectations differ by track.
-->

