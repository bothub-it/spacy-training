FROM python:3.6

ENV SPACY_HOME /usr/src/spaCy
ENV APP_HOME /usr/src/app

WORKDIR ${APP_HOME}

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN git clone --branch $GITHUB_BRANCH https://github.com/${GITHUB_REPOSITORY} $SPACY_HOME
RUN pip install -e $SPACY_HOME

COPY . .

COPY $GITHUB_KEY_PATH /root/.ssh
COPY $GITHUB_KEY_RSA_PATH /root/.ssh

RUN chmod +x entrypoint.sh
ENTRYPOINT $APP_HOME/entrypoint.sh