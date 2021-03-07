from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.decorators import api_view, permission_classes
from subscribe.service import *


class RegisterApi(generics.GenericAPIView):
    serializer_class = UserSerializer
    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class ShowUser(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    def get(self, request, pk, *args, **kwargs):
        if is_swipes_valid(request.user.id) and is_radius_valid(request.user.longitude, request.user.latitude, pk):
            user = User.objects.get(pk=pk)
            serializer = self.serializer_class(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response("Swipes end or so far")


    def post(self, request, pk, *args,  **kwarg):
        user = User.objects.get(pk=pk)
        user.match.add(pk)
        user.save()
        return Response(status=status.HTTP_200_OK)
