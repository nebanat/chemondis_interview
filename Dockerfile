FROM python:3.6-slim
MAINTAINER Aaron Biliyok  <abiliyok@gmail.com>

#RUN apk update && apk add build-base postgresql-dev

ENV INSTALL_PATH /api
RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
RUN pip install --editable .

CMD gunicorn -b 0.0.0.0:8000 --access-logfile - "api.app:create_app()"
