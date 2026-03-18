"""
DeepL Translation Utility
Thin wrapper around the DeepL free API for batched text translation.
Used by the translation middleware to translate user-facing content.
"""

import re
import requests

from ..config import Config
from ..utils.logger import get_logger

logger = get_logger('mirofish.translator')

# DeepL free-tier endpoint (keys ending in :fx)
DEEPL_API_URL = "https://api-free.deepl.com/v2/translate"

# Regex patterns for content that should never be translated
_SKIP_PATTERNS = [
    re.compile(r'^https?://'),           # URLs
    re.compile(r'^wss?://'),             # WebSocket URLs
    re.compile(r'^\d[\d.:\-/T]+Z?$'),   # Timestamps, dates, pure numbers
    re.compile(r'^[a-f0-9\-]{8,}$', re.I),  # UUIDs / hex IDs
    re.compile(r'^(proj|sim|task|report|graph|mirofish)_'), # Internal IDs
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


def translate_texts(texts, target_lang, source_lang=None):
    """
    Translate a list of strings via DeepL in a single batched API call.

    Args:
        texts: list of strings to translate.
        target_lang: 'EN' or 'ZH' (DeepL language codes).
        source_lang: optional source language hint ('EN' or 'ZH').

    Returns:
        list of translated strings (same length/order as input).
        On failure, returns the original texts unchanged.
    """
    api_key = Config.DEEPL_API_KEY
    if not api_key or not texts:
        return texts

    # Build index of translatable texts
    translatable = []
    indices = []
    for i, t in enumerate(texts):
        if _should_translate(t):
            translatable.append(t)
            indices.append(i)

    if not translatable:
        return texts

    try:
        payload = {
            'text': translatable,
            'target_lang': target_lang,
        }
        if source_lang:
            payload['source_lang'] = source_lang

        resp = requests.post(
            DEEPL_API_URL,
            data=payload,
            headers={'Authorization': f'DeepL-Auth-Key {api_key}'},
            timeout=15,
        )
        resp.raise_for_status()

        translations = resp.json().get('translations', [])
        result = list(texts)
        for idx, tr in zip(indices, translations):
            result[idx] = tr['text']
        return result

    except requests.exceptions.HTTPError as e:
        status = e.response.status_code if e.response is not None else 'N/A'
        logger.warning(f"DeepL API error (HTTP {status}): {e}")
        return texts
    except Exception as e:
        logger.warning(f"Translation failed: {e}")
        return texts
