# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='yyUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('phoneNum', models.CharField(unique=True, max_length=20)),
                ('nickName', models.CharField(max_length=30, null=True)),
                ('smallIconURL', models.ImageField(null=True, upload_to=b'images/profile_icon/')),
                ('largeIconURL', models.ImageField(null=True, upload_to=b'images/profile_icon/')),
                ('gender', models.SmallIntegerField(default=3, choices=[(1, b'Male'), (2, b'Female'), (3, b'-')])),
                ('selfDesc', models.CharField(max_length=300, null=True)),
                ('address', models.CharField(max_length=100, null=True)),
                ('zipcode', models.CharField(max_length=20, null=True)),
                ('email', models.EmailField(max_length=75, null=True)),
                ('type', models.SmallIntegerField(default=1, choices=[(1, b'Normal'), (2, b'Admin')])),
                ('regProvince', models.SmallIntegerField(null=True)),
                ('regCity', models.SmallIntegerField(null=True)),
                ('authValue', models.SmallIntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('createTime', models.DateTimeField(auto_now_add=True)),
                ('updateTime', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
