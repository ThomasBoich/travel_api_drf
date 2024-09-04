# Generated by Django 5.0.3 on 2024-08-30 05:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0002_trip_finish_trip_status'),
        ('users', '0012_carbrand_usercar_customuser_cars'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='citiin',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='citiin', to='users.city'),
        ),
    ]