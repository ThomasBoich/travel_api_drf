from rest_framework import serializers
from travels.models import Travel, Country
from users.serializers import CitySerializer, CustomUserSerializer
from .models import Trip, TripOther

class TripOtherSerializer(serializers.ModelSerializer):
    class Meta:
        model = TripOther
        fields = '__all__'

class TripSerializer(serializers.ModelSerializer):
    cityin = CitySerializer()
    user = CustomUserSerializer()
    cityin = CitySerializer(read_only=True)
    city = CitySerializer(read_only=True)
    trip_users = CustomUserSerializer(read_only=True, many=True)
    trip_car = CitySerializer(read_only=True)
    trip_others = TripOtherSerializer(many=True)
    

    class Meta:
        model = Trip
        fields = '__all__'
