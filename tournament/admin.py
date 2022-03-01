from django.contrib import admin


from tournament.models import Tournament, TournamentMove

admin.site.register(Tournament)
admin.site.register(TournamentMove)
