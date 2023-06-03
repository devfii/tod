# syntax=docker/dockerfile:1
FROM python:3.11.3-slim-buster

#set working  directory
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY app.py app.py

EXPOSE 8000

CMD python3 -m flask run --host 0.0.0.0 --port 8000

#install app

