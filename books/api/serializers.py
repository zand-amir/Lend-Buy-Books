
from rest_framework import serializers

from books.models import(

    Books ,
    Proposed_Book

)

class CreateBookSerializer(serializers.ModelSerializer):

    class Meta:
        model=Books
        fields = "__all__"
        #     [
        #     'id',
        #     'Title',
        #     'Description',
        #     'BookIMG',
        #     'BookIMG2',
        #     'Categories',
        #     'Publish_date',
        #     'Author',
        #     'ISBN',
        #     'Publisher',
        #     'PDF_Book',
        #     'Audio_Book',
        #
        #
        # ]
        extra_kwargs = {'BookIMG2': {'required': False},
                        'PDF_Book':{'required': False},
                        'Audio_Book' : {'required': False}
                        }



class Proposed_BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Proposed_Book
        fields = '__all__'



class FindOBJID(serializers.Serializer):
    Object_ID=serializers.IntegerField()

