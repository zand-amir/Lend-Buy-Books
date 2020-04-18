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
    #Owner = models.ForeignKey(user , related_name='books',on_delete=models.CASCADE)
    Title = models.CharField(max_length=100, blank=False, default='بدون عنوان')
    Description = models.TextField(default='بدون توضیحات', blank=False)
    Categories = models.CharField(max_length=100, blank=False, null=False, choices=CATEGORY, default = "بدون دسته بندی")
    Publish_date = models.CharField(max_length=100 , blank=False , default='تاریخ ذکر نشده است')
    publish_series = models.CharField(max_length=100, blank=False, default=' ذکر نشده است')
    Author = models.CharField(max_length=100 , blank= False , default='بدون نویسنده')
    Price = models.CharField(max_length=100 , blank= False , default='بدون قیمت')
    ISBN = models.CharField(max_length=100, blank=False, default='بدون شابک')
    Publisher = models.CharField(max_length=100 , blank= False , default= 'بدون ناشر')
    BookIMG = models.ImageField(upload_to='Image/%Y/%m/%d/', blank=True)
    BookIMG2 = models.ImageField(upload_to='Image/%Y/%m/%d/', blank=True)
    PDF_Book = models.FileField(upload_to='PDF/%Y/%m/%d/', blank=True  , name= 'کتاب الکترونیکی')
    Audio_Book = models.FileField(upload_to='Audios/%Y/%m/%d/', blank=True , name='کتاب صوتی')




    def __unicode__(self):
        return self.Title


    def __str__(self):
        return self.Title



class Proposed_Book(models.Model):


    Owner = models.ForeignKey(user ,on_delete = models.CASCADE,null=True, related_name='have_book')
    #Proposed_book = models.ForeignKey(Books ,on_delete = models.CASCADE,null=True, related_name='proposedBook')
    Proposed_book = models.ManyToManyField(Books)
    Offered_price = models.CharField(max_length=100 , blank= False , default='بدون قیمت')
    Descriptions = models.CharField(max_length=100 , blank= False , default='بدون توضیحات')

    def __str__(self):
        result = ''
        qs = self.Proposed_book.all()
        for i in qs:
            result += str(i)+', '
        return result + 'Offered By ' + '"' + str(self.Owner) + '"'


class Borrow_book(models.Model):


    Owner = models.ForeignKey(user ,on_delete = models.CASCADE,null=True, related_name='want_to_borrow')
    #Proposed_book = models.ForeignKey(Books ,on_delete = models.CASCADE,null=True, related_name='proposedBook')
    Offered_to_borrow = models.ManyToManyField(Books)
    StartBorrowingTime = models.DateTimeField(null=True, blank=True)
    EndBorrowingTime = models.DateTimeField(null=True, blank=True)
    Descriptions = models.CharField(max_length=1000 , blank= False , default='بدون توضیحات')

    def __str__(self):
        result = ''
        qs = self.Offered_to_borrow.all()
        for i in qs:
            result += str(i)+', '
        return result + 'Offered By ' + '"' + str(self.Owner) + '"'

    
class BookRate(models.Model):
    user = models.ForeignKey(user , related_name= 'user_who_rated',on_delete=models.CASCADE)
    Book = models.ForeignKey(Books , on_delete=models.CASCADE)
    rate=models.IntegerField(blank=True)




