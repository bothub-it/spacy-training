import os.path
import csv

from .conllu_to_json_converter import convert
from .train import train_run
from jinja2 import Template
from pathlib import Path

from distutils.dir_util import copy_tree
from shutil import copyfile

def run(_dir, _code, _name):
    output(_dir, _code, 'stop_words.py', read_csv(_dir, _code, 'stop_words.csv'))
    output(_dir, _code, 'lemmatizer.py', read_csv(_dir, _code, 'lemmas.csv'))
    output(_dir, _code, 'norm_exceptions.py', read_csv(
        _dir, _code, 'same_spelling.csv'))
    output(_dir, _code, 'tokenizer_exceptions.py', read_csv(
        _dir, _code, 'contracted_words.csv'))
    output(_dir, _code, 'morph_rules.py', read_csv(
        _dir, _code, 'personal_pronouns.csv'))
    output(_dir, _code, '__init__.py', [_name, _code])
    convert_ud(_dir, _code)
    train_run(_dir,_code)
    add_language(_dir, _code)

def add_language(_dir, _code):
    path = os.path.join(_dir, '..', 'spaCy', 'spacy', 'data', _code)
    if not os.path.exists(path):
        os.makedirs(path)

    string = render_template(_dir, 'language__init__.py', {})

    with open(os.path.join(path, '__init__.py'), "w") as f:
        f.write(string)

    # copy subdirectory
    name = _code + "_-0.0.0"
    copy_tree(os.path.join(_dir, '..', 'models', 'model4'), os.path.join(path, name))

    # copy metadata
    copyfile(os.path.join(path, name, 'meta.json'), os.path.join(path, 'meta.json'))


def read_csv(_dir, _code, filename):
    result = []
    try:
        with open(os.path.join(_dir, 'input', _code, filename)) as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                stripped_row = list(map(str.strip, row))
                result.append(stripped_row)
    except:
        print("Could not read csv " + filename)
        pass
    return result


def output(_dir, _code, filename, data):
    if data is None:
        return
    write_template(_dir, _code, filename, render_template(_dir, filename, data))


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
    input_path = os.path.join(_dir, 'input', _code, 'ud_train.conllu')
    convert(Path(input_path), Path(output_path))
    input_path = os.path.join(_dir, 'input', _code, 'ud_dev.conllu')
    convert(Path(input_path), Path(output_path))
