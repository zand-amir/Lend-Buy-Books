



from django.conf.urls import url

from django.contrib import admin

from .views import BPostCreate, BCommentSubmit, BPostView, BPostRetrieve, BPostLike, BPostDislike, BCommentLike, BCommentDislike


from django.conf import settings

from django.conf.urls.static import static

urlpatterns = [


    url(r'Post/Create/', BPostCreate.as_view(), name='create'),
    url(r'Comment/Submit/(?P<BPostID>.+)/$', BCommentSubmit.as_view() , name = 'com_sub'),
    url(r'List/View/', BPostView.as_view() , name = 'post_view'),
    url(r'Post/Retrive/(?P<BPostID>.+)/$', BPostRetrieve.as_view() , name = 'post_retrieve'),
    url(r'Post/Like/(?P<BPostID>.+)/$', BPostLike.as_view() , name = 'post_like'),
    url(r'Post/Dislike/(?P<BPostID>.+)/$', BPostDislike.as_view() , name = 'post_dislike'),
    url(r'Comment/Like/(?P<BCommentID>.+)/$', BCommentLike.as_view() , name = 'com_like'),
    url(r'Comment/Dislike/(?P<BCommentID>.+)/$', BCommentDislike.as_view() , name = 'com_dislike'),


    # url(r'CreatePost/', BPostCreate.as_view(), name='create'),
    # url(r'SubmitComment/(?P<BPostID>.+)/$', BCommentSubmit.as_view() , name = 'com_sub'),
    # url(r'ViewPosts/', BPostView.as_view() , name = 'post_view'),
    # url(r'RetrievePost/(?P<BPostID>.+)/$', BPostRetrieve.as_view() , name = 'post_retrieve'),
    # url(r'LikePost/(?P<BPostID>.+)/$', BPostLike.as_view() , name = 'post_like'),
    # url(r'DislikePost/(?P<BPostID>.+)/$', BPostDislike.as_view() , name = 'post_dislike'),
    # url(r'LikeComment/(?P<BCommentID>.+)/$', BCommentLike.as_view() , name = 'com_like'),
    # url(r'DislikeComment/(?P<BCommentID>.+)/$', BCommentDislike.as_view() , name = 'com_dislike'),
   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
