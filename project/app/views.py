from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from django.contrib.auth.models import User
from .models import Files
from .serializers import *
from rest_framework_simplejwt.tokens import RefreshToken


class UserViewSet(viewsets.ViewSet):
    @action(methods=['post'])
    def register(self,request):
        serializer=UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"User Registered Successfully!"},status=status.HTTP_201_CREATED)
        return Response({'error'})