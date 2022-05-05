from rest_framework.routers import DefaultRouter
from creatures import views

router = DefaultRouter()
router.register(r'creatures', views.CreatureViewSet, basename='creatures')
urlpatterns = router.urls
