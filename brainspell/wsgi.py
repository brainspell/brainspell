# -*- coding: utf-8 -*-

import os, sys

PROJECT_NAME = 'brain'

WEB_ROOT = '/home/www'
VENV_ROOT = '/home/metamatik/.virtualenvs'
VENV_SP_PATH = 'lib/python2.6/site-packages'

INITIAL_PYTHONPATH = sys.path

# --- reset pythonpath
sys.path = []

# --- append the virtualenv site-packages
venv = '%s' % (PROJECT_NAME)
venv_fullpath = os.path.join(VENV_ROOT, venv, VENV_SP_PATH)
sys.path.append(venv_fullpath)

# --- append our application itself
app_fullpath = os.path.dirname(os.path.abspath(__file__))
apps_fullpath = os.path.join(app_fullpath, 'apps')
sys.path.append(app_fullpath)
sys.path.append(apps_fullpath)

# --- append the previous PYTHONPATH
for path in INITIAL_PYTHONPATH:
    sys.path.append(path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

# This application object is used by any WSGI server configured to use this
# file. This includes Django's development server, if the WSGI_APPLICATION
# setting points here.

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# Apply WSGI middleware here.
# from helloworld.wsgi import HelloWorldApplication
# application = HelloWorldApplication(application)
