# Generated by Django 2.2.7 on 2020-01-17 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='end',
            field=models.TimeField(default='15:00:00'),
        ),
        migrations.AlterField(
            model_name='table',
            name='start',
            field=models.TimeField(default='12:00:00'),
        ),
    ]
