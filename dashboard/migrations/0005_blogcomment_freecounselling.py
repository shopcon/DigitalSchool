# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20180622_1338'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.TextField(verbose_name=b'Please Comment Here')),
                ('name', models.CharField(max_length=20, verbose_name=b'Enter Your Name')),
                ('phone', models.BigIntegerField(verbose_name=b'Enter Your Mobile Number')),
            ],
        ),
        migrations.CreateModel(
            name='FreeCounselling',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.BigIntegerField()),
            ],
        ),
    ]
