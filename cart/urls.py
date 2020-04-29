
from django.conf.urls import url

from django.contrib import admin

from cart.views import (
                CartViewSet ,
                Remove_Item_from_list
)


from django.conf import settings

from django.conf.urls.static import static

urlpatterns = [

    url(r'my-cart/', CartViewSet.as_view({'get': 'list'}), name='create'),
    url(r'remove/', Remove_Item_from_list.as_view(), name='remove'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)