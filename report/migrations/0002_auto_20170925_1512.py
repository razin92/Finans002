# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-25 15:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reporttransactionperson',
            name='person',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lib.Person'),
        ),
        migrations.AlterField(
            model_name='reporttransactionpouch',
            name='pouch',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lib.Pouch'),
        ),
    ]