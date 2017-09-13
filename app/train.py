from spacy.cli import train
import os.path

current_dir = os.path.dirname(__file__)

no_entities = True
cmd = 'train'
lang = 'da'
output_dir = current_dir
train_data = current_dir + "/../output/ud_train.jsonu"
dev_data = current_dir + "/../output/ud_dev.jsonu"
n_iter = 5
n_sents = 10

# def run():
#     train(cmd, lang, output_dir, train_data, dev_data, n_iter, n_sents, no_entities=True)
