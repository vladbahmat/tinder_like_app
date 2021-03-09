from .models import Subscribe
from math import inf
from geopy.distance import geodesic
from users.models import User
from django.contrib.gis.geoip2 import GeoIP2


class Service():
    @staticmethod
    def create_basic_subsribe(id):
        subscribe = Subscribe()
        subscribe.user_id = id
        subscribe.swipes = 25.0
        subscribe.radius = 10
        subscribe.name = 'basic'
        subscribe.save()


    @staticmethod
    def is_swipes_valid(id):
        subscribe = Subscribe.objects.get(user_id=id)
        if subscribe.swipes > 0:
            subscribe.swipes -= 1
            subscribe.save()

            return True
        else:

            return False


    @staticmethod
    def is_radius_valid(longitude, latitude, id):
        subscribe = Subscribe.objects.get(user_id=id)
        user = User.objects.get(pk=id)
        first_point = (longitude, latitude)
        second_point = (user.longitude, user.latitude)
        print(first_point, second_point)
        if geodesic(first_point, second_point).km > subscribe.radius:
            return False
        else:
            return True
