
from rest_framework import serializers
from books.models import Books

class CreateBookSerializer(serializers.ModelSerializer):

    class Meta:
        model=Books
        fields = [
            'id',
            'Title',
            'Description',
            'BookIMG',
            'BookIMG2',
            'Categories',
            'Publish_date',
            'Author',
            'ISBN',
            'Publisher',
            'PDF_Book',
            'Audio_Book',


        ]
        extra_kwargs = {'BookIMG2': {'required': False},
                        'PDF_Book':{'required': False},
                        'Audio_Book' : {'required': False}
                        }

