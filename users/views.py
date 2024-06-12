from django.shortcuts import render
from rest_framework.permissions import IsAdminUser
from users.models import User
from rest_framework.response import Response
from rest_framework import status

from rest_framework.views import APIView

from users.serializers import UserSerializer
# Create your views here.


class UserListAPIView(APIView):
    permission_classes = [IsAdminUser]
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(instance=users, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)