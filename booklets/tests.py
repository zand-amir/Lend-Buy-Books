import json
import tempfile

from random_username.generate import generate_username

import random

import requests

from PIL import Image


from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase ,APIClient
from rest_framework import status
# Create your tests here.

class CreationBookletsTestCase(APITestCase):
    def setUp(self) :
        self.random_username = generate_username()[0]
        data = {
            "username": self.random_username,
            "password": "SomeStrongPassword",
            "email": self.random_username + '@me.com',
            "first_name": "HisName",
            "last_name": "HisLastName",
            "phone_number": "09126687452",
            "address": "This is the test so computer doesnt have any address or location",
            "postal_code": "1545685215"

        }
        self.registeration = self.client.post("/api/User/sign-up/", data)
        self.client = APIClient()
        log_data = {
            "username" : self.random_username,
            "password" : "SomeStrongPassword"
        }
        self.log = self.client.post("/api/User/token/" , log_data)
        self.Token = self.log.data["access"]





    def test_CreateBooklets(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer '+self.Token)
        data_for_booklets = {
            "Title" : "Test Booklet Name" ,
            "Category" : "بدون دسته بندی" ,
            "Professor_name" : "Test Name",
            "Description" : "Test Descriptions" ,
            "Course_name" : "Test course" ,
            "University_name" : "Test UNI Name" ,
            "Semester" : "Test Semester"
        }
        response = self.client.post("/api/Booklets/CreateBooklet/" , data_for_booklets)
        self.assertEqual(response.status_code , status.HTTP_201_CREATED)


    def test_CreateBooklets_UNAUTHORIZED(self):

        data_for_booklets = {
            "Title" : "Test Booklet Name" ,
            "Category" : "بدون دسته بندی" ,
            "Professor_name" : "Test Name",
            "Description" : "Test Descriptions" ,
            "Course_name" : "Test course" ,
            "University_name" : "Test UNI Name" ,
            "Semester" : "Test Semester"
        }
        response = self.client.post("/api/Booklets/CreateBooklet/" , data_for_booklets)
        self.assertEqual(response.status_code , status.HTTP_401_UNAUTHORIZED)


class BookletsTestCase(APITestCase):
    def setUp(self) :
        self.random_username = generate_username()[0]
        data = {
            "username": self.random_username,
            "password": "SomeStrongPassword",
            "email": self.random_username + '@me.com',
            "first_name": "HisName",
            "last_name": "HisLastName",
            "phone_number": "09126687452",
            "address": "This is the test so computer doesnt have any address or location",
            "postal_code": "1545685215"

        }
        self.registeration = self.client.post("/api/User/sign-up/", data)
        self.client = APIClient()
        log_data = {
            "username" : self.random_username,
            "password" : "SomeStrongPassword"
        }
        self.log = self.client.post("/api/User/token/" , log_data)
        self.Token = self.log.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.Token)
        data_for_booklets = {
            "Title": "Test Booklet Name",
            "Category": "بدون دسته بندی",
            "Professor_name": "Test Name",
            "Description": "Test Descriptions",
            "Course_name": "Test course",
            "University_name": "Test UNI Name",
            "Semester": "Test Semester"
        }
        self.Booklet = self.client.post("/api/Booklets/CreateBooklet/", data_for_booklets)


    def test_Viewlets(self):

        response = self.client.get("/api/Booklets/Book-let-list/")
        self.assertEqual(response.status_code , status.HTTP_200_OK)

    def test_Booklets(self):

        requestToGetID = self.client.get("/api/Booklets/BookLetsView/")
        BookletID = requestToGetID.data[0].get('id')
        response = self.client.get("/api/Booklets/BookLetsView/?q={}".format(BookletID))
        self.assertEqual(response.status_code , status.HTTP_200_OK)


