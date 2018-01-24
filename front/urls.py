from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.board_list, name='board_list'),
    url(r'^board/(?P<pk>\d+)/$', views.board_detail, name='board_detail'),
    url(r'^board/new/$', views.board_new, name='board_new'),
    url(r'^board/(?P<pk>\d+)/edit$', views.board_edit, name='board_edit'),
    url(r'^board/(?P<pk>\d+)/destroy$', views.board_destroy, name='board_destroy'),
    url(r'^list/new/$', views.list_new, name='list_new'),
    url(r'^list/(?P<pk>\d+)/edit$', views.list_edit, name='list_edit'),
    url(r'^list/(?P<pk>\d+)/destroy$', views.list_destroy, name='list_destroy'),
]
