# Generated by Django 5.0.3 on 2024-07-06 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_customuser_habits_alter_customuser_interests'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='media/users/%Y/%m/%d/', verbose_name='Avatar'),
        ),
    ]
