

from django.conf.urls import url

from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from .views import BookletCreationAPI
urlpatterns = [

    url(r'CreateBooklet/', BookletCreationAPI.as_view() , name='Create_booklets'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)