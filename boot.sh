#!/bin/sh
source venv/bin/activate
exec gunicorn -b :5200 --access-logfile - --error-logfile - e6fibo:app