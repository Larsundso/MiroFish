"""
Translation Middleware
Intercepts Flask requests/responses and translates user-facing text
when the X-Lang: en header or ?lang=en query param is present.

- Inbound (EN→ZH): translates known user-input fields so the
  Chinese-only backend receives Chinese.
- Outbound (ZH→EN): detects Chinese strings in JSON responses
  and translates them to English.

Zero overhead when no language header is present.
"""

import json
import re

from flask import request, g

from ..utils.translator import translate_texts
from ..utils.logger import get_logger

logger = get_logger('mirofish.translation')

# Regex to detect strings containing Chinese characters
_HAS_CHINESE = re.compile(r'[\u4e00-\u9fff]')

# Request fields that may contain user-facing English text to translate
_INPUT_TEXT_FIELDS = {
    'simulation_requirement', 'message', 'query',
    'additional_context', 'project_name', 'graph_name', 'prompt',
}

# Response keys whose values should NEVER be translated even if they
# contain Chinese (internal state, IDs, enum values, etc.)
_SKIP_RESPONSE_KEYS = {
    'status', 'success', 'project_id', 'simulation_id', 'task_id',
    'report_id', 'graph_id', 'agent_id', 'filename', 'download_name',
    'task_type', 'platform', 'action', 'action_type', 'has_report',
    'interview_unlocked', 'already_generated', 'already_completed',
    'is_complete', 'traceback', 'section_index', 'total_sections',
    'from_line', 'has_more', 'total_lines', 'count',
}

# Maximum characters to send in a single DeepL batch (stay under 128KB)
_MAX_BATCH_CHARS = 80_000


def _wants_english():
    """Check if the current request wants English translation."""
    if request.headers.get('X-Lang', '').lower() == 'en':
        return True
    if request.args.get('lang', '').lower() == 'en':
        return True
    return False


# ── Inbound: EN→ZH ──────────────────────────────────────────────

def _translate_request_body():
    """Translate known user-input fields from English to Chinese."""
    # Handle JSON requests (most API endpoints)
    if request.is_json:
        body = request.get_json(silent=True)
        if not body or not isinstance(body, dict):
            return
        _translate_dict_fields(body)
        return

    # Handle multipart form data (e.g. ontology/generate)
    content_type = request.content_type or ''
    if 'multipart' not in content_type and 'form' not in content_type:
        return

    # Force Flask to parse form data, then replace with translated copy
    from werkzeug.datastructures import ImmutableMultiDict
    original = dict(request.form)
    if not original:
        return

    texts_to_translate = []
    keys = []
    for key in _INPUT_TEXT_FIELDS:
        val = original.get(key)
        if isinstance(val, str) and val.strip() and not _HAS_CHINESE.search(val):
            texts_to_translate.append(val)
            keys.append(key)

    if not texts_to_translate:
        return

    translated = translate_texts(texts_to_translate, target_lang='ZH', source_lang='EN')
    for key, new_val in zip(keys, translated):
        original[key] = new_val

    # Instance __dict__ takes precedence over Werkzeug's descriptor
    request.__dict__['form'] = ImmutableMultiDict(original)


def _translate_dict_fields(body):
    """Translate known text fields in a dict (JSON body) from EN to ZH in place."""
    texts_to_translate = []
    keys = []
    for key in _INPUT_TEXT_FIELDS:
        val = body.get(key)
        if isinstance(val, str) and val.strip() and not _HAS_CHINESE.search(val):
            texts_to_translate.append(val)
            keys.append(key)

    if not texts_to_translate:
        return

    translated = translate_texts(texts_to_translate, target_lang='ZH', source_lang='EN')
    for key, new_val in zip(keys, translated):
        body[key] = new_val


# ── Outbound: ZH→EN ─────────────────────────────────────────────

def _collect_chinese_strings(obj, path='', collected=None, key_name=None):
    """
    Recursively walk a JSON-serializable object and collect
    (path, value) pairs for every string containing Chinese.
    """
    if collected is None:
        collected = []

    if isinstance(obj, str):
        if key_name and key_name in _SKIP_RESPONSE_KEYS:
            return collected
        if _HAS_CHINESE.search(obj) and len(obj.strip()) >= 2:
            collected.append((path, obj))
    elif isinstance(obj, dict):
        for k, v in obj.items():
            _collect_chinese_strings(v, f'{path}.{k}', collected, key_name=k)
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            _collect_chinese_strings(v, f'{path}[{i}]', collected, key_name=key_name)

    return collected


def _set_by_path(obj, path, value):
    """Set a value in a nested dict/list by dotted path like '.data.message'."""
    parts = []
    for segment in path.lstrip('.').split('.'):
        # Handle list indices like 'items[2]'
        if '[' in segment:
            key, rest = segment.split('[', 1)
            if key:
                parts.append(key)
            parts.append(int(rest.rstrip(']')))
        else:
            parts.append(segment)

    current = obj
    for part in parts[:-1]:
        if isinstance(part, int):
            current = current[part]
        else:
            current = current[part]

    last = parts[-1]
    if isinstance(last, int):
        current[last] = value
    else:
        current[last] = value


def _translate_response_body(response):
    """Translate Chinese strings in JSON response body to English."""
    content_type = response.content_type or ''
    if 'json' not in content_type:
        return response

    try:
        data = response.get_json(silent=True)
    except Exception:
        return response

    if data is None:
        return response

    collected = _collect_chinese_strings(data)
    if not collected:
        return response

    # Batch: respect the character limit
    paths = [c[0] for c in collected]
    texts = [c[1] for c in collected]

    # Split into batches if total chars exceed limit
    batches = []
    current_batch_paths = []
    current_batch_texts = []
    current_chars = 0

    for p, t in zip(paths, texts):
        char_count = len(t)
        if current_chars + char_count > _MAX_BATCH_CHARS and current_batch_texts:
            batches.append((current_batch_paths, current_batch_texts))
            current_batch_paths = []
            current_batch_texts = []
            current_chars = 0
        current_batch_paths.append(p)
        current_batch_texts.append(t)
        current_chars += char_count

    if current_batch_texts:
        batches.append((current_batch_paths, current_batch_texts))

    # Translate each batch
    all_translated_paths = []
    all_translated_texts = []
    for batch_paths, batch_texts in batches:
        translated = translate_texts(batch_texts, target_lang='EN', source_lang='ZH')
        all_translated_paths.extend(batch_paths)
        all_translated_texts.extend(translated)

    # Apply translations back
    for path, translated_text in zip(all_translated_paths, all_translated_texts):
        try:
            _set_by_path(data, path, translated_text)
        except (KeyError, IndexError, TypeError):
            pass  # Path no longer valid, skip

    response.set_data(json.dumps(data, ensure_ascii=False))
    return response


# ── Registration ─────────────────────────────────────────────────

def register_translation_middleware(app):
    """Register the translation before/after request hooks on the Flask app."""

    @app.before_request
    def translation_before():
        g._translate_to_english = _wants_english()
        if g._translate_to_english:
            _translate_request_body()

    @app.after_request
    def translation_after(response):
        if not getattr(g, '_translate_to_english', False):
            return response
        return _translate_response_body(response)
