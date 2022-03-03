from rest_framework import viewsets

from tournament.models import Tournament, TournamentMove
from tournament.serializers import TournamentSerializer, TournamentMoveSerializer

class TournamentViewSet(viewsets.ModelViewSet):
    queryset = Tournament.objects.all().order_by('-start_time')
    serializer_class = TournamentSerializer


class TournamentMoveViewSet(viewsets.ModelViewSet):
    queryset = TournamentMove.objects.all()
    serializer_class = TournamentMoveSerializer
