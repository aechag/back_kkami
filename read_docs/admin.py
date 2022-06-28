from django.contrib import admin

# Register your models here.
from .models import doc, Audio

admin.site.register(doc)
admin.site.register(Audio)