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
    
    def put(self, request, pk, format=None):
        user = models.USER.objects.get(pk=pk)
        print(user) # These are here for error checking
        serializer = serializers.UserSerialized(user, data=request.data)
        if serializer.is_valid():
            print(request.data) # These are here for error checking
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class Requests (APIView):
    def get(self, request, format=None):
        request = models.REQUEST.objects.all()
        serializer = serializers.RequestSerializer(request, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = serializers.RequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class RequestDetails (APIView):
    def delete(self, request, pk, format=None):
        userRequest = models.REQUEST.objects.filter(pk=pk)
        userRequest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class Shifts (APIView):
    def get(self, request, format=None):
        shift = models.SCHEDULE_SHIFTS.objects.all()
        serializer = serializers.ShiftSerializer(shift, many=True)
        return Response(serializer.data)

class Departments (APIView):
    def post(self, request, format=None):
        serializer = serializers.DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(request.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DepartmentDetails (APIView):
    def put(self, request, pk, format=None):
        department = models.DEPARTMENT.objects.get(pk=pk)
        serializer = serializers.DepartmentSerializer(department, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)