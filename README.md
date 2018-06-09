Linguist
========
Tool used to create language files for spaCy.

Installation
----------
Install dependencies
```
% virtualenv env
% source env/bin/activate
% pip install -r requirements.txt
```

Clone spaCy and install in the virtualenv
```
% cd ..
% git clone https://github.com/explosion/spaCy.git spacy
% cd spacy
% pip install -e .
```

How to use
----------
Once spaCy 2.0 is configured at the root directory as spacy-training, and you provided the language requirements files, run the following command line inside spacy-training project:
```
% python -m app pt_br "Brazilian Portuguese"
```

Testing
-------

We use pytest for testing. Run all tests with:
```
python3 -m pytest
```

Universal dependencies
----------------------
For each language, universal dependency files must be provided. (see http://universaldependencies.org/)

The files (with .conllu extension) should be put in the input folder for the target language.

For each language, file containing development data and training data must be provided. E.g. for Danish:

`linguist/input/da/ud_dev.conllu`

`linguist/input/da/ud_train.conllu`

lemmas.csv
---------------------

Furthermore a list of "lemmas" for the particular language should be provided.

A lemma is the canonical formof a set of a word.

(See https://en.wikipedia.org/wiki/Lemma_(morphology))

The lemmas must be included in a .csv file named lemmas.csv. E.g. for Danish:

linguist/input/da/lemmas.csv

The first column in lemmas.csv must contain the original word, and the second column must contain the lemma. E.g.:

```
-------|-------
worked | work
-------|-------
men    | man
-------|-------
...
```

Besides from the universal dependencies and the lemmas, a number of optional files can be specified:

contracted_words.csv
--------------------
Should contain words that have been contracted into a single word.
The first column must contain the contracted form, and the subsequent columns must contain each contracted word. E.g.:

```
-------|-------|-------
i'm    | i     | am
-------|-------|-------
we'll  | we    | will
-------|-------|-------
...
```

personal_pronouns.csv
---------------------
Should contain a single column with all the personal pronouns of the language. E.g.:
(See https://en.wikipedia.org/wiki/Personal_pronoun)

```
i
me
you
he
she
it
...
```

same_spelling.csv
-----------------
Should contain two columns of words that can be spelled in the same way.
The file should contain exactly two columns, E.g.:

```
-------|---------
color  | colour
-------|---------
cos    | because
-------|---------
...
```

stop_words.csv
--------------
Should contain a single column with common words that carry little semantic meaning. E.g.:
(See https://en.wikipedia.org/wiki/Stop_words)
```
a
about
after
so
that
...
```
