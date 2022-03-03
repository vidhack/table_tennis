from rest_framework import routers
from django.urls import include, path

from tournament import views

router = routers.DefaultRouter()
router.register(r'tournament', views.TournamentViewSet)
router.register(r'tournament_move', views.TournamentMoveViewSet)

urlpatterns = [
    path(r'^', include(router.urls)),
]

