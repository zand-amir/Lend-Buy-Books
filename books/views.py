from django.shortcuts import render

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser

)

from rest_framework.generics import CreateAPIView

# from rest_framework import

from rest_framework.parsers import (
    MultiPartParser,
    FormParser
)

from books.api.serializers import CreateBookSerializer

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Books


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
