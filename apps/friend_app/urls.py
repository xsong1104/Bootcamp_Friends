from django.conf.urls import url
from . import views

app_name = "friend"
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^add$', views.add, name="add"),
    url(r'^add/new$', views.addfriend, name="addfriend"),
    url(r'^show$', views.show, name="show"),
    url(r'^delete/(?P<id>\d+)$', views.delete, name="del"),
    # url(r'^edit/(?P<id>\d+)$', views.edit, name="edit"),
    # url(r'^update/(?P<id>\d+)$', views.update, name="update"),
    # url(r'^like/(?P<id>\d+)$', views.like, name="like")
]
