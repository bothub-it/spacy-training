from spacy.cli import train
import os.path

current_dir = os.path.dirname(__file__)


def train_run(_dir, _code):
    models_path = os.path.join(_dir, '..', 'models')
    if not os.path.exists(models_path):
        os.makedirs(models_path)

    train_data = current_dir + "/../output/ud_train.jsonu"
    dev_data = current_dir + "/../output/ud_dev.jsonu"
    no_entities = True

    n_iter = 5
    n_sents = 10

    train('train', _code, models_path, train_data,
          dev_data, n_iter, n_sents, no_entities=True)
