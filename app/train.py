from spacy.cli import train, init_model
import os.path
import json

current_dir = os.path.dirname(__file__)


def measure_size(data_file):
    with open(data_file) as data_file:
        data = json.load(data_file)
        return len(data) * len(data[0]['paragraphs'][0]['sentences'])


def train_run(_dir, _code):
    models_path = os.path.join(_dir, '..', 'models')
    if not os.path.exists(models_path):
        os.makedirs(models_path)

    train_data = current_dir + "/../output/ud_train.json"
    dev_data = current_dir + "/../output/ud_dev.json"
    no_entities = True

    n_iter = 10
    n_sents = measure_size(train_data) + measure_size(dev_data) / 2

    train(_code, models_path, train_data, dev_data, n_iter, n_sents, no_entities=no_entities)


def train_fast_text(_dir, _code):
    models_path = os.path.join(_dir, '..', 'models')
    if not os.path.exists(models_path):
        os.makedirs(models_path)

    train_data = current_dir + "/../input/{0}/cc.{0}.300.vec.gz".format(_code)
    init_model(_code, models_path, train_data)
