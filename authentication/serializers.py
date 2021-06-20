from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from .models import *


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ['email', 'username', 'password',
                  'first_name', 'last_name']


class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'username', 'profile_image', 'about',
                  'linkedin_profile', 'twitter_profile', 'facebook_profile', 'other_links', 'education', 'address']


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'username', 'profile_image', 'about',
                  'linkedin_profile', 'twitter_profile', 'facebook_profile', 'other_links', 'education', 'address']
