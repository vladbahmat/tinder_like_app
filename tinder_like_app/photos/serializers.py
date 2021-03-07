from rest_framework import  serializers
from .models import Photo


class PhotoSerializer(serializers.ModelSerializer):
    #__all__ = serializers.JSONField()
    class Meta:
        model = Photo
        fields = '__all__'