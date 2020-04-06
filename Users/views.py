from django.shortcuts import render

from rest_framework.permissions import (
    AllowAny
)

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import user
from Users.api.serializers import SignupSerializer


# Create your views here.

class SignupAPI(APIView):
    permission_classes = (AllowAny,)
    serializer_class = SignupSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            username = serializer.data['username']
            email = serializer.data['email']
            password = serializer.data['password']
            first_name = serializer.data['first_name']
            last_name = serializer.data['last_name']
            phone_number = serializer.data['phone_number']
            address = serializer.data['address']
            postal_code = serializer.data['postal_code']
            try:
                new_user = user.objects.get(username=username)
                content = {'detail':
                               'This user already exists '}
                return Response(content, status=status.HTTP_400_BAD_REQUEST)

            except:

                new_user = user.objects.create_user(username=username , email=email, password=password,
                                             first_name=first_name, last_name=last_name  )

                new_user.phone_number = phone_number
                new_user.address = address
                new_user.postal_code = postal_code
                if ('img' in request.data):
                    new_user.avatar = request.data['img']
                new_user.save()
                content = {'detail': 'new user successfully created ! ' }

                return Response(content, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
