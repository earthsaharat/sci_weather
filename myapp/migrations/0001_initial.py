# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-02 15:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('nodeid', models.CharField(max_length=3)),
                ('temp', models.FloatField(default=0.0)),
                ('humi', models.FloatField(default=0.0)),
                ('israin', models.BooleanField(default=False)),
            ],
        ),
    ]
