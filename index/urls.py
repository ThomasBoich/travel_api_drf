from django.urls import path, include
from .views import index, profile, user_logout, AppLoginView,UpdateUserView,travels,about,travel

urlpatterns = [
    path('', index, name='index'),
    path('/about', about, name='about'),
    path('profile/<user_id>/', profile, name='profile'),
    path('profile/settings/<int:user_id>/', UpdateUserView.as_view(), name='update_user'),
    path('logout/', user_logout, name='logout'),
    path('login/', AppLoginView.as_view(), name='custom_login'),
    path('travels/', travels, name='travels'),
    path('travel/<travel_id>/', travel, name='travel')
]