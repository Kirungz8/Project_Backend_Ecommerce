from django.contrib.auth.models import AbstractUser
from django.db import models

class user(AbstractUser):
    is_admin = models.BooleanField('is_admin', default=False)
    is_staff = models.BooleanField('is_staff', default=False)
    is_pelanggan = models.BooleanField('is_staff', default=False)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    image = models.ImageField(upload_to='image', null=True, blank=True)
    adress = models.CharField(max_length=225, null=True, blank=True)
    email = models.EmailField(max_length=225, unique=True, null=True, blank=True)

    def __str__(self):
        return self.username
# Create your models here.
