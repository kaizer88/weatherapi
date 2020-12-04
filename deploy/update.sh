#!/usr/bin/env bash

set -e

PROJECT_BASE_PATH='/usr/local/apps/weatherapi'

git pull
$PROJECT_BASE_PATH/env/bin/python manage.py migrate
$PROJECT_BASE_PATH/env/bin/python manage.py collectstatic --noinput
supervisorctl restart weather_api

echo "DONE! :)"
