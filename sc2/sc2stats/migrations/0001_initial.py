# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('map_id', models.CharField(unique=True, max_length=128)),
                ('map_size', models.IntegerField(default=2)),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('match_id', models.IntegerField(unique=True)),
                ('map_id', models.CharField(max_length=128)),
                ('player_1', models.CharField(max_length=128)),
                ('player_2', models.CharField(max_length=128)),
                ('winner', models.CharField(max_length=128)),
                ('season', models.CharField(max_length=128)),
                ('league', models.CharField(max_length=128)),
                ('expansion', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('player_id', models.CharField(unique=True, max_length=128)),
                ('race', models.CharField(max_length=10)),
            ],
        ),
    ]
