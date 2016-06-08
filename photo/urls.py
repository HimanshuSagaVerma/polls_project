from django.conf.urls import patterns, url
from photo import views
from photo import api

urlpatterns = [
    url(r'^api/list/$', api.photo_list_api),
    # url(r'^$', views.home_page),
    url(r'^photo/home/$', views.home_page),
]