# Generated by Django 2.2.7 on 2020-05-31 22:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20200531_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 31, 22, 2, 27, 687160, tzinfo=utc)),
        ),
    ]