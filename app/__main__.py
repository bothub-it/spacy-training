import argparse
from .linguist import run
import os.path

parser = argparse.ArgumentParser(description='Add a new language to spaCy.')

parser.add_argument(
    'code', type=str, help='The language code of the target language')
parser.add_argument('name', type=str, help='The name of the target language')

args = parser.parse_args()

run(os.path.join(os.path.dirname(__file__), '..'), args.code, args.name)
