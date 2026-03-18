"""
Translation Utility

Translation priority:
1. Local i18n dict — ~70 fixed backend strings, instant, free
2. In-memory cache — previously translated strings, instant, free
3. MyMemory API — free public translation API for dynamic content
4. LLM English suffix — new LLM output comes in English natively (see llm_client.py)
"""

import re
import requests

from ..utils.logger import get_logger

logger = get_logger('mirofish.translator')

MYMEMORY_API_URL = "https://api.mymemory.translated.net/get"

_LANG_MAP = {'ZH': 'zh-CN', 'EN': 'en'}

# In-memory translation cache
_cache = {}
_CACHE_MAX = 10000

# Regex patterns for content that should never be translated
_SKIP_PATTERNS = [
    re.compile(r'^https?://'),
    re.compile(r'^wss?://'),
    re.compile(r'^\d[\d.:\-/T]+Z?$'),
    re.compile(r'^[a-f0-9\-]{8,}$', re.I),
    re.compile(r'^(proj|sim|task|report|graph|mirofish)_'),
]


def _should_translate(text):
    """Return False for values that should never be translated."""
    if not isinstance(text, str):
        return False
    stripped = text.strip()
    if not stripped or len(stripped) < 2:
        return False
    for pat in _SKIP_PATTERNS:
        if pat.match(stripped):
            return False
    return True


def _translate_mymemory(translatable, target_lang, source_lang):
    """Free translation using MyMemory API."""
    m_target = _LANG_MAP.get(target_lang, target_lang.lower())
    m_source = _LANG_MAP.get(source_lang, source_lang.lower()) if source_lang else 'zh-CN'
    langpair = f'{m_source}|{m_target}'

    try:
        from concurrent.futures import ThreadPoolExecutor

        def translate_one(text):
            try:
                resp = requests.get(
                    MYMEMORY_API_URL,
                    params={'q': text[:500], 'langpair': langpair},
                    timeout=10,
                )
                if resp.status_code == 200:
                    data = resp.json()
                    if data.get('quotaFinished'):
                        return text
                    return data['responseData']['translatedText']
            except Exception:
                pass
            return text

        with ThreadPoolExecutor(max_workers=5) as pool:
            results = list(pool.map(translate_one, translatable))
        return results

    except Exception as e:
        logger.warning(f"MyMemory failed: {e}")
        return None


def translate_texts(texts, target_lang, source_lang=None):
    """
    Translate a list of strings.

    Priority: local dict → cache → MyMemory (free)
    """
    if not texts:
        return texts

    from .backend_i18n import lookup as _i18n_lookup

    result = list(texts)
    uncached = []
    uncached_indices = []

    for i, t in enumerate(texts):
        if not _should_translate(t):
            continue
        # 1) Local dict (free, instant)
        if target_lang == 'EN':
            local = _i18n_lookup(t)
            if local is not None:
                result[i] = local
                continue
        # 2) Cache (free, instant)
        cache_key = (t, target_lang)
        if cache_key in _cache:
            result[i] = _cache[cache_key]
        else:
            # 3) Queue for MyMemory
            uncached.append(t)
            uncached_indices.append(i)

    if not uncached:
        return result

    translated = _translate_mymemory(uncached, target_lang, source_lang)
    if translated:
        if len(_cache) > _CACHE_MAX:
            _cache.clear()
        for idx, orig, tr in zip(uncached_indices, uncached, translated):
            result[idx] = tr
            _cache[(orig, target_lang)] = tr

    return result
