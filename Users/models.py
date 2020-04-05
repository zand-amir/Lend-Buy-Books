from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class user(User):

    address = models.CharField(min_length=15, max_length=200, allow_blank=True)
    postal_code = models.CharField(min_length=9, allow_blank=True)
    phone_number=models.CharField(max_length=15)
    img =models.ImageField(default='media/profile/images.png',upload_to='profile')