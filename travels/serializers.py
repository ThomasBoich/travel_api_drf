from rest_framework import serializers
from .models import Travel, Country

class TravelSerializer(serializers.ModelSerializer):
    travel_count = serializers.IntegerField(read_only=True)
    class Meta:
        model = Travel
        fields = '__all__'

class CountrySerializer(serializers.ModelSerializer):
    travel_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Country
        fields = ['id', 'name', 'image', 'travel_count']