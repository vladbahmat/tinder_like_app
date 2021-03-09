from django.db import models
from users.models import User


class Subscribe(models.Model):
    swipes = models.FloatField()
    name = models.CharField(max_length=15)
    radius = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)