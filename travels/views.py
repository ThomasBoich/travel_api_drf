from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Count, Q
from .models import Travel, Country
from .serializers import TravelSerializer, CountrySerializer
from users.models import City
from users.serializers import CitySerializer
from rest_framework import status

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

# class TravelViewSet(generics.ListAPIView):
#     def get_queryset(self):
#         queryset = Travel.objects.all()
#         country_name = self.request.query_params.get('country')
#         city_name = self.request.query_params.get('city')
#         interest_name = self.request.query_params.get('interest')
#         from_moscow = self.request.query_params.get('from_moscow')

#         if country_name:
#             queryset = queryset.filter(country__name=country_name).distinct()
#         if city_name:
#             queryset = queryset.filter(from_city__name=city_name).distinct()
#         if country_name and city_name:
#             queryset = queryset.filter(Q(from_city__name=city_name), Q(country__name=country_name))
#         if country_name and city_name and interest_name:
#             queryset = queryset.filter(Q(from_city__name=city_name), Q(country__name=country_name), Q(gender_search=interest_name))
#         if interest_name:
#             interest = Interests.objects.filter(name=interest_name).first()
#             if interest:
#                 queryset = queryset.filter(interests=interest)
#         if from_moscow:
#             queryset = queryset.filter(from_city__name=from_moscow).distinct()

#         return queryset


class CountryViewSet(viewsets.ModelViewSet):
    # queryset = Country.objects.annotate(travel_count=Count('travels'))
    queryset = Country.objects.annotate(travel_count=Count('travels'))
    # queryset = Country.with_travel_counts()
    serializer_class = CountrySerializer

    # @action(detail=False, methods=['get'])
    # def total_country_count(self, request):
    #     total_count = Country.objects.count()
    #     return Response({'total_country_count': total_count})
    
class CityViewSet(viewsets.ModelViewSet):
    # queryset = Country.objects.annotate(travel_count=Count('travels'))
    queryset = City.objects.all()
    # queryset = Country.with_travel_counts()
    serializer_class = CitySerializer

    # @action(detail=False, methods=['get'])
    # def total_country_count(self, request):
    #     total_count = Country.objects.count()
    #     return Response({'total_country_count': total_count})
    
class TravelViewSetFromMoscow(viewsets.ModelViewSet):
    queryset = Travel.objects.filter(from_city__name='Москва')[0:3]
    serializer_class = TravelSerializer
    
from django.shortcuts import render, redirect
from .forms import TravelForm

def create_travel(request):
    if request.method == 'POST':
        form = TravelForm(request.POST, user=request.user)
        if form.is_valid():
            new_travel = form.save()
            return redirect('travel', travel_id=new_travel.id)  # Redirect to the created travel page
    else:
        form = TravelForm(user=request.user)
    return render(request, 'pages/create_travel.html', {'form': form})

class TravelListAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        from_city_name = request.query_params.get('from_city')
        country_name = request.query_params.get('country')

        queryset = Travel.objects.all()

        if from_city_name:
            queryset = queryset.filter(from_city__name=from_city_name)
        if country_name:
            queryset = queryset.filter(country__name=country_name)

        serializer = TravelSerializer(queryset, many=True)
        return Response(serializer.data)





from rest_framework.permissions import AllowAny

class TravelFilterView(APIView):
    permission_classes = [AllowAny]  # Разрешаем доступ всем

    def post(self, request):
        from_city_name = request.data.get('from_city')
        to_country_name = request.data.get('to_country')
        what_query = request.data.get('what')
        print(f'from_city_name {from_city_name}')
        print(what_query)
        from_city = False
        to_country = False
        what = None

        if what_query == 'Не важно':
            what = None
        if what_query == 'Мужчину':
            what = 'Женщину'
        if what_query == 'Женщину':
            what = 'Мужчину'
        if what_query == 'Семью':
            what = 'Семью'
        

        if from_city_name == False:
            to_country = Country.objects.get(name=to_country_name)
        elif from_city_name and to_country_name == False:
            from_city = City.objects.get(name=from_city_name)
            to_country = False            
        else:
            from_city = City.objects.get(name=from_city_name)
            to_country = Country.objects.get(name=to_country_name)
        
        print(f'from_city {from_city}')
        print(f'to_country {to_country_name}')
        
        try:
            if from_city_name == False and to_country_name:
                if what == None:
                    travels = Travel.objects.filter(country=to_country)
                    serializer = TravelSerializer(travels, many=True)
                    print('Выполнилось без города')
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:                    
                    travels = Travel.objects.filter(country=to_country, gender_search=what)
                    serializer = TravelSerializer(travels, many=True)
                    print('Выполнилось без города')
                    return Response(serializer.data, status=status.HTTP_200_OK)
            if from_city_name and to_country_name == False:
                if what == None:                
                    travels = Travel.objects.filter(from_city=from_city)
                    serializer = TravelSerializer(travels, many=True)
                    print('Выполнилось без страны')
                    print(what)
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    travels = Travel.objects.filter(from_city, gender_search=what)
                    serializer = TravelSerializer(travels, many=True)
                    print('Выполнилось без страны')
                    print(what)
                    return Response(serializer.data, status=status.HTTP_200_OK)
            if from_city_name and to_country_name:
                if what == None:
                    travels = Travel.objects.filter(from_city=from_city, country=to_country)
                    serializer = TravelSerializer(travels, many=True)
                    print('Выполнилось с городом')
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:                    
                    travels = Travel.objects.filter(from_city=from_city, country=to_country, gender_search=what)
                    serializer = TravelSerializer(travels, many=True)
                    print('Выполнилось с городом')
                    return Response(serializer.data, status=status.HTTP_200_OK)
            if from_city_name == False and to_country_name == False:
                if what == None:
                    travels = Travel.objects.all()
                    serializer = TravelSerializer(travels, many=True)
                    print('Выполнилось с городом')
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:                    
                    travels = Travel.objects.filter(gender_search=what)
                    serializer = TravelSerializer(travels, many=True)
                    print('Выполнилось с городом')
                    return Response(serializer.data, status=status.HTTP_200_OK)               
        except Travel.DoesNotExist:
            return Response([], status=status.HTTP_200_OK)

        # try:
        #     from_city = City.objects.get(name=from_city_name)
        #     to_country = Country.objects.get(name=to_country_name)
        # except (City.DoesNotExist, Country.DoesNotExist):
        #     return Response(
        #         {"error": "Город или страна не найдены"},
        #         status=status.HTTP_404_NOT_FOUND
        #     )


class TravelFilterInfoView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        travel_id = request.data.get('travel_id')
        try:
            travels = Travel.objects.get(id=travel_id)
            serializer = TravelSerializer(travels)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Travel.DoesNotExist:
            return Response([], status=status.HTTP_200_OK)


class UserTravelsFilterInfoView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, user_id):
        travels = Travel.objects.filter(user=user_id)
        serializer = TravelSerializer(travels, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)