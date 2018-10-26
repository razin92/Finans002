# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-07-18 13:16
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('salary', '0013_auto_20180711_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='total',
            name='date',
            field=models.DateField(default=datetime.datetime(2018, 7, 1, 13, 16, 54, 951461, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='workcalc',
            name='time_range',
            field=models.CharField(choices=[('Оклад', 'salary'), ('Месяц', 'month'), ('День', 'day'), ('Час', 'hour'), ('Процент', 'percent')], max_length=20),
        ),
        migrations.AlterUniqueTogether(
            name='workreport',
            unique_together=set([('working_date', 'work', 'user', 'quarter', 'building', 'apartment', 'comment')]),
        ),
    ]
