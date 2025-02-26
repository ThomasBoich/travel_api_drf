from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.forms import CustomUserChangeForm, CustomUserCreationForm
from users.models import CustomUser, Profile, Habits, Interests, City, Friends, Favorites,CarBrand,CarModel,UserCar

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = (
        'email',
        'first_name',
        'last_name',
        'patronymic',
        'is_staff',
        'is_active',
        'phone',
        'bonus_points',
        'age',
        'description',
        'small_description',
        'city',
        'premium',
        'premium_activate',
        # 'interests',
        # 'habits'
    )
    list_filter = ('email', 'is_staff', 'is_active', 'groups')
    fieldsets = (
        (None, {'fields': (
            'email',
            'password',
            'first_name',
            'last_name',
            'patronymic',
            'photo',
            'phone',
            'bonus_points',
            'age',
            'description',
            'small_description',
            'city',
            'interests',
            'habits',
            'cars',
            'premium',
            'premium_activate',
        )}),
        ('Permissions', {
            'fields': ('is_superuser', 'ban', 'type', 'is_staff', 'is_active', 'groups')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'password1',
                'password2',
                'is_staff',
                'is_active',
                'is_superuser',
                'ban',
                'type',
                'first_name',
                'last_name',
                'patronymic',
                'phone',
                'age',
                'description',
                'small_description',
                'city',
                'interests',
                'habits',
                'cars',
                'premium',
                'groups'

            )}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


class ProfileAdmin(admin.ModelAdmin):
    save_as = True
    list_display = ('user',)
    search_fields = ('user',)
    readonly_fields = ('user',)



class HabitsAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class InterestsAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Profile, ProfileAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Habits, HabitsAdmin)
admin.site.register(Interests, InterestsAdmin)


class CityAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class FriendsAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user',)


class FavoritesAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user',)
    
class CarBrandAdmin(admin.ModelAdmin):
    pass

class CarModelAdmin(admin.ModelAdmin):
    pass
    
class UserCarAdmin(admin.ModelAdmin):
    pass
    
admin.site.register(City,CityAdmin)
admin.site.register(Friends,FriendsAdmin)
admin.site.register(Favorites,FavoritesAdmin)
admin.site.register(CarBrand, CarBrandAdmin)
admin.site.register(CarModel, CarModelAdmin)
admin.site.register(UserCar, UserCarAdmin)