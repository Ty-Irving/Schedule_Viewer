from ast import Return
from re import L
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from . import models

from . import serializers

# Create your views here.
class Logins(APIView):
    def get(self, request, pk, format=None):
        login = models.LOGIN.objects.get(pk=pk)
        serializer = serializers.LoginSerializer(login)
        return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)

class Users (APIView):
    def post(self, request, format=None):
        serializer = serializers.UserSerialized (data=request.data)
        login_serializer = serializers.LoginSerializer (data=request.data)
        if login_serializer.is_valid():
            login_serializer.save()
        else:
            return Response(data=login_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        if serializer.is_valid():
            serializer.save()
            return Response (data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer._errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, format=None):
        users = models.USER.objects.all()
        serializer = serializers.UserSerialized(users, many=True)
        return Response(serializer.data)

class Employee(APIView):
    def get(self, request, pk, format=None):
        emp = models.EMPLOYEE.objects.get(pk=pk)
        serializer = serializers.EmployeeSerializer(emp)
        return Response(serializer.data)

class UserDetails (APIView):
    def get(self, request, pk, format=None):
        user = models.USER.objects.get(pk=pk)
        serializer = serializers.UserSerialized(user)
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
    def post(self, request, format=None):
        serializer = serializers.ShiftSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(request.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        shift = models.SCHEDULE_SHIFTS.objects.all()
        serializer = serializers.ShiftSerializer(shift, many=True)
        return Response(serializer.data)

class ShiftDetail (APIView):
    def get(self, request, scheduleId, date, format=None):
        shift = models.SCHEDULE_SHIFTS.objects.filter(ScheduleID=scheduleId).get(Date=date)

        # I think I got it now: we can keep filtering as much as we want, and if we want to return the actual results we do that
        # with .all or .get, and these will actually return the values

        serializer = serializers.ShiftSerializer(shift)
        return Response(serializer.data)
    
    def put(self, request, scheduleId, date, format=None):
        shift = models.SCHEDULE_SHIFTS.objects.filter(ScheduleID=scheduleId).get(Date=date) # this query gets us the specific shift that we want to update
        serializer = serializers.ShiftSerializer(shift, request.data)
        if serializer.is_valid():
            print(request.data)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, scheduleId, date, format=None):
        shift = models.SCHEDULE_SHIFTS.objects.filter(ScheduleID=scheduleId).filter(Date=date)
        shift.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class ShiftRangeDetails (APIView):
    def get(self, request, scheduleId, startRangeDate, endRangeDate, format=None):
        shifts = models.SCHEDULE_SHIFTS.objects.filter(ScheduleID=scheduleId).filter(Date__gte=startRangeDate).filter(Date__lte=endRangeDate).all()

        # I think I got it now: we can keep filtering as much as we want, and if we want to return the actual results we do that
        # with .all or .get, and these will actually return the values

        serializer = serializers.ShiftSerializer(shifts, many=True)
        return Response(serializer.data)

class Departments (APIView):
    def get(self, request, format=None):
        request = models.DEPARTMENT.objects.all()
        serializer = serializers.DepartmentSerializer(request, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = serializers.DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(request.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DepartmentDetails (APIView):
    def get(self, request, pk, format=None):
        department = models.DEPARTMENT.objects.get(pk=pk)
        serializer = serializers.DepartmentSerializer(department)
        return Response(serializer.data)
        
    def put(self, request, pk, format=None):
        department = models.DEPARTMENT.objects.get(pk=pk)
        serializer = serializers.DepartmentSerializer(department, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        department = models.DEPARTMENT.objects.filter(pk=pk)
        department.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class Managers (APIView):
    def get(self, request, format=None):
        manager = models.MANAGER.objects.all()
        serializer = serializers.ManagerSerializer(manager, many=True)
        return Response(serializer.data)

class Logins(APIView):
    def get(self, request, pk, format=None):
        login = models.LOGIN.objects.get(pk=pk)
        serializer = serializers.LoginSerializer(login)
        return Response(serializer.data)

class Projects (APIView):
    def post(self, request, format=None):
        serializer = serializers.ProjectSerializer(data=request.data)
        if serializer.is_valid():
            print(request.data)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, format=None):
        projects = models.PROJECT.objects.all()
        serializer = serializers.ProjectSerializer(projects, many=True)
        return Response(serializer.data)

class ProjectDetails (APIView):
    def delete(self, request, pk, format=None):
        project = models.PROJECT.objects.filter(ProjectId=pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TimeLogs (APIView):
    def post(self, request, format=None):
        serializer = serializers.TimeLogSerializer(data=request.data)
        if serializer.is_valid():
            print(request.data)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class TimeLogDetails (APIView):
    def get(self, request, pk, format=None):
        timeLogs = models.TIME_LOG.objects.filter(EndTime__isnull=True).filter(EmpID=pk).all()
        serializer = serializers.TimeLogSerializer(timeLogs, many=True)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        timeLog = models.TIME_LOG.objects.filter(EndTime__isnull=True).get(EmpID=pk)
        serializer = serializers.TimeLogSerializer(timeLog, data=request.data)
        if serializer.is_valid():
            print(request.data)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)