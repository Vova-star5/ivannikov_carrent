from django.db import models
from django.contrib.auth.models import User

    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    lastname = models.CharField(max_length=20, null=True, blank=True)
    name = models.CharField(max_length=20, null=True, blank=True)
    surname = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=12, null=True, blank=True)
    delivery_adress = models.TextField(null=True, blank=True, max_length=100)
