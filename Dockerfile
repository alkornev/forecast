FROM python:3.8.5-alpine

RUN adduser -D forecast

WORKDIR /home/forecast

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN apk add --no-cache nano gcc g++ musl-dev python3-dev libffi-dev openssl-dev cargo
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install pymysql

COPY app app
COPY migrations migrations
COPY most_populated.txt most_populated.txt
COPY forecast.py config.py boot.sh run_scheduler.sh rq_process.py ./
RUN chmod a+x boot.sh
RUN chmod a+x run_scheduler.sh


ENV FLASK_APP forecast.py

RUN chown -R forecast:forecast ./
USER forecast

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
