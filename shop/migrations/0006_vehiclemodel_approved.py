# Generated by Django 3.2.18 on 2023-04-11 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_vehiclemodel_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiclemodel',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]