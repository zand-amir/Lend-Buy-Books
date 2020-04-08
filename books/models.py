from django.db import models

from Users.models import user


# Create your models here.

class Books(models.Model):
    CATEGORY = (
        ("بدون دسته بندی","بدون دسته بندی"),
        ("ادبیات", "ادبیات"),
        ("سفرنامه", "سفرنامه"),
        ("رمان", "رمان"),
        ("جغرافیا", "جغرافیا"),
        ("کتاب مرجع", "کتاب مرجع"),
        ("ورزشی", "ورزشی"),
        ("حقوقی", "حقوقی"),
        ("آشپزی", "آشپزی"),
        ("روانشناسی", "روانشناسی"),
        ("کتاب مصور", "کتاب مصور"),
        ("تاریخی", "تاریخی"),
        ("اجتماعی", "اجتماعی"),

    )
    Owner = models.ForeignKey(user , related_name='posts',on_delete=models.CASCADE)
    Title = models.CharField(max_length=100, blank=False, default='بدون عنوان')
    Description = models.TextField(default='بدون توضیحات', blank=False)
    categories = models.CharField(max_length=100, blank=False, null=False, choices=CATEGORY, default = "بدون دسته بندی")



    def __unicode__(self):
        return self.title



    def __str__(self):
        return self.title

