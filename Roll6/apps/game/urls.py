from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.create_game, name='create-game'),
    path('join/', views.join_game, name='join-game'),
    path(r'<slug:gameid>/choosecharacter/', views.choosecharacter, name='choosecharacter'),
    path(r'<slug:gameid>/<slug:hunter>/', views.game, name='game'),
    path(r'<slug:gameid>/fill/<slug:hunter>/', views.fillsheet, name='fill-sheet'),
    path(r'dice/', views.dice, name='dice'),
    path(r'<slug:gameid>/<slug:hunter>/update', views.update_sheet, name='update')
]