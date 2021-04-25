FROM python:3.7-buster

WORKDIR /opt/app/

RUN apt update
RUN apt upgrade -y
RUN apt-get install python3-dev default-libmysqlclient-dev build-essential -y

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
