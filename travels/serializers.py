from rest_framework import serializers
from .models import Travel, Country
from users.serializers import CitySerializer

class CountrySerializer(serializers.ModelSerializer):
    travel_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Country
        fields = ['id', 'name', 'image', 'travel_count']

class TravelSerializer(serializers.ModelSerializer):
    travel_count = serializers.IntegerField(read_only=True)
    from_city = CitySerializer()
    country = CountrySerializer()
    class Meta:
        model = Travel
        fields = '__all__'