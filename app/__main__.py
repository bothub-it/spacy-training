import argparse
from .linguist import run, TYPE_UNIVERSAL_DEPS, TYPE_FAST_TEXT
import os.path

parser = argparse.ArgumentParser(description='Add a new language to spaCy.')

parser.add_argument('code', type=str, help='The language code of the target language')
parser.add_argument('name', type=str, help='The name of the target language')
parser.add_argument('type', type=str, choices=[TYPE_UNIVERSAL_DEPS, TYPE_FAST_TEXT],
                    help='The type of the model')
parser.add_argument('overwrite', type=bool, default=True, help='Should overwrite language files')

args = parser.parse_args()

run(os.path.join(os.path.dirname(__file__), '..'), args.code, args.name, args.type, args.overwrite)
