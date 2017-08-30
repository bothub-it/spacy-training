from ..app.conllu_to_json_converter import convert as run
import os.path

from pathlib import Path

current_dir = os.path.dirname(__file__)

def test_answer():
    input_path = os.path.join(current_dir, 'fixtures', 'ud.conllu')
    run(Path(input_path), Path(current_dir))
