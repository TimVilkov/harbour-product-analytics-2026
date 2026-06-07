// Generates dist/index.html: the course landing page linking every built deck.
// Runs in CI after all decks are built into dist/<slug>/.
import { readdirSync, statSync, writeFileSync, existsSync } from 'node:fs'
import { join } from 'node:path'

const DIST = 'dist'

// slug -> display title. Folders not listed here fall back to a prettified slug.
const TITLES = {
  '01-product-metrics-1': 'Product Metrics 1',
  '02-product-metrics-2': 'Product Metrics 2',
  '03-sql': 'SQL',
  '04-data-viz': 'Data Visualisation & Storytelling',
  '05-statistics-1': 'Statistics 1',
  '06-statistics-2': 'Statistics 2',
  '07-statistics-3': 'Statistics 3',
  '08-experiments-1': 'A/B Testing 1',
  '09-experiments-2': 'A/B Testing 2',
  '10-experiments-3': 'A/B Testing 3',
  '11-causal-inference': 'Causal Thinking',
  '12-segmentation': 'Segmentation',
  '13-cohort-unit-economics': 'Cohort Analysis & Modeling',
  '14-product-analyst-role': 'Product Analyst Role',
  '15-final-project': 'Final Project Presentations',
}

const prettify = (slug) =>
  slug.replace(/^\d+-/, '').replace(/-/g, ' ').replace(/\b\w/g, (c) => c.toUpperCase())

const decks = readdirSync(DIST)
  .filter((name) => {
    const p = join(DIST, name)
    return statSync(p).isDirectory() && existsSync(join(p, 'index.html'))
  })
  .sort()

const rows = decks
  .map((slug) => {
    const num = (slug.match(/^(\d+)/)?.[1] ?? '').replace(/^0/, '')
    const title = TITLES[slug] ?? prettify(slug)
    return `      <a class="row" href="./${slug}/">
        <span class="num">${num.padStart(2, '0')}</span>
        <span class="title">${title}</span>
        <span class="arrow">&rarr;</span>
      </a>`
  })
  .join('\n')

const html = `<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Product Analytics — Harbour.Space 2026</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&family=Bricolage+Grotesque:opsz,wght@12..96,700;12..96,800&family=JetBrains+Mono:wght@500&display=swap" rel="stylesheet" />
  <style>
    :root { --ink:#1A1A1A; --muted:#8A8A8A; --line:#ECECEC; --pink:#FF00FF; }
    * { box-sizing: border-box; }
    body {
      margin:0; background:#fff; color:var(--ink);
      font-family:'Inter',system-ui,sans-serif;
      -webkit-font-smoothing:antialiased;
    }
    .wrap { max-width:760px; margin:0 auto; padding:8vh 28px 12vh; }
    .kicker {
      font-family:'JetBrains Mono',monospace; font-size:0.72rem; letter-spacing:0.18em;
      text-transform:uppercase; color:var(--muted); margin:0 0 1.4rem;
    }
    h1 {
      font-family:'Bricolage Grotesque',sans-serif; font-weight:800;
      font-size:clamp(2.2rem,6vw,3.4rem); line-height:1.05; letter-spacing:-0.02em; margin:0;
    }
    h1 .dot { color:var(--pink); }
    .sub { font-size:1.05rem; color:var(--muted); margin:1.1rem 0 3.2rem; line-height:1.5; }
    .list { display:flex; flex-direction:column; }
    .row {
      display:flex; align-items:baseline; gap:1.2rem; text-decoration:none; color:var(--ink);
      padding:1.05rem 0.4rem; border-top:1px solid var(--line); transition:padding .18s ease;
    }
    .list .row:last-child { border-bottom:1px solid var(--line); }
    .row:hover { padding-left:1.1rem; }
    .row:hover .title { color:var(--pink); }
    .row:hover .arrow { opacity:1; transform:translateX(0); }
    .num {
      font-family:'JetBrains Mono',monospace; font-size:0.95rem; color:var(--pink);
      min-width:2ch; font-weight:500;
    }
    .title { font-size:1.18rem; font-weight:600; flex:1; transition:color .18s ease; }
    .arrow { color:var(--pink); opacity:0; transform:translateX(-6px); transition:all .18s ease; }
    footer { margin-top:4rem; font-size:0.85rem; color:var(--muted); line-height:1.6; }
    @media (max-width:520px){ .row:hover{padding-left:0.4rem;} }
  </style>
</head>
<body>
  <main class="wrap">
    <p class="kicker">Harbour.Space · Barcelona · 2026</p>
    <h1>Product Analytics<span class="dot">.</span></h1>
    <p class="sub">Lecture decks. Open one, use arrow keys to navigate, clicks reveal step by step.</p>
    <nav class="list">
${rows}
    </nav>
    <footer>
      Timofey Vilkov · Senior Product Analyst, Manychat<br />
      timofey.vilkov@manychat.com
    </footer>
  </main>
</body>
</html>
`

writeFileSync(join(DIST, 'index.html'), html)
console.log(`index.html written with ${decks.length} deck(s): ${decks.join(', ')}`)
