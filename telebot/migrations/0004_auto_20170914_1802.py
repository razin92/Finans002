# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-14 18:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('telebot', '0003_auto_20170914_1800'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='date_accept',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='date_close',
        ),
    ]
