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
        total_count = Travel.objects.count()
        return Response({'total_travel_count': total_count})

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.annotate(travel_count=Count('travels'))
    serializer_class = CountrySerializer
    @action(detail=False, methods=['get'])
    def total_country_count(self, request):
        total_count = Country.objects.count()
        return Response({'total_country_count': total_count})