# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StaffInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dealType', models.SmallIntegerField(default=1, choices=[(1, b'Trade'), (2, b'Present'), (3, b'Switch')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
