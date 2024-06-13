FROM python:3.9.19

ENV FLASK_APP=app

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt