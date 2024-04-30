from django.shortcuts import render, redirect
from django.contrib.auth import logout

from travels.models import Country, Travel
from users.models import City, CustomUser, Interests
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
    countries_from_moscow = Country.objects.filter(travels__from_city__name='Москва').distinct()
    context = {
        'countries': countries[:12],
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
    context = {
        'travels': travels,
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