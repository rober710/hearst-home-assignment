FROM python:3.6.6-stretch

ARG SERVER_DIR=/srv/django-server/server
ENV SERVER_DIR=${SERVER_DIR}

RUN mkdir -p ${SERVER_DIR}

COPY docker/production/app/docker-entrypoint.sh /usr/bin/docker-entrypoint.sh
COPY server ${SERVER_DIR}/


RUN useradd -m -c 'Django application' --shell /bin/bash django \
    && dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')"; \
    GOSU_VERSION=1.10; \
    wget -O /usr/bin/gosu "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch" \
    && chmod +x /usr/bin/gosu \
    && chmod +x /usr/bin/docker-entrypoint.sh

EXPOSE 8000
ENTRYPOINT [ "/usr/bin/docker-entrypoint.sh" ]
