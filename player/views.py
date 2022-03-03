from rest_framework import viewsets
from rest_framework import permissions

from player.models import Player
from player.serializers import PlayerSerializer

class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

