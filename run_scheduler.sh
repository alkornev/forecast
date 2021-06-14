#!/bin/sh
source venv/bin/activate
sleep 80
nohup rq worker forecast -u $REDIS_URL &
while true; do
  python ./rq_process.py;
  sleep 80;
done

