from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^join/$', views.signup, name='join'),
    url(r'^login/$', views.signin, name='login'),
    url(r'^$', views.index, name='index'),
]
