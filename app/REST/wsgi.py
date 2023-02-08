"""
 * Author: Connor Pandolph
 * Project: Creatures
 * API: REST
 * Framework: Django
 * Container: Docker
 * Date: 2022
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'REST.settings')

application = get_wsgi_application()
