# encoding: utf8
from __future__ import unicode_literals
from ...symbols import ORTH


_contacted_words = {}

{%- for row in data %}
_contacted_words["{{row[0]}}"] = [{%- for word in row %}{% if not loop.first %}{ORTH: "{{word}}"}{% if not loop.last %}, {% endif %}{% endif %}{%- endfor %}]
{%- endfor %}

TOKENIZER_EXCEPTIONS = dict(_contacted_words)
