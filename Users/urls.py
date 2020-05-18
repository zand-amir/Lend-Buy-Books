

from django.conf.urls import  url
from django.urls import re_path
from django.urls import path
from rest_framework.authtoken import views
from Users.views import SignupAPI, UserProfile, AddCreditAPI

from django.conf.urls.static import static

from django.conf import settings

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from books.views import RateBookAPIView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    url(r'^sign-up/$', SignupAPI.as_view(), name='register'),
    url(r'^token/$', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url(r'^token/refresh/$', TokenRefreshView.as_view(), name='token_refresh'),
    url(r'RateBook/',RateBookAPIView.as_view() , name= 'bookRate'),
    url(r'AddCredit/',AddCreditAPI.as_view() , name= 'creditIncreament'),
    url(r'Profile/(?P<user>.+)/$',UserProfile.as_view() , name= 'OthersProfile'),
    url(r'Profile/',UserProfile.as_view() , name= 'OwnProfile')

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
