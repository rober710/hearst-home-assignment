FROM python:3.6.6-stretch

# In developement, the repository is mounted inside the container.
ENV MOUNT_POINT=/srv/django-server

COPY docker/developement/app/docker-entrypoint.sh /usr/bin/docker-entrypoint.sh
COPY docker/developement/app/check_user.sh /usr/bin/check_user.sh

RUN useradd -m -c 'Django application' --shell /bin/bash django \
    && dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')"; \
    GOSU_VERSION=1.10; \
    wget -O /usr/bin/gosu "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch" \
    && chmod +x /usr/bin/gosu \
    && chmod +x /usr/bin/docker-entrypoint.sh \
    && chmod +x /usr/bin/check_user.sh

EXPOSE 8000
ENTRYPOINT [ "/usr/bin/docker-entrypoint.sh" ]
