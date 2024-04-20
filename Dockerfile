FROM python:3.12-slim

EXPOSE 8000

WORKDIR /code

RUN pip install --upgrade pip
RUN pip install poetry

COPY pyproject.toml /code

RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi --with dev

COPY . /code

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
