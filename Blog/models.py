from django.db import models
from Users.models import user

class BComment(models.Model):
    Author = models.ForeignKey(user,on_delete=models.CASCADE,null=False)
    Date = models.DateTimeField(null=False)
    Title = models.CharField(max_length=40,null=False,blank=False,default="بدون عنوان")
    Text = models.CharField(max_length=100,null=False,blank=False)
    Likes = models.IntegerField(null=False,default=0)

class BPost(models.Model):
    Author = models.ForeignKey(user,on_delete=models.CASCADE,null=False)
    Date = models.DateTimeField(null=False)
    Thumbnail = models.ImageField(upload_to='Blog/thumbnails/%Y/%m/%d',blank = True)
    Title = models.CharField(max_length = 40,null=False,blank=False)
    Text = models.TextField(null=False,blank=False)
    PostImage = models.ImageField(upload_to='Blog/posts/%Y/%m/%d',blank = True)
    Likes = models.IntegerField(null=False,default=0)
    Comments = models.ManyToManyField(BComment)
