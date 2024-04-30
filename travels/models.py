from django.db import models
from users.models import CustomUser, City
from django.db.models import Count
# Create your models here.

class Travel(models.Model):
    
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Пользователь')

    MEN = 'Мужчина'
    GIRL = 'Женщина'

    GENDERS_LIST = [
        (MEN, 'Мужчина'),
        (GIRL, 'Женщина')
    ]


    SEARCH_MEN = 'Мужчину'
    SEARCH_GIRL = 'Женщину'
    SEARCH_FAMIlY = 'Семью'


    SEARCH_GENDERS_LIST = [
        (SEARCH_MEN, 'Мужчину'),
        (SEARCH_GIRL, 'Женщину'),
        (SEARCH_FAMIlY, 'Семью'),
    ]

    gender = models.CharField(max_length=15, choices=GENDERS_LIST, default=MEN, verbose_name='Пол', null=True, blank=True)
    gender_search = models.CharField(max_length=15, choices=SEARCH_GENDERS_LIST, default=SEARCH_GIRL, verbose_name='Ищу', blank=True, null=True)
    city = models.CharField(max_length=200, verbose_name='Город, Курорт', blank=True, null=True)
    country = models.ManyToManyField('Country', related_name='travels', verbose_name='Страна')
    days = models.IntegerField(verbose_name='Количество дней', blank=True, null=True)
    date = models.DateField(verbose_name='Когда', blank=True, null=True)
    description = models.TextField(verbose_name='Описание путешествия', blank=True, null=True)
    travel_now = models.BooleanField(default=False, verbose_name='Уже путешествую', blank=True, null=True)
    from_city = models.ForeignKey(City, blank=True, null=True, on_delete=models.CASCADE, verbose_name='Откуда')

    def __str__(self):
        return self.city


    class Meta:
        verbose_name = "Путешествие"
        verbose_name_plural = "Путешествия"


class Country(models.Model):
    name = models.CharField(max_length=200, verbose_name='Страна', blank=True, null=True)
    image = models.ImageField(upload_to='countries/%Y/%m/%d/', blank=True, null=True)
    cities = models.ManyToManyField(City, related_name='city_countries', verbose_name='Города', blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'

    @property
    def travel_count(self):
        return self.travels.count()

    @classmethod
    def with_travel_counts(cls):
        return cls.objects.annotate(travel_count=Count('travels'))