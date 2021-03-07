from django.urls import path, include
from .views import ChangeSubscribe



urlpatterns = [
    path('subscribe', ChangeSubscribe.as_view()),
]