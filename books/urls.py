



from django.conf.urls import url

from django.contrib import admin

from books.views import( CreateBookAPIView,
                Proposed_bookCreationAPI
                         )


from django.conf import settings

from django.conf.urls.static import static

urlpatterns = [

    url(r'CreateBook/', CreateBookAPIView.as_view(), name='create'),
    url(r'^Book-propose/$', Proposed_bookCreationAPI.as_view() , name = 'propose_book'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)