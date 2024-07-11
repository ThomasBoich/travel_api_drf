from django.contrib import admin
# Register your models here.
from django.contrib import admin
from .models import *
# Register your models here.

class MessageAdmin(admin.ModelAdmin):
    # list_display = ('city',)
    # search_fields = ('city',)
    pass

class DialogAdmin(admin.ModelAdmin):
    # list_display = ('name',)
    # search_fields = ('name',)
    pass

class FolderAdmin(admin.ModelAdmin):
    # list_display = ('name',)
    # search_fields = ('name',)
    pass

admin.site.register(Dialog, DialogAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Folder, FolderAdmin)
