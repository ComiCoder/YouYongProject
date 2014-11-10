# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album2Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('isPrimary', models.BooleanField(default=b'False')),
                ('status', models.SmallIntegerField(default=1, choices=[(1, b'default'), (2, b'delete')])),
                ('createTime', models.DateTimeField(auto_now_add=True)),
                ('updateTime', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AlbumInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', max_length=100)),
                ('description', models.CharField(default=b'', max_length=300)),
                ('status', models.SmallIntegerField(default=1, choices=[(1, b'default'), (2, b'delete')])),
                ('createTime', models.DateTimeField(auto_now_add=True)),
                ('updateTime', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ImageInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('imgURL', models.ImageField(upload_to=b'images/normalImgs/')),
                ('width', models.SmallIntegerField()),
                ('height', models.SmallIntegerField()),
                ('type', models.SmallIntegerField(default=1, choices=[(1, b'Staff'), (2, b'Activity')])),
                ('createTime', models.DateTimeField(auto_now_add=True)),
                ('updateTime', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='albuminfo',
            name='images',
            field=models.ManyToManyField(to='ImageManager.ImageInfo', through='ImageManager.Album2Image'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='album2image',
            name='ImageInfo',
            field=models.ForeignKey(to='ImageManager.ImageInfo'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='album2image',
            name='albumInfo',
            field=models.ForeignKey(to='ImageManager.AlbumInfo'),
            preserve_default=True,
        ),
    ]
