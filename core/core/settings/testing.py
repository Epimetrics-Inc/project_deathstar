import os

from .base import *

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dev',
        'USER': 'dev',
        'PASSWORD': 'dev',
        'HOST': 'localhost',
        'PORT': '',
    }
}
