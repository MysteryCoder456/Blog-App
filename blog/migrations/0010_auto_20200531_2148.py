# Generated by Django 3.0.6 on 2020-05-31 21:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_blog_creation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 31, 21, 48, 44, 875786, tzinfo=utc)),
        ),
    ]
