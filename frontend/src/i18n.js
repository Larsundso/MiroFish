import { createI18n } from 'vue-i18n'
import zh from './locales/zh.json'
import en from './locales/en.json'

// Restore saved language preference, default to Chinese
const savedLang = localStorage.getItem('mirofish-lang') || 'zh'

const i18n = createI18n({
  legacy: false,           // use Composition API mode
  locale: savedLang,
  fallbackLocale: 'zh',
  messages: { zh, en }
})

export default i18n
