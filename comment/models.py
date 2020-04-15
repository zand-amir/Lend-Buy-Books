from django.db import models
from books.models import Proposed_Book
from Users.models import user




class Comment(models.Model):
    Addressed_Book = models.OneToOneField(Proposed_Book,on_delete=models.CASCADE)
    Comment_Author = models.OneToOneField(user,on_delete=models.CASCADE)
    Comment_Text = models.TextField(default='نظر کاربر')

    Owners_HR = models.CharField(max_length=8,choices=[('0','bad'),('1','medium'),('2','good'),('n/a','N/A')],default=('n/a'))        #Owner`s Honesty Rating

    def __str__(self):
        return '"' + str(self.Comment_Author)+ '"' + '`s Comment On ' + '<<' + str(self.Addressed_Book) + ">>"
