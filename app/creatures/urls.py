"""
 * Author: Connor Pandolph
 * Project: Creatures
 * API: REST
 * Framework: Django
 * Container: Docker
 * Date: 2022
"""

from rest_framework.routers import DefaultRouter
from creatures import views

#Database URLs
router = DefaultRouter()
router.register(r'creatures', views.CreatureViewSet, basename='creatures')
urlpatterns = router.urls
