# Generated by Django 3.0.2 on 2020-04-09 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submitsys', '0008_auto_20200409_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_name',
            field=models.CharField(default='Course Name', max_length=8),
        ),
    ]
