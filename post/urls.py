from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^post/(?P<id>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_create'),
    url(r'^post/delete/$', views.post_delete, name='post_delete'),
    url(r'^post/update/(?P<id>\d+)/$', views.post_edit, name='post_update'),

    url(r'^comment/new/(?P<bidx>\d+)/$', views.comment_new, name='comment_create'),
]