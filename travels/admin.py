from django.contrib import admin
from .models import Travel, Country
# Register your models here.

class TravelAdmin(admin.ModelAdmin):
    list_display = ('city',)
    search_fields = ('city',)

class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Travel, TravelAdmin)
admin.site.register(Country, CountryAdmin)
