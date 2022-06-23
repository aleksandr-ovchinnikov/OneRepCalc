from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('support/', views.support, name='support'),
    path('calculate/', views.calculate, name='calculate')
]
