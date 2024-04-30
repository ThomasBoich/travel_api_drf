from django.urls import path, include
from .views import index, profile, user_logout, AppLoginView

urlpatterns = [
    path('', index, name='index'),
    path('profile/<user_id>/', profile, name='profile'),
    path('logout/', user_logout, name='logout'),
    path('login/', AppLoginView.as_view(), name='custom_login'),
]