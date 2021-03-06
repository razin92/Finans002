# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-05-15 16:48
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('salary', '0006_auto_20171204_1213'),
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Вид работ')),
            ],
        ),
        migrations.CreateModel(
            name='WorkReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filling_date', models.DateField(auto_now=True, verbose_name='Дата заполнения')),
                ('working_date', models.DateField(verbose_name='Дата выполнения')),
                ('hours_qty', models.SmallIntegerField(default=1, verbose_name='Кол-во часов')),
                ('quarter', models.SmallIntegerField(verbose_name='Квартал')),
                ('building', models.CharField(max_length=4, verbose_name='Дом')),
                ('apartment', models.SmallIntegerField(blank=True, null=True, verbose_name='Квартира')),
                ('confirmed', models.BooleanField(default=False, verbose_name='Принята')),
                ('cost', models.IntegerField(default=0, verbose_name='Стоимость')),
                ('comment', models.CharField(blank=True, max_length=250, null=True, verbose_name='Комментарий')),
                ('coworker', models.ManyToManyField(blank=True, null=True, to='salary.Worker', verbose_name='Помощники')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Ответственный')),
                ('work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salary.Work', verbose_name='Вид работ')),
            ],
        ),
        migrations.AlterField(
            model_name='total',
            name='date',
            field=models.DateField(default=datetime.datetime(2018, 5, 1, 16, 48, 1, 881279)),
        ),
        migrations.AlterField(
            model_name='workcalc',
            name='time_range',
            field=models.CharField(choices=[('Процент', 'percent'), ('День', 'day'), ('Оклад', 'salary'), ('Месяц', 'month'), ('Час', 'hour')], max_length=20),
        ),
    ]
