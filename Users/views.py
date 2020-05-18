from django.shortcuts import render

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated
)

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import user
from Users.api.serializers import UserInformationSerializer


# Create your views here.

class SignupAPI(APIView):
    permission_classes = (AllowAny,)
    serializer_class = UserInformationSerializer

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

                new_user = user.objects.create_user(username=username, email=email, password=password,
                                                    first_name=first_name, last_name=last_name)

                new_user.phone_number = phone_number
                new_user.address = address
                new_user.postal_code = postal_code
                if ('img' in request.data):
                    new_user.avatar = request.data['img']
                new_user.save()
                content = {'detail': 'new user successfully created ! '}

                return Response(content, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfile(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserInformationSerializer

    def get(self,request,format=None,*args,**kwargs):
        if self.kwargs.get('user'):
            usr = user.objects.get(id=self.kwargs['user'])
        else:
            usr = user.objects.get(username=request.user)
        content = model_to_dict(usr)
        content['img'] = 'media/'+str(content['img']).split(':')[-1]
        return Response(content, status=status.HTTP_200_OK)

    def patch(self,request,format=None):
        serializer = self.serializer_class(data=request.data, partial=True)

        if serializer.is_valid():
            usr = user.objects.get(username = self.request.user)
            for i in serializer.validated_data.keys():
                if i != 'password':
                    usr.__dict__[i] = serializer.validated_data[i]
            usr.save()
            content={
                "detail":"success",
                "user":model_to_dict(usr)}
            content["user"]['img'] = 'media/'+str(content["user"]['img']).split(':')[-1]
            return Response(content, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


