from django.urls import path, include
from rest_framework_simplejwt import views
from rest_framework import routers
from users.views import RegisterApi, ShowUser


router = routers.DefaultRouter()
router.register(r'users', RegisterApi)
router.register(r'authorization', views.TokenObtainPairView)
router.register(r'users/<int:pk>', ShowUser)

urlpatterns = [
    path('', include(router.urls)),
]
