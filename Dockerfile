FROM jenkins/jenkins:latest
USER root
MAINTAINER aliaksandr_shkuratau@epam.com
COPY . /my_app
WORKDIR /my_app
RUN apt-get update && apt-get install -y python3-pip && apt-get install -y python3-venv && pip install  pytest
