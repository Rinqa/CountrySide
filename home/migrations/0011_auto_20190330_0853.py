# Generated by Django 2.1.5 on 2019-03-30 12:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20190329_0559'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='state',
            name='Latitude',
        ),
        migrations.RemoveField(
            model_name='state',
            name='Longitude',
        ),
        migrations.RemoveField(
            model_name='state',
            name='Rating',
        ),
    ]
