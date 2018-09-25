# Build file to start a PostgreSQL instance for the development app. This container should be started first.

FROM postgres:10.5-alpine

ENV POSTGRES_INITDB_ARGS="--encoding=UTF8 --locale=C"
ENV POSTGRES_PASSWORD="postgres"

COPY  docker/develoement/db/setup_db.sql /docker-entrypoint-initdb.d/
