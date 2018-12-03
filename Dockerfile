FROM alpine:3.8

RUN mkdir -p /app
WORKDIR /app
ENV PORT 80

COPY . .

RUN apk add --no-cache build-base python3-dev python-dev
RUN pip3 install -r requirements.txt

EXPOSE 80

CMD python3 ./index.py
