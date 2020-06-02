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

class CreationBookTestCase(APITestCase):
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





    def test_CreateBook(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer '+self.Token)
        # image = Image.new('RGB' , (100,100))
        # temp_file = tempfile.NamedTemporaryFile(suffix='.jpg')
        # image.save(temp_file)
        # temp_file.seek(0)
        data = {
            "Title": "TestTitle",
            "Description": "TestDescription",
            "Categories": "بدون دسته بندی",
            "Publish_date": "TestDate",
            "publish_series": "TestSeries",
            "Author": "TestAuthor",
            "Price": "TestPrice",
            "ISBN": "TestISBN",
            "Publisher": "TestPub",
            #"BookIMG": temp_file
        }
        response = self.client.post("/api/Books/CreateBook/",data=data)
        self.assertEqual(status.HTTP_201_CREATED , response.status_code)
    def test_UnAuthorizedUserCreateBook(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer '+ "")
        # image = Image.new('RGB' , (100,100))
        # temp_file = tempfile.NamedTemporaryFile(suffix='.jpg')
        # image.save(temp_file)
        # temp_file.seek(0)
        data = {
            "Title": "TestTitle",
            "Description": "TestDescription",
            "Categories": "بدون دسته بندی",
            "Publish_date": "TestDate",
            "publish_series": "TestSeries",
            "Author": "TestAuthor",
            "Price": "TestPrice",
            "ISBN": "TestISBN",
            "Publisher": "TestPub",
            #"BookIMG": temp_file
        }
        response = self.client.post("/api/Books/CreateBook/",data=data)
        self.assertEqual(status.HTTP_401_UNAUTHORIZED , response.status_code)

    def test_ViewBookTestCase(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.Token)
        creation = self.client.post("/api/Books/CreateBook/", {})
        response = self.client.get("/api/Books/BookView/?q={}/".format(creation.data["id"]))
        self.assertEqual(status.HTTP_200_OK,response.status_code)


class ProposeBookTestCase(APITestCase):
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
        self.client.credentials(HTTP_AUTHORIZATION='Bearer '+self.Token)
        self.Book = self.client.post("/api/Books/CreateBook/", {})

        self.ID_of_book = self.Book.data["id"]





    def test_ProposeBook(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.Token)
        data_to_propose = {
            "Offered_price" : random.randint(1000,10000),
            "Descriptions" : "Test Description for certain offer :)",
            "books" : [self.ID_of_book]
        }
        response = self.client.post("/api/Books/Book-propose/" , data=data_to_propose)
        self.assertEqual(status.HTTP_201_CREATED,response.status_code)

    def test_RateBook(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.Token)
        data_to_rate = {
            "BookID" : self.ID_of_book ,
            "rate" : random.randint(1,20)

        }
        response = self.client.post("/api/User/RateBook/", data=data_to_rate)
        self.assertEqual(status.HTTP_201_CREATED , response.status_code)


class SearchBookTestCases(APITestCase):
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
        self.client.credentials(HTTP_AUTHORIZATION='Bearer '+self.Token)
        self.Book = self.client.post("/api/Books/CreateBook/", {})


        self.ID_of_book = self.Book.data["id"]
        self.Book_title = self.Book.data["Title"]
        self.Book_Description = self.Book.data["Description"]
        self.Book_Category = self.Book.data["Categories"]
        self.Book_publish_date = self.Book.data['Publish_date']
    def test_SimpleSearch(self):
        response = self.client.get('/api/Books/SearchBookView/?q={}'.format(self.ID_of_book))
        self.assertEqual(status.HTTP_200_OK , response.status_code)

    def test_AdvanceSearch(self):
        response = self.client.get("/api/Books/BookAdvancedSearch/?id={}"
                                   "&Title={}"
                                   "&Description={}"
                                   "&Categories={}"
                                   "&Publish_date={}".format(
            self.ID_of_book,
            self.Book_title,
            self.Book_Description,
            self.Book_Category,
            self.Book_publish_date))
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_rateBookView_notrated(self):

        response = self.client.get("/api/Books/Books-Rate-View/{}/"
                                   .format(self.ID_of_book) )
        data_not_rated ={'detail': 'No user rated yet'}

        self.assertEqual(response.data , data_not_rated)
    def test_rate_bookView_rated(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.Token)
        data_to_rate = {
            "BookID": self.ID_of_book,
            "rate": random.randint(1, 20)

        }
        rate = self.client.post("/api/User/RateBook/", data=data_to_rate)
        response = self.client.get("/api/Books/Books-Rate-View/{}/"
                                   .format(self.ID_of_book))
        self.assertEqual(response.status_code,status.HTTP_200_OK)







