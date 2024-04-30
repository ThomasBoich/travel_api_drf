from django.urls import path, include
from .views import index, profile, user_logout, AppLoginView,UpdateUserView

urlpatterns = [
    path('', index, name='index'),
    path('profile/<user_id>/', profile, name='profile'),
    path('profile/settings/<int:user_id>/', UpdateUserView.as_view(), name='update_user'),
    path('logout/', user_logout, name='logout'),
    path('login/', AppLoginView.as_view(), name='custom_login'),
]