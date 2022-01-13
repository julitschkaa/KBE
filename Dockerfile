# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
SHELL ["/bin/bash", "-c"]
RUN pip install poetry

RUN poetry --version

WORKDIR /code

#COPY static static
#COPY templates templates
COPY poetry.lock pyproject.toml /code/

RUN poetry install

COPY . /code/

RUN source `poetry env info --path`/bin/activate
