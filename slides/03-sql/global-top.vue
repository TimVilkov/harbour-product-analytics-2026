<script setup lang="ts">
import { useNav } from '@slidev/client'
import { computed, onMounted, watch, nextTick } from 'vue'

const { currentSlideNo, currentSlideRoute } = useNav()

const isDarkSlide = computed(() => {
  const layout = currentSlideRoute.value?.meta?.slide?.frontmatter?.layout
  return layout === 'intro' || layout === 'intro-image-right'
})

// === Click-to-copy on code blocks AND tagged cells ==============
// Code: every <pre class="shiki ..."> rendered by Slidev.
// Cells: any element with class="copyable-cell" (e.g. login table values).
// On every slide change, attach a click handler that copies and
// flashes a "copied" badge.

function flashBadge(badge: HTMLElement, text: string, pink = true) {
  badge.textContent = text
  if (pink) badge.classList.add('copied')
  setTimeout(() => {
    badge.textContent = 'copy'
    badge.classList.remove('copied')
  }, 1200)
}

async function attachCopyHandlers() {
  await nextTick()

  // 1. Code blocks
  const blocks = document.querySelectorAll('pre.shiki:not([data-copy-bound])') as NodeListOf<HTMLPreElement>
  blocks.forEach((pre) => {
    pre.setAttribute('data-copy-bound', '1')
    pre.classList.add('copyable-code')

    const badge = document.createElement('span')
    badge.className = 'copy-badge'
    badge.textContent = 'copy'
    pre.appendChild(badge)

    pre.addEventListener('click', async (ev) => {
      if ((ev as MouseEvent).detail > 1) return
      const text = pre.innerText.replace(/\n?copy\n?$/, '').trim()
      try {
        await navigator.clipboard.writeText(text)
        flashBadge(badge, 'copied')
      } catch {
        flashBadge(badge, 'press ⌘C', false)
      }
    })
  })

  // 2. Tagged cells (use data-copy attribute for the exact value)
  const cells = document.querySelectorAll('.copyable-cell:not([data-copy-bound])') as NodeListOf<HTMLElement>
  cells.forEach((cell) => {
    cell.setAttribute('data-copy-bound', '1')
    cell.classList.add('copyable-code')

    const badge = document.createElement('span')
    badge.className = 'copy-badge'
    badge.textContent = 'copy'
    cell.appendChild(badge)

    cell.addEventListener('click', async (ev) => {
      if ((ev as MouseEvent).detail > 1) return
      const text = cell.getAttribute('data-copy') || cell.innerText.replace(/\n?copy\n?$/, '').trim()
      try {
        await navigator.clipboard.writeText(text)
        flashBadge(badge, 'copied')
      } catch {
        flashBadge(badge, 'press ⌘C', false)
      }
    })
  })
}

onMounted(attachCopyHandlers)
watch(currentSlideNo, attachCopyHandlers)
</script>

<template>
  <!-- Persistent header bar on every slide except the cover (slide 1) -->
  <div
    v-if="currentSlideNo > 1"
    class="course-header"
    :class="{ 'course-header-dark': isDarkSlide }"
  >
    <div class="course-header-left">Harbour.Space</div>
    <div class="course-header-right">Product Analytics &middot; Session 03</div>
  </div>
</template>

<style>
.course-header {
  position: absolute;
  top: 1.5rem;
  left: 3.5rem;
  right: 3.5rem;
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  padding-bottom: 0.6rem;
  border-bottom: 1px solid #1A1A1A;
  z-index: 10;
  pointer-events: none;
  color: #1A1A1A;
}
.course-header-dark {
  color: #fff;
  border-bottom-color: #fff;
}
.course-header-left {
  font-family: 'Bricolage Grotesque', sans-serif;
  font-weight: 800;
  font-size: 1rem;
  letter-spacing: -0.01em;
}
.course-header-right {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.7rem;
  text-transform: uppercase;
  letter-spacing: 0.12em;
}

/* === Copy-on-click for code blocks =========================== */
.copyable-code {
  position: relative;
  cursor: copy;
  user-select: text !important;
  -webkit-user-select: text !important;
  transition: outline-color 0.15s;
  outline: 1px solid transparent;
}
.copyable-code:hover {
  outline-color: rgba(255, 0, 255, 0.4);
}
.copyable-code code {
  user-select: text !important;
  -webkit-user-select: text !important;
}
.copy-badge {
  position: absolute;
  top: 0.4rem;
  right: 0.5rem;
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.65rem;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: #6B6B6B;
  background: rgba(255, 255, 255, 0.85);
  padding: 0.15rem 0.45rem;
  border-radius: 3px;
  opacity: 0;
  transition: opacity 0.15s, color 0.15s;
  pointer-events: none;
}
.copyable-code:hover .copy-badge {
  opacity: 1;
}
.copy-badge.copied {
  color: #FF00FF;
  opacity: 1 !important;
}
</style>
