FROM python:3.7

ENV APP_HOME /app
ENV SPACY_LANG_MODELS_HOME /spacy-lang-models
ENV SPACY_LANG_PATH /usr/local/lib/python3.7/site-packages/spacy/lang
ARG GITHUB_SSH_PRIVATE_KEY

WORKDIR ${APP_HOME}

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN git clone --depth=1 https://github.com/Ilhasoft/spacy-lang-models.git ${SPACY_LANG_MODELS_HOME}
RUN cp -r ${SPACY_LANG_MODELS_HOME}/pt_br/ ${SPACY_LANG_PATH} && \
    cp -r ${SPACY_LANG_MODELS_HOME}/ha/ ${SPACY_LANG_PATH} && \
    cp -r ${SPACY_LANG_MODELS_HOME}/mn/ ${SPACY_LANG_PATH}

COPY . .

RUN echo $TRAINING_TYPE

RUN chmod +x docker/entrypoint.sh
ENTRYPOINT $APP_HOME/docker/entrypoint.sh
