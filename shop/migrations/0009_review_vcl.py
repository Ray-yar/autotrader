# Generated by Django 3.2.18 on 2023-04-30 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='vcl',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='shop.vehicle'),
        ),
    ]
