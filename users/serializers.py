from rest_framework import serializers
from .models import CustomUser, Interests, Habits

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

class InterestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interests
        fields = '__all__'

class HabitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habits
        fields = '__all__'