FROM python:3.11-slim

COPY . /app
WORKDIR /app

RUN pip install poetry
RUN poetry config virtualenvs.in-project true
RUN poetry install --no-root

CMD poe prod
