# Generated by Django 2.2.7 on 2020-02-03 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_auto_20200127_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='end',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='table',
            name='start',
            field=models.TimeField(),
        ),
    ]
