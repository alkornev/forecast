FROM python:3.8.5-alpine

RUN adduser -D forecast

WORKDIR /home/forecast

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN apk add gcc g++ musl-dev python3-dev libffi-dev openssl-dev cargo
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install pymysql

COPY app app
COPY migrations migrations
COPY forecast.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP forecast.py

RUN chown -R forecast:forecast ./
USER forecast

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
