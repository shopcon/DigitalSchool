# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_testimonial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('para1', models.TextField(verbose_name=b' 1st Paragraph ')),
                ('para2', models.TextField(verbose_name=b'2nd Paragraph')),
                ('image', models.ImageField(height_field=b'height_field', width_field=b'width_field', null=True, upload_to=b'blog', blank=True)),
                ('height_field', models.IntegerField(default=0)),
                ('width_field', models.IntegerField(default=0)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='comment',
            field=models.TextField(verbose_name=b'Enter Comment Here:'),
        ),
    ]
