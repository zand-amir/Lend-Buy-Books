
from django.contrib.contenttypes.models import ContentType

from Users.models import user

from rest_framework import serializers


class SignupSerializer(serializers.Serializer):
    username = serializers.CharField()
    password=serializers.CharField()
    email = serializers.EmailField(allow_blank=True)
    first_name = serializers.CharField(allow_blank=True)
    last_name = serializers.CharField(allow_blank=True)
    phone_number = serializers.CharField(max_length=15 , allow_blank=True)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ('id','username', 'email', 'first_name', 'last_name', 'password','phone_number','img')

