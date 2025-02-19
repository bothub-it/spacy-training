export MODEL_NAME=${LANG_ISO}_vectors_web_${LANG_SIZE}-1.0.0

python -m app $LANG_ISO $LANG_NAME $TRANING_TYPE $OVERWRITE_LANG $LANG_SIZE $PRUNE_VECTORS $DOWNLOAD_SOURCE

mkdir output/
python -m spacy package ../models/$LANG_ISO/ output/

cd output/$MODEL_NAME
python setup.py sdist

aws s3 cp dist/${MODEL_NAME}.tar.gz s3://bothub-models/spacy/${MODEL_NAME}.tar.gz

if [ -z $OVERWRITE_LANG ] || [ $OVERWRITE_LANG != 'False' ]
then
    cd $SPACY_HOME

    git add .
    git -c user.name="$GITHUB_USERNAME" -c user.email="$GITHUB_EMAIL" commit -m "Add ${LANG_NAME} language files"

    git remote set-url origin git+ssh://git@github.com/ilhasoft/spaCy.git

    ssh-keyscan github.com >> /root/.ssh/known_hosts

    git -c user.name="$GITHUB_USERNAME" -c user.email="$GITHUB_EMAIL" pull origin feature/processing --no-edit
    git push origin feature/processing
fi

