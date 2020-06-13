from django.shortcuts import render
from rest_framework.parsers import (FileUploadParser,
                                    MultiPartParser,
                                    FormParser)

from rest_framework.permissions import (AllowAny,
                                        IsAuthenticated
                                        )
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Q
from rest_framework import generics

from .api.filters import Dynamic_BookLets_search_Filter

from rest_framework.generics import ListAPIView

from rest_framework.viewsets import ModelViewSet

from .api.serializers import (
    BookletSerializer,
    Booklet_all_serializer,
    ViewBookletsSerializer
)

from rest_framework.filters import (
    SearchFilter,
    OrderingFilter,

)

import django_filters
from Users.models import user
from .models import Booklets
from rest_framework import status
from django.core.files import File
import PyPDF2
import random


def pageGrab(pdFile):
    currentFile = PyPDF2.PdfFileReader(pdFile)
    newFile = PyPDF2.PdfFileWriter()

    page = 0
    lastpage = currentFile.getNumPages()
    pagelist = []

    while (page <= lastpage):
        pagelist.append(random.randrange(page, min(page + 50, lastpage)))
        page += 50

    for p in pagelist:
        newFile.addPage(currentFile.getPage(p))

    return newFile


class BookletCreationAPI(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = BookletSerializer

    # parser_classes = (FileUploadParser,MultiPartParser , FormParser)
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            Owner = user.objects.get(username=request.user)
            Title = serializer.data.get("Title")
            Category = serializer.data.get("Category")
            Professor_name = serializer.data.get("Professor_name")
            Description = serializer.data.get("Description")
            Course_name = serializer.data.get("Course_name")
            University_name = serializer.data.get("University_name")
            Semester = serializer.data.get("Semester")

            try:

                booklet = Booklets(Owner=Owner, Title=Title, Category=Category, Description=Description,
                                   Course_name=Course_name,Professor_name = Professor_name,
                                   University_name=University_name, Semester=Semester)

                if ('Image' in request.FILES):
                    booklet.BookletIMG = File(request.FILES['Image'])

                if ('PDF' in request.FILES):
                    f = request.FILES['PDF']
                    nf = pageGrab(f)
                    booklet.PDF_Validate_File = File(nf)
                    booklet.PDF_FILE = File(f)
                booklet.save()

                content = {
                    'detail': 'successfully added booklet'}
                return Response(content, status=status.HTTP_201_CREATED)
            except:

                content = {'detail': 'Failed to create booklet '}

                return Response(content, status=status.HTTP_400_BAD_REQUEST)
        else:

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookletsView(APIView):

    def get(self, request, format=None, *args, **kwargs):

        booklets = Booklets.objects.all()
        serializer = Booklet_all_serializer(booklets, many=True)
        return Response({"List of all booklets ": serializer.data})


class ViewBookLetsAPI(ListAPIView):
    serializer_class = ViewBookletsSerializer

    filter_backends = [SearchFilter, OrderingFilter]

    search_fields = [
        'id',
        'Title',
        'Category',
        'Description'
        'Course_name',
        'University_name',
        'Professor_name',
        'Semester',
    ]

    def get_queryset(self, *args, **kwargs):
        queryset_list = Booklets.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            queryset_list = queryset_list.filter(
                Q(id__iexact=query) |
                Q(Title__iexact=query) |
                Q(Category__iexact=query) |
                Q(Description__icontains=query) |
                Q(Course_name__iexact=query) |
                Q(University_name__iexact=query) |
                Q(Professor_name__icontains=query) |
                Q(Semester__iexact=query)
            ).distinct()
        return queryset_list


class Searching_Booklets_View(ListAPIView):
    filter_backends = (Dynamic_BookLets_search_Filter,)
    queryset = Booklets.objects.all()
    serializer_class = ViewBookletsSerializer


class Booklets_Advance_Search(ModelViewSet):
    Our_fields = ('id',
                  'Title',
                  'Category',
                  'Description',
                  'Course_name',
                  'University_name',
                  'Professor_name',
                  'Semester',
                  )

    queryset = Booklets.objects.all()
    serializer_class = ViewBookletsSerializer

    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, SearchFilter, OrderingFilter)

    filter_fields = Our_fields
    search_fields = Our_fields
