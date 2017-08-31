# coding: utf8
from __future__ import unicode_literals

from ...symbols import LEMMA
from ...deprecated import PRON_LEMMA

MORPH_RULES = {
    "PRP": {
    {%- for row in data %}
        "{{row[0]}}": {LEMMA: PRON_LEMMA, "PronType": "Prs"}{% if not loop.last %},{% endif %}
    {%- endfor %}
    }
}
