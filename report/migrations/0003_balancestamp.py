# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-10-24 11:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lib', '0002_auto_20170914_1615'),
        ('report', '0002_auto_20170925_1512'),
    ]

    operations = [
        migrations.CreateModel(
            name='BalanceStamp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('pouch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lib.Pouch')),
            ],
        ),
    ]