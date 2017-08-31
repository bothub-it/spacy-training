# coding: utf8
from __future__ import unicode_literals

LOOKUP = {
{%- for row in data %}
    "{{ row[0] }}": "{{ row[1] }}"{% if not loop.last %},{% endif %}
{%- endfor %}
}
