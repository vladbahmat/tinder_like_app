from rest_framework import generics, permissions, mixins
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from subscribe.models import Subscribe
from subscribe.serializers import SubscribeSerializer


class ChangeSubscribe(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = SubscribeSerializer

    def put(self, request):
        saved_subscribe = Subscribe.objects.get(user_id=request.user.id)
        serializer = SubscribeSerializer(
            instance=saved_subscribe, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            subscribe_saved = serializer.save()
        return Response("Subscribe changed")
