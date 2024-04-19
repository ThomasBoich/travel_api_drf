from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Count
from .models import Travel, Country
from .serializers import TravelSerializer, CountrySerializer

class TravelViewSet(viewsets.ModelViewSet):
    queryset = Travel.objects.all()
    serializer_class = TravelSerializer
    @action(detail=False, methods=['get'])
    def total_travel_count(self, request):
        travels = Travel.objects.all()
        total_count = travels.count()

        return Response({'total_travel_count': total_count})

    @action(detail=False, methods=['get'])
    def countries_from_moscow(self, request):
        countries_from_moscow = Country.objects.filter(travels__from_city__name='Москва').distinct()
        serializer = CountrySerializer(countries_from_moscow, many=True)
        return Response(serializer.data)


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.annotate(travel_count=Count('travels'))
    serializer_class = CountrySerializer

    @action(detail=False, methods=['get'])
    def total_country_count(self, request):
        total_count = Country.objects.count()
        return Response({'total_country_count': total_count})