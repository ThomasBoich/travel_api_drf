"""
URL configuration for travelo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers, permissions
from rest_framework.routers import DefaultRouter
from users.views import CustomUserViewSet, InterestsViewSet, HabitsViewSet, JWTLoginView, JWTRegisterView, JWTLogoutView, UserProfileInfoView
from travels.views import TravelViewSet, CountryViewSet, TravelViewSetFromMoscow, TravelListAPIView, CityViewSet, TravelFilterView, TravelFilterInfoView
from trips.views import TripFilterView, TripFilterInfoView, TriplViewSet

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.DefaultRouter()
router.register(r'users', CustomUserViewSet)
router.register(r'travels', TravelViewSet)
router.register(r'trips', TriplViewSet)
router.register(r'countries', CountryViewSet)
router.register(r'cities', CityViewSet)
router.register(r'interests', InterestsViewSet)
router.register(r'habits', HabitsViewSet)
router.register(r'from_moscow', TravelViewSetFromMoscow, basename="from_moscow")


from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="TRAVELO API",
      default_version='v1',
      description="API Для сайта Travelo",
      terms_of_service="https://www.example.com/policies/terms/",
      contact=openapi.Contact(email="contact@example.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

from chat import views as chat_views
from django.urls import re_path
from trips.views import UserTripsFilterInfoView
from travels.views import UserTravelsFilterInfoView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')), #  <- include the allauth urls here
    path('', include('index.urls')),
    path('api/', include(router.urls)),
    path('api/login/', JWTLoginView.as_view(), name='jwt_login'),
    path('api/logout/', JWTLogoutView.as_view(), name='jwt_logout'),
    path('api/register/', JWTRegisterView.as_view(), name='jwt_register'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/profile-info/', UserProfileInfoView.as_view(), name='user_profile'),
    path('api/user/travels/<user_id>/', UserTravelsFilterInfoView.as_view(), name='user_travels'),
    path('api/user/trips/<user_id>/', UserTripsFilterInfoView.as_view(), name='user_trips'),
    # path('api/travels/filter/', TravelFilterView.as_view(), name='travel-filter'),    
    re_path(r'^api/travels/filter/?$', TravelFilterView.as_view(), name='travel-filter'),
    re_path(r'^api/travels/filter/info?$', TravelFilterInfoView.as_view(), name='travel-filter-info'),
    re_path(r'^api/trips/filter/?$', TripFilterView.as_view(), name='trips-filter'),
    re_path(r'^api/trips/filter/info?$', TripFilterInfoView.as_view(), name='trip-filter-info'),
    path('travels/list/', TravelListAPIView.as_view(), name='travel-list'),
    path('api-auth/', include('rest_framework.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # APIs
    # path('online-users/', chat_views.api_online_users, name='online-users'),
    # path('online-users/<int:id>', chat_views.api_online_users, name='online-users'),
    # path('chat-messages/<int:id>', chat_views.api_chat_messages, name='chat_messages'),
    # path('unread/', chat_views.api_unread, name='api_unread'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.site.site_header = settings.ADMIN_SITE_HEADER