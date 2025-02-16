from rest_framework import serializers
from travels.models import Travel, Country
from users.serializers import CitySerializer, CustomUserSerializer
from .models import Trip

class TripSerializer(serializers.ModelSerializer):
    cityin = CitySerializer()
    user = CustomUserSerializer()
    cityin = CitySerializer(read_only=True)

    class Meta:
        model = Trip
        fields = '__all__'
