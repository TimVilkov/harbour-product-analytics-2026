<script setup lang="ts">
import { ref, watch } from 'vue'
import { useNav } from '@slidev/client'

const props = defineProps<{
  src: string
  height?: string
}>()

const { currentSlideNo } = useNav()
const bust = ref(Date.now())

watch(currentSlideNo, () => {
  bust.value = Date.now()
})

function finalSrc() {
  const sep = props.src.includes('?') ? '&' : '?'
  return `${props.src}${sep}t=${bust.value}`
}
</script>

<template>
  <iframe
    :key="bust"
    :src="finalSrc()"
    :style="{ width: '100%', height: height || '260px', border: 0, borderRadius: '6px' }"
  />
</template>
