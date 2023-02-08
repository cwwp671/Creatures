"""
 * Author: Connor Pandolph
 * Project: World of Warcraft Creature Database
 * API: REST
 * Framework: Django
 * Container: Docker
 * Date: 2022
"""

from django.apps import AppConfig

class CreaturesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'creatures'
