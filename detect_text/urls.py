from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from detect_text import views

urlpatterns = [
    path('detectText/', views.detectText),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)