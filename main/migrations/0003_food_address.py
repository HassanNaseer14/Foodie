# Generated by Django 3.0.5 on 2020-07-08 17:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_food_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='address',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
