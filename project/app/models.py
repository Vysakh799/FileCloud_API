from django.db import models
from django.contrib.auth.models import User
    
class Files(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    file=models.FileField(null=False)
    uploaded_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.file.name