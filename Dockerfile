# pull official base image
FROM python:3.10.1-slim-buster

# set working directory
WORKDIR /app
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update \
  && apt-get -y install netcat gcc \
  && apt-get clean

# install python dependencies
RUN pip install --upgrade pip
COPY ./requierements/base.txt .
RUN pip install -r base.txt

# add app
COPY . .
