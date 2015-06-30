# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0002_auto_20150625_1501'),
    ]

    operations = [
        migrations.AddField(
            model_name='samplelog',
            name='rush',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
