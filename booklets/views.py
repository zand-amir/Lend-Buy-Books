from django.shortcuts import render

from rest_framework.permissions import( AllowAny ,
                                        IsAuthenticated
                                        )
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from .api.serializers import BookletSeroalizer
from Users.models import user
from .models import Booklets
from rest_framework import status
# Create your views here.

class BookletCreationAPI(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = BookletSeroalizer

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
                    booklet.PDF_FILE = request.data['PDF_FILE']
                    # some extra comment for arash
                    # hey man
                    #  see booklet.PDF_FILE stores the contents that you need
                    # u can use this and write what ever you need
                    # good luck :)
                Booklets.save()

                content = {
                    'detail': 'successfully added booklet'}
                return Response(content, status=status.HTTP_201_CREATED)
            except:

                content = {'detail': 'Failed to create booklet '}

                return Response(content, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


