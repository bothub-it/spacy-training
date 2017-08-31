from ..app.__main__ import *

_dir = os.path.join(os.path.dirname(__file__), 'fixtures')

_templates_dir = os.path.join(os.path.dirname(__file__), '..')

def test_render_stop_words():
    data = read_csv(_dir, 'stop_words.csv')
    result = render_template(_templates_dir, 'stop_words.py', data)
    expected = '''
# encoding: utf8
from __future__ import unicode_literals

STOP_WORDS = set("""
ad
af
""".split())
'''.strip()
    assert result == expected

def test_render_lemmatizer():
    data = read_csv(_dir, 'lemmas.csv')
    result = render_template(_templates_dir, 'lemmatizer.py', data)
    expected = '''
# coding: utf8
from __future__ import unicode_literals

LOOKUP = {
    "var": "er",
    "arbejdede": "arbejde"
}
'''.strip()
    assert result == expected

def test_render_morph_rules():
    data = read_csv(_dir, 'personal_pronouns.csv')
    result = render_template(_templates_dir, 'morph_rules.py', data)
    expected = '''
# coding: utf8
from __future__ import unicode_literals

from ...symbols import LEMMA
from ...deprecated import PRON_LEMMA

MORPH_RULES = {
    "PRP": {
        "jeg": {LEMMA: PRON_LEMMA, "PronType": "Prs"},
        "mig": {LEMMA: PRON_LEMMA, "PronType": "Prs"},
        "du": {LEMMA: PRON_LEMMA, "PronType": "Prs"}
    }
}
'''.strip()
    assert result == expected

def test_render_norm_exceptions():
    data = read_csv(_dir, 'same_spelling.csv')
    result = render_template(_templates_dir, 'norm_exceptions.py', data)
    expected = '''
# coding: utf8
from __future__ import unicode_literals

_exc = {
    "mayonnaise": "majonæse"
}

NORM_EXCEPTIONS = {}

for string, norm in _exc.items():
    NORM_EXCEPTIONS[string] = norm
    NORM_EXCEPTIONS[string.title()] = norm
'''.strip()
    assert result == expected

def test_render_tokenizer_exceptions():
    data = read_csv(_dir, 'contracted_words.csv')
    result = render_template(_templates_dir, 'tokenizer_exceptions.py', data)
    expected = '''
# encoding: utf8
from __future__ import unicode_literals
from ...symbols import ORTH

_contacted_words = {}
_contacted_words["imorgen"] = [{ORTH: "i"}, {ORTH: "morgen"}]
_contacted_words["iovermorgen"] = [{ORTH: "i"}, {ORTH: "over"}, {ORTH: "morgen"}]

TOKENIZER_EXCEPTIONS = dict(_contacted_words)
'''.strip()
    assert result == expected
