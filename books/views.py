from django.shortcuts import render

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser

)


from rest_framework.generics import CreateAPIView


from books.api.serializers import FindOBJID

# from rest_framework import

from rest_framework.parsers import (
    MultiPartParser,
    FormParser
)

from books.api.serializers import (
    CreateBookSerializer,
    Proposed_BookSerializer
)

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import (
    Books ,
    Proposed_Book
)


from Users.models import user
from books.api.serializers import ProposeBookCreationSerializer

# Create your views here.

class CreateBookAPIView(CreateAPIView):
    queryset = Books.objects.all()
    serializer_class = CreateBookSerializer
    permission_classes = (IsAuthenticated, IsAdminUser)
    parser_classes = (MultiPartParser, FormParser)

    # def post(self, request, format=None):
    #     print(request.data)
    #     print("\n\n\n")
    #     serializer = PictureSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse(serializer.data)
    #     return JsonResponse(serializer.errors, status=400)
    #
    #


class TravelLougeCreationAPI(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProposeBookCreationSerializer

    def post(self, request, format=None):

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():

            creator = user.objects.get(username=request.user)

            Offered_price = serializer.data['Offered_price']

            Descriptions = serializer.data['Descriptions']

            books = serializer.data['books']

            try:

                proposed = Proposed_Book(Owner=creator, Offered_price=Offered_price, Descriptions=Descriptions)



                proposed.save()

                for b in books:
                    book = Books.objects.get(id=b)

                    proposed.Proposed_book.add(book)

                content = {

                    'detail': 'successfuly added the Proposed book'}

                return Response(content, status=status.HTTP_201_CREATED)

            except:

                content = {'detail': 'Failed to add Proposed book'}

                return Response(content, status=status.HTTP_400_BAD_REQUEST)

        else:

            return Response(serializer.errors,

                            status=status.HTTP_400_BAD_REQUEST)

class BookProposedAPI(APIView):
    permission_classes=(AllowAny,)
    serializer_class = FindOBJID
    serializer_class2 = Proposed_BookSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        book = Proposed_Book.objects.get(id=serializer.data['Object_ID'])
        serializer2 = self.serializer_class2(book)
        Data = serializer2.data
        Owner = book.Owner.username
        Data['Offered_price'] = serializer2.data['Offered_price']
        Data['Descriptions'] = serializer2.data['Descriptions']
        Data['Owner'] = Owner

        Data['Book_title'] = []
        for b in Data['Proposed_book']:
            __book = Books.objects.get(id=b)

            Data['Book_title'].append({'id': b , 'title': __book.title})

        return Response(b, status=status.HTTP_200_OK)


