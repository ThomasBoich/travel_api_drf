# Generated by Django 5.0.3 on 2024-08-30 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0008_carbrand_carmodel_usercar_trip_trip_car'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='trip_animals',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='trip',
            name='trip_baggage',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='trip',
            name='trip_hild_seat',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='trip',
            name='trip_smoking',
            field=models.BooleanField(default=False),
        ),
    ]
