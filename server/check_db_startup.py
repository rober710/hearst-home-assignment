# encoding: utf-8

"""
Checks whether the database is up and ready to accept connections. If not, waits until it is ready for a maximum of
10 seconds. This script is used during Docker initialization so the server starts after the database
is ready.
"""

import os, time


os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'project.settings')

if __name__ == '__main__':
    print("Checking database connection...")

    # Bootstrap Django.
    import django
    django.setup()

    # Wait until database becomes ready
    from django.db import connection, OperationalError

    counter = 0
    while True:
        counter += 1
        try:
            with connection.cursor():
                break
        except OperationalError:
            if counter <= 10:
                print("Database not ready yet. Retrying to connect...")
                time.sleep(1)
            else:
                raise
