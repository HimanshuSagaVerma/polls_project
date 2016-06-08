from django.conf.urls import patterns, url
from polls_app import views

urlpatterns = [
    url(r'^$', views.list_all_polls_on_web),
    url(r'^(?P<page_no>\d+)/$', views.page),
    url(r'^index/(?P<pge>\d+)/$', views.pg),
    url(r'my-first-api/', views.my_first_api),
    url(r'all-polls/', views.list_polls),
    url(r'detail-poll/(?P<poll_id>\d+)/', views.detail_polls),
    url(r'student-api/', views.StudentApi.as_view()),   
    url(r'my-first-form/', views.my_first_form)
]