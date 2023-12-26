#!/bin/bash

while ! nc -z ${DOCKER_DB_HOST} ${POSTGRES_PORT}; do
  echo "Waiting for PostgreSQL..."
  sleep 0.1
done
echo "PostgreSQL started"

cd src/test_django/

python3 manage.py collectstatic --noinput

python3 manage.py migrate 

python3 manage.py createsuperuser --noinput

gunicorn -b ${APP_HOST}:${APP_PORT} config.wsgi:application
