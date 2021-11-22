# Normal dockerfile to run fastapi application

FROM python:3.8

COPY ./requirements.txt ./requirements.txt

RUN pip install -r ./requirements.txt

COPY ./api ./api

ENTRYPOINT uvicorn api.main:app --host 0.0.0.0 --port 5000