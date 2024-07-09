# from django.db import models

# # Create your models here.
# from concurrent.futures import thread
# from chat.managers import ThreadManager
# import os, uuid
# from users.models import CustomUser

# # Create your models here.
# def random_file_name(instance, filename):
#     ext = filename.split('.')[-1]
#     filename = "%s.%s" % (uuid.uuid4(), ext)
#     return os.path.join('profile-pics', filename)


# class UserSetting(models.Model):
#     user = models.OneToOneField(CustomUser, null=True, on_delete=models.CASCADE)
#     username = models.CharField(max_length=32, default="")
#     profile_image = models.ImageField(upload_to=random_file_name, blank=True, null=True,
#                                       default='\\profile-pics\\default.jpg')
#     is_online = models.BooleanField(default=False)

#     def __str__(self):
#         return str(self.user)


# class TrackingModel(models.Model):
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         abstract = True


# class Thread(TrackingModel):
#     name = models.CharField(max_length=50, null=True, blank=True)
#     users = models.ManyToManyField(CustomUser, related_name='thread_customer')
#     unread_by_1 = models.PositiveIntegerField(default=0)
#     unread_by_2 = models.PositiveIntegerField(default=0)

#     objects = ThreadManager()

#     def __str__(self):
#         return f'{self.name} \t -> \t {self.users.first()} - {self.users.last()}'


# class Message(TrackingModel):
#     thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
#     sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     text = models.TextField(blank=False, null=False)
#     isread = models.BooleanField(default=False)

#     def __str__(self):
#         return f'From Thread - {self.thread.name}'
from django.db import models
# from django.contrib.auth.models import User
from users.models import CustomUser as User

class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return f'{self.sender} -> {self.recipient}: {self.content}'
    
    
class Dialog(models.Model):
    user = models.ForeignKey(User, related_name='dialogs', on_delete=models.CASCADE)
    with_user = models.ForeignKey(User, on_delete=models.CASCADE)
    last_message = models.ForeignKey(Message, on_delete=models.SET_NULL, null=True)
    messages = models.ManyToManyField(Message, related_name='messages_list')  # Связь с моделью Message для хранения всех сообщений в диалоге

    def __str__(self):
        return f'от {self.user.email} -> кому {self.with_user.email}'
    
    # def save(self, *args, **kwargs):
    #     existing_dialog = Dialog.objects.filter(user=self.user, with_user=self.with_user).first()
    #     if existing_dialog:
    #         existing_dialog.last_message = self.last_message
    #         existing_dialog.save()
    #     else:
    #         super(Dialog, self).save(*args, **kwargs)
    
    
    
class ChatRoom(models.Model):
    name = models.CharField(max_length=100)

class ChatMessage(models.Model):
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    