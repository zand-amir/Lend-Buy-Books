from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from .models import Comment
from books.models import Books
from Users.models import user
from .serializers import CommentSerializer, CommentCreationSerializer
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser

)
from rest_framework.response import Response
from rest_framework import status

class CommentViewAPI(APIView):
    serializer_class = CommentSerializer
    perimission_classes = (IsAuthenticated,)
    #queryset = Comment.objects.all()

    def post(self, request, format=None):
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            if not(Books.objects.filter(id = serializer.data['BookID'])):
                content = {'detail': 'Invalid Book ID'}
                return Response(content, status=status.HTTP_400_BAD_REQUEST)
            Intended_Book = Books.objects.get(id = serializer.data['BookID'])
            comlist = [{'auth':com.Comment_Author.username ,'text':com.Comment_Text}for com in Comment.objects.filter(Addressed_Book = Intended_Book)]
            content = {'detail':'Success','Comments':comlist}
            return Response(content, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

class SubmitCommentAPI(APIView):
    perimission_classes = (IsAuthenticated,)
    serializer_class = CommentCreationSerializer

    def post(self, request, format = None):
        serializer = self.serializer_class(data = request.data)
        
        if serializer.is_valid():
            if not(user.objects.filter(username=request.user)):
                content = {'detail': 'Invalid User!'}
                return Response(content, status=status.HTTP_401_UNAUTHORIZED)
            Author = user.objects.get(username=request.user)
            CT = serializer.data['Comment_text']
            if not(Books.objects.filter(id=serializer.data['BookID'])):
                content = {'detail': 'Invalid Book ID!'}
                return Response(content, status=status.HTTP_400_BAD_REQUEST)
            AB = Books.objects.get(id=serializer.data['BookID'])
            try:
                CommentInstance = Comment(Addressed_Book = AB, Comment_Author = Author, Comment_Text = CT)
                CommentInstance.save()
                content = {
                   'detail': 'successfuly Submiited the comment'}
                return Response(content, status=status.HTTP_201_CREATED)
            except:
               content = {'detail': 'Failed to Submit the comment'}
               return Response(content, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        
            
    
