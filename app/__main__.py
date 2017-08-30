import os.path
import conllu_to_json_converter
import stop_words_generator
import train
from pathlib import Path

current_dir = os.path.dirname(__file__)

def run():
    stop_words_generator.read_stop_words()
    stop_words_generator.write_stop_words()

    convert_ud()
    #train.run()
    
def convert_ud():
    output_path = os.path.join(current_dir, '..', 'output')
    input_path = os.path.join(current_dir, '..', 'input', 'da', 'ud_train.conllu')
    conllu_to_json_converter.convert(Path(input_path), Path(output_path))
    input_path = os.path.join(current_dir, '..', 'input', 'da', 'ud_dev.conllu')
    conllu_to_json_converter.convert(Path(input_path), Path(output_path))

run()

print("done")
