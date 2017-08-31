# coding: utf8
from __future__ import unicode_literals

_exc = {
{%- for row in data %}
    "{{ row[0] }}": "{{ row[1] }}"{% if not loop.last %},{% endif %}
{%- endfor %}
}

NORM_EXCEPTIONS = {}

for string, norm in _exc.items():
    NORM_EXCEPTIONS[string] = norm
    NORM_EXCEPTIONS[string.title()] = norm
