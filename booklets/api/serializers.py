
from rest_framework import serializers
from booklets.models import Booklets

class BookletSeroalizer(serializers.ModelSerializer):

    class Meta:
        model = Booklets
        fields = (
            'Title',
            'Category',
            'Description',
            'Course_name',
            'University_name',
            'Professor_name',
            'Semester',
            'BookletIMG',
            'PDF_FILE',
        )

        extra_kwargs = {'Category': {'required': False},
                        'Description': {'required': False},
                        'Course_name': {'required': False} ,
                        'University_name': {'required': False},
                        'Professor_name': {'required': False},
                        'Semester': {'required': False}
                        }


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



