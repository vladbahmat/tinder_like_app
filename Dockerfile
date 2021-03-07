FROM python:3.7-alpine

ENV PYTHONBUFFERED 1
COPY ./requirments.txt /requirments.txt

RUN apk add --update --no-cache postgres-client jpeg-dev

RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev
RUN pip install -r /requirments.txt
RUN apk del .tmp-build-deps
