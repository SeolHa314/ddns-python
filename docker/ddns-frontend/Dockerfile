FROM python:3.9.1-alpine3.13

WORKDIR /code

RUN apk add --no-cache git

RUN git clone https://github.com/SeolHa314/ddns-python .
RUN apk del git
RUN pip install -r requirements.txt

CMD uvicorn api.frontend.main:app