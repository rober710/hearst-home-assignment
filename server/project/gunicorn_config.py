# encoding: utf-8

import multiprocessing, os

bind = '0.0.0.0:{0}'.format(os.environ.setdefault("GUNICORN_PORT", '8000'))
workers = multiprocessing.cpu_count() * 2 + 1
errorlog = os.environ.setdefault("GUNICORN_LOG", '-')
