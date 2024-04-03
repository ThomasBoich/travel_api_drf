# Generated by Django 5.0.3 on 2024-04-03 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habits',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='habits/%Y/m/%d/'),
        ),
        migrations.AlterField(
            model_name='interests',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='interests/%Y/%m/%d/', verbose_name='Значок'),
        ),
    ]
