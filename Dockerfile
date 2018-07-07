FROM python:3.6

ENV SPACY_HOME /usr/src/spaCy
ENV APP_HOME /usr/src/app

WORKDIR ${APP_HOME}

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN git clone --branch v2.0.12 https://github.com/explosion/spaCy.git $SPACY_HOME
RUN pip install -e $SPACY_HOME

COPY . .

RUN chmod +x entrypoint.sh
ENTRYPOINT $APP_HOME/entrypoint.sh