# Generated by Django 3.0.2 on 2020-04-09 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submitsys', '0007_auto_20200408_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submissionfile',
            name='file_contents',
            field=models.TextField(default='NULL'),
        ),
        migrations.AlterField(
            model_name='submissionfile',
            name='file_name',
            field=models.CharField(default='NULL', max_length=15),
        ),
    ]
