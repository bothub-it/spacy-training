# coding: utf8
from __future__ import unicode_literals

from ...symbols import LEMMA
from ...deprecated import PRON_LEMMA

MORPH_RULES = {
    "PRP": {
        "jeg": {LEMMA: PRON_LEMMA, "PronType": "Prs"},
        "mig": {LEMMA: PRON_LEMMA, "PronType": "Prs"},
        "du": {LEMMA: PRON_LEMMA, "PronType": "Prs"},
        "ham": {LEMMA: PRON_LEMMA, "PronType": "Prs"},
        "han": {LEMMA: PRON_LEMMA, "PronType": "Prs"},
        "hende": {LEMMA: PRON_LEMMA, "PronType": "Prs"}
    }
}