from .views import CommentViewAPI,SubmitCommentAPI


from django.conf.urls import url

from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

      url(r'Submit/', SubmitCommentAPI.as_view(), name='Comment_Submit'),
      url(r'View/', CommentViewAPI.as_view(), name='Comment_View'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
