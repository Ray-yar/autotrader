# Generated by Django 3.2.19 on 2023-07-23 06:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_vehicle_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='rating',
        ),
    ]
