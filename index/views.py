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
from travels.forms import TravelForm
from trips.forms import TravelersForm
from trips.models import Trip
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from users.forms import CustomUserRegistrationForm

def register_user(request):
    if request.method == 'POST':
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            # Authenticate and login the user
            username = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                
            return redirect('update_user', user_id=user.id)  # Redirect to the index page after successful registration
    else:
        form = CustomUserRegistrationForm()
    
    return render(request, 'index.html', {'form_reg': form})


def index(request):
    form = TravelForm(user=request.user)
    form_travelers = TravelersForm(user=request.user)
    countries = Country.objects.all()
    travels = Travel.objects.all()
    cities = City.objects.all()
    users = CustomUser.objects.all()
    users = CustomUser.objects.all()
    interests = Interests.objects.all()
    countries_from_moscow = Country.objects.filter(travels__from_city__name='Москва').distinct()[0:3]
    context = {
        'form': form,
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
    return render(request, 'index.html', context)

def travelers(request):
    form = TravelersForm(user=request.user)
    countries = Country.objects.all()
    travels = Travel.objects.all()
    trips = Trip.objects.all()
    cities = City.objects.all()
    users = CustomUser.objects.all()
    users = CustomUser.objects.all()
    interests = Interests.objects.all()
    countries_from_moscow = Country.objects.filter(travels__from_city__name='Москва').distinct()[0:3]
    context = {
        'form': form,
        'countries': countries[:12],
        'countries_list': countries,
        'total_popular_countries': countries.count(),
        'travels': travels,
        'trips': trips,
        'cities': cities,
        'users': users[0:5],
        'title': f'Travelo',
        'interests': interests,
        'countries_from_moscow': countries_from_moscow,
        'countries_from_moscow_count': countries_from_moscow.count(),
        'form_reg': CustomUserRegistrationForm(request.POST)
    }
    return render(request, 'travelers.html', context)

def about(request):
    context = {}
    return render(request, 'about.html', context)

def tarifs(request):
    context = {}
    return render(request, 'tarifs.html', context)

def favorites(request):
    context = {}
    return render(request, 'favorites.html', context)

def friends(request):
    context = {}
    return render(request, 'friends.html', context)

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
    user_travels = Travel.objects.filter(user=user)
    context = {
        'travels': travels,
        'habits': habits,
        'interests': interests,
        'user': user,
        'title': f'{user.first_name}',
        'user_travels': user_travels,
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

def trips(request):
    if request.method == 'GET':
        trips = Trip.objects.all()
        travels_title = f'Поиск поездок - {trips.count()} шт.'
        city_name = request.GET.get('city')
        from_city = request.GET.get('from_city')
        date = request.GET.get('date')
        cities = City.objects.all()
        filters = Q()
        
     
        if from_city:
            travels_title = f'Поиск поездок из города {from_city}'
            trips = Trip.objects.filter(city__name=from_city).distinct()
            
        if date:
            travels_title = travels_title
            trips = Trip.objects.filter(trip_in_time__date=date).distinct()
            
        if from_city and date:
            trips = Trip.objects.filter(Q(city__name=from_city), Q(trip_in_time__date=date)).distinct()
            travels_title = f"Поездки: {from_city} — {date}"
            
        if city_name and date:
            trips = Trip.objects.filter(Q(cityin__name=city_name), Q(trip_in_time__date=date)).distinct()
            travels_title = f"Поездки: в {city_name} — {date}"
            
        if from_city and city_name:
            trips = Trip.objects.filter(Q(city__name=from_city), Q(cityin__name=city_name)).distinct()
            travels_title = f"Поездки: {from_city} — {city_name} — {date}"

        if from_city and city_name and date:
            trips = Trip.objects.filter(Q(cityin__name=city_name), Q(city__name=from_city), Q(trip_in_time__date=date))
            travels_title = f"Поездки: {from_city} — {city_name} — {date}"

        # if interest_name:
        #     interest = get_object_or_404(Interests, name=interest_name)
        #     filters &= Q(interests=interest)

        # if from_moscow:
        #     travels = Country.objects.filter(travels__from_city__name=from_moscow).distinct()
        #     travels_title = f'Популярные направления из Москвы'

        # if not country_name and not city_name and not interest_name:
        #     travels = Travel.objects.all()
        #     travels_title = f'Поиск поездок - {travels.count()} шт.'
            
    context = {
        'title': f'Travelo',
        'travels_title': travels_title,
        'trips': trips,
        # 'countries_list': Country.objects.all(),
        'cities': cities,
    }
    return render(request, 'trips.html', context)
    #   else:
    #     travels = Travel.objects.filter(filters)
    #     travels_title = 'Поиск поездок'


def users(request):
    if request.method == 'GET':
        users_list = CustomUser.objects.all()
        interests = Interests.objects.all()
        #from_moscow = Country.objects.filter(travels__from_city__name='Москва').distinct()
        users_title = f'Поиск друзей - {users_list.count()} шт.'
        #country_name = request.GET.get('country')
        city_name = request.GET.get('city')
        interest_name = request.GET.get('interest')
        #from_moscow = request.GET.get('from_moscow')
        cities = City.objects.all()
        filters = Q()
        
        # if country_name:
        #     travels_title = f'Поиск поездок в {country_name}'
        #     travels = Travel.objects.filter(country__name=country_name).distinct()
        
        if city_name:
            users_title = f'Поиск друзей из города — {city_name}'
            users_list = CustomUser.objects.filter(city__name=city_name).distinct()
        
        if interest_name and city_name:
            interests_list = interest_name.split(',')
            print(interests_list)
            interests = Interests.objects.filter(name=interests_list)
            users_list = CustomUser.objects.filter(city__name=city_name, interests__name=interest_name).distinct()
            users_title = f'Поиск друзей asdasd- {users_list.count()} шт.'

        # if country_name and city_name and interest_name:
        #     travels = Travel.objects.filter(Q(from_city__name=city_name), Q(country__name=country_name), Q(gender_search=interest_name))
        #     travels_title = f"Поездки: {city_name} — {country_name}"

        if interest_name:
            interests_list = interest_name.split(',')
            print(interests_list)
            interests = Interests.objects.filter(name=interests_list)
            users_list = CustomUser.objects.filter(interests__name=interest_name).distinct()
            users_title = f'Поиск друзей - {users_list.count()} шт.'

        # if from_moscow:
        #     travels = Country.objects.filter(travels__from_city__name=from_moscow).distinct()
        #     travels_title = f'Популярные направления из Москвы'

        # if not country_name and not city_name and not interest_name:
        #     travels = Travel.objects.all()
        #     travels_title = f'Поиск поездок - {travels.count()} шт.'
            
    context = {
        'title': f'Travelo',
        'users_title': users_title,
        #'travels': travels,
        'users_list': users_list,
        'cities': cities,
        'interests': interests,
    }
    return render(request, 'users.html', context)
    #   else:
    #     travels = Travel.objects.filter(filters)
    #     travels_title = 'Поиск поездок'

def travel(request, travel_id):
    travel = Travel.objects.get(id=travel_id)
    user = travel.user
    context = {
        'travel': travel,
        'user_travels': Travel.objects.filter(user=user),
    }
    return render(request, 'travel.html', context)

def trip(request, trip_id):
    trip = Trip.objects.get(id=trip_id)
    user = trip.user
    context = {
        'trip': trip,
        'user_trips': Trip.objects.filter(user=user),
    }
    return render(request, 'trip.html', context)


from chat.models import *
from django.db.models import Q
from chat.forms import MessageForm,FolderForm
@login_required
def chats(request):
    user = request.user
    dialogs = Dialog.objects.filter(Q(user=user) or Q(with_user=user))
    chats = Message.objects.filter(Q(recipient=request.user) | Q(sender=request.user)).order_by('-timestamp')
    # people = CustomUser.objects.filter(Q(recipient=request.user) | Q(sender=request.user)).order_by('-timestamp')
    dialogs_response = Dialog.objects.filter(Q(user=request.user) | Q(with_user=request.user)) #recipient,
    folders = Folder.objects.filter(user=request.user)[0:2]
    folders_count = Folder.objects.filter(user=request.user).count()
    
    # recipient = User.objects.get(id=recipient_id)
    # messages = Message.objects.filter(sender=request.user, recipient=recipient) | Message.objects.filter(sender=recipient, recipient=request.user).order_by('timestamp')
    if dialogs_response:
        #messages = Message.objects.filter(dialog=dialog)
        message_count = 0
    else:
        messages = []
        message_count = 0
        
    context = {
        'chats': chats,
        # 'messages': messages,
        # 'dialog_count': message_count,
        'dialogs': dialogs_response,
        'folders': folders,
        'folders_count': folders_count,
        'title_chat': 'Мои чаты',
    }
    
    return render(request, 'chats.html', context)


@login_required
def folder(request, folder_id):
    user = request.user.id
    folder = Folder.objects.get(user=user, id=folder_id)
    folders = Folder.objects.filter(user=request.user)[0:2]
    folders_count = Folder.objects.filter(user=request.user).count()
    return render(request, 'folder.html', {'folder': folder, 'title_chat': f'{folder.name}', 'folders': folders,'folders_count':folders_count,})


def folderCreate(request):
    # if not request.user.is_premium and request.user.folders.count() >= 4:
    #     return redirect("chats")
    
    if request.method == 'POST':
        form = FolderForm(request.POST)
        if form.is_valid():
            new_folder = form.save(commit=False)
            new_folder.user = request.user  # Установка текущего пользователя
            new_folder.save()
            
            selected_dialogs = request.POST.getlist('dialog')
            print(selected_dialogs)
            for dialog_id in selected_dialogs:
                dialog = Dialog.objects.get(id=dialog_id)
                new_folder.dialogs.add(dialog)
                
            return redirect('chats')
    else:
        form = FolderForm()
    
    return render(request, 'chats.html', {'form': form})    

@login_required
def message(request, recipient_id):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            sender = request.user
            recipient = User.objects.get(id=recipient_id)
            content = form.cleaned_data['message_content']
            message = Message(sender=sender, recipient=recipient, content=content)
            message.save()
            
            # Проверяем существующий диалог между отправителем и получателем
            if not Dialog.objects.filter(user=sender, with_user=recipient).first():            
                if not Dialog.objects.filter(user=recipient, with_user=sender).first():
                    dialog = Dialog.objects.create(user=sender, with_user=recipient)
                
                        
            dialog = Dialog.objects.filter(Q(user=sender, with_user=recipient) | Q(user=recipient, with_user=sender)).first()
            print(dialog)
            dialog.messages.add(message)  # Добавляем сообщение в диалог
            dialog.last_message = message
            dialog.save()
            
            return redirect('message', recipient_id=recipient_id)
    else:
        form = MessageForm()        
        # form = MessageForm()
        recipient = User.objects.get(id=recipient_id)
        #dialog = Dialog.objects.filter(user=request.user, with_user=recipient).first()
        messages = Message.objects.filter(sender=request.user, recipient=recipient) | Message.objects.filter(sender=recipient, recipient=request.user).order_by('timestamp')
        # if dialog:
        #     messages = Message.objects.filter(dialog=dialog)
        # else:
        #     messages = []
                
    return render(request, 'message.html', {
        'recipient': recipient,
        'messages': messages,
        'form': form,
        # 'dialogs': dialogs
    })
        
        # if recipient_id != request.user:
        #     recipient = User.objects.get(id=recipient_id)
        #     # Проверяем существующий диалог между отправителем и получателем
        #     dialog = Dialog.objects.filter(user=sender, with_user=recipient).first()
        # if not dialog:
        #     dialog = Dialog.objects.create(user=sender, with_user=recipient)        
        # dialog.save()
        
        # user = request.user
        # dialogs = Dialog.objects.filter(Q(user=user) | Q(with_user=user))
        # form = MessageForm()      
        # recipient = CustomUser.objects.get(Q(id=recipient_id) | Q(id=user.id))           
         
        # if not dialogs:
        #     pass
        # else:                              
        #     # Получаем все сообщения между отправителем и получателем
        #     dialog_message = Dialog.objects.filter(user=request.user, with_user=recipient) | Dialog.objects.filter(user=recipient, with_user=request.user).first()
            
        #     if dialog_message:
        #         messages = dialog_message.messages.all().order_by('timestamp')
        #     else:
        #         messages = []
                    # Получаем все сообщения между отправителем и получателем


def display_messages(request, recipient_id):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            sender = request.user
            recipient = User.objects.get(id=recipient_id)
            content = form.cleaned_data['message_content']
            message = Message(sender=sender, recipient=recipient, content=content)
            message.save()
            dialog, created = Dialog.objects.get_or_create(user=sender, with_user=recipient)
            dialog.last_message = message
            dialog.save()
            return redirect('display_messages', recipient_id=recipient_id)
    else:
        form = MessageForm()        
        # form = MessageForm()
        recipient = User.objects.get(id=recipient_id)
        #dialog = Dialog.objects.filter(user=request.user, with_user=recipient).first()
        messages = Message.objects.filter(sender=request.user, recipient=recipient) | Message.objects.filter(sender=recipient, recipient=request.user).order_by('timestamp')
        # if dialog:
        #     messages = Message.objects.filter(dialog=dialog)
        # else:
        #     messages = []
    
    return render(request, 'display_messages.html', {'recipient': recipient, 'messages': messages, 'form': form})