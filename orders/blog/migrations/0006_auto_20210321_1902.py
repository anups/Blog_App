# Generated by Django 3.1.7 on 2021-03-21 13:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20210321_0824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 21, 13, 32, 58, 897140, tzinfo=utc)),
        ),
    ]