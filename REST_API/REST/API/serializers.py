from rest_framework import serializers
from . import models

class UserSerialized (serializers.ModelSerializer):
    class Meta:
        model = models.USER
        fields = '__all__'