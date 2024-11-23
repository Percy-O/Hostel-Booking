from .common import *
import os
import django_heroku
import dj_database_url

SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['hostel-mgts.herokuapp.com']


DATABASES = {
    'default': dj_database_url.config()
}

# Activating Django-Heroku
django_heroku.settings(locals())