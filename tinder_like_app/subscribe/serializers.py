from rest_framework import serializers
from .models import Subscribe
from math import inf


class SubscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribe
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.swipes = validated_data.get('swipes', instance.swipes)
        instance.name = validated_data.get('name', instance.name)
        instance.radius = validated_data.get('radius', instance.radius)
        instance.user_id = validated_data.get('user_id', instance.user_id)
        instance.save()
        return instance

    def validate(self, data):
        if data['name'] == 'basic':
            data['swipes'] = 25.0
            data['radius'] = 10
            return data
        if data['name'] == 'vip':
            data['swipes'] = 100.0
            data['radius'] = 25
            return data
        if data['name'] == 'premium':
            data['swipes'] = inf
            return data
