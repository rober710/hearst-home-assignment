#!/bin/sh
# Docker entrypoint to run django for development. This one uses Django's development server.

if [ "x$MOUNT_POINT" = "x" ]; then
    echo "No mountpoint defined."
    exit 1
fi

if ! test -d $MOUNT_POINT; then
    echo "Source folders not mounted!"
    echo "Use docker compose to run this container or use the -v or --mount option of docker run to mount the repository in $MOUNT_POINT"
    exit 1
fi

/usr/bin/check_user.sh
pip install -r $MOUNT_POINT/server/requirements.txt

cd $MOUNT_POINT/server
gosu django:django python check_db_startup.py
gosu django:django python manage.py runserver 0.0.0.0:8000
