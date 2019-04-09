from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='game'),
    path('join/', views.join_game, name='join-game'),
    path(r'<slug:gameid>/choosecharacter/', views.choosecharacter, name='choosecharacter'),
    path(r'fill/<slug:hunter>/', views.fillsheet, name='fill-sheet'),
]