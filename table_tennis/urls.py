"""table_tennis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from rest_framework import routers

from django.contrib import admin
from django.urls import include, path

from player import urls as player_urls
from player import views as player_views

from tournament import urls as tournament_urls
from tournament import views as tournament_views


router = routers.DefaultRouter()
router.register(r'player', player_views.PlayerViewSet)
router.register(r'tournament', tournament_views.TournamentViewSet)
router.register(r'tournament_move', tournament_views.TournamentMoveViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'api/', include(router.urls))
#    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

