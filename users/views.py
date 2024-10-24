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

Configuration.account_id = "478867"
Configuration.secret_key = "test_k-_pd0qm2t0fkZDKmNYwoLwnpPAn4XhOxFD2OSSOJXo"

def create_payment(request):
    if request.method == 'POST':
        summa = request.POST.get('summa')
        user = request.user.email
        idempotence_key = str(uuid.uuid4())
        payment = Payment.create({
                "id": request.user.id,
                "status": "pending",
                "paid": False,
                "capture": True,
                "amount": {
                "value": 399.00,
                "currency": "RUB"
                },
                "payment_method_data": {
                "type": "bank_card"
                },
                "metadata": {
                    "user_id": request.user.id
                },
                "confirmation": {
                "type": "redirect",
                "return_url": "https://kudaugodno.com"
                },
                "description": "Оформление подписки на сайте",
                "receipt": {
                    "items": [
                        {
                            "description": "ВИП Подписка На Сайте",  # Название товара
                            "quantity": 1.0,  # Количество
                            "amount": {
                                "value": 399.00,  # Сумма товара
                                "currency": "RUB"
                            },
                            "vat_code": 1  # Код НДС (если требуется)
                        }
                    ],
                    "email": request.user.email,
                    "phone": request.user.phone,
                },
                "refundable": False,
                "test": True               
            }, idempotence_key)

        # Перенаправляем пользователя на страницу YooKassa для ввода данных карты
        return redirect(payment.confirmation.confirmation_url)
    else:
        return redirect('index')


from django.views.decorators.csrf import csrf_exempt
import json
from datetime import datetime
@csrf_exempt
def activate_premium(request):

    if request.method == 'POST':

        notification = json.loads(request.body)
        try:
            # Проверяем, что это событие успешного платежа
            if notification.get('event') == 'payment.succeeded':
                payment_id = notification['object']['id']
                user_id = notification['object']['metadata']['user_id']
            
            premium = CustomUser.objects.get(id=user_id)

            premium.premium = True
            premium.premium_activate = datetime.now()
            premium.save()

            return redirect('index')
        except:
            return redirect('index')

    else:
        return redirect('index')
    