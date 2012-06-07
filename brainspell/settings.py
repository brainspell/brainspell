# -*- coding: utf-8 -*-

import os
import sys

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
APPS_ROOT    = os.path.join(PROJECT_ROOT, 'apps')
LOG_ROOT     = os.path.join(PROJECT_ROOT, 'logs')
MEDIA_ROOT   = os.path.join(PROJECT_ROOT, 'media')
STATIC_ROOT  = os.path.join(PROJECT_ROOT, 'static')
TPL_ROOT     = os.path.join(PROJECT_ROOT, 'templates')

sys.path.append(PROJECT_ROOT)
sys.path.append(APPS_ROOT)

ROOT_URLCONF = 'urls'

AUTH_PROFILE_MODULE = 'accounts.Profile'

TIME_ZONE = 'Europe/Paris'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1

USE_I18N = True
USE_L10N = True
USE_TZ = True

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    
    os.path.join(PROJECT_ROOT, 'site_static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '6shmwd)tf9udh!)bxfk9s0+)t&amp;!6&amp;gmm2^p$1$l%xv2c1bmbr&amp;'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages'
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'pagination.middleware.PaginationMiddleware',
)

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.

    TPL_ROOT,
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.comments',

    'django_extensions',
    'pagination',

    'accounts',
    'baccara',
    'contents',
    'papers',
    'website',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'simple':  { 'format': '%(asctime)s %(levelname)s %(message)s' },
        'verbose': { 'format': '%(asctime)s %(levelname)s %(module)s %(process)d %(thread)d %(message)s' },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'django.utils.log.NullHandler'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        'logfile':     {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'verbose',
            'filename': os.path.join(LOG_ROOT, 'django.log')
        },
        'logfile_sql': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'verbose',
            'filename': os.path.join(LOG_ROOT, 'sql.log')
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.db.backends': { 
            'handlers': ['null'],
            'level' : 'DEBUG',
            'propagate': False,
        },
    }
}

PAGINATION_DEFAULT_PAGINATION = 5

try:
    from local_settings import *
except ImportError:
    pass
