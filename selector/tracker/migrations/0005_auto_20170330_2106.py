# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-30 21:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0004_auto_20170328_2324'),
    ]

    operations = [
        migrations.RenameField(
            model_name='option',
            old_name='description',
            new_name='details',
        ),
    ]
