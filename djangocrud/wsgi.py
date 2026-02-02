"""
WSGI config for djangocrud project.

It exposes the WSGI callable as a module-level variable named ``application``.
"""

import os
import sys
from django.core.wsgi import get_wsgi_application

# Añadimos el directorio base al path para que Python encuentre los módulos sin problemas
# Esto evita el error de "ModuleNotFoundError" durante el despliegue en Render
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

# Establecemos el módulo de configuración por defecto
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangocrud.settings')

application = get_wsgi_application()