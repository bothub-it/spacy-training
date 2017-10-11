from app.conllu_to_json_converter import *
import os.path

from pathlib import Path

current_dir = os.path.dirname(__file__)

expected = [
  {
    "id":0,
    "paragraphs":[
      {
        "sentences":[
          {
            "tokens":[
              {
                "orth":"Hvor",
                "tag":"ADV",
                "head":1,
                "dep":"advmod"
              },
              {
                "orth":"kommer",
                "tag":"VERB",
                "head":0,
                "dep":"ROOT"
              },
              {
                "orth":"julemanden",
                "tag":"NOUN",
                "head":-1,
                "dep":"nsubj"
              },
              {
                "orth":"fra",
                "tag":"ADP",
                "head":-3,
                "dep":"case"
              },
              {
                "orth":"?",
                "tag":"PUNCT",
                "head":-3,
                "dep":"punct"
              }
            ]
          }
        ]
      }
    ]
  }
]

def test_answer():
    input_path = os.path.join(current_dir, 'fixtures', 'input', 'da', 'ud.conllu')
    result = render(Path(input_path), n_sents=1)
    assert result == expected
