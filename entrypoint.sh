python -m app $LANG_ISO $LANG_NAME $TRANING_TYPE

python -m spacy package ../models/$LANG_ISO/ output/

cd output/${LANG_ISO}_vectors_web_lg-1.0.0
python setup.py sdist
