# Generated by Django 2.2.7 on 2019-11-20 01:45

from django.db import migrations
import pyuploadcare.dj.models


class Migration(migrations.Migration):

    dependencies = [
        ('klooni', '0002_auto_20191119_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=pyuploadcare.dj.models.ImageField(),
        ),
    ]
