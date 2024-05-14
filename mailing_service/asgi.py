"""
ASGI config for mailing_service project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this learning_material, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mailing_service.settings')

application = get_asgi_application()
