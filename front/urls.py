from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.board_list, name='board_list'),
    url(r'^board/(?P<pk>\d+)/$', views.board_detail, name='board_detail'),
]
