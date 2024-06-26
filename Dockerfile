FROM python:3.9.19

ENV FLASK_APP=app
ENV PYTHONPATH=/app:$PYTHONPATH

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN export PYTHONPATH="/app:$PYTHONPATH"

CMD ["flask", "run", "--host=0.0.0.0"]
