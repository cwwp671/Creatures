"""
 * Author: Connor Pandolph
 * Project: Creatures
 * API: REST
 * Framework: Django
 * Container: Docker
 * Date: 2022
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'REST.settings')

application = get_asgi_application()
