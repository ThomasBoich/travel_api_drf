from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .models import CustomUser, Interests, Habits
from .serializers import CustomUserSerializer, InterestsSerializer, HabitsSerializer

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class InterestsViewSet(viewsets.ModelViewSet):
    queryset = Interests.objects.all()
    serializer_class = InterestsSerializer

class HabitsViewSet(viewsets.ModelViewSet):
    queryset = Habits.objects.all()
    serializer_class = HabitsSerializer