# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-02-14 05:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hesabe_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='credential',
            name='failure_url',
        ),
        migrations.RemoveField(
            model_name='credential',
            name='success_url',
        ),
    ]
