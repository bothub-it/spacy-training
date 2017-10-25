# coding: utf8
from __future__ import unicode_literals

from .tokenizer_exceptions import TOKENIZER_EXCEPTIONS
from .stop_words import STOP_WORDS
from .norm_exceptions import NORM_EXCEPTIONS
from .morph_rules import MORPH_RULES
from .lemmatizer import LOOKUP

from ..tokenizer_exceptions import BASE_EXCEPTIONS
from ..norm_exceptions import BASE_NORMS
from ...language import Language
from ...lemmatizerlookup import Lemmatizer
from ...attrs import LANG, NORM
from ...util import update_exc, add_lookups


class {{ data[0] }}Defaults(Language.Defaults):
    lex_attr_getters = dict(Language.Defaults.lex_attr_getters)
    lex_attr_getters[LANG] = lambda text: '{{ data[1] }}'
    lex_attr_getters[NORM] = add_lookups(Language.Defaults.lex_attr_getters[NORM], BASE_NORMS)

    tokenizer_exceptions = update_exc(BASE_EXCEPTIONS, TOKENIZER_EXCEPTIONS)
    stop_words = set(STOP_WORDS)

    @classmethod
    def create_lemmatizer(cls, nlp=None):
        return Lemmatizer(LOOKUP)


class {{ data[0] }}(Language):
    lang = '{{ data[1] }}'
    Defaults = {{data[0]}}Defaults

__all__ = ['{{data[0]}}']
