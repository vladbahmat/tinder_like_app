from rest_framework import  serializers
from rest_framework.permissions import IsAuthenticated
from django.db import models
from .models import User
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from photos.serializers import PhotoSerializer
from subscribe.service import create_basic_subsribe

class UserSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many = True, read_only=True)
    class Meta:
        model = User
        fields = ('username', 'photos', 'match', 'password', 'latitude', 'longitude')
        extra_kwargs = {'password': {'write_only': True}}


    def create(self, validated_data):
        user = super().create(validated_data)
        p = user.password
        user.set_password(p)
        create_basic_subsribe(user.id)
        user.save()
        return user