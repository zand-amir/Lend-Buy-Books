



from django.conf.urls import url

from django.contrib import admin

from books.views import( CreateBookAPIView,
                Proposed_bookCreationAPI,
                Borrow_bookCreationAPI,
                StartBorrowAPI ,
                Book_all_View
                         )


from django.conf import settings

from django.conf.urls.static import static

urlpatterns = [

    url(r'CreateBook/', CreateBookAPIView.as_view(), name='create'),
    url(r'^Book-propose/$', Proposed_bookCreationAPI.as_view() , name = 'propose_book'),
    url(r'^Book-BorrowOffer/$', Borrow_bookCreationAPI.as_view() , name = 'Borrow_offer'),
    url(r'^Book-BorrowStart/$', StartBorrowAPI.as_view() , name = 'Borrow_start'),
    url('Books-View/',Book_all_View.as_view(),name='BooksView'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
