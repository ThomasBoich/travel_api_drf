from django.db import models
from users.models import CustomUser, City
# Create your models here.

class Trip(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    tipr_users = models.ManyToManyField(CustomUser, related_name='trip_users')
    trip_date = models.DateTimeField()
    free_seats = models.IntegerField(default=0)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    status = models.BooleanField(default=True, blank=True, null=True)
    finish = models.BooleanField(default=False, blank=True, null=True)
    
    def __str__(self):
        return self.user.email
 
# class CarBrand(models.Model):
#     name = models.CharField(max_length=200)
    
# class UserCar(models.Model):
#     model = models.ForeignKey(CarBrand, on_delete=models.CASCADE)