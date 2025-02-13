# Generated by Django 2.2.7 on 2020-02-04 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_auto_20200203_2041'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.CharField(max_length=20)),
                ('subject', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='guest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=20)),
            ],
        ),
    ]
