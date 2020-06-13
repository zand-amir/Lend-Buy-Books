from rest_framework import serializers

class BPostSerializer(serializers.Serializer):
    Title = serializers.CharField(max_length = 40,allow_blank=False)
    Text = serializers.CharField(allow_blank=False)

class BCommentSerializer(serializers.Serializer):
    Title = serializers.CharField(max_length = 40,allow_blank=False)
    Text = serializers.CharField(max_length = 100,allow_blank=False)
