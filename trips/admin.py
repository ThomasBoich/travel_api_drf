from django.contrib import admin
from .models import Trip, TripOther
from django import forms
# Register your models here.

class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = '__all__'

    # def __init__(self, *args, **kwargs):
    #     user = kwargs.pop('user', None)
    #     super().__init__(*args, **kwargs)
    #     if user:
    #         self.fields['trip_car'].queryset = user.cars.all()  # Ограничьте выбор машин только для текущего пользователя

class TripAdmin(admin.ModelAdmin):
    form = TripForm
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.user = request.user  # Передаем текущего пользователя в форму
        return form
    list_display = ('user', 'city', 'price',)  # 'trip_date', Укажите поля, которые хотите видеть в списке 'trip_car'
    search_fields = ('user__email', 'city__name')  # Поля для поиска
    list_filter = ('city',)  # Фильтры 'trip_date'

# class UserCarAdmin(admin.ModelAdmin):
#     pass

# class CarBrandAdmin(admin.ModelAdmin):
#     pass

# class CarModelAdmin(admin.ModelAdmin):
#     pass

class TripOtherAdmin(admin.ModelAdmin):
    pass

admin.site.register(Trip, TripAdmin)
# admin.site.register(UserCar, UserCarAdmin)
# admin.site.register(CarBrand, CarBrandAdmin)
# admin.site.register(CarModel, CarModelAdmin)
admin.site.register(TripOther, TripOtherAdmin)