from django.shortcuts import render
from users.forms import CustomUserRegistrationForm
from .forms import TravelersForm
from users.models import CustomUser, City, Interests
from travels.models import Travel, Country
# Create your views here.

def travelers(request):
    form_travelers = TravelersForm(user=request.user)
    countries = Country.objects.all()
    travels = Travel.objects.all()
    cities = City.objects.all()
    users = CustomUser.objects.all()
    users = CustomUser.objects.all()
    interests = Interests.objects.all()
    countries_from_moscow = Country.objects.filter(travels__from_city__name='Москва').distinct()[0:3]
    context = {
        'form_travelers': form_travelers,
        'countries': countries[:12],
        'countries_list': countries,
        'total_popular_countries': countries.count(),
        'travels': travels,
        'cities': cities,
        'users': users[0:5],
        'title': f'Travelo',
        'interests': interests,
        'countries_from_moscow': countries_from_moscow,
        'countries_from_moscow_count': countries_from_moscow.count(),
        'form_reg': CustomUserRegistrationForm(request.POST)
    }
    return render(request, 'travelers.html', context)



from django.shortcuts import render, redirect
from .forms import TravelersForm

def create_trip(request):
    if request.method == 'POST':
        form = TravelersForm(request.POST, user=request.user)
        if form.is_valid():
            new_trip = form.save()
            return redirect('trip', travel_id=new_trip.id)  # Redirect to the created travel page
    else:
        form = TravelersForm(user=request.user)
    return render(request, 'index.html', {'trip_form': form})