from django.contrib.auth.models import User, Group
from rest_framework import serializers

from tournament.models import Tournament, TournamentMove


class TournamentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tournament
        fields = '__all__'


class TournamentMoveSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TournamentMove
        fields = '__all__'


