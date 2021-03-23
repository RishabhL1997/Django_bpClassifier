from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about),
    path('contact/', views.contact, name='contact'),
    path('result/', views.result, name='result'),
]