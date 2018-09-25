# Reverse proxy and assets server for production.

FROM nginx:1.15.4-alpine

# The directory here must be the same as STATIC_ROOT in Django settings.
RUN mkdir -p /srv/www/static

COPY production/nginx/nginx.conf /etc/nginx/nginx.conf
