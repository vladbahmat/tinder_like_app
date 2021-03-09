from django.urls import path, include
from rest_framework import routers
from photos.views import AddPost


router = routers.DefaultRouter()
router.register(r'photos', AddPost)


urlpatterns = [
    path('', include(router.urls)),
]
