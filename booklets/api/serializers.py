
from rest_framework import serializers
from booklets.models import Booklets

class BookletSeroalizer(serializers.ModelSerializer):

    class Meta:
        model = Booklets
        fields = [
            'Title',
            'Category',
            'Description',
            'Course_name',
            'University_name',
            'Professor_name',
            'Semester',
            'BookletIMG',
            'PDF_FILE',
        ]


class Booklet_all_serializer(serializers.ModelSerializer):
    class Meta:
        model = Booklets
        fields = '__all__'

class ViewBookletsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booklets
        fields = [
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



