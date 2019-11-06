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

Docker
----------
Using docker is the easiest way of processing the models. You can just go into docker directory and build the image:
```bash
docker-compose build --build-arg GITHUB_SSH_PRIVATE_KEY="$(cat ~/.ssh/id_rsa)"
```
`GITHUB_SSH_PRIVATE_KEY` is the key for your Github Account, that needs to have write permission on any fork from spaCy [repository](https://github.com/explosion/spaCy.git).

After that, you can create a `.env` file inside the same directory with the following environment variables:
```
LANG_ISO: Language code for the current input (e.g. pt, en, id);
LANG_NAME: Language name for the current input (e.g. BrazilianPortuguese, English, Indonesian);
LANG_SIZE: Model size according to the vectors count. Available choices: sm, md or lg;
DOWNLOAD_LANG_ISO: Language code that will be downloaded from fastText [repository](https://github.com/facebookresearch/fastText/blob/master/docs/crawl-vectors.md);
PRUNE_VECTORS: The vectors count that you want to prune (e.g. 1000);
TRANING_TYPE: Training type used for the current input. Available choices: ud or fasttext;
OVERWRITE_LANG: If needs to overwrite language features on spaCy. Available choices: True or False;
AWS_ACCESS_KEY_ID: AWS Access Key of the bucket to save the final model;
AWS_SECRET_ACCESS_KEY: AWS Secret Key of the bucket to save the final model;
GITHUB_USERNAME: Username of the Github account that will receive languages features;
GITHUB_EMAIL: Email of the Github account that will receive language features;
```
Finally, you can run the up command to start processing:
```bash
docker-compose -f docker/docker-compose.yml up
```

Testing
-------

We use pytest for testing. Run all tests with:
```bash
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
