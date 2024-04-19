from django.shortcuts import render

from travels.models import Country, Travel
from users.models import City, CustomUser


# Create your views here.

def index(request):
    countries = Country.objects.all()
    travels = Travel.objects.all()
    cities = City.objects.all()
    users = CustomUser.objects.all()
    context = {
        'countries': countries,
        'travels': travels,
        'cities': cities,
        'users': users,
        'title': f'Travelo',
    }
    return render(request, 'index.html', context)


def me(request):
    travels = Travel.objects.all()
    user = CustomUser.get(id=request.user.id)
    context = {
        'travels': travels,
        'user': user,
        'title': f'{user.first_name}',
    }
    return render(request, 'index.html', context)


def profile(request, user_id):
    travels = Travel.objects.all()
    user = CustomUser.get(id=user_id)
    context = {
        'travels': travels,
        'user': user,
        'title': f'{user.first_name}',
    }
    return render(request, 'index.html', context)