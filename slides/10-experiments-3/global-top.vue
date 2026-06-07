<script setup lang="ts">
import { useNav } from '@slidev/client'
import { computed } from 'vue'

const { currentSlideNo, currentSlideRoute } = useNav()

const isDarkSlide = computed(() => {
  const layout = currentSlideRoute.value?.meta?.slide?.frontmatter?.layout
  return layout === 'intro' || layout === 'intro-image-right'
})
</script>

<template>
  <!-- Persistent header bar on every slide except the cover (slide 1) -->
  <div
    v-if="currentSlideNo > 1"
    class="course-header"
    :class="{ 'course-header-dark': isDarkSlide }"
  >
    <div class="course-header-left">Harbour.Space</div>
    <div class="course-header-right">Product Analytics &middot; Session 10</div>
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
</style>
