from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class user(User):

    phone_number=models.CharField(max_length=15)
    img =models.ImageField(default='media/profile/images.png',upload_to='profile')