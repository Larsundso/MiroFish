<template>
  <button class="lang-toggle" @click="toggleLang" :title="currentLang === 'zh' ? 'Switch to English' : '切换到中文'">
    <span class="lang-label">{{ currentLang === 'zh' ? 'EN' : '中' }}</span>
  </button>
</template>

<script setup>
import { ref, watch } from 'vue'
import { useI18n } from 'vue-i18n'

const { locale } = useI18n()
const currentLang = ref(localStorage.getItem('mirofish-lang') || 'zh')

const toggleLang = () => {
  currentLang.value = currentLang.value === 'zh' ? 'en' : 'zh'
  locale.value = currentLang.value
  localStorage.setItem('mirofish-lang', currentLang.value)
}
</script>

<style scoped>
.lang-toggle {
  width: 32px;
  height: 32px;
  border: 1px solid currentColor;
  background: transparent;
  color: inherit;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  font-family: 'JetBrains Mono', monospace;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0;
  transition: all 0.2s;
  opacity: 0.7;
}

.lang-toggle:hover {
  opacity: 1;
}
</style>
