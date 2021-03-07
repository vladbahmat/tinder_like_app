from django.urls import path, include
from .views import RegisterApi, ShowUser
from rest_framework_simplejwt import views



urlpatterns = [
      path('users', RegisterApi.as_view()),
      path('authorization', views.TokenObtainPairView.as_view(),
        name='token_obtain_pair'),
      path('users/<int:pk>', ShowUser.as_view()),
]