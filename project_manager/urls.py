from django.conf.urls import patterns, url

from project_manager import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^project/(?P<project_pk>\d+)/$', views.project, name='project'),
)