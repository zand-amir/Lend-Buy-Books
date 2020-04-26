from django.shortcuts import render
from rest_framework.parsers import (FileUploadParser ,
                                    MultiPartParser ,
                                    FormParser)

from rest_framework.permissions import( AllowAny ,
                                        IsAuthenticated
                                        )
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from .api.serializers import (
    BookletSeroalizer ,
    Booklet_all_serializer
)
from Users.models import user
from .models import Booklets
from rest_framework import status
from django.core.files import File
import  PyPDF2
import random


def pageGrab(pdFile):
    currentFile = PyPDF2.PdfFileReader(pdFile)
    newFile = PyPDF2.PdfFileWriter()

    page = 0
    lastpage = currentFile.getNumPages()
    pagelist = []

    while (page <= lastpage):
        pagelist.append(random.randrange(page,min(page+50,lastpage)))
        page += 50

    for p in pagelist:
        newFile.addPage(currentFile.getPage(p))

    return newFile

class BookletCreationAPI(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = BookletSeroalizer
    #parser_classes = (FileUploadParser,MultiPartParser , FormParser)
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            Owner = user.objects.get(username=request.user)
            Title = serializer.data['Title']
            Category = serializer.data['Category']
            Description = serializer.data['Description']
            Course_name = serializer.data['Course_name']
            University_name = serializer.data['University_name']
            Semester = serializer.data['Semester']
            try:

                booklet = Booklets(Owner = Owner , Title = Title , Category = Category , Description = Description , Course_name=Course_name ,
                                   University_name = University_name , Semester =Semester)

                if ('BookletIMG' in request.data):
                    booklet.BookletIMG = request.data['BookletIMG']

                if ('PDF_FILE' in request.data):
                    f = request.data['PDF_FILE']
                    booklet.PDF_FILE = f
                    booklet.PDF_Validate_File = File(pageGrab(f))
  
                Booklets.save()

                content = {
                    'detail': 'successfully added booklet'}
                return Response(content, status=status.HTTP_201_CREATED)
            except:

                content = {'detail': 'Failed to create booklet '}

                return Response(content, status=status.HTTP_400_BAD_REQUEST)
        else:

            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



class BookletsView(APIView):

    def get(self,request,format=None,*args, **kwargs):
        def get(self, request, format=None, *args, **kwargs):
            booklets = Booklets.objects.all()
            serializer = Booklet_all_serializer(booklets, many=True)
            return Response({"List of all booklets ": serializer.data})






