FROM alpine

MAINTAINER Aidan Harris <mail@aidanharris.io>

EXPOSE 8000

COPY . /htdocs

WORKDIR /htdocs

RUN apk update && apk add python3 git && cd /htdocs && git checkout gh-pages && apk del --purge git

CMD ["python3","-m","http.server","--bind","0.0.0.0","8000"]