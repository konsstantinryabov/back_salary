from rest_framework import serializers
from post.models import User, Salary
from djoser.serializers import UserSerializer


class CustomUserSerializer(UserSerializer):

    """Сериализатор для отображения информации пользователях"""

    class Meta:
        model = User
        fields = ('id',
                  'username',
                  'first_name',
                  'last_name')


class AdminSalarySerializer(serializers.ModelSerializer):

    """Сериализатор для создания данных для работника"""
    worker = serializers.SlugRelatedField(
        slug_field='username', queryset=User.objects.all())

    class Meta:
        model = Salary
        fields = ('id',
                  'worker',
                  'salar',
                  'date')


class SalarySerializer(serializers.ModelSerializer):

    """Сериализатор для получения своих данных работником"""

    class Meta:
        model = Salary
        fields = ('id',
                  'salar',
                  'date')
