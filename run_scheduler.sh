#!/bin/sh
source venv/bin/activate
export FLASK_APP=./app/tasks.py
exec rq empty forecast -u $REDIS_URL &
exec rq worker forecast -u $REDIS_URL &
exec flask run
