from django.db import models
from django.contrib.auth.models import AbstractUser

class custom_user(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_worker = models.BooleanField(default=False)
    birth_date = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=10, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    zip_code = models.CharField(max_length=6, null=True, blank=True)
