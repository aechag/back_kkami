# Generated by Django 4.0.4 on 2022-05-02 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('read_docs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('audio', models.FileField(blank=True, null=True, upload_to='audios/')),
            ],
        ),
    ]
