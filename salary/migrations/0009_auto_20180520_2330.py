# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-05-20 23:30
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salary', '0008_auto_20180516_1742'),
    ]

    operations = [
        migrations.AddField(
            model_name='workreport',
            name='deleted',
            field=models.BooleanField(default=False, verbose_name='Удален'),
        ),
        migrations.AlterField(
            model_name='total',
            name='date',
            field=models.DateField(default=datetime.datetime(2018, 5, 1, 23, 30, 35, 155225)),
        ),
        migrations.AlterField(
            model_name='work',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Вид работ'),
        ),
        migrations.AlterField(
            model_name='workcalc',
            name='time_range',
            field=models.CharField(choices=[('Оклад', 'salary'), ('Месяц', 'month'), ('Процент', 'percent'), ('Час', 'hour'), ('День', 'day')], max_length=20),
        ),
    ]
