from django.db import models

# Create your models here.

class Ajaxvalue(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField(null=True)
    dept=models.CharField(max_length=100)
    created_time = models.DateTimeField(auto_now_add=True, null=True)
    updated_time = models.DateTimeField(auto_now=True, null=True)
    
