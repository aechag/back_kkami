# Generated by Django 4.0.4 on 2022-05-03 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('read_docs', '0003_audio_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='audio',
            name='num_pdf',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
