



from django.conf.urls import url

from django.contrib import admin

from books.views import CreateBookAPIView

urlpatterns = [

    url(r'CreateBook/', CreateBookAPIView.as_view(), name='create'),

]