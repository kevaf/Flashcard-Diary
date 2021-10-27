from rest_framework import serializers
from .models import Cards
from django.contrib.auth.models import User

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cards
        fields = ('title', 'notes', 'courses', 'pub_date')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user