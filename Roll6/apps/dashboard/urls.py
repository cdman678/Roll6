from django.urls import path

from . import views

urlpatterns = [
    path('', views.main_dash, name='main_dash'),
    path('motwfaq/', views.motwfaq, name='motwfaq'),
    path('roll6faq/', views.roll6faq, name='roll6faq'),
    path('choosecharacter/', views.choosecharacter, name='choosecharacter'),
]

