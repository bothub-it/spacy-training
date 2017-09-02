# encoding: utf8
from __future__ import unicode_literals
from ...symbols import ORTH

_contacted_words = {}
_contacted_words["imorgen"] = [{ORTH: "i"}, {ORTH: "morgen"}]
_contacted_words["iovermorgen"] = [{ORTH: "i"}, {ORTH: "over"}, {ORTH: "morgen"}]

TOKENIZER_EXCEPTIONS = dict(_contacted_words)