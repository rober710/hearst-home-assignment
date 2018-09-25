#!/bin/sh

# Docker entrypoint to run django in staging/production environments. This one starts Gunicorn to serve
# the Django application.

pip install -r $SERVER_DIR/requirements.txt

cd $SERVER_DIR
# Collect static files from swagger views as root, to make them read only to the django user.
python manage.py collectstatic
chmod -R go-wx $SERVER_DIR/staticfiles
chmod -R go+X /srv

gosu django:django python check_db_startup.py
gosu django:django python manage.py migrate
gosu django:django gunicorn -c $SERVER_DIR/project/gunicorn_config.py project.wsgi:application
