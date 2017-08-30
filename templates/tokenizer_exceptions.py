# encoding: utf8
from __future__ import unicode_literals

from ...symbols import ORTH, LEMMA

_exc = {}

ORTHS = set("""
{%- for orth in orths %}
{{ orth }}
{%- endfor %}
""".split())

for orth in ORTHS:
    _exc[orth] = [{ORTH: orth}]

TOKENIZER_EXCEPTIONS = dict(_exc)
