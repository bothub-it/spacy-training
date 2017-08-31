# encoding: utf8
from __future__ import unicode_literals

STOP_WORDS = set("""
{%- for row in data %}
{{ row[0] }}
{%- endfor %}
""".split())
