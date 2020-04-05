

from django.conf.urls import  url
from rest_framework.authtoken import views
from Users.views import SignupAPI

urlpatterns = [
    url(r'^sign-up/$', SignupAPI.as_view() , name='register'),
]