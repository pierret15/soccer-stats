from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='home'),
    path('player/<int:playerId>',views.player,name='player'),
    path('league/<int:leagueId>',views.league,name='league'),
    path('team/<int:teamId>',views.team,name='team')
]