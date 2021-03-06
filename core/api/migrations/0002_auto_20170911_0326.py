# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-11 03:26
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='body',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='docnum',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='doctype',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='images',
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='raw_body',
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='sign',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='signtitle',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='subject',
            field=models.TextField(null=True),
        ),
    ]
