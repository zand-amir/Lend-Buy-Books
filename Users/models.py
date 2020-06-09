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

class Message(models.Model):
    Text = models.CharField(max_length=100,blank = False)
    Date = models.DateTimeField()

class Conversation(models.Model):
    Participant1 = models.ForeignKey(user, on_delete = models.CASCADE,related_name='participant1', unique = False)
    Participant2 = models.ForeignKey(user, on_delete = models.CASCADE,related_name='participant2', unique = False)
    Log = models.ManyToManyField(Message)

