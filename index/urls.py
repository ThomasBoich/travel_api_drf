from django.urls import path, include
from .views import index, profile, user_logout, AppLoginView,UpdateUserView,travels,about,travel,register_user,chats,message,folder,folderCreate,users,tarifs,friends,favorites,trips,trip
from trips.views import travelers,create_trip,trip_boocking,close_boocking
from travels.views import create_travel
from chat.views import private_chat, send_message, display_messages
from users.views import addToFriends, addFavorites

from users.decorators import check_recaptcha

urlpatterns = [
    path('', index, name='index'),
    path('travelers/', travelers, name='travelers'),
    path('about/', about, name='about'),
    path('tarifs/', tarifs, name='tarifs'),
    path('friends/', friends, name='friends'),
    path('favorits/', favorites, name='favorits'),
    path('profile/<user_id>/', profile, name='profile'),
    path('profile/settings/<int:user_id>/', UpdateUserView.as_view(), name='update_user'),
    path('logout/', user_logout, name='logout'),
    path('login/', AppLoginView.as_view(), name='custom_login'),
    path('registration/', check_recaptcha(register_user), name='register_user'),
    path('travels/', travels, name='travels'),
    path('trips/', trips, name='trips'),
    path('trip_boocking/<int:trip_id>/', trip_boocking, name='trip_boocking'),
    path('close_boocking/<int:trip_id>/', close_boocking, name='close_boocking'),
    path('users/', users, name='users'),
    path('travel/<travel_id>/', travel, name='travel'),
    path('trip/<trip_id>/', trip, name='trip'),
    path('create_travel', create_travel, name='create_travel'),
    path('create_trip/', create_trip, name='create_trip'),
    path('chats/', chats, name='chats'),
    path('chats/folder/<int:folder_id>/', folder, name='folder'),
    path('chats/folderCreate/', folderCreate, name='folderCreate'),
    path('chats/message/<int:recipient_id>/', message, name='message'),        
    path('private_chat/<int:recipient_id>/', private_chat, name='private_chat'),
    path('send_message/<int:recipient_id>/', send_message, name='send_message'),
    path('display_messages/<int:recipient_id>/', display_messages, name='display_messages'),
    path('add_friend/<int:user_id>/', addToFriends, name="addToFriends"),
    path('add_favorites/<int:user_id>/', addFavorites, name="addFavorites")
    # path('display_messages/<int:recipient_id>/', display_messages, name='display_messages'),
]