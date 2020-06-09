from django.shortcuts import render
from django.utils import timezone

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser

)

from django.db.models import Avg

import django_filters

from rest_framework.generics import CreateAPIView


from books.api.serializers import FindOBJID

# from rest_framework import

from rest_framework.parsers import (
    MultiPartParser,
    FormParser,
    JSONParser
)
from .api.filters import Dynamic_Books_search_Filter

from books.api.serializers import (
    rateViewSerializer,
    CreateBookSerializer,
    Proposed_BookSerializer,
    BuySerializer,
    RateSerializer,
    BorrowBookCreationSerializer,
    Borrow_BookSerializer,
    BorrowBookStartBorrowSerializer ,
    Book_all_serializer ,
    ViewBooksSerializer,
    WishSerializer,
    RateViewSerializer,
    Propose_bookView_Serializer

)

from django.db.models import Q

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import (
    Books,
    Proposed_Book,
    Borrow_book,
    BookRate,
    Wishlist
)

from Users.models import user
from books.api.serializers import ProposeBookCreationSerializer
from rest_framework.generics import ListAPIView

from rest_framework.filters import (
        SearchFilter,
        OrderingFilter,

)

from rest_framework.viewsets import ModelViewSet
# Create your views here.

class CreateBookAPIView(CreateAPIView):
    queryset = Books.objects.all()
    serializer_class = CreateBookSerializer
    permission_classes = (IsAuthenticated,)


    # def post(self, request, format=None):
    #     print(request.data)
    #     print("\n\n\n")
    #     serializer = PictureSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse(serializer.data)
    #     return JsonResponse(serializer.errors, status=400)




class Proposed_bookCreationAPI(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProposeBookCreationSerializer

    def post(self, request, format=None):

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():

            creator = user.objects.get(username=request.user.username)
            Offered_price = serializer.data['Offered_price']
            Descriptions = serializer.data['Descriptions']
            books = serializer.data['books']

            try:

                proposed = Proposed_Book(Owner=creator, Offered_price=Offered_price, Descriptions=Descriptions)
                proposed.save()
                for b in books:
                    book = Books.objects.get(id=b)
                    proposed.Proposed_book.add(book)
                    if Wishlist.objects.filter(WishedBook=b).exists():
                        wi = Wishlist.objects.get(WishedBook=b).Wishers
                        if wi.exists():
                            for u in wi.all():
                                print(str(u)+' wants this book')
                                #notify the u user (send emails,etc...)

                content = {
                    'detail': 'successfuly added the Proposed book'}
                return Response(content, status=status.HTTP_201_CREATED)

            except:
                content = {'detail': 'Failed to add Proposed book'}
                return Response(content, status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


class BuyAPI(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = BuySerializer

    def post(self, request, format=None):

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            Buyer = user.objects.get(username=request.user)
            Offer = Proposed_Book.objects.get(id=serializer.data['OfferID'])
            a = Offer.Offered_price
            b = Buyer.credit
            if Buyer.credit < Offer.Offered_price:
                content = {
                    'detail':'User does not have the requested credit!'}
                return Response(content, status=status.HTTP_200_OK)
            Buyer.credit -= Offer.Offered_price
            Seller.credit += Offer.Offered_price
            Buyer.save()
            Seller.save()
            print(str(Offer) + 'has been completed.')
            Offer.delete()
            content = {
                    'detail': 'Success'}
            return Response(content, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


class ViewBooksAPI(ListAPIView):

    serializer_class = ViewBooksSerializer
    filter_backends= [SearchFilter, OrderingFilter]

    search_fields = [
        'id',
        'Title',
        'Categories',
        'Description'
        'Publish_date',
        'publish_series',
        'Author',
        'Price',
        'ISBN',
        'Publisher'
    ]

    def get_queryset(self, *args, **kwargs):
        queryset_list = Books.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            queryset_list = queryset_list.filter(
                Q(id__iexact = query) |
                Q(Title__iexact=query) |
                Q(Categories__iexact=query) |
                Q(Description__icontains=query) |
                Q(Publish_date__iexact=query) |
                Q(publish_series__iexact=query) |
                Q(Author__iexact=query) |
                Q(Price__iexact=query) |
                Q(ISBN__iexact=query) |
                Q(Publisher__iexact=query)
            ).distinct()
        return queryset_list


class ViewRateapiView(ListAPIView):
    #serializer_class = RateViewSerializer

    def get(self , request , *args , **kwargs):
        getBookid = self.kwargs['BookID']
        list_of_all_rates = BookRate.objects.filter(Book__exact=getBookid)
        saved_list = []
        for rates in list_of_all_rates:
            saved_list.append(rates.rate)
        sum = 0
        length_of_int =len(saved_list)
        if length_of_int !=0:
            for i in saved_list:
                sum += i
            sum =sum/length_of_int

            content = {"average":sum}
            return Response(content,status=status.HTTP_200_OK)
        else:
            content = {"detail":"No user rated yet"}
            return Response(content , status = status.HTTP_204_NO_CONTENT)

    # def get_queryset(self):
    #
    #     getBookid = self.kwargs['BookID']
    #     return BookRate.objects.filter(Boo

# class ViewProposeAdvanceapiView(ListAPIView):
#     #serializer_class = RateViewSerializer
#
#     def get(self , request , *args , **kwargs):
#         getBookProposeid = self.kwargs['booksID']
#         Offer =Proposed_Book.objects.filter(Proposed_book__exact=getBookProposeid)
#         for instance in Offer:
#             instance.Owner.username
#             instance.Owner.address
#
#
#         print(.get())
#
#
#         return Response({"aa":"aa"},status=status.HTTP_200_OK)



class ViewProposed_book_apiView(ListAPIView):

    serializer_class = Propose_bookView_Serializer

    def get_queryset(self):
        getID = self.kwargs['booksID']
        return Proposed_Book.objects.filter(Proposed_book__in=getID)
    # def get_queryset(self):
    #
    #     getBookid = self.kwargs['BookID']
    #     return BookRate.objects.filter(Book__exact=getBookid)



class Searching_Book_View(ListAPIView):

    filter_backends = (Dynamic_Books_search_Filter,)
    queryset = Books.objects.all()
    serializer_class = ViewBooksSerializer



class Book_Advance_Search(ModelViewSet):

    Our_fields = ('id',
                  'Title',
                  'Categories',
                  'Publish_date',
                  'publish_series',
                  'Author',
                  'Price',
                  'ISBN',
                  'Publisher'
                  )

    queryset = Books.objects.all()
    serializer_class = ViewBooksSerializer

    filter_backends = (django_filters.rest_framework.DjangoFilterBackend , SearchFilter, OrderingFilter)

    filter_fields = Our_fields
    search_fields = Our_fields


class RateBookAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = RateSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            This_user = user.objects.get(username=request.user.username)
            bookID = serializer.data['BookID']
            Value_of_rate = serializer.data['rate']

            book = Books.objects.get(id=bookID)
            try:

                rate = BookRate.objects.get(user=This_user, Book=book)

                rate.rate = Value_of_rate

            except:

                rate = BookRate(user=This_user, Book=book, rate=Value_of_rate)

            rate.save()

            content = {'Book': book.Title, 'user': This_user.username, 'rate': rate.rate,
                       'detail': 'successfully added rate for book :) '}
            return Response(content, status=status.HTTP_201_CREATED)

        else:

            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)




class Borrow_bookCreationAPI(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = BorrowBookCreationSerializer

    def post(self, request, format=None):

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():

            creator = user.objects.get(username=request.user)
            Descriptions = serializer.data['Descriptions']
            books = serializer.data['books']

            try:

                bor = Borrow_book(Owner=creator, Descriptions=Descriptions)
                bor.save()
                for b in books:
                    book = Books.objects.get(id=b)
                    bor.Offered_to_borrow.add(book)

                content = {
                    'detail': 'successfuly added the Borrow book offer'}
                return Response(content, status=status.HTTP_201_CREATED)

            except:
                content = {'detail': 'Failed to add Borrow book offer'}
                return Response(content, status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


def DeterminTimes():
    return (timezone.now(),timezone.now() + timezone.timedelta(days=7))

class StartBorrowAPI(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = BorrowBookStartBorrowSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():

            Intended_Offer_ID = serializer.data['BorrowOfferID']

            try:
                bor = Borrow_book.objects.get(id=Intended_Offer_ID)
                (bor.StartBorrowingTime,bor.EndBorrowingTime) = (timezone.now(),timezone.now() + timezone.timedelta(days=7))
                bor.save()
                content = {
                    'detail': 'successfuly Started the Borrow book action'}
                return Response(content, status=status.HTTP_201_CREATED)
            except:
                content = {'detail': 'Failed to Start the Borrow book action'}
                return Response(content, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


class Book_all_View(APIView):
    def get(self,request,format=None,*args, **kwargs):

        books = Books.objects.all()
        serializer = Book_all_serializer(books,many=True)

        return Response({"This is list of all Books ":serializer.data})

class WishBook(APIView):
    permision_classes = (IsAuthenticated,)
    serializer_class = WishSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            try:
                BID = serializer.data['BookID']
                print(BID)
                book = Books.objects.get(id=BID)
                print(book)
                if Wishlist.objects.filter(WishedBook = book).exists():
                    print(1111111111111111)
                    WlInstance = Wishlist.objects.get(WishedBook=book)
                    print(2222222222222222)
                else:
                    WlInstance = Wishlist(WishedBook=book)
                print("WI CREATED")
                WlInstance.save()
                wisher = user.objects.get(username=request.user)
                print(wisher)
                WlInstance.Wishers.add(wisher)
                print('added')
                propose_list = Proposed_Book.objects.filter(Proposed_book = book)
                if propose_list.exists():
                    content = {'detail' : 'offers exist','offer_list':propose_list}
                    return Response(content, status=status.HTTP_201_CREATED)
                else:
                    content = {'detail' : 'no offer'}
                    return Response(content, status=status.HTTP_201_CREATED)
            except:
                content = {'detail': 'Failed to perform the action'}
                return Response(content, status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


#
# class BookProposedAPI(APIView):
#     permission_classes=(AllowAny,)
#     serializer_class = FindOBJID
#     serializer_class2 = Proposed_BookSerializer
#
#     def post(self, request, format=None):
#         serializer = self.serializer_class(data=request.data)
#
#         book = Proposed_Book.objects.get(id=serializer.data['Object_ID'])
#         serializer2 = self.serializer_class2(book)
#         Data = serializer2.data
#         Owner = book.Owner.username
#         Data['Offered_price'] = serializer2.data['Offered_price']
#         Data['Descriptions'] = serializer2.data['Descriptions']
#         Data['Owner'] = Owner
#
#         Data['Book_title'] = []
#         for b in Data['Proposed_book']:
#             __book = Books.objects.get(id=b)
#
#             Data['Book_title'].append({'id': b , 'title': __book.title})
#
#         return Response(b, status=status.HTTP_200_OK)
