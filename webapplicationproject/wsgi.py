"""
WSGI config for webapplicationproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""
import os

from django.core.wsgi import get_wsgi_application

if os.environ.get('name') == 'production':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webapplicationproject.production')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webapplicationproject.settings')

application = get_wsgi_application()
