from django.shortcuts import render
from django.urls import reverse_lazy
# Create your views here.

from django.views.generic import CreateView
from rest_framework import viewsets
from .models import CustomUser, Interests, Habits
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
    