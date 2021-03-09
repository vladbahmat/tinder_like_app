FROM python:3.7-alpine
ENV PYTHONBUFFERED 1
WORKDIR /tinder-like-app
COPY requirments.txt /tinder-like-app
RUN pip install -r /requirments.txt
COPY . /tinder-like-app/
