# Generated by Django 3.0.6 on 2020-06-02 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20200602_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='creation_date',
            field=models.DateField(),
        ),
    ]
