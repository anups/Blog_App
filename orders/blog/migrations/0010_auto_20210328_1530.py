# Generated by Django 3.1.7 on 2021-03-28 10:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20210328_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 28, 10, 0, 41, 558362, tzinfo=utc)),
        ),
    ]
