# Generated by Django 5.0.3 on 2024-04-03 08:48

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Страна')),
                ('image', models.ImageField(blank=True, null=True, upload_to='city/%Y/%m/%d/')),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
            },
        ),
        migrations.CreateModel(
            name='Habits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Привычка')),
                ('image', models.ImageField(upload_to='habits/%Y/m/%d/')),
            ],
            options={
                'verbose_name': 'Привычка',
                'verbose_name_plural': 'Привычки',
            },
        ),
        migrations.CreateModel(
            name='Interests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Интерес')),
                ('image', models.ImageField(upload_to='interests/%Y/%m/%d/', verbose_name='Значок')),
            ],
            options={
                'verbose_name': 'Интерес',
                'verbose_name_plural': 'Интересы',
            },
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True, verbose_name='Email adress')),
                ('first_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='First Name')),
                ('last_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Last Name')),
                ('patronymic', models.CharField(blank=True, max_length=100, null=True, verbose_name='Patronymic')),
                ('user_profile_id', models.IntegerField(blank=True, null=True, verbose_name='ID User')),
                ('phone', models.CharField(blank=True, max_length=24, null=True, verbose_name='Phone')),
                ('photo', models.ImageField(blank=True, default='../static/assets/img/default_avatar.png', null=True, upload_to='media/users/%Y/%m/%d/', verbose_name='Avatar')),
                ('is_active', models.BooleanField(blank=True, default=True, null=True, verbose_name='Activate')),
                ('is_admin', models.BooleanField(blank=True, default=False, null=True, verbose_name='Administrator')),
                ('is_staff', models.BooleanField(blank=True, default=False, null=True, verbose_name='staff status')),
                ('is_superuser', models.BooleanField(blank=True, default=False, null=True, verbose_name='super user')),
                ('date_joined', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('age', models.IntegerField(blank=True, default=0, null=True)),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание страницы')),
                ('small_description', models.CharField(blank=True, max_length=99, null=True, verbose_name='Краткое описание')),
                ('bonus_points', models.FloatField(default=0, verbose_name='Бонусные баллы')),
                ('type', models.CharField(choices=[('AD', 'Administrator'), ('OA', 'Manager'), ('CL', 'Client'), ('OO', 'Client Manager')], default='CL', max_length=6, verbose_name='Type User')),
                ('ban', models.BooleanField(default=False, verbose_name='Baned')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.city')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Профиль пользователя',
                'verbose_name_plural': 'Профили пользователей',
            },
        ),
    ]
