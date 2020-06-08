
from rest_framework import serializers
from booklets.models import Booklets

class BookletSerializer(serializers.Serializer):
    CATEGORY = (

        ("بدون دسته بندی" , "بدون دسته بندی"),
        ("پزشکی", "پزشکی"),
        ("علوم پایه", "علوم پایه"),
        ("زیست شناسی", "زیست شناسی"),
        ("زمین شناسی", "زمین شناسی"),
        ("مهندسی", "مهندسی"),
        ("روانشناسی", "روانشناسی"),
        ("حقوق", "حقوق"),

)
    Title = serializers.CharField(max_length = 25,allow_blank=False)
    Category = serializers.ChoiceField(choices=CATEGORY,default=CATEGORY[0][1])
    Description = serializers.CharField(max_length = 100,allow_blank=False)
    Course_name = serializers.CharField(max_length = 25,allow_blank = False)
    University_name = serializers.CharField(max_length = 25,allow_blank = False)
    Professor_name = serializers.CharField(max_length = 25,allow_blank = False)
    Semester = serializers.CharField(max_length = 25,allow_blank = False)



class Booklet_all_serializer(serializers.ModelSerializer):
    class Meta:
        model = Booklets
        fields = '__all__'

class ViewBookletsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booklets
        fields = [
            'id',
            'Title',
            'Category',
            'Description',
            'Course_name',
            'University_name',
            'Professor_name',
            'Semester',
            'BookletIMG',
            'PDF_FILE',
            'PDF_Validate_File',
        ]



