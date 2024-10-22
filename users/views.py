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
from yookassa import Payment, Configuration

from travelo.settings import YOOKASSA_SHOP_ID, YOOKASSA_SECRET_KEY
import uuid

Configuration.account_id = YOOKASSA_SHOP_ID
Configuration.secret_key = YOOKASSA_SECRET_KEY

def create_payment(request):
    if request.method == 'POST':
        summa = request.POST.get('summa')
        user = request.user.email
        idempotence_key = str(uuid.uuid4())
        payment = Payment.create({
                "id": 500,
                "status": "pending",
                "paid": False,
                "capture": True,
                "amount": {
                "value": 999.00,
                "currency": "RUB"
                },
                "payment_method_data": {
                "type": "bank_card"
                },
                "confirmation": {
                "type": "redirect",
                "return_url": "https://kudaugodno.com"
                },
                "description": ""
            }, idempotence_key)

        # Перенаправляем пользователя на страницу YooKassa для ввода данных карты
        return redirect(payment.confirmation.confirmation_url)
    else:
        return redirect('index')