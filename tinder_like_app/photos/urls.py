from django.urls import path, include
from .views import AddPost

urlpatterns = [
      path('photos', AddPost.as_view()),
]