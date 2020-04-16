from django.shortcuts import render
from rest_framework import viewsets
from .models import Comment
from books.models import Books
from .serializers import CommentSerializer

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def get_queryset(self, request):
        Intended_Book = Books.objects.get(id = request.book_id)
        return self.queryset.filter(Addressed_Book = Intended_Book)
