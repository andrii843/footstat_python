# Generated by Django 2.0.3 on 2018-04-02 16:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0002_auto_20180401_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='users',
            field=models.ManyToManyField(related_name='players', through='teams.PlayerShip', to=settings.AUTH_USER_MODEL),
        ),
    ]
