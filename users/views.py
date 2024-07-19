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