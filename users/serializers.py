from rest_framework import serializers
from .models import CustomUser, Interests, Habits, City, Friends, Friendship

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

class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser  # Предполагается, что друзья — это пользователи
        fields = ['id', 'first_name', 'last_name', 'photo']  # Добавьте необходимые поля

class FriendsSerializer(serializers.ModelSerializer):
    friends = FriendSerializer(many=True, read_only=True)

    class Meta:
        model = Friends
        fields = ['user', 'friends']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user'] = instance.user.id  # Добавляем поле user только один раз
        return representation

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












class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'first_name', 'last_name', 'photo']

class FriendshipSerializer(serializers.ModelSerializer):
    from_user = UserSerializer(read_only=True)
    to_user = UserSerializer(read_only=True)

    class Meta:
        model = Friendship
        fields = ['id', 'from_user', 'to_user', 'status', 'created_at', 'updated_at']

class FriendshipCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friendship
        fields = ['to_user']  # Только получатель, отправитель определяется из запроса

class FriendshipUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friendship
        fields = ['status']  # Только статус для обновления