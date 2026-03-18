from django.db import models
from django.contrib.auth.models import User

def upload_img(instance: "Car", filename):
    path = f"cars/{instance.pk}/{filename}"
    return path

class Car(models.Model):
    name = models.CharField(max_length=100)
    carmodel = models.CharField(max_length=100)
    description = models.TextField(null=False, blank=True)
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    discount = models.SmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    archived = models.BooleanField(default=False)
    img = models.ImageField(null=True, blank=True, upload_to=upload_img)

    
class Order(models.Model):
    delivery_adress = models.TextField(null=False, blank=True)
    promocode = models.CharField(max_length=20, null=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    # products = models.ManyToManyField(Product, related_name="orders")