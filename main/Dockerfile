# pull official base image
FROM python:3.7

# set environment varibles
ENV PYTHONUNBUFFERED 1

# set work directory
WORKDIR /src/main

# install dependencies
COPY requirements.txt /src/main/requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . /src/main