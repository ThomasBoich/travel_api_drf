from django.shortcuts import render,redirect
from django.urls import reverse_lazy
# Create your views here.
from django.http import HttpResponse
from django.views.generic import CreateView
from rest_framework import viewsets
from .models import CustomUser, Interests, Habits, Friends, Favorites
from .serializers import CustomUserSerializer, InterestsSerializer, HabitsSerializer

from .forms import CustomUserCreationForm

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class InterestsViewSet(viewsets.ModelViewSet):
    queryset = Interests.objects.all()
    serializer_class = InterestsSerializer

class HabitsViewSet(viewsets.ModelViewSet):
    queryset = Habits.objects.all()
    serializer_class = HabitsSerializer
    
def addToFriends(request, user_id):
    user = request.user
    friend = CustomUser.objects.get(id=user_id)
    friends, created = Friends.objects.get_or_create(user=user)
    friends.friends.add(friend)
    return redirect('index')

def addFavorites(request, user_id):
    user = request.user
    favorit = CustomUser.objects.get(id=user_id)
    favorites, created = Favorites.objects.get_or_create(user=user)
    favorites.favorites.add(favorit)
    return redirect('index')


from django.http import JsonResponse
from yookassa import Payment

from travelo.settings import YOOKASSA_SHOP_ID, YOOKASSA_SECRET_KEY

def create_payment(request):
    if request.method == 'POST':
        summa = request.POST.get('summa')
        user = request.user.email
        
        payment = Payment.create({
            "amount": {
                "value": f"{summa}",  # Сумма платежа
                "currency": "RUB"  # Валюта
            },
            "confirmation": {
                "type": "redirect",
                "return_url": "https://kudaugodno.com"  # URL для возврата после оплаты
            },
            "capture": True,
            "description": f"Покупка VIP Статуса пользователем: {user}"
        }, shop_id=YOOKASSA_SHOP_ID, secret_key=YOOKASSA_SECRET_KEY)

        # Перенаправляем пользователя на страницу YooKassa для ввода данных карты
        return redirect(payment.confirmation.confirmation_url)
    else:
        return redirect('index')