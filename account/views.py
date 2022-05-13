from django.shortcuts import render
from rest_framework import generics, permissions

from account import serializers
from account.models import CustomUser


class UserRegistrationView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = serializers.UserRegisterSerializer
