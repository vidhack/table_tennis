from rest_framework import routers
from django.urls import include, path

from  player import views

router = routers.DefaultRouter()
router.register(r'player', views.PlayerViewSet)


urlpatterns = [
    path(r'^', include(router.urls)),
]
