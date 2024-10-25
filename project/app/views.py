from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework.decorators import action
from django.contrib.auth.models import User
from .models import Files
from .serializers import *
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.parsers import MultiPartParser, FormParser

class UserViewSet(viewsets.ViewSet):
    @action(detail=False, methods=['post'])
    def register(self,request):
        serializer=UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"User Registered Successfully!"},status=status.HTTP_201_CREATED)
        return Response({'error':serializer.errors},status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['post'])
    def login(self,request):
        serializer=UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username,password=password)
            if user is not None:
                refresh =RefreshToken.for_user(user)
                return Response({
                    'message' : 'Login successfull',
                    'refresh' : str(refresh),
                    'access' : str(refresh.access_token),
                })
            return Response({'error':'Invlaid credentials'},status=status.HTTP_401_UNAUTHORIZED)
        return Response({'error' : serializer.errors},status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['get'])
    def me(self, request):
        user = request.user
        # print(user)
        return Response({
            'username': user.username,
            'email': user.email,
        })

class FileViewSet(viewsets.ModelViewSet):
    queryset = Files.objects.all()
    serializer_class =FileSerializer
    permission_classes=[IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]  # Handle file uploads
    def get_queryset(self):
        return Files.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    

# User:

#     POST /api/users/register/
#     POST /api/users/login/

# File-related endpoints:

#     GET /api/files/
#     POST /api/files/
#     GET /api/files/<id>/
#     PUT /api/files/<id>/
#     DELETE /api/files/<id>/