# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from . import views
#from myproject.myapp.views import register,user_login,user_logout
urlpatterns = patterns('myproject.myapp.views',
    url(r'^login/$', 'user_login', name='login'),
    url(r'^list/$', 'list', name='list'),
    url(r'^register/$', 'register', name='register'),
    url(r'^restricted/$', 'restricted', name='restricted'),
    url(r'^logout/$','user_logout', name='logout'),
    
)