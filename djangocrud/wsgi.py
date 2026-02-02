"""
WSGI config for djangocrud project.

It exposes the WSGI callable as a module-level variable named ``application``.
"""

import os

from django.core.wsgi import get_wsgi_application

# Cambiamos 'django_portfolio.settings' por 'djangocrud.settings' 
# para que coincida con el nombre de tu carpeta actual.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangocrud.settings')

application = get_wsgi_application()