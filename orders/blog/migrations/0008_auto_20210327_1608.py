# Generated by Django 3.1.7 on 2021-03-27 10:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20210327_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 27, 10, 38, 27, 120838, tzinfo=utc)),
        ),
    ]
