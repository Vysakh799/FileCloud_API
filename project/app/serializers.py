from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import check_password

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Files
        fields='__all__'

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','email','password']
        