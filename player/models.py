from django.db import models
from django.contrib.auth.models import User


from core.choices import PLAYER_LEVEL, PLAYER_MODE
from core.models import BasicConfiguration


class Player(BasicConfiguration):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    player_mode = models.CharField(max_length=20, choices=PLAYER_MODE)
    player_level = models.CharField(max_length=20, choices=PLAYER_LEVEL)

    def __str__(self):
        return f"{self.user.username}  {self.player_mode} {self.player_level}"
