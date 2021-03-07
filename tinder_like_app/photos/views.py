from django.shortcuts import render
from .serializers import PhotoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, generics


class AddPost(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PhotoSerializer
    def post(self, request, *args, **kwargs):
        data = {**request.data, 'user':request.user.id}
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)