from django.urls import path, include
from .views import index, profile, user_logout, AppLoginView,UpdateUserView,travels,about,travel,register_user,chats,message
from travels.views import create_travel

from chat.views import private_chat, send_message

from chat.views import display_messages

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('profile/<user_id>/', profile, name='profile'),
    path('profile/settings/<int:user_id>/', UpdateUserView.as_view(), name='update_user'),
    path('logout/', user_logout, name='logout'),
    path('login/', AppLoginView.as_view(), name='custom_login'),
    path('registration/', register_user, name='register_user'),
    path('travels/', travels, name='travels'),
    path('travel/<travel_id>/', travel, name='travel'),
    path('create_travel', create_travel, name='create_travel'),
    path('chats/', chats, name='chats'),
    path('chats/message/<int:recipient_id>/', message, name='message'),        
    path('private_chat/<int:recipient_id>/', private_chat, name='private_chat'),
    path('send_message/<int:recipient_id>/', send_message, name='send_message'),
    path('display_messages/<int:recipient_id>/', display_messages, name='display_messages'),
    # path('display_messages/<int:recipient_id>/', display_messages, name='display_messages'),
]