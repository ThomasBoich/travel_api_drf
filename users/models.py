from django.db import models
from django.contrib.auth.models import AbstractBaseUser, Permission, Group
from django.contrib.auth.models import PermissionsMixin
from django.dispatch import receiver
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.db.models.signals import post_save
from .managers import CustomUserManager
# Create your models here.
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True, verbose_name='Email adress')
    first_name = models.CharField(u"First Name", max_length=100)
    last_name = models.CharField(u"Last Name", max_length=100)
    patronymic = models.CharField(u"Patronymic", max_length=100)
    user_profile_id = models.IntegerField(blank=True, verbose_name='ID User', null=True, default=0)
    phone = models.CharField(max_length=24, blank=True, null=True, verbose_name='Phone')
    photo = models.ImageField(upload_to='media/users/%Y/%m/%d/', blank=True, null=True, verbose_name='Avatar') # default='../static/assets/img/default_avatar.png',
                              
    is_active = models.BooleanField(default=True, verbose_name='Activate', blank=True, null=True)
    is_admin = models.BooleanField(default=False, verbose_name='Administrator', blank=True, null=True)
    is_staff = models.BooleanField(_('staff status'), default=False, blank=True, null=True)
    is_superuser = models.BooleanField(_('super user'), default=False, blank=True, null=True)
    date_joined = models.DateTimeField(u'date joined', blank=True, null=True, default=timezone.now)
    last_login = models.DateTimeField(u'last login', blank=True, null=True)
    age = models.IntegerField(default=0, blank=True, null=True)
    description = models.TextField(verbose_name='Описание страницы', blank=True, null=True)
    small_description = models.CharField(max_length=99, verbose_name='Краткое описание', blank=True, null=True)
    bonus_points = models.FloatField(
        verbose_name='Бонусные баллы',
        default=0,
    )
    habits = models.ManyToManyField('Habits', related_name='user_habits', blank=True)
    interests = models.ManyToManyField('Interests', related_name='users_interests', blank=True)
    premium = models.BooleanField(default=False, verbose_name='premium', blank=True, null=True)
    
    ADMINISTRATOR = 'AD'
    MANAGER = 'OA'
    CLIENT = 'CL'
    CLMANAGER = 'OO'

    TYPE_ROLE = [
        (ADMINISTRATOR, 'Administrator'),
        (MANAGER, 'Manager'),
        (CLIENT, 'Client'),
        (CLMANAGER, 'Client Manager')
    ]

    type = models.CharField(max_length=6, choices=TYPE_ROLE, default=CLIENT, verbose_name='Type User')
    ban = models.BooleanField(default=False, verbose_name='Baned')
    city = models.ForeignKey('City', blank=True, null=True, on_delete=models.CASCADE)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return ' '.join(filter(None, (self.last_name, self.first_name, self.patronymic)))
        
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def get_absolute_url(self):
        return reverse('user_info', kwargs={'user_id': self.id})
    
    def save(self, *args, **kwargs):
        self.bonus_points = round(self.bonus_points, 2)
        super(CustomUser, self).save(*args, **kwargs)


# ПРОФИЛЬ ПОЛЬЗОВАТЕЛЯ С ДОПОЛНИТЕЛЬНОЙ ИНФОРМАЦИЕЙ #
class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f" {self.user.first_name} {self.user.last_name}"

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'

    def get_absolute_url(self):
        return reverse('profile', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def first_name(self):
        return self.user.first_name


@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Interests(models.Model):
    name = models.CharField(max_length=255, verbose_name='Интерес')
    image = models.ImageField(upload_to='interests/%Y/%m/%d/', verbose_name='Значок', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Интерес'
        verbose_name_plural = 'Интересы'


class Habits(models.Model):
    name = models.CharField(max_length=255, verbose_name='Привычка')
    image = models.ImageField(upload_to='habits/%Y/m/%d/', blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'


class City(models.Model):
    name = models.CharField(max_length=200, verbose_name='Страна', blank=True, null=True)
    image = models.ImageField(upload_to='city/%Y/%m/%d/', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'



class Friends(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    friends = models.ManyToManyField(CustomUser, related_name='users_friends', blank=True, null=True)

    def __str__(self):
        return f'{self.user} - {self.friends.all()}'

    class Meta:
        verbose_name = 'Друг'
        verbose_name_plural = 'Друзья'


class Favorites(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    favorites = models.ManyToManyField(CustomUser, related_name='users_favorites', blank=True, null=True)

    def __str__(self):
        return f'{self.user} - {self.favorites.all()}'

    class Meta:
        verbose_name = 'Избранный'
        verbose_name_plural = 'Избранные'