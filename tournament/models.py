import uuid

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


from core.models import BasicConfiguration
from core.choices import TOURNAMENT_RESULT, TOURNAMENT_STATE
from core.constants import TOURNAMENT_MAX_SCORE, TOURNAMENT_MIN_SCORE
from player.models import Player


class Tournament(BasicConfiguration):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    player1 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player1_tournament')
    player2 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player2_tournament')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    result = models.CharField(max_length=20, choices = TOURNAMENT_RESULT)
    winner = models.ForeignKey(Player, blank=True, null=True, on_delete=models.CASCADE)
    # this field will keep updating after updating TournamentMove, possibaly by post_save signal
    player_turn = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player_turn')


    def __str__(self):
        return f"{self.player1.user.username} vs {self.player2.user.username}"

class TournamentMove(BasicConfiguration):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    move_no = models.IntegerField()
    score = models.IntegerField(default=0, validators=[MinValueValidator(TOURNAMENT_MIN_SCORE), MaxValueValidator(TOURNAMENT_MAX_SCORE)])

    def __str__(self):
        return f"{self.tournament.id} {self.player.user.username} {self.move_no} {self.score}"
