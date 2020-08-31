# dockerfile for recipe app
FROM python:3.7-alpine

# who maintains
MAINTAINER Borja 

# tell python to not buffer outputs, just print them
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

# install file
RUN pip install -r /requirements.txt

# move to the target folder and copy app info
RUN mkdir /app
WORKDIR /app
COPY ./app /app

# create user
RUN adduser -D user

# switch to our user created
USER user