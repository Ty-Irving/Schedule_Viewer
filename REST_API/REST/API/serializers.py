from rest_framework import serializers
from . import models

class UserSerialized (serializers.ModelSerializer):
    class Meta:
        model = models.USER
        fields = '__all__'

class RequestSerializer (serializers.ModelSerializer):
    class Meta:
        model = models.REQUEST
        fields = '__all__'

class ShiftSerializer (serializers.ModelSerializer):
    class Meta:
        model = models.SCHEDULE_SHIFTS
        fields = '__all__' # this may have to change

class DepartmentSerializer (serializers.ModelSerializer):
    class Meta:
        model = models.DEPARTMENT
        fields = '__all__'