# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-11-20 07:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lib', '0004_category_color'),
        ('calc', '0002_auto_20170925_1233'),
        ('report', '0002_auto_20170925_1512'),
    ]

    operations = [
        migrations.CreateModel(
            name='BalanceStamp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('sum_val', models.IntegerField(default=0)),
                ('balance_before', models.IntegerField(default=0)),
                ('balance_after', models.IntegerField(default=0)),
                ('reason', models.CharField(max_length=20)),
                ('pouch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lib.Pouch')),
                ('transaction', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='calc.Transaction')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='TransactionChangeHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', models.IntegerField(blank=True, default=0)),
                ('date_before', models.DateTimeField(blank=True)),
                ('date_after', models.DateTimeField(blank=True, null=True)),
                ('sum_val_before', models.IntegerField(blank=True, default=0)),
                ('sum_val_after', models.IntegerField(blank=True, default=0)),
                ('category_before', models.CharField(blank=True, max_length=20)),
                ('category_after', models.CharField(blank=True, max_length=20)),
                ('who_is_before', models.CharField(blank=True, max_length=50)),
                ('who_is_after', models.CharField(blank=True, max_length=50)),
                ('comment_before', models.CharField(blank=True, max_length=50)),
                ('comment_after', models.CharField(blank=True, max_length=50)),
                ('money_before', models.CharField(blank=True, max_length=80)),
                ('money_after', models.CharField(blank=True, max_length=80)),
                ('typeof_before', models.BooleanField(default=True)),
                ('typeof_after', models.BooleanField(default=True)),
                ('date_of_create', models.DateTimeField(blank=True)),
                ('date_of_change', models.DateTimeField(blank=True)),
                ('creator', models.CharField(blank=True, max_length=150)),
                ('changer', models.CharField(blank=True, max_length=150)),
            ],
        ),
        migrations.AddField(
            model_name='balancestamp',
            name='transaction_change',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='report.TransactionChangeHistory'),
        ),
    ]
