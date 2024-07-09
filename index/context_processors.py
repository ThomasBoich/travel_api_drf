from typing import Any
from django.db.models import QuerySet
from travels.models import City, Country
from chat.models import Dialog, Message
from chat.models import *
from django.db.models import Q

def get_cities(request):
    cities_as: QuerySet[Any] = City.objects.all()
    return {'cities_as': cities_as}

def get_countries(request):
    return {'countries_as': Country.objects.all()}

def get_dealog(request):
    dialog = Dialog.objects.filter(Q(user=request.user) | Q(with_user=request.user)).first() #recipient,
    # messages = Message.objects.filter(sender=request.user, recipient=recipient) | Message.objects.filter(sender=recipient, recipient=request.user).order_by('timestamp')
    if dialog:
        messages = Message.objects.filter(dialog=dialog).count()
    else:
        messages = []
    return {'dialog_as': messages}