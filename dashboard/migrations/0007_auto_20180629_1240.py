# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_auto_20180627_1144'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BlogComment',
        ),
        migrations.AddField(
            model_name='blog',
            name='title',
            field=models.CharField(default=1, max_length=40, verbose_name=b'Title'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='freecounselling',
            name='timestamp',
            field=models.DateTimeField(default=1, auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='freecounselling',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 29, 12, 40, 50, 332127, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='freecounselling',
            name='email',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='freecounselling',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
