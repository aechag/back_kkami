from django.db import models

# Create your models here.
class Img_audio(models.Model):
    name = models.CharField(max_length=50)
    audio = models.FileField(null=True, blank=True, upload_to='text_audio/')