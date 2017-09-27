"""
WSGI config for core project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

activate_env=os.path.expanduser("/home/vagrant/.virtualenvs/prod/bin/postactivation.py")
exec(open(activate_env).read())

application = get_wsgi_application()
