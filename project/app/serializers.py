from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import check_password

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Files
        fields = ['id', 'uploaded_file', 'uploaded_at']  # Exclude 'user' from this list
        read_only_fields = ['user']

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','email','password']
        extra_kwargs={'password' : {'write_only' : True}}
     
    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class UserLoginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()
        