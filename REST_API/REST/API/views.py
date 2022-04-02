from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from . import models

from . import serializers

# Create your views here.
class UserDetails (APIView):
    def post(self, request, format=None):
        serializer = serializers.UserSerialized (data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer._errors, status=status.HTTP_400_BAD_REQUEST)
