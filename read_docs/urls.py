from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from read_docs import views

urlpatterns = [
    path('read/', views.pdf_to_audio),
    path('all/', views.get_all),
    path('get/', views.read_by_id),
    path('get_by_pdf/', views.read_by_pdf),
    path('update_count/', views.update_nbr_page),
]
#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)