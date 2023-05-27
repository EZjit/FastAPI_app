# base image
FROM python:3.11.3-alpine3.18
# creator email
LABEL maintainer='weinbloodlust@gmail.com'

# set work directory
RUN mkdir trading_app
WORKDIR /trading_app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# upgrade pip package manager
RUN pip install --upgrade pip

# copy requirements in docker folder
COPY requirements.txt .

# install all dependencies and create non-root user
RUN pip install -r requirements.txt

# copy whole project to docker home directory.
COPY . .

