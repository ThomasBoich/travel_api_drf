# Generated by Django 5.0.3 on 2024-08-30 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0005_rename_citiin_trip_cityin'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='trip_in_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='trip',
            name='trip_out_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
