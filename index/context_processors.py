from typing import Any

from django.db.models import QuerySet

from travels.models import City, Country

def get_cities(request):
    cities_as: QuerySet[Any] = City.objects.all()
    return {'cities_as': cities_as}

def get_countries(request):
    return {'countries_as': Country.objects.all()}

