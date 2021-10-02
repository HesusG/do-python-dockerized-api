FROM python:3.8-slim

RUN apt-get update
RUN apt-get install -y build-essential python3-dev python3-pip python3-venv python3-six

ENV FLASK_APP=api.py
ENV FLASK_DEBUG=1
ENV FLASK_ENV=development

WORKDIR /application

ADD ./requirements.txt /application

RUN python3 --version
RUN python3 -c "import platform; print(platform.architecture()[0])"
RUN pip install --upgrade pip
RUN pip --version

RUN pip install -r requirements.txt

EXPOSE 8000
