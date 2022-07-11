#
# Based on the Dockerfile from this project - https://github.com/bmaingret/coach-planner
#

ARG APP_NAME=nornir_example
ARG APP_PATH=/opt/$APP_NAME
ARG PYTHON_VERSION=3.10.1
ARG POETRY_VERSION=1.1.13

#
# Stage: staging
#
FROM python:$PYTHON_VERSION-slim as staging
ARG APP_NAME
ARG APP_PATH
ARG POETRY_VERSION

ENV \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONFAULTHANDLER=1
ENV \
    POETRY_VERSION=$POETRY_VERSION \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1

RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        curl \
        build-essential

# Install Poetry - respects $POETRY_VERSION & $POETRY_HOME
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python
ENV PATH="$POETRY_HOME/bin:$PATH"

# Import our project files
WORKDIR $APP_PATH
COPY ./poetry.lock ./pyproject.toml ./
COPY ./src/$APP_NAME ./src/$APP_NAME

#
# Stage: build
#
FROM staging as build
ARG APP_PATH

WORKDIR $APP_PATH
RUN poetry build --format wheel
RUN poetry export --format requirements.txt --output constraints.txt --without-hashes

#
# Stage: production
#
FROM python:$PYTHON_VERSION-slim as production
ARG APP_NAME
ARG APP_PATH

ENV \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONFAULTHANDLER=1

ENV \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

# Get build artifact wheel and install it respecting dependency versions
WORKDIR $APP_PATH
COPY --from=build $APP_PATH/dist/*.whl ./
COPY --from=build $APP_PATH/constraints.txt ./
RUN pip install ./$APP_NAME*.whl --constraint constraints.txt

# Entrypoint script
COPY ./docker/docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]