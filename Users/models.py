from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
# Create your models here.

class user(User):

    address = models.CharField(max_length=200,   blank= True)
    postal_code = models.CharField( max_length = 15 , blank=True)
    phone_number = models.CharField(max_length=15)
    img = models.ImageField(default='media/profile/images.png',upload_to='profile')
    credit = models.IntegerField(default=0)
