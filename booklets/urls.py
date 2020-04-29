

from django.conf.urls import url

from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from .views import (BookletCreationAPI ,
                    BookletsView ,
                    ViewBookLetsAPI ,
                    Searching_Booklets_View
                    )
urlpatterns = [

    url(r'CreateBooklet/', BookletCreationAPI.as_view() , name='Create_booklets'),
    url(r'Book-let-list/' , BookletsView.as_view() , name='List_booklets') ,
    url(r'BookLetsView/', ViewBookLetsAPI.as_view(), name='View'),
    url(r'SearchBookLetsView/',Searching_Booklets_View.as_view(),name='SearchBooklets'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)