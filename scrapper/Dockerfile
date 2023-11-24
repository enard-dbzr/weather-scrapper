FROM python:3.10-slim-buster
LABEL authors="enard"

WORKDIR /app

COPY . .

RUN apt update && apt -y install libpq-dev gcc

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python", "main.py"]