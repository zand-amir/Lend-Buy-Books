from .serializers import BPostSerializer, BCommentSerializer
from .models import BComment, BPost
from Users.models import user

from django.core.files import File
from django.utils import timezone
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response

class BPostCreate(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = BPostSerializer

    def post(self, request, format=None, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            if not(user.objects.filter(username=request.user)):
                content = {'detail': 'Invalid User!'}
                return Response(content, status=status.HTTP_401_UNAUTHORIZED)
            Author = user.objects.get(username=request.user)
            Title = serializer.data['Title']
            Text = serializer.data['Text']
            Date = timezone.now()
            bpost = BPost(Author=Author,Date=Date,Title=Title,Text=Text,Likes=0)
            
            if ('ThumbnailIMG' in request.FILES):
                bpost.Thumbnail = File(request.FILES['ThumbnailIMG'])
            if ('PostIMG' in request.FILES):
                bpost.PostImage = File(request.FILES['PostIMG'])

            bpost.save()

            content = {'detail': 'Successfully added the post!'}
            return Response(content, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BCommentSubmit(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = BPostSerializer

    def post(self, request, format=None, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            if not(BPost.objects.filter(id=self.kwargs['BPostID'])):
                content = {'detail': 'Invalid post ID!'}
                return Response(content, status=status.HTTP_400_BAD_REQUEST)
            bpost = BPost.objects.get(id=self.kwargs['BPostID'])
            if not(user.objects.filter(username=request.user)):
                content = {'detail': 'Invalid User!'}
                return Response(content, status=status.HTTP_401_UNAUTHORIZED)
            Author = user.objects.get(username=request.user)
            Title = serializer.data['Title']
            Text = serializer.data['Text']
            Date = timezone.now()
            bcom = BComment(Author=Author,Date=Date,Title=Title,Text=Text,Likes=0)
            bcom.save()

            bpost.Comments.add(bcom)

            content = {'detail': 'Successfully submitted the comment!'}
            return Response(content, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BPostView(APIView):
    permission_classes = (AllowAny,)

    def get(self,request,format=None):
        content = {'detail':'Success!','Posts':[]}
        
        for bp in BPost.objects.all():
            bpdict = {'id':bp.id, 'Author':bp.Author.username, 'Title':bp.Title, 'Thumbnail':'N/A', 'Date':bp.Date, 'Text':bp.Text[:100], 'continued':bool(bp.Text[100:]), 'Likes':bp.Likes}
            if bp.Thumbnail:
                bpdict['Thumbnail'] = bp.Thumbnail
            content['Posts'].append(bpdict)
            
        if not content['Posts']:
            content['detail']='No post available yet!'
        return Response(content, status=status.HTTP_200_OK)

class BPostRetrieve(APIView):
    permission_classes = (AllowAny,)

    def get(self,request,format=None,*args,**kwargs):
        
        if not(BPost.objects.filter(id=self.kwargs['BPostID'])):
            content = {'detail': 'Invalid post ID!'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        bpost = BPost.objects.get(id=self.kwargs['BPostID'])
        content = {'detail':'Success!', 'id':bpost.id, 'Author':bpost.Author.username, 'Title':bpost.Title, 'Thumbnail':'N/A', 'Date':bpost.Date, 'Text':bpost.Text, 'PostImage':'N/A', 'Likes':bpost.Likes, 'Comments':[]}
        if bpost.Thumbnail:
            content['Thumbnail'] = bpost.Thumbnail
        if bpost.PostImage:
            content['PostImage'] = bpost.PostImage
        for com in bpost.Comments.all():
            comdict = {'id':com.id, 'Author':com.Author.username, 'Title':com.Title, 'Date':com.Date, 'Text':com.Text, 'Likes':com.Likes}
            content['Comments'].append(comdict)

        return Response(content, status=status.HTTP_200_OK)

class BPostLike(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self,request,format=None,*args,**kwargs):
        
        if not(BPost.objects.filter(id=self.kwargs['BPostID'])):
            content = {'detail': 'Invalid post ID!'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        bpost = BPost.objects.get(id=self.kwargs['BPostID'])
        bpost.Likes += 1
        bpost.save()
        content = {'detail': 'Success!','Likes':bpost.Likes}
        return Response(content, status=status.HTTP_200_OK)

class BPostDislike(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self,request,format=None,*args,**kwargs):
        
        if not(BPost.objects.filter(id=self.kwargs['BPostID'])):
            content = {'detail': 'Invalid post ID!'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        bpost = BPost.objects.get(id=self.kwargs['BPostID'])
        bpost.Likes -= 1
        bpost.save()
        content = {'detail': 'Success!','Likes':bpost.Likes}
        return Response(content, status=status.HTTP_200_OK)

class BCommentLike(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self,request,format=None,*args,**kwargs):
        
        if not(BComment.objects.filter(id=self.kwargs['BCommentID'])):
            content = {'detail': 'Invalid comment ID!'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        bcom = BComment.objects.get(id=self.kwargs['BCommentID'])
        bcom.Likes += 1
        bcom.save()
        content = {'detail': 'Success!','Likes':bcom.Likes}
        return Response(content, status=status.HTTP_200_OK)

class BCommentDislike(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self,request,format=None,*args,**kwargs):
        
        if not(BComment.objects.filter(id=self.kwargs['BCommentID'])):
            content = {'detail': 'Invalid comment ID!'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        bcom = BComment.objects.get(id=self.kwargs['BCommentID'])
        bcom.Likes -= 1
        bcom.save()
        content = {'detail': 'Success!','Likes':bcom.Likes}
        return Response(content, status=status.HTTP_200_OK)
    
