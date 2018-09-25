# Hearst Home Assignment

You can start the application using docker-compose. There are two environments on which
you can test the application: development and production.

The development environment starts a Python container and mounts the current repository into the container,
so that changes made outside of the container are visible inside an vice-versa.

To start the application in development mode run the following command from the root of the repository:

```
docker-compose -f docker/development/docker-compose.yml up -d
```
This will start a postgres instance with the database ready to receive connections. A second
container running the Django development server will be started, listening on port 8080. You can check
the app is working by visiting the URL `http://localhost:8080/docs` which will present an overview of the
API available endpoints.

After the application is started, you need to get into the container and run the migrations manually,
with these commands

```
# From your shell outside of the container
docker exec -it -u django:django <container_name_or_id> /bin/bash

# Now you should be inside the container's shell. Run these commands:
cd /srv/django-server/server/
python manage.py migrate
# Now the app is ready to use!
```

## Production configuration

For the production environment, the app container starts Gunicorn to serve the application, whereas an nginx
instance serves static files to display the Swagger views. To start the app in this
mode, run this command from the root of the repository:

```
docker-compose -f docker/production/docker-compose.yml up -d
```

The app will be listening on port 8080 by default.


## How to run the tests

To run the test suites, you need to start the application in development mode. By default, the app container's
name will be `development_app_1`. Run these commands to get into the container's shell:

```
# From your shell outside the container:
docker exec -it -u django:django development_app_1 /bin/bash

# Now in the container's shell
cd /srv/django-server/server/
python manage.py test
```
