# Pull official base image
FROM python:3.7-alpine

# Set environment varibles for logging
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /src/api_manager

# Update For MySQL for python-alpine
RUN apk update
RUN apk add musl-dev mariadb-dev gcc

# Install dependencies
COPY requirements.txt /src/api_manager/requirements.txt
RUN pip install -r requirements.txt

# Copy project
COPY . /src/api_manager