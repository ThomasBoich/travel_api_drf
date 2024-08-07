# Generated by Django 5.0.3 on 2024-07-19 14:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_friends'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friends',
            name='friends',
            field=models.ManyToManyField(blank=True, null=True, related_name='users_friends', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Favorits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favorites', models.ManyToManyField(blank=True, null=True, related_name='users_favorites', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Избранный',
                'verbose_name_plural': 'Избранные',
            },
        ),
    ]
