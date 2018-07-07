import json
from pathlib import Path

import os.path
from spacy.cli import train, init_model

from app.utils import download

current_dir = os.path.dirname(__file__)

FAST_TEXT_URL_FORMAT = 'https://s3-us-west-1.amazonaws.com/fasttext-vectors/word-vectors-v2/{0}'


def measure_size(data_file):
    with open(data_file) as data_file:
        data = json.load(data_file)
        return len(data) * len(data[0]['paragraphs'][0]['sentences'])


def train_run(_dir, _code):
    models_path = create_models_path(_code, _dir)

    train_data = current_dir + '/../output/ud_train.json'
    dev_data = current_dir + '/../output/ud_dev.json'
    no_entities = True

    n_iter = 10
    n_sents = measure_size(train_data) + measure_size(dev_data) / 2

    train(_code, models_path, train_data, dev_data, n_iter, n_sents, no_entities=no_entities)


def create_models_path(_code, _dir):
    models_path = os.path.join(_dir, '..', 'models', _code)
    if not os.path.exists(models_path):
        os.makedirs(models_path)
    return models_path


def train_fast_text(_dir, _code):
    models_path = create_models_path(_code, _dir)

    filename = 'cc.{0}.300.vec.gz'.format(_code)
    train_data = current_dir + '/../input/{0}/{1}'.format(_code, filename)

    if not os.path.exists(train_data):
        download(FAST_TEXT_URL_FORMAT.format(filename), filename, train_data)

    return init_model(_code, Path(models_path), vectors_loc=train_data)
