from re import L
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from . import models

from . import serializers

# Create your views here.
class Users (APIView):
    def post(self, request, format=None):
        serializer = serializers.UserSerialized (data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer._errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetails (APIView):
    def get(self, request, pk, format=None):
        user = models.USER.objects.get(pk=pk)
        serializer = serializers.UserSerialized (user)
        return Response(serializer.data)
    
class Requests (APIView):
    def get(self, request, format=None):
        request = models.REQUEST.objects.all()
        serializer = serializers.RequestSerializer(request, many=True)
        return Response(serializer.data)
        
