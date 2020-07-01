from django.shortcuts import render
from django.forms.models import model_to_dict
from django.utils import timezone

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated
)

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import user, Message, Conversation
from Users.api.serializers import UserInformationSerializer, CreditSerializer, MessageSerializer


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
                    new_user.img = request.data['img']
                new_user.save()
                content = {'detail': 'new user successfully created ! '}

                return Response(content, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AddCreditAPI(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CreditSerializer

    def post(self, request, format = None):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            if not(user.objects.filter(username=request.user)):
                content = {'detail': 'Invalid User!'}
                return Response(content, status=status.HTTP_401_UNAUTHORIZED)
            usr = user.objects.get(username = self.request.user)
            usr.credit += serializer.data['Amount']
            usr.save()
            content = {'detail': 'success'}
            return Response(content, status=status.HTTP_200_OK)
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


class SendMessageAPI(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = MessageSerializer

    def post(self,request,format=None,*args,**kwargs):
        serializer = self.serializer_class(data=request.data, partial=True)

        if serializer.is_valid():
            if not(user.objects.filter(username=request.user)):
                content = {'detail': 'Invalid User!'}
                return Response(content, status=status.HTTP_401_UNAUTHORIZED)
            p1 = user.objects.get(username=request.user)
            if not(user.objects.filter(id=self.kwargs['recipient'])):
                content = {'detail': 'Invalid Recipiant ID!'}
                return Response(content, status=status.HTTP_400_BAD_REQUEST)
            p2 = user.objects.get(id=self.kwargs['recipient'])

            text = serializer.data['Text']
            message = Message(Text=text,Date=timezone.now())
            message.save()
            l = Conversation.objects.filter(Participant1 = p1)
            if l:
                c = l.filter(Participant2 = p2)
                if c:
                    conversation = c[0]
                else:
                    conversation = Conversation(Participant1 = p1, Participant2 = p2)
                    conversation.save()
            else:
                l = Conversation.objects.filter(Participant1 = p2)
                if l:
                    c = l.filter(Participant2 = p1)
                    if c:
                        conversation = c[0]
                    else:
                        conversation = Conversation(Participant1 = p2, Participant2 = p1)
                        conversation.save()
                else:
                    conversation = Conversation(Participant1 = p1, Participant2 = p2)
                    conversation.save()

            conversation.Log.add(message)
            content = {'detail':'Success!'}
            return Response(content, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

                
                
class getConversationAPI(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self,request,format=None,*args,**kwargs):
        if not(user.objects.filter(username=request.user)):
            content = {'detail': 'Invalid User!'}
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)
        p1 = user.objects.get(username=request.user)
        if not(user.objects.filter(id=self.kwargs['recipient'])):
            content = {'detail': 'Invalid Recipiant ID!'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        p2 = user.objects.get(id=self.kwargs['recipient'])
            
        l = Conversation.objects.filter(Participant1 = p1)
        if l:
            c = l.filter(Participant2 = p2)
            if c:
                conversation = c[0]
            else:
                conversation = 'N/A'
        else:
            l = Conversation.objects.filter(Participant1 = p2)
            if l:
                c = l.filter(Participant2 = p1)
                if c:
                    conversation = c[0]
                else:
                    conversation = 'N/A'
            else:
                conversation = 'N/A'

        if conversation == 'N/A':
            content = {'detail':'No messages yet!'}
            return Response(content, status=status.HTTP_200_OK)
        content = {'Messages':[]}
        for message in conversation.Log.all():
            m = {'text':message.Text,'date':message.Date}
            content['Messages'].append(m)
        return Response(content, status=status.HTTP_200_OK)
