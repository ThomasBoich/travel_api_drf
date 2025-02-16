from rest_framework import serializers
from .models import CustomUser, Interests, Habits, City

class InterestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interests
        fields = '__all__'

class HabitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habits
        fields = '__all__'

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class CustomUserSerializer(serializers.ModelSerializer):
    habits = HabitsSerializer(many=True, read_only=True)
    interests = InterestsSerializer(many=True, read_only=True)
    city = CitySerializer(read_only=True)
    class Meta:
        model = CustomUser
        fields = '__all__'


from django.contrib.auth.password_validation import validate_password

from users.models import CustomUser


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    # referral_code = serializers.CharField(required=False, allow_null=True, max_length=15)

    class Meta:
        model = CustomUser
        fields = '__all__'

    # def create(self, validated_data):
    #     user = CustomUser.objects.create_user(
    #         # username=validated_data['username'],
    #         email=validated_data['email'],
    #         password=validated_data['password']
    #     )
    #     return user