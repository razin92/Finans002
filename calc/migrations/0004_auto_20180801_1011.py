# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-08-01 05:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0003_auto_20180706_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='create_date',
            field=models.DateTimeField(verbose_name='Дата создания/изменения'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='date',
            field=models.DateTimeField(verbose_name='Время проведения'),
        ),
    ]
