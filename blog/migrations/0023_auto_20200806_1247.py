# Generated by Django 3.1 on 2020-08-06 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_auto_20200714_1604'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='num_vote_down',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='num_vote_up',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='vote_score',
        ),
    ]