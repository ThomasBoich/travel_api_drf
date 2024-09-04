# Generated by Django 5.0.3 on 2024-09-04 11:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_carbrand_usercar_customuser_cars'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='usercar',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='usercars/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='usercar',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='cars',
            field=models.ManyToManyField(blank=True, null=True, related_name='user_cars', to='users.usercar'),
        ),
        migrations.AlterField(
            model_name='usercar',
            name='model',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.carbrand'),
        ),
    ]