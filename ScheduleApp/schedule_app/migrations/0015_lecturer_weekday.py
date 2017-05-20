# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-20 15:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('schedule_app', '0014_auto_20170520_1509'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lecturer',
            fields=[
                ('prim_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('classroom', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Weekday',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_name', models.CharField(max_length=200)),
                ('lecturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule_app.Lecturer')),
            ],
        ),
    ]
