# Generated by Django 3.2.18 on 2023-04-11 11:49

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VehicleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=128)),
                ('model', models.CharField(max_length=128)),
                ('color', models.CharField(max_length=128)),
                ('body', models.CharField(max_length=128)),
                ('year', models.IntegerField()),
                ('fuel', models.CharField(max_length=128)),
                ('milage', models.IntegerField()),
                ('reg_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('featured_photo', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('transmission', models.CharField(max_length=128)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
    ]