from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.create_game, name='create-game'),
    path('join/', views.join_game, name='join-game'),
    path(r'<slug:gameid>/choosecharacter/', views.choosecharacter, name='choosecharacter'),
    path(r'<slug:gameid>/game/', views.game, name='game'),
    path(r'<slug:gameid>/fill/<slug:hunter>/', views.fillsheet, name='fill-sheet'),
]