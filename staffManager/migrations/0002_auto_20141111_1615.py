# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userManager', '0004_auto_20141110_1508'),
        ('ImageManager', '0002_auto_20141111_1615'),
        ('staffManager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='staffinfo',
            name='albumInfo',
            field=models.ForeignKey(to='ImageManager.AlbumInfo', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='staffinfo',
            name='createTime',
            field=models.DateTimeField(auto_now_add=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='staffinfo',
            name='lagituite',
            field=models.FloatField(default=0.0, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='staffinfo',
            name='longitute',
            field=models.FloatField(default=0.0, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='staffinfo',
            name='position',
            field=models.CharField(default=b'-', max_length=100),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='staffinfo',
            name='price',
            field=models.FloatField(default=0.0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='staffinfo',
            name='publisher',
            field=models.ForeignKey(to='userManager.UserInfo', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='staffinfo',
            name='staffDesc',
            field=models.CharField(max_length=300, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='staffinfo',
            name='status',
            field=models.SmallIntegerField(default=1, choices=[(0, b'delete'), (1, b'default')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='staffinfo',
            name='updateTime',
            field=models.DateTimeField(auto_now=True, null=True),
            preserve_default=True,
        ),
    ]
