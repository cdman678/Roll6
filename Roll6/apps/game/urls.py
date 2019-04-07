from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='game'),
    path('choosecharacter/', views.choosecharacter, name='choosecharacter'),
    path('fill/<slug:hunter>/', views.fillsheet, name='fill-sheet'),
]