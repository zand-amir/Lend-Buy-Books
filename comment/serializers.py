from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.Serializer):
    BookID = serializers.CharField()
    
class CommentCreationSerializer(serializers.Serializer):
    BookID = serializers.CharField()
    Comment_text = serializers.RegexField('')

