# coding: utf8
from __future__ import unicode_literals
import ujson

ALLOWED_TAGS = set("""
ADJ
ADP
PUNCT
ADV
AUX
SYM
INTJ
CCONJ
X
NOUN
DET
PROPN
NUM
VERB
PART
PRON
SCONJ
""".split())


def convert(input_path, output_path, n_sents=10, use_morphology=False):
    docs = render(input_path, n_sents=10, use_morphology=False)
    write(input_path, output_path, docs)


def write(input_path, output_path, docs):
    output_filename = input_path.parts[-1].replace(".conllu", ".json")
    output_file = output_path / output_filename

    with output_file.open('w', encoding='utf-8') as f:
        f.write(ujson.dumps(docs, indent=2, escape_forward_slashes=False))


def render(input_path, n_sents=10, use_morphology=False):
    docs = []
    sentences = []
    conll_tuples = __read_conllx(input_path, use_morphology=use_morphology)

    for i, (raw_text, tokens) in enumerate(conll_tuples):
        sentence, brackets = tokens[0]
        sentences.append(__generate_sentence(sentence))
        if len(sentences) % n_sents == 0:
            doc = __create_doc(sentences, i)
            docs.append(doc)
            sentences = []
    return docs


def __read_conllx(input_path, use_morphology=False, n=0):
    text = input_path.open('r', encoding='utf-8').read()
    i = 0
    for sent in text.strip().split('\n\n'):
        lines = sent.strip().split('\n')
        if lines:
            while lines[0].startswith('#'):
                lines.pop(0)
            tokens = []
            for line in lines:

                parts = line.split('\t')
                id_, word, lemma, tag, _unused, morph, head, dep, _1, _2 = parts
                if '-' in id_ or '.' in id_:
                    continue
                try:
                    id_ = int(id_) - 1
                    head = (int(head) - 1) if head != '0' else id_
                    dep = 'ROOT' if dep == 'root' else dep

                    if tag not in ALLOWED_TAGS:
                        raise Exception("Tag not allowed: " + tag)

                    tokens.append((id_, word, tag, head, dep, 'O'))
                except Exception as e:
                    print("Line: %s, [ERROR: %s]" % (line, e.args))
                    raise
            tuples = [list(t) for t in zip(*tokens)]
            yield (None, [[tuples, []]])
            i += 1
            if 1 <= n <= i:
                break


def __generate_sentence(sent):
    (id_, word, tag, head, dep, _) = sent
    tokens = []
    for i, id in enumerate(id_):
        tokens.append({
                "orth": word[i],
                "tag": tag[i],
                "head": head[i] - id,
                "dep": dep[i],
        })
    return {
        "tokens": tokens
    }


def __create_doc(sentences, id):
    return {
        "id": id,
        "paragraphs": [{"sentences": sentences}]
    }
