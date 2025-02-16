from django.shortcuts import render,redirect
from django.urls import reverse_lazy
# Create your views here.
from django.http import HttpResponse
from django.views.generic import CreateView
from rest_framework import viewsets
from .models import CustomUser, Interests, Habits, Friends, Favorites
from .serializers import CustomUserSerializer, InterestsSerializer, HabitsSerializer
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication

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


from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny, IsAuthenticated
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from .serializers import RegisterSerializer
from rest_framework import generics, status, viewsets

class JWTRegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    # @staticmethod
    # def send_confirmation_email(user, request):
    #     # Генерация uid и JWT токена
    #     uid = urlsafe_base64_encode(force_bytes(user.pk))
    #     token = RefreshToken.for_user(user).access_token

    #     mail_subject = 'Подтвердите ваш email'

    #     # Генерация ссылки для подтверждения
    #     activation_link = f"{request.scheme}://{settings.FRONTEND_DOMAIN}/auth/registration?uid={uid}&token={token}"

    #     message = (
    #         f"Здравствуйте, {user.username}!\n\n"
    #         "Пожалуйста, подтвердите ваш email, перейдя по ссылке ниже:\n"
    #         f"{activation_link}\n\n"
    #         "Если вы не регистрировались на нашем сайте, проигнорируйте это письмо.\n"
    #     )

    #     send_mail(mail_subject, message, settings.DEFAULT_FROM_EMAIL, [user.email])

    @swagger_auto_schema(
        operation_summary="Создать пользователя",
        operation_description="Регистрирует нового пользователя. Реферальный код является необязательным.",
        request_body=RegisterSerializer,
        responses={
            201: openapi.Response(
                description="Пользователь успешно создан и ожидает подтверждения email.",
                examples={
                    "application/json": {
                        "message": "Пользователь успешно создан. Пожалуйста, подтвердите ваш email."
                    }
                }
            ),
            400: openapi.Response(
                description="Ошибка валидации или проблема с реферальным кодом (если указан).",
                examples={
                    "application/json": {
                        "error": "Реферальный код не существует."
                    }
                }
            ),
            500: "Ошибка при создании пользователя."
        }
    )
    @csrf_exempt
    def post(self, request, *args, **kwargs):
        try:
            # Валидируем входные данные
            # email, username, password, referral_code_value = self._validate_request_data(request)
            email, password = self._validate_request_data(request)

            # Проверяем существование пользователя с таким email
            existing_user = self._check_existing_user(email, request)
            if existing_user:
                return existing_user

            # Проверяем реферальный код
            # inviter = self._validate_referral_code(referral_code_value)

            # Создаем пользователя через сервис
            # user = UserService.create_user(email, username, password, inviter=inviter)
            user, create = CustomUser.objects.get_or_create(email=email)
            user.is_active = True
            user.set_password(password)
            user.save()

            # Отправляем подтверждение email
            # self.send_confirmation_email(user, request)

            return Response({
                "message": "Пользователь успешно создан. Пожалуйста, подтвердите ваш email."
            }, status=201)

        except ValidationError as e:
            return Response({"error": str(e)}, status=400)
        except Exception as e:
            return Response({"error": str(e)}, status=500)

    # Частные методы для декомпозиции логики
    @staticmethod
    def _validate_request_data(request):
        """
        Проверяет входные данные и выбрасывает ValidationError при ошибке.
        """
        email = request.data.get('email')
        # username = request.data.get('username')
        password = request.data.get('password')
        # referral_code_value = request.data.get('referral_code')

        if not email:
            raise ValidationError("Email обязателен.")
        # if not username:
            # raise ValidationError("Имя пользователя обязательно.")
        if not password:
            raise ValidationError("Пароль обязателен.")

        # return email, username, password, referral_code_value
        return email, password

    def _check_existing_user(self, email, request):
        """
        Проверяет, существует ли пользователь с указанным email.
        Возвращает Response или None.
        """
        existing_user = CustomUser.objects.filter(email=email).first()
        if existing_user:
            if not existing_user.is_active:
                # self.send_confirmation_email(existing_user, request)
                return Response({
                    "message": "Пользователь уже зарегистрирован, но не активирован. Письмо отправлено повторно."
                }, status=200)
            else:
                return Response({
                    "error": "Пользователь с таким email уже существует и активирован."
                }, status=400)
        return None

    # @staticmethod
    # def _validate_referral_code(referral_code_value):
    #     """
    #     Проверяет валидность реферального кода и возвращает пользователя, пригласившего.
    #     Если реферальный код отсутствует, возвращает None.
    #     """
    #     if not referral_code_value:
    #         return None

    #     referral_code = ReferralCode.objects.filter(code=referral_code_value).first()
    #     if not referral_code:
    #         raise ValidationError("Реферальный код не существует.")
    #     return referral_code.user

class JWTLoginView(TokenObtainPairView):
    permission_classes = (AllowAny,)

    @swagger_auto_schema(
        operation_summary="Авторизация пользователя",
        operation_description="Выполняет авторизацию пользователя и возвращает access и refresh токены.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'email': openapi.Schema(type=openapi.TYPE_STRING, description='Email пользователя'),
                'password': openapi.Schema(type=openapi.TYPE_STRING, description='Пароль пользователя'),
            },
            required=['email', 'password']
        ),
        responses={
            200: openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'access_token': openapi.Schema(type=openapi.TYPE_STRING, description='Access токен для доступа'),
                    'refresh_token': openapi.Schema(type=openapi.TYPE_STRING,
                                                    description='Refresh токен для обновления'),
                }
            ),
            401: "Неверные учетные данные"
        }
    )
    @csrf_exempt
    def post(self, request, *args, **kwargs):
        # Получаем стандартные токены через родительский метод
        response = super().post(request, *args, **kwargs)

        # Изменяем имена ключей в ответе
        response_data = response.data
        return Response({
            'access_token': response_data.get('access'),
            'refresh_token': response_data.get('refresh'),
        })


from rest_framework import permissions, generics, viewsets
from rest_framework.exceptions import AuthenticationFailed, NotFound, ValidationError
# from .services import UserService

class JWTLogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(
        operation_summary="Логаут пользователя",
        operation_description="Удаляет refresh-токен из черного списка, чтобы завершить сессию пользователя.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'refresh_token': openapi.Schema(type=openapi.TYPE_STRING, description='Refresh токен пользователя'),
            },
            required=['refresh_token']
        ),
        responses={
            205: "Logout successful",
            400: "Invalid token or request data"
        }
    )
    @csrf_exempt
    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=205)
        except Exception as e:
            return Response(status=400)


class UserProfileInfoView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    serializer_class = CustomUserSerializer

    @swagger_auto_schema(
        operation_summary="Получение информации о пользователе",
        operation_description="Возвращает данные о текущем авторизованном пользователе.",
        responses={
            200: openapi.Response(
                description="Информация о пользователе",
                schema=serializer_class
            ),
            401: "Неверные или отсутствующие учетные данные",
        },
        manual_parameters=[
            openapi.Parameter(
                'Authorization',
                openapi.IN_HEADER,
                description="JWT токен для авторизации",
                type=openapi.TYPE_STRING,
                required=True
            )
        ]
    )
    def get(self, request):
        user = request.user
        serializer = self.serializer_class(user)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Обновление информации о пользователе",
        operation_description="Позволяет обновить часть данных текущего авторизованного пользователя.",
        request_body=serializer_class,
        responses={
            200: openapi.Response(
                description="Успешное обновление данных",
                schema=serializer_class
            ),
            400: "Неверные данные",
            401: "Неверные или отсутствующие учетные данные",
        }
    )
    def patch(self, request):
        user = request.user
        serializer = self.serializer_class(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)