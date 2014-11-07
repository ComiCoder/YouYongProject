# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userManager', '0002_userinfo_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='largeIconURL',
            field=models.ImageField(null=True, upload_to=b''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='smallIconURL',
            field=models.ImageField(null=True, upload_to=b''),
            preserve_default=True,
        ),
    ]
