# pull official base image
FROM python:3.9.12-slim-bullseye

# set environment variables
# PYTHONFAULTHANDLER=1 Display trace if a sefault occurs.
# PIP_NO_CACHE_DIR=off Disable pip cache for smaller Docker images.
# PYTHONUNBUFFERED=1 Allow statements and log messages to immediately appear in the Knative logs
# PIP_DISABLE_PIP_VERSION_CHECK=on Ignore pip new version warning.
# PIP_DEFAULT_TIMEOUT=100 Give pip longer than the 15 second timeout.
# PYTHONDONTWRITEBYTECODE=1 - Don't write byte code during install

ENV PYTHONFAULTHANDLER=1 \
  PYTHONDONTWRITEBYTECODE=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100

# appropriate directories:
ENV HOME=/home/app
ENV APP_ROOT=$HOME/bot

# Update new packages, Get Ubuntu packages, clean cache
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        libpq-dev \
        build-essential \
        curl \
        htop  \
        mc \
        nano \
    # Cleaning cache: \
    && pip install --upgrade pip \
    && pip install --no-cache-dir --no-cache --no-deps -r requirements.txt \
    && apt-get -qq clean \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*


RUN mkdir -p $HOME \
    && mkdir -p $APP_ROOT \
    && mkdir -p $HOME/.cache/mc

WORKDIR $APP_ROOT

COPY . $APP_ROOT

EXPOSE 8000 3978

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
