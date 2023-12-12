FROM python:3.10-slim-buster
LABEL authors="enard"

EXPOSE 8000

WORKDIR /app

COPY webpanel .
COPY database database/

RUN apt update && apt -y install libpq-dev gcc

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:8000", "main:init_app()"]