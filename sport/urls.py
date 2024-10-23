from django.urls import path, include
from rest_framework.routers import DefaultRouter

from sport.apps import SportConfig
from sport.views import TrainerViewSet, DirectionViewSet

app_name = SportConfig.name

router = DefaultRouter()
router.register(r'trainers', TrainerViewSet)
router.register(r'directions', DirectionViewSet)

urlpatterns = [
    path('', include(router.urls))
]

