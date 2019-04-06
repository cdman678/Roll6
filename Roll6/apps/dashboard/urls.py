from django.urls import path

from . import views

urlpatterns = [
    path('motwfaq/', views.motw_faq, name='motwfaq'),
    path('roll6faq/', views.roll6_faq, name='roll6faq'),
]

