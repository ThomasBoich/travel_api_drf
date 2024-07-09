# from django.shortcuts import render

# # Create your views here.
# #   python manage.py runserver 0.0.0.0:8000
# #   python manage.py migrate --run-syncdb
# from concurrent.futures import thread
# from rich.console import Console
# console = Console(style='bold green')
# import re, json
# from django.shortcuts import render, redirect
# from .models import Message, UserSetting, Thread
# from .managers import ThreadManager
# from django.conf import settings
# from django.http import JsonResponse, HttpResponse
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.models import User


# def email_valid(email):
#     regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
#     if (re.fullmatch(regex, email)): return True
#     return False


# @login_required
# def api_online_users(request, id=0):
#     users_json = {}

#     if id != 0:
#         user = User.objects.get(id=id)
#         user_settings = UserSetting.objects.get(user=user)
#         users_json['user'] = get_dictionary(user, user_settings)

#     else:
#         all_users = User.objects.all().exclude(username=request.user)
#         for user in all_users:
#             user_settings = UserSetting.objects.get(user=user)
#             users_json[user.id] = get_dictionary(user, user_settings)

#     return HttpResponse(
#         json.dumps(users_json),
#         content_type='application/javascript; charset=utf8'
#     )


# def get_dictionary(user, user_settings):
#     return {
#         'id': user.id,
#         'username': user_settings.username,
#         'profile-image': user_settings.profile_image.url,
#         'is-online': user_settings.is_online
#     }


# @login_required
# def api_chat_messages(request, id):
#     messages_json = {}
#     count = int(request.GET.get('count', 0))

#     thread_name = ThreadManager.get_pair('self', request.user.id, id)
#     thread = Thread.objects.get(name=thread_name)
#     messages = Message.objects.filter(thread=thread).order_by('-id')

#     for i, message in enumerate(messages, start=1):
#         messages_json[message.id] = {
#             'sender': message.sender.id,
#             'text': message.text,
#             'timestamp': message.created_at.isoformat(),
#             'isread': message.isread,
#         }
#         if i == count: break

#     return HttpResponse(
#         json.dumps(messages_json),
#         content_type='application/javascript; charset=utf8'
#     )


# @login_required
# def api_unread(request):
#     messages_json = {}

#     user = request.user
#     threads = Thread.objects.filter(users=user)
#     for i, thread in enumerate(threads):
#         if (user == thread.users.first()):
#             sender = thread.users.last()
#             unread = thread.unread_by_1
#         else:
#             sender = thread.users.first()
#             unread = thread.unread_by_2

#         messages_json[i] = {
#             'sender': sender.id,
#             'count': unread,
#         }

#     return HttpResponse(
#         json.dumps(messages_json),
#         content_type='application/javascript; charset=utf8'
#     )


# @login_required
# def index(request, id=0):
#     user = User.objects.get(username=request.user)
#     Usettings = UserSetting.objects.get(user=user)

#     context = {
#         "settings": Usettings,
#         'id': id,
#     }
#     return render(request, 'index.html', context=context)


# def login_view(request):
#     logout(request)
#     context = {}

#     if request.POST:
#         email = request.POST['email']
#         password = request.POST['password']

#         user = authenticate(username=email, password=password)

#         if user is not None:
#             if user.is_active:
#                 login(request, user)
#                 return redirect('/')
#         else:
#             context = {
#                 "error": 'Email or Password was wrong.',
#             }

#     return render(request, 'login.html', context)


# def signup_view(request):
#     logout(request)

#     if request.method == 'POST':
#         email = request.POST.get('email')
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         error = ''

#         if not email_valid(email):
#             error = "Wrong email address."
#         try:
#             if User.objects.get(username=email) is not None:
#                 error = 'This email is already used.'
#         except:
#             pass

#         if error:  return render(request, "signup.html", context={'error': error})

#         user = User.objects.create_user(
#             username=email,
#             password=password,
#         )
#         userset = UserSetting.objects.create(user=user, username=username)

#         login(request, user)
#         return redirect('/')

#     return render(request, 'signup.html')


# @login_required
# def settings_view(request):
#     user = User.objects.get(username=request.user)
#     Usettings = UserSetting.objects.get(user=user)

#     if request.method == 'POST':
#         try:
#             avatar = request.FILES["avatar"]
#         except:
#             avatar = None
#         username = request.POST['username']

#         Usettings.username = username
#         if (avatar != None):
#             Usettings.profile_image.delete(save=True)
#             Usettings.profile_image = avatar
#         Usettings.save()

#     context = {
#         "settings": Usettings,
#         'user': user,
#     }
#     return render(request, 'settings.html', context=context)


from django.shortcuts import render
from .models import Message,ChatRoom,ChatMessage
from users.models import CustomUser as User
from django.contrib.auth.decorators import login_required

def private_chat(request, recipient_id):
    recipient = User.objects.get(id=recipient_id)
    messages = Message.objects.filter(sender=request.user, recipient=recipient) | Message.objects.filter(sender=recipient, recipient=request.user).order_by('timestamp')

    return render(request, 'private_chat.html', {'recipient': recipient, 'messages': messages})


def chat_room(request, room_id):
    room = ChatRoom.objects.get(id=room_id)
    messages = ChatMessage.objects.filter(room=room).order_by('timestamp')

    return render(request, 'chat_room.html', {'room': room, 'messages': messages})



from django.shortcuts import redirect
from .models import Message

from django.shortcuts import redirect, render
from .forms import MessageForm
from .models import Message
from users.models import CustomUser as User
from users.models import CustomUser

def send_message(request, recipient_id):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            sender = request.user
            recipient = User.objects.get(id=recipient_id)
            content = form.cleaned_data['message_content']
            message = Message(sender=sender, recipient=recipient, content=content)
            message.save()
            return render(request, 'display_messages.html', {'recipient': recipient, 'messages': messages})
    else:
        form = MessageForm(initial={'recipient_id': recipient_id})
    
    return render(request, 'display_messages.html', {'form': form})

from django.shortcuts import render
from .models import Message
from users.models import CustomUser as User

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import MessageForm
from .models import Message,Dialog
from users.models import CustomUser as User

# def display_messages(request, recipient_id):
#     if request.method == 'POST':
#         form = MessageForm(request.POST)
#         if form.is_valid():
#             sender = request.user
#             recipient = User.objects.get(id=recipient_id)
#             content = form.cleaned_data['message_content']
#             message = Message(sender=sender, recipient=recipient, content=content)
#             message.save()
#             print(recipient)
#             return redirect('display_messages', recipient_id=recipient_id)
#     else:
#         form = MessageForm()
        
#     form = MessageForm()
#     recipient = User.objects.get(id=recipient_id)
#     messages = Message.objects.filter(sender=request.user, recipient=recipient) | Message.objects.filter(sender=recipient, recipient=request.user).order_by('timestamp')


#     return render(request, 'display_messages.html', {'recipient': recipient, 'messages': messages, 'form': form})
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
        dialog = Dialog.objects.filter(user=request.user, with_user=recipient).first()
        messages = Message.objects.filter(sender=request.user, recipient=recipient) | Message.objects.filter(sender=recipient, recipient=request.user).order_by('timestamp')
        # if dialog:
        #     messages = Message.objects.filter(dialog=dialog)
        # else:
        #     messages = []
    
    return render(request, 'display_messages.html', {'recipient': recipient, 'messages': messages, 'form': form})

# def send_message(request, recipient_id):
#     if request.method == 'POST':
#         form = MessageForm(request.POST)
#         if form.is_valid():
#             sender = request.user
#             recipient = User.objects.get(id=recipient_id)
#             content = form.cleaned_data['message_content']
#             message = Message(sender=sender, recipient=recipient, content=content)
#             message.save()
#             return redirect('private_chat', recipient_id=recipient_id)
#     else:
#         form = MessageForm()
    
#     return render(request, 'send_message.html', {'form': form})