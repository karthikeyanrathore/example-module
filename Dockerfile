FROM python:3.12-slim as base
LABEL author="<karthikerathore@gmail.com>"

WORKDIR /home

ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential gcc libncursesw5-dev openssl netcat-traditional \
    libssl-dev libsqlite3-dev tk-dev libgdbm-dev \
    libc6-dev libbz2-dev libffi-dev python3-dev python3-pip \
    libxml2-dev libxslt1-dev zlib1g zlib1g-dev python3-lxml \
    && rm -rf /var/lib/apt/lists/*


COPY ./requirements.docker.txt  /requirements.docker.txt
RUN pip3 install --upgrade pip
RUN pip3 install -r /requirements.docker.txt

COPY ./apps /home/apps/
COPY ./wait-for.sh /home/

RUN mkdir scripts/
COPY scripts/ /home/scripts

# CMD sh ./wait-for.sh products-db:27017 -- echo "mongoDB is up!" &&  while true; do foo; sleep 2; done
CMD sh ./wait-for.sh products-db:27017 -- echo "mongoDB is up!" && python3 scripts/populate_mongodb.py &&  uvicorn scripts.wsgi:application --host 0.0.0.0 --port 9000

