# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-11 03:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('api', '0002_auto_20170911_0326'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='document',
            options={'ordering': ('date', 'modified')},
        ),
    ]
