-- Creates the user and the database for the django server.
-- This script must be run with the PostgreSQL superuser.

CREATE USER hearst WITH PASSWORD 'hearst' CREATEDB;
CREATE DATABASE hearstdb WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE='en_US.UTF-8' LC_CTYPE='en_US.UTF-8' OWNER hearst;
