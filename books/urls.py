



from django.conf.urls import url

from django.contrib import admin

from books.views import( CreateBookAPIView,
                Proposed_bookCreationAPI,
                BuyAPI,
                Borrow_bookCreationAPI,
                StartBorrowAPI ,
                Book_all_View ,
                ViewBooksAPI,
                Book_Advance_Search,
                Searching_Book_View,
                WishBook,
                ViewRateapiView,
                ViewProposed_book_apiView,
                # ViewProposeAdvanceapiView
                         )


from django.conf import settings

from django.conf.urls.static import static

urlpatterns = [

    url(r'Create/', CreateBookAPIView.as_view(), name='create'),
    url(r'^Proposals/Create/$', Proposed_bookCreationAPI.as_view() , name = 'propose_book'),
    url(r'^Proposals/Buy/$', BuyAPI.as_view() , name = 'Buy'),
    url(r'^Loans/Create/$', Borrow_bookCreationAPI.as_view() , name = 'Borrow_offer'),
    url(r'^Loans/Begin/$', StartBorrowAPI.as_view() , name = 'Borrow_start'),
    url(r'List/View/', ViewBooksAPI.as_view(), name='View'),
    url(r'List/View/Search/',Searching_Book_View.as_view(),name='SearchBookView'),
    url(r'List/View/Advance-Search/',Book_Advance_Search.as_view({'get': 'list'}),name='book_advance_search'),
    url('Lists/View/',Book_all_View.as_view(),name='BooksView'),
    url('Rate/View/(?P<BookID>.+)/$',ViewRateapiView.as_view(),name='RateView'),
    url('Proposals/View/(?P<booksID>.+)/$',ViewProposed_book_apiView.as_view(),name='RateView'),
    # url('BooksProposedAdvanceView/(?P<booksID>.+)/$',ViewProposeAdvanceapiView.as_view(),name='RateView'),
    url(r'^Wishes/Submit/$', WishBook.as_view() , name = 'Book_Wish'),

    # url(r'CreateBook/', CreateBookAPIView.as_view(), name='create'),
    # url(r'^Book-propose/$', Proposed_bookCreationAPI.as_view() , name = 'propose_book'),
    # url(r'^Buy/$', BuyAPI.as_view() , name = 'Buy'),
    # url(r'^Book-BorrowOffer/$', Borrow_bookCreationAPI.as_view() , name = 'Borrow_offer'),
    # url(r'^Book-BorrowStart/$', StartBorrowAPI.as_view() , name = 'Borrow_start'),
    # url(r'BookView/', ViewBooksAPI.as_view(), name='View'),
    # url(r'SearchBookView/',Searching_Book_View.as_view(),name='SearchBookView'),
    # url(r'BookAdvancedSearch/',Book_Advance_Search.as_view({'get': 'list'}),name='book_advance_search'),
    # url('Books-View/',Book_all_View.as_view(),name='BooksView'),
    # url('Books-Rate-View/(?P<BookID>.+)/$',ViewRateapiView.as_view(),name='RateView'),
    # url('BooksProposedView/(?P<booksID>.+)/$',ViewProposed_book_apiView.as_view(),name='RateView'),
    # # url('BooksProposedAdvanceView/(?P<booksID>.+)/$',ViewProposeAdvanceapiView.as_view(),name='RateView'),
    # url(r'^Book-Wish/$', WishBook.as_view() , name = 'Book_Wish'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
