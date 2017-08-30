import os.path
from jinja2 import Template

current_dir = os.path.dirname(__file__)

stop_words = []

def read_stop_words():
    with open(os.path.join(current_dir, '..', 'input', 'da', 'stop_words.csv')) as f:
        for line in f:
            stop_words.append(line.lower().strip())

def write_stop_words():
    with open(os.path.join(current_dir, '..', 'templates','stop_words.py')) as f:
        tmpl = Template(f.read())
        result = tmpl.render(
            stop_words = stop_words
        )

        with open(os.path.join(current_dir, '..', 'output','stop_words.py'), "w") as f:
            f.write(result)

    return False

