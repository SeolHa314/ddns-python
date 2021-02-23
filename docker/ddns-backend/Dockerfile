FROM python:3.9.1-alpine3.13

RUN apk add --no-cache git

RUN git clone https://github.com/SeolHa314/ddns-python
RUN apk del git
WORKDIR /ddns-python
RUN pip install -r requirements.txt

WORKDIR /ddns-python/api/backend
CMD uvicorn main:app --reload