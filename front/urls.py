from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.board_list, name='board_list'),
    url(r'^board/(?P<pk>\d+)/$', views.board_detail, name='board_detail'),
    url(r'^board/new/$', views.board_new, name='board_new'),
    url(r'^board/(?P<pk>\d+)/edit$', views.board_edit, name='board_edit'),
    url(r'^board/(?P<pk>\d+)/board_destroy$', views.board_destroy, name='board_destroy'),
]
