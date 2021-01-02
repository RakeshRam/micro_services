# pull official base image
FROM python:3.7

# set environment varibles
ENV PYTHONUNBUFFERED 1

# set work directory
WORKDIR /src/api_manager

# install dependencies
COPY requirments.txt /src/api_manager/requirments.txt
RUN pip install -r requirments.txt

# copy project
COPY . /src/api_manager

# copy entrypoint.sh
COPY ./entrypoint.sh /api_demo_app/entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]