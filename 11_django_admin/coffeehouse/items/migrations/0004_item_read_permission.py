# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-22 03:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_menu_creator'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'permissions': (('read_item', 'Can read item'),)},
        ),
    ]
