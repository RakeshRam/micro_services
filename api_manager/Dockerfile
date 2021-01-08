# pull official base image
FROM python:3.7

# set environment varibles for logging
ENV PYTHONUNBUFFERED 1

# set work directory
WORKDIR /src/api_manager

# install dependencies
COPY requirements.txt /src/api_manager/requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . /src/api_manager