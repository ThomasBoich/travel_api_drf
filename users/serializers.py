from rest_framework import serializers
from .models import CustomUser, Interests, Habits, City

class InterestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interests
        fields = '__all__'

class HabitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habits
        fields = '__all__'

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class CustomUserSerializer(serializers.ModelSerializer):
    habits = HabitsSerializer()
    iterests = InterestsSerializer()
    class Meta:
        model = CustomUser
        fields = '__all__'