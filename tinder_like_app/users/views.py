from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_object_or_404
from subscribe.service import Service
from users.serializers import UserSerializer


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
        if Service.is_swipes_valid(request.user.id) and Service.is_radius_valid(request.user.longitude, request.user.latitude, pk):
            user = get_object_or_404(User, pk=pk)
            serializer = self.serializer_class(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response("Swipes end or so far", status=status.HTTP_204_NO_CONTENT)

    def post(self, request, pk, *args,  **kwarg):
        user = get_object_or_404(User, pk=pk)
        user.match.add(pk)
        user.save()
        return Response(status=status.HTTP_200_OK)
