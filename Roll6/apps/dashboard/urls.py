from django.urls import path

from . import views

urlpatterns = [
    path('', views.maindash, name='maindash'),
    path('motwfaq/', views.motwfaq, name='motwfaq'),
    path('roll6faq/', views.roll6faq, name='roll6faq'),
]

