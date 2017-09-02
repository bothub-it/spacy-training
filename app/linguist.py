import os.path
import csv

from .conllu_to_json_converter import convert
from .train import train
from jinja2 import Template
from pathlib import Path

def run(_dir, _code, _name):
    output(_dir, 'stop_words.py', read_csv(_dir, _code, 'stop_words.csv'))
    output(_dir, 'lemmatizer.py', read_csv(_dir, _code, 'lemmas.csv'))
    output(_dir, 'norm_exceptions.py', read_csv(_dir, _code, 'same_spelling.csv'))
    output(_dir, 'tokenizer_exceptions.py', read_csv(_dir, _code, 'contracted_words.csv'))
    output(_dir, 'morph_rules.py', read_csv(_dir, _code, 'personal_pronouns.csv'))
    output(_dir, '__init__.py', [_name, _code])
    convert_ud(_dir, _code)
    
def read_csv(_dir, _code, filename):
    result = []
    try: 
        with open(os.path.join(_dir, 'input', _code, filename)) as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                stripped_row = list(map(str.strip, row))
                result.append(stripped_row)
    except:
        result = None
    return result

def output(_dir, filename, data):
    if (data is None):
        return
    write_template(_dir, filename, render_template(_dir, filename, data))

def render_template(_dir, filename, data):
    with open(os.path.join(_dir, 'templates', filename)) as f:
        tmpl = Template(f.read())
        return tmpl.render(data = data)

def write_template(_dir, filename, string):
        with open(os.path.join(_dir, 'output', filename), "w") as f:
            f.write(string)

def convert_ud(_dir, _code):
    output_path = os.path.join(_dir, 'output')
    input_path = os.path.join(_dir, 'input', _code, 'ud_train.conllu')
    convert(Path(input_path), Path(output_path))
    input_path = os.path.join(_dir, 'input', _code, 'ud_dev.conllu')
    convert(Path(input_path), Path(output_path))