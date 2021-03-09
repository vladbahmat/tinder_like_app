from django.urls import path, include
from rest_framework import routers
from subscribe.views import ChangeSubscribe


router = routers.DefaultRouter()
router.register(r'subscribe', ChangeSubscribe)


urlpatterns = [
    path('', include(router.urls)),
]
