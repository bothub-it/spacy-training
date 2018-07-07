export MODEL_NAME=${LANG_ISO}_vectors_web_lg-1.0.0

python -m app $LANG_ISO $LANG_NAME $TRANING_TYPE
python -m spacy package ../models/$LANG_ISO/ output/

cd output/$MODEL_NAME
python setup.py sdist

aws s3 cp dist/${MODEL_NAME}.tar.gz s3://bothub-models/spacy/${MODEL_NAME}.tar.gz

cd $SPACY_HOME

git add .
git commit -m "Add ${LANG_NAME} language files"
git push origin feature/processing

