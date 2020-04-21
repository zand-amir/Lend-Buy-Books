from django.db import models
from Users.models import user

# Create your models here.


class Booklets(models.Model):
    CATEGORY = (

        ("بدون دسته بندی" , "بدون دسته بندی"),
        ("پزشکی", "پزشکی"),
        ("علوم پایه", "علوم پایه"),
        ("زیست شناسی", "زیست شناسی"),
        ("زمین شناسی", "زمین شناسی"),
        ("مهندسی", "منهدسی"),
        ("روانشناسی", "روانشناسی"),
        ("حقوق", "حقوق"),

    )

    Owner = models.ForeignKey(user , related_name="Book_let_owner" , on_delete=models.CASCADE )
    Title = models.CharField(max_length=100, blank=False, default='بدون ذکر نام')
    Category = models.CharField(max_length=100, blank=False, null=False, choices=CATEGORY, default=CATEGORY[0][1])
    Description = models.TextField(default='بدون توضیحات', blank=False)
    Course_name = models.CharField(max_length=100, blank=False, default='بدون ذکر نام درس')
    University_name = models.CharField(max_length=100, blank=False, default='بدون ذکر نام دانشگاه')
    Professor_name = models.CharField(max_length=100, blank=False, default='بدون ذکر نام استاد')
    Semester = models.CharField(max_length=100, blank=False, default='بدون ذکر ترم')
    BookletIMG = models.ImageField(upload_to='BookLET/%Y/%m/%d/', blank=True)
    PDF_FILE = models.FileField(upload_to='BookLETPDF/%Y/%m/%d/', blank=True)
    # Arash should make a decision
    # PDF_Validate_File = models.FileField(upload_to='ValPDF/%Y/%m/%d/', blank=True)

    def __unicode__(self):
        return self.Title

    def __str__(self):
        return self.Title




