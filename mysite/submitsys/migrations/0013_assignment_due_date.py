# Generated by Django 3.0.2 on 2020-04-22 19:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submitsys', '0012_auto_20200422_1504'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 6, 15, 32, 44, 175983)),
        ),
    ]