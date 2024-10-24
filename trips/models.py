from django.db import models
from users.models import CustomUser, City, UserCar
# Create your models here.

class Trip(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    trip_users = models.ManyToManyField(CustomUser, related_name='trip_users', blank=True, null=True)
    # trip_date = models.DateTimeField(blank=True, null=True)
    free_seats = models.IntegerField(default=0, blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, blank=True, null=True)
    price = models.IntegerField(default=0, blank=True, null=True)
    status = models.BooleanField(default=True, blank=True, null=True)
    finish = models.BooleanField(default=False, blank=True, null=True)
    cityin = models.ForeignKey(City, on_delete=models.CASCADE, related_name='citiin', blank=True, null=True)
    trip_in_time = models.DateTimeField(blank=True, null=True)
    trip_out_time = models.DateTimeField(blank=True, null=True)
    trip_car = models.ForeignKey(UserCar, on_delete=models.CASCADE, blank=True, null=True)
    # trip_baggage = models.BooleanField(default=False, blank=True, null=True)
    # trip_smoking = models.BooleanField(default=False, blank=True, null=True)
    # trip_hild_seat = models.BooleanField(default=False, blank=True, null=True)
    # trip_animals = models.BooleanField(default=False, blank=True, null=True)
    trip_others = models.ManyToManyField("TripOther", blank=True, null=True, related_name="trip_others")
    
    def __str__(self):
        return self.user.email
    
    class Meta:
        verbose_name = "Поездка"
        verbose_name_plural = "Поездки"
 
# class CarBrand(models.Model):
#     name = models.CharField(max_length=200)
#     image = models.ImageField(upload_to="cars/brands/%Y/%m/%d/")
    
# class UserCar(models.Model):
#     car = models.ForeignKey(CarBrand, on_delete=models.CASCADE)
#     model = models.ForeignKey("CarModel", on_delete=models.CASCADE)

# class CarModel(models.Model):
#     name = models.CharField(max_length=200)

class TripOther(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="trips/others/%Y/%m/%d/")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Дополнительная опция"
        verbose_name_plural = "Дополнительные опции"