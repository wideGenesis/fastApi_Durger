#!/bin/bash

gunicorn app:app --bind=0.0.0.0:8000  --timeout 800 --workers 1 -k uvicorn.workers.UvicornWorker --access-logfile '-' --error-logfile '-'
#uvicorn app:app --host 0.0.0.0 --port 8000 --workers 1 --access-log
