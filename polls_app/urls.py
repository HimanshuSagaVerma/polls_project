from django.conf.urls import patterns, url
from polls_app import views

urlpatterns = [
    url(r'^(?P<page_no>\d+)/$', views.page),
    url(r'^index/(?P<pge>\d+)/$', views.pg),
    url(r'my-first-api/', views.my_first_api),
    url(r'all-polls/', views.list_polls),
    url(r'detail-poll/(?P<poll_id>\d+)/', views.detail_polls),
]