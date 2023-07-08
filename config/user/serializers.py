from djoser.serializers import UserSerializer, UserCreateSerializer

from .models import CustomUser


class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = CustomUser
        fields = ('id', 'tel', 'vk_link', 'email', 'first_name', 'last_name', 'password')


class CustomUserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = CustomUser
        fields = ('id', 'tel', 'vk_link', 'email', 'first_name', 'last_name')
