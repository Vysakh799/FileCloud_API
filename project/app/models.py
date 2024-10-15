from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.
class User(models.Model):
    username=models.TextField(unique=True)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=9)

    def save(self, *arg, **kwargs):
        self.password=make_password(self.password)

    def __str__(self):
        return self.username
    
class Files(models.Model):
    file=models.FileField(null=False)
    uploaded_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title