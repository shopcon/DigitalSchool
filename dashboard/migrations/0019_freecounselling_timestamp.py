# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0018_remove_freecounselling_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='freecounselling',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 3, 18, 17, 38, 56304, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
