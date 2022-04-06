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