import json

import os.path
import csv

from .conllu_to_json_converter import convert
from .train import train_run, train_fast_text
from jinja2 import Template
from pathlib import Path
from distutils.dir_util import copy_tree

TYPE_UNIVERSAL_DEPS = 'ud'
TYPE_FAST_TEXT = 'fasttext'

DEFAULT_FAST_TEXT_NAME = 'vectors_web_{0}'
MODEL_NAME_FORMAT = '{0}_{1}-1.0.0'


def run(_dir, _code, _name, _type, _overwrite, _size, _prune_vectors, _download_source):
    if _overwrite:
        output(_dir, _code, 'stop_words.py',
               read_csv(_dir, _code, 'stop_words.csv'))
        output(_dir, _code, 'lemmatizer.py', read_csv(_dir, _code, 'lemmas.csv'))
        output(_dir, _code, 'norm_exceptions.py', read_csv(
            _dir, _code, 'same_spelling.csv'))
        output(_dir, _code, 'tokenizer_exceptions.py', read_csv(
            _dir, _code, 'contracted_words.csv'))
        output(_dir, _code, 'morph_rules.py', read_csv(
            _dir, _code, 'personal_pronouns.csv'))
        output(_dir, _code, '__init__.py', [_name, _code])

    if _type == TYPE_UNIVERSAL_DEPS:
        convert_ud(_dir, _code)
        train_run(_dir, _code)
    elif _type == TYPE_FAST_TEXT:
        train_fast_text(_dir, _code, _download_source, _prune_vectors)

    add_language(_dir, _code, _name, _type, _size)


def add_language(_dir, _code, _name, _type, _size):
    model_path = os.path.join(_dir, '..', 'models', _code)

    data_path = os.path.join(_dir, '..', 'spaCy', 'spacy', 'data', _code)
    if not os.path.exists(data_path):
        os.makedirs(data_path)

    string = render_template(_dir, 'language__init__.py', {})

    with open(os.path.join(data_path, '__init__.py'), "w") as f:
        f.write(string)

    model_prefix = DEFAULT_FAST_TEXT_NAME.format(_size)
    data = metadata(_code, _name, model_prefix)
    subdir_name = MODEL_NAME_FORMAT.format(_code, model_prefix)
    # copy subdirectory
    if _type == TYPE_UNIVERSAL_DEPS:
        copy_tree(os.path.join(model_path, 'model4'),
                  os.path.join(data_path, subdir_name))

        string = render_template(_dir, 'meta.json', data)
        with open(os.path.join(data_path, 'meta.json'), "w") as f:
            f.write(string)
        with open(os.path.join(data_path, subdir_name, 'meta.json'), "w") as f:
            f.write(string)
    else:
        with open(os.path.join(model_path, 'meta.json'), 'r', encoding='utf-8') as outfile:
            meta = json.load(outfile)
            meta.update(data)

        with open(os.path.join(model_path, 'meta.json'), 'w') as outfile:
            outfile.truncate(0)
            json.dump(meta, outfile, ensure_ascii=False, indent=2)

        copy_tree(model_path, os.path.join(data_path, subdir_name))


def metadata(_code, _name, _model_name):
    # copy metadata
    data = {
        'lang': _code,
        'name': _model_name,
        'version': '1.0.0',
        'description': '{0} model generated from fastText vectors'.format(_name),
        'author': 'Bothub',
        'email': 'bothub@ilhasoft.com.br',
        'url': 'https://bothub.it',
        'license': 'MIT'
    }
    return data


def read_csv(_dir, _code, filename):
    result = []
    try:
        with open(os.path.join(_dir, 'input', _code, filename)) as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                stripped_row = list(map(str.strip, row))
                result.append(stripped_row)
    except Exception as e:
        print("Could not read csv %s, [ERROR: %s]" % (filename, e.args))
        pass
    return result


def output(_dir, _code, filename, data):
    if data is None:
        return
    write_template(_dir, _code, filename,
                   render_template(_dir, filename, data))


def render_template(_dir, filename, data):
    with open(os.path.join(_dir, 'templates', filename)) as f:
        tmpl = Template(f.read())
        return tmpl.render(data=data)


def write_template(_dir, _code, filename, string):
    output_path = os.path.join(_dir, '..', 'spaCy', 'spacy', 'lang', _code)
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    with open(os.path.join(output_path, filename), "w") as f:
        f.write(string)


def convert_ud(_dir, _code):
    output_path = os.path.join(_dir, 'output')
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    input_path = os.path.join(_dir, 'input', _code, 'ud_train.conllu')
    convert(Path(input_path), Path(output_path))
    input_path = os.path.join(_dir, 'input', _code, 'ud_dev.conllu')
    convert(Path(input_path), Path(output_path))
