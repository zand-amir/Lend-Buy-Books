import json

from random_username.generate import generate_username

from .models import user
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework import status
from .api.serializers import UserInformationSerializer


class RegistrationTestCase(APITestCase):
    def test_sign_up(self):
        random_username = generate_username()[0]
        data = {
            "username": random_username ,
            "password":"SomeStrongPassword",
            "email": random_username + '@me.com',
            "first_name":"HisName",
            "last_name":"HisLastName",
            "phone_number":"09126687452",
            "address":"This is the test so computer doesnt have any address or location",
            "postal_code":"1545685215"

        }
        response = self.client.post("/api/User/sign-up/",data)

        self.assertEqual(response.status_code,status.HTTP_201_CREATED)


class LoginTestCase(APITestCase):
    def test_sign_up(self):
        random_username = generate_username()[0]
        data = {
            "username": random_username,
            "password": "SomeStrongPassword",
            "email": random_username + '@me.com',
            "first_name": "HisName",
            "last_name": "HisLastName",
            "phone_number": "09126687452",
            "address": "This is the test so computer doesnt have any address or location",
            "postal_code": "1545685215"

        }
        registeration = self.client.post("/api/User/sign-up/",data)
        data_Login = {
            "username":random_username,
            "password": "SomeStrongPassword"
        }
        response = self.client.post("/api/User/token/",data_Login)
        self.assertEqual(response.status_code,status.HTTP_200_OK)