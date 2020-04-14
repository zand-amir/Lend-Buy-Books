from rest_framework import serializers
from .models import Comment

class SubmitCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model=Comment
        fields = [
            'Addressed_Book',
            'Comment_Author',
            'Comment_Text',
            ]

