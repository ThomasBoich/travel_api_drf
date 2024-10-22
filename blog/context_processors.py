from typing import Any
from django.db.models import QuerySet
from travels.models import City, Country, Travel
from chat.models import Dialog, Message
from chat.models import *
from django.db.models import Q
from .models import Category




def get_categories(request):
    categories = Category.objects.all()
    return {'categories': categories}