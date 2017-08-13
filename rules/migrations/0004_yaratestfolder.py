# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2017-08-10 23:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rules', '0003_auto_20170303_0310'),
    ]

    operations = [
        migrations.CreateModel(
            name='YaraTestFolder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75, unique=True)),
                ('path', models.CharField(max_length=4096, unique=True)),
                ('description', models.TextField()),
            ],
        ),
    ]