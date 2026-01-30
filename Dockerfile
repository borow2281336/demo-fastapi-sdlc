FROM python:3.11-slim

COPY . /app
WORKDIR /app

RUN pip install poetry
RUN poetry config virtualenvs.in-project true
RUN poetry install --no-root

CMD ["poetry","run","uvicorn","app.main:app","--host","0.0.0.0","--port","8000"]

