# Generated by Django 5.0.3 on 2024-08-30 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0006_trip_trip_in_time_trip_trip_out_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='trip_in_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='trip',
            name='trip_out_time',
            field=models.DateTimeField(),
        ),
    ]
