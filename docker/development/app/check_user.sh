#!/bin/bash -e

# Check the source folders are mounted and this script is run as root. This allows making changes inside the
# container that will be visible from the outside and vice-versa. Useful to make changes in an IDE and testing
# them inside the container! This is necessary in Linux systems, where the UID if the filesystem is
# preserved when mounting. On MacOS, the user is always root.

if [ "$UID" != "0" ]; then
    echo "This script must be run as root."
    exit 1
fi

if ! test -d $MOUNT_POINT/server ; then
    echo "Source folders not mounted!"
    echo "Use docker compose to run this container or use the -v or --mount option of docker run to mount the repository in $MOUNT_POINT"
    exit 1
fi

# Taken from https://github.com/Graham42/mapped-uid-docker/blob/master/make-tim.sh
# Checks the user of the mounted folders and recreates the same UID inside the container.
SAMPLE_FOLDER=$MOUNT_POINT/server
USERID=$(stat -c %u $SAMPLE_FOLDER)
GROUPID=$(stat -c %g $SAMPLE_FOLDER)

if ! getent group $GROUPID > /dev/null 2>&1 ; then
    groupmod -o -g $GROUPID django
fi

usermod -o -u $USERID -g $GROUPID django
chown $USERID:$GROUPID /home/django
