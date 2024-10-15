from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import FileSerializer
# Create your views here.

class FileViewSet(viewsets.ModelViewSet):
    queryset=Files.objects.all()
    serializer_class=FileSerializer