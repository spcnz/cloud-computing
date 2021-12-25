FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
RUN pip install poetry
COPY poetry.lock pyproject.toml /code/
RUN poetry install
COPY . /code/