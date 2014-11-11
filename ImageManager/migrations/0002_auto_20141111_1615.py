# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ImageManager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album2image',
            name='status',
            field=models.SmallIntegerField(default=1, choices=[(0, b'delete'), (1, b'default')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='albuminfo',
            name='status',
            field=models.SmallIntegerField(default=1, choices=[(0, b'delete'), (1, b'default')]),
            preserve_default=True,
        ),
    ]
