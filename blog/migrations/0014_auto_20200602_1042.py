# Generated by Django 3.0.6 on 2020-06-02 10:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20200601_0617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='creation_date',
            field=models.DateField(default=datetime.datetime(2020, 6, 2, 10, 42, 43, 446359, tzinfo=utc)),
        ),
    ]
