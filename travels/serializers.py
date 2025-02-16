from rest_framework import serializers
from .models import Travel, Country
from users.serializers import CitySerializer, CustomUserSerializer

class CountrySerializer(serializers.ModelSerializer):
    travel_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Country
        fields = ['id', 'name', 'image', 'travel_count']

class TravelSerializer(serializers.ModelSerializer):
    from_city = CitySerializer()
    country = CountrySerializer(many=True, read_only=True)
    user = CustomUserSerializer()
    from_city = CitySerializer(read_only=True)

    class Meta:
        model = Travel
        fields = '__all__'
