# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phoneNum', models.CharField(max_length=20, null=True)),
                ('nickName', models.CharField(max_length=30, null=True)),
                ('smallIconURL', models.URLField(max_length=100, null=True)),
                ('largeIconURL', models.URLField(max_length=100, null=True)),
                ('gender', models.SmallIntegerField(default=3, choices=[(1, b'Male'), (2, b'Female'), (3, b'-')])),
                ('selfDesc', models.CharField(max_length=300, null=True)),
                ('address', models.CharField(max_length=100, null=True)),
                ('zipcode', models.CharField(max_length=20, null=True)),
                ('email', models.EmailField(max_length=75, null=True)),
                ('type', models.SmallIntegerField(default=1, choices=[(1, b'Normal'), (2, b'Admin')])),
                ('regProvince', models.SmallIntegerField(null=True)),
                ('regCity', models.SmallIntegerField(null=True)),
                ('authValue', models.SmallIntegerField(default=0)),
                ('createTime', models.DateTimeField(auto_now_add=True)),
                ('updateTime', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
