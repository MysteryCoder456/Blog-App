# Generated by Django 2.2.13 on 2020-07-10 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_auto_20200619_1752'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='points',
            field=models.IntegerField(default=0),
        ),
    ]
