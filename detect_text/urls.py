from django.contrib import admin
from django.urls import path

from detect_text import views

urlpatterns = [
    path('detectText/', views.detectText),
]