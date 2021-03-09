from django.db import models
from users.models import User


class Photo(models.Model):
    image = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
