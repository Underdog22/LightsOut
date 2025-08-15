#!/bin/sh

sleep 1.0

python manage.py makemigrations
python manage.py migrate

echo "Starting Server..."
exec "$@"