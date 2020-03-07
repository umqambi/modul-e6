#!/bin/sh
source venv/bin/activate
memcached
exec gunicorn -b :5000 --access-logfile - --error-logfile - e6fibo:app