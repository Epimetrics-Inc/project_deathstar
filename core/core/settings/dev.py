import os

from .base import *

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = True

INSTALLED_APPS += (
    'debug_toolbar',
)

MIDDLEWARE += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

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


def show_toolbar(request):
    return True


DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK": show_toolbar,
}

import debug_toolbar
from ..urls import urlpatterns
from django.conf.urls import url, include

urlpatterns = [
                  url(r'^__debug__/', include(debug_toolbar.urls)),
              ] + urlpatterns
