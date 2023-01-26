from django.db import models
from django.conf import settings
# Create your models here.
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from datetime import datetime  


class UserDetails(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    dob = models.DateField(null=True)
    address = models.TextField(null=True)
    phone = models.TextField(null=True)

class Supplier(models.Model):
    TYPE_CHOICES = [
        ('customer', 'Customer'),
        ('supplier', 'Supplier')
    ]
    name = models.CharField(max_length=191,null=True)
    legal_form = models.CharField(max_length=191,null=True)
    uid = models.CharField(max_length=191,null=True)
    website = models.CharField(max_length=800,null=True)
    internal_number = models.CharField(max_length=191)
    phone = models.CharField(max_length=191,null=True)
    categories = models.CharField(max_length=191,null=True)
    type = models.CharField(max_length=40,choices=TYPE_CHOICES,default='supplier')
    created_on = models.DateTimeField(default=datetime.now, blank=True)
    updated_on = models.DateTimeField(default=datetime.now, blank=True)


