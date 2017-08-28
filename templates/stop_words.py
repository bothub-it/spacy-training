# encoding: utf8
from __future__ import unicode_literals

STOP_WORDS = set("""
{%- for stop_word in stop_words %}
{{ stop_word }}
{%- endfor %}
""".split())
