from rest_framework import serializers
from photos.serializers import PhotoSerializer
from subscribe.service import Service
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('username', 'photos', 'match',
                  'password', 'latitude', 'longitude')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = super().create(validated_data)
        p = user.password
        user.set_password(p)
        Service.create_basic_subsribe(user.id)
        user.save()
        return user
