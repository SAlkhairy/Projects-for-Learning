from django.conf.urls import url
from . import views

app_name = 'newsapp'
urlpatterns = [
    url(r'^$' , views.index),
    url(r'^list/$', views.list),
    url(r'^(?P<article_id>\d+)/show/$', views.show, name='show'),
    url(r'^(?P<article_id>\d+)/comment/$', views.comment, name='comment'),

]























# url(r'^(?P<article_id>\d+)/show/$', views.show_article, name='show'),
# url(r'^list/$', views.show_list),
