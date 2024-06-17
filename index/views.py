from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.db.models import Q
from django.shortcuts import get_object_or_404
from travels.models import Country, Travel
from users.models import City, CustomUser, Interests, Habits
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.contrib.auth import authenticate, login
from users.forms import LoginForm, CustomUserCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy
# Create your views here.
def index(request):
    countries = Country.objects.all()
    travels = Travel.objects.all()
    cities = City.objects.all()
    users = CustomUser.objects.all()
    users = CustomUser.objects.all()
    interests = Interests.objects.all()
    countries_from_moscow = Country.objects.filter(travels__from_city__name='Москва').distinct()[0:3]
    context = {
        'countries': countries[:12],
        'countries_list': countries,
        'total_popular_countries': countries.count(),
        'travels': travels,
        'cities': cities,
        'users': users,
        'title': f'Travelo',
        'interests': interests,
        'countries_from_moscow': countries_from_moscow,
        'countries_from_moscow_count': countries_from_moscow.count(),
    }
    return render(request, 'index.html', context)

def about(request):
    context = {}
    return render(request, 'about.html', context)

def me(request):
    travels = Travel.objects.all()
    user = CustomUser.objects.get(id=request.user.id)
    context = {
        'travels': travels,
        'user': user,
        'title': f'{user.first_name}',
    }
    return render(request, 'profile.html', context)


def profile(request, user_id):
    travels = Travel.objects.all()
    user = CustomUser.objects.get(id=user_id)
    interests = Interests.objects.filter(users_interests=user)
    habits = Habits.objects.filter(user_habits=user)
    context = {
        'travels': travels,
        'habits': habits,
        'interests': interests,
        'user': user,
        'title': f'{user.first_name}',
    }
    return render(request, 'profile.html', context)

def user_logout(request):
    logout(request)
    return redirect('index')


# class AppLoginView(LoginView):
#     form_class = LoginForm
#     template_name = 'navigation.html'
#     success_url = reverse_lazy('index')
#     def get_success_url(self):
#         return reverse_lazy('index')
    
from django.contrib.auth.views import LoginView, LogoutView
from users.forms import LoginForm, CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from users.forms import LoginForm

class AppLoginView(LoginView):
    form_class = LoginForm
    template_name = 'navigation.html'
    success_url = reverse_lazy('index')
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('index')

    def form_valid(self, form):
        print("Form is valid")
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        print("Email:", email)
        print("Password:", password)

        user = form.get_user()
        if user is not None:
            print("User found:", user)
            self.request.session.cycle_key()  # Обновляем сеанс после успешного входа
            login(self.request, user)
            print("User logged in")
            return HttpResponseRedirect(self.get_success_url())
        else:
            print("User not found")
            return super().form_invalid(form)
        

from django.views import View
from users.forms import UserUpdateForm
from django.views.generic import UpdateView
class UpdateUserView(UpdateView):
    model = CustomUser
    form_class = UserUpdateForm
    template_name = 'settings.html'
    pk_url_kwarg = 'user_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['interests'] = user.interests.all()
        context['all_interests'] = Interests.objects.all()
        context['habits'] = Habits.objects.all()
        context['cities'] = City.objects.all()
        return context

    def get_success_url(self):
        return reverse_lazy('update_user', kwargs={'user_id': self.object.pk})
    

def travels(request):
    if request.method == 'GET':
        travels = Travel.objects.all()
        from_moscow = Country.objects.filter(travels__from_city__name='Москва').distinct()
        travels_title = f'Поиск поездок - {travels.count()} шт.'
        country_name = request.GET.get('country')
        city_name = request.GET.get('city')
        interest_name = request.GET.get('interest')
        from_moscow = request.GET.get('from_moscow')
        cities = City.objects.all()
        filters = Q()
        
        if country_name:
            travels_title = f'Поиск поездок в {country_name}'
            travels = Travel.objects.filter(country__name=country_name).distinct()
        
        if city_name:
            travels_title = f'Поиск поездок из города {city_name}'
            travels = Travel.objects.filter(from_city__name=city_name).distinct()
        
        if country_name and city_name:
            travels = Travel.objects.filter(Q(from_city__name=city_name), Q(country__name=country_name))
            travels_title = f"Поездки: {city_name} — {country_name}"

        if country_name and city_name and interest_name:
            travels = Travel.objects.filter(Q(from_city__name=city_name), Q(country__name=country_name), Q(gender_search=interest_name))
            travels_title = f"Поездки: {city_name} — {country_name}"

        if interest_name:
            interest = get_object_or_404(Interests, name=interest_name)
            filters &= Q(interests=interest)

        if from_moscow:
            travels = Country.objects.filter(travels__from_city__name=from_moscow).distinct()
            travels_title = f'Популярные направления из Москвы'

        if not country_name and not city_name and not interest_name:
            travels = Travel.objects.all()
            travels_title = f'Поиск поездок - {travels.count()} шт.'
            
    context = {
        'title': f'Travelo',
        'travels_title': travels_title,
        'travels': travels,
        'from_moscow': from_moscow,
        'countries_list': Country.objects.all(),
        'cities': cities,
    }
    return render(request, 'travels.html', context)
    #   else:
    #     travels = Travel.objects.filter(filters)
    #     travels_title = 'Поиск поездок'
    
    
from travels.models import *
def travel(request, travel_id):
    context = {
        'travel': Travel.objects.get(id=travel_id),
    }
    return render(request, 'travel.html', context)