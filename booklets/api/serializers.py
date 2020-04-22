
from rest_framework import serializers
from booklets.models import Booklets

class BookletSeroalizer(serializers.ModelSerializer):

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
            'PDF_FILE'
        ]