# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0017_remove_freecounselling_updated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='freecounselling',
            name='timestamp',
        ),
    ]
