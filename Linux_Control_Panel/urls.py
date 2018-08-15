#coding:utf8

from django.conf.urls import url
from django.contrib import admin
from sys_info import views, search

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='home'),
    url(r'^notification/$', views.notification, name='notification'),
    url(r'^task/$', views.task, name='task'),
    url(r'^taskmanage/$', views.task_manage, name='task_manage'),
    url(r'^cpu/$', views.cpu, name='cpu'),
    # url(r'^memory/$', views.memory, name='mem'),
    # url(r'^network/$', views.cpu, name='net'),
    # url(r'^disk/$', views.root_disk, name='disk'),
    # url(r'^process/$', views.cpu, name='proc'),
    # url(r'^about/$', views.about, name='about'),
    # url(r'^console/$', views.console, name='console'),
    # url(r'^doc/$', views.doc, name='doc'),
    url(r'^test/$', views.test, name='test'),
    url(r'^ajax_list/$', views.ajax_list, name='ajax-list'),
    url(r'^cpu_percent/$', views.cpu_percent, name='cpu_percent'),
    url(r'^add/$', views.add, name='add'),

    url(r'^search/$', search.search),
    url(r'^searchform$', search.search_form)
]
