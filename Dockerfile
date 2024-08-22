FROM python:3.12-alpine

WORKDIR /app



RUN pip install poetry

COPY . /app

RUN poetry config virtualenvs.create false && poetry update



CMD ["poetry", "run", "python", "backend/manage.py", "runserver","0.0.0.0:8000"]